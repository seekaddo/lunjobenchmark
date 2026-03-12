from __future__ import annotations

import argparse
import datetime as dt
import platform
import subprocess
import sys
from pathlib import Path

from _bench_common import BENCH_ROOT, DEFAULT_BINARY, detect_target, ensure_binary, load_json, write_json


def run_suite_script(name: str, command: list[str], output_json: Path, log_path: Path) -> dict:
    proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    log_parts: list[str] = [f"$ {' '.join(command)}"]
    if proc.stdout:
        log_parts.append("STDOUT:")
        log_parts.append(proc.stdout.rstrip())
    if proc.stderr:
        log_parts.append("STDERR:")
        log_parts.append(proc.stderr.rstrip())
    log_text = "\n".join(log_parts).rstrip() + "\n"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(log_text, encoding="utf-8")

    print(f"=== {name} output ===", flush=True)
    if proc.stdout:
        print(proc.stdout, end="" if proc.stdout.endswith("\n") else "\n", flush=True)
    if proc.stderr:
        print(proc.stderr, end="" if proc.stderr.endswith("\n") else "\n", flush=True)

    if proc.returncode != 0:
        raise RuntimeError(f"{name} failed with exit code {proc.returncode}. See {log_path}.")
    return load_json(output_json)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", default=str(DEFAULT_BINARY))
    parser.add_argument("--target", default=detect_target())
    parser.add_argument("--output-dir", default=str(BENCH_ROOT / "bench_results" / "incoming"))
    parser.add_argument("--syntax-repeat", type=int, default=3)
    parser.add_argument("--phase-runs", type=int, default=5)
    args = parser.parse_args()

    binary = ensure_binary(Path(args.binary))
    target_dir = Path(args.output_dir) / args.target
    target_dir.mkdir(parents=True, exist_ok=True)
    log_dir = target_dir / "raw_logs"

    print(f"Benchmark target: {args.target}", flush=True)
    print(f"Using binary: {binary}", flush=True)
    print("Running syntaxcheck suite...", flush=True)
    syntax_json = target_dir / "syntaxcheck.json"
    syntax_data = run_suite_script(
        "syntaxcheck",
        [
            sys.executable,
            str(BENCH_ROOT / "benchmark_syntaxcheck.py"),
            "--binary",
            str(binary),
            "--repeat",
            str(args.syntax_repeat),
            "--output-json",
            str(syntax_json),
        ],
        syntax_json,
        log_dir / "syntaxcheck.log",
    )
    print("Running realworld phase suite...", flush=True)
    phases_json = target_dir / "realworld_phases.json"
    phases_data = run_suite_script(
        "realworld_phases",
        [
            sys.executable,
            str(BENCH_ROOT / "benchmark_realworld_phases.py"),
            "--binary",
            str(binary),
            "--runs",
            str(args.phase_runs),
            "--output-json",
            str(phases_json),
        ],
        phases_json,
        log_dir / "realworld_phases.log",
    )
    print("Running realworld resource suite...", flush=True)
    resources_json = target_dir / "realworld_resources.json"
    resources_data = run_suite_script(
        "realworld_resources",
        [
            sys.executable,
            str(BENCH_ROOT / "benchmark_realworld_resources.py"),
            "--binary",
            str(binary),
            "--output-json",
            str(resources_json),
        ],
        resources_json,
        log_dir / "realworld_resources.log",
    )

    summary = {
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "target": args.target,
        "host_system": platform.system(),
        "host_machine": platform.machine(),
        "binary": str(binary),
        "suites": {
            "syntaxcheck": syntax_data,
            "realworld_phases": phases_data,
            "realworld_resources": resources_data,
        },
    }

    summary_path = target_dir / "summary.json"
    write_json(summary_path, summary)
    print(f"Wrote benchmark summary: {summary_path}", flush=True)


if __name__ == "__main__":
    main()
