from __future__ import annotations

import json
import math
import os
import platform
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any


BENCH_ROOT = Path(__file__).resolve().parent
FIXTURE_ROOT = BENCH_ROOT / "test_semantic"
IS_WINDOWS = os.name == "nt"
EXE_NAME = "voltcc.exe" if IS_WINDOWS else "voltcc"
DEFAULT_BINARY = BENCH_ROOT / EXE_NAME


def detect_target() -> str:
    env_target = os.environ.get("VOLTCC_TARGET")
    if env_target:
        return env_target

    system = platform.system().lower()
    machine = platform.machine().lower()
    if system == "linux":
        if machine in {"x86_64", "amd64"}:
            return "linux-x86_64"
        if machine in {"i386", "i686", "x86"}:
            return "linux-i386"
        if machine in {"aarch64", "arm64"}:
            return "linux-aarch64"
    if system == "darwin":
        if machine in {"aarch64", "arm64"}:
            return "macos-aarch64"
        if machine in {"x86_64", "amd64"}:
            return "macos-x86_64"
    if system == "windows":
        if machine in {"x86_64", "amd64"}:
            return "windows-x86_64"
        if machine in {"i386", "i686", "x86"}:
            return "windows-i386"
    raise RuntimeError(f"unsupported host for benchmark target detection: system={system} machine={machine}")


def ensure_binary(binary: Path) -> Path:
    if not binary.exists():
        raise FileNotFoundError(f"benchmark binary missing: {binary}")
    return binary


def fixture_path(relative_path: str) -> Path:
    return FIXTURE_ROOT / relative_path


def to_posix_string(path: Path) -> str:
    return path.as_posix()


def run_elapsed(command: list[str]) -> dict[str, Any]:
    start = time.perf_counter()
    proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    elapsed = time.perf_counter() - start
    if proc.returncode != 0:
        raise RuntimeError(
            f"command failed ({proc.returncode}): {' '.join(command)}\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
        )
    return {"elapsed_sec": elapsed}


def sample_process(command: list[str], sample_interval: float = 0.1) -> dict[str, Any]:
    proc = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    peak_rss_kb: int | None = None
    peak_cpu_pct: float | None = None

    while True:
        if proc.poll() is not None:
            break

        if IS_WINDOWS:
            ps_cmd = [
                "powershell",
                "-NoProfile",
                "-Command",
                (
                    "$p = Get-Process -Id "
                    f"{proc.pid}"
                    " -ErrorAction SilentlyContinue; "
                    "if ($p) { "
                    "[Console]::Write(($p.WorkingSet64 / 1kb).ToString()) "
                    "}"
                ),
            ]
            sample = subprocess.run(ps_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            text = sample.stdout.strip()
            if text:
                rss_kb = int(float(text))
                peak_rss_kb = rss_kb if peak_rss_kb is None else max(peak_rss_kb, rss_kb)
        else:
            sample = subprocess.run(
                ["ps", "-p", str(proc.pid), "-o", "%cpu=,rss="],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
            )
            text = sample.stdout.strip()
            if text:
                cpu_text, rss_text = text.split()
                cpu_pct = float(cpu_text)
                rss_kb = int(float(rss_text))
                peak_cpu_pct = cpu_pct if peak_cpu_pct is None else max(peak_cpu_pct, cpu_pct)
                peak_rss_kb = rss_kb if peak_rss_kb is None else max(peak_rss_kb, rss_kb)

        time.sleep(sample_interval)

    rc = proc.wait()
    if rc != 0:
        raise RuntimeError(f"command failed ({rc}): {' '.join(command)}")
    return {
        "peak_rss_kb": peak_rss_kb,
        "peak_cpu_pct": peak_cpu_pct,
    }


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def stddev(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    avg = mean(values)
    return math.sqrt(sum((value - avg) ** 2 for value in values) / (len(values) - 1))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def latest_release_archives_root() -> Path:
    for candidate in (BENCH_ROOT / "releases", BENCH_ROOT.parent / "releases"):
        if candidate.exists():
            return candidate
    return BENCH_ROOT / "releases"


def normalize_label(label: str) -> str:
    return label.replace("/", "_").replace("\\", "_").replace(" ", "_")
