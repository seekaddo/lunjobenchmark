from __future__ import annotations

import argparse
import datetime as dt
import platform
import re
from pathlib import Path

from _bench_common import write_json


SYNTAX_RUN_RE = re.compile(r"elapsed=([0-9.]+) sec")
PHASE_TIME_RE = re.compile(
    r"Time \(mean ± σ\):\s+([0-9.]+)\s+([a-zµ]+)\s+±\s+([0-9.]+)\s+([a-zµ]+)",
    re.IGNORECASE,
)
PHASE_ABS_RE = re.compile(r"Time \(abs ≡\):\s+([0-9.]+)\s+([a-zµ]+)", re.IGNORECASE)

# Poop output patterns
POOP_BENCHMARK_RE = re.compile(r"Benchmark \d+ \((\d+) runs\):")
POOP_WALL_TIME_RE = re.compile(r"wall_time\s+([0-9.]+)([a-zµ]+)\s+±\s+([0-9.]+)([a-zµ]+)")

RESOURCE_RE = re.compile(
    r"^\s*(parse-only|syntaxcheck)\s+.*(?:peak cpu|cpu)=([^%]+)%\s+(?:peak rss|max rss)=([0-9.]+)\s+(KB|MB|GB)",
    re.IGNORECASE,
)


def clean_fixture(label: str) -> str:
    return label.strip().removeprefix("test_semantic/")


def to_seconds(value: str, unit: str) -> float:
    amount = float(value)
    unit = unit.lower()
    if unit == "s":
        return amount
    if unit == "ms":
        return amount / 1000.0
    if unit in {"us", "µs"}:
        return amount / 1_000_000.0
    if unit == "ns":
        return amount / 1_000_000_000.0
    raise ValueError(f"unsupported time unit: {unit}")


def rss_to_kb(value: str, unit: str) -> int:
    amount = float(value)
    unit = unit.upper()
    if unit == "KB":
        return int(amount)
    if unit == "MB":
        return int(amount * 1024)
    if unit == "GB":
        return int(amount * 1024 * 1024)
    raise ValueError(f"unsupported rss unit: {unit}")


def parse_syntax_log(path: Path) -> dict:
    targets: list[dict] = []
    current_fixture: str | None = None
    measurements: list[float] = []

    def flush() -> None:
        nonlocal current_fixture, measurements
        if current_fixture is None:
            return
        targets.append(
            {
                "fixture": current_fixture,
                "kind": "file" if current_fixture.endswith(".asn") else "dir",
                "repeat": len(measurements),
                "measurements_sec": measurements[:],
                "mean_sec": (sum(measurements) / len(measurements)) if measurements else 0.0,
            }
        )
        current_fixture = None
        measurements = []

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line.startswith("==> "):
            flush()
            current_fixture = clean_fixture(raw_line[4:])
            continue
        match = SYNTAX_RUN_RE.search(raw_line)
        if match:
            measurements.append(float(match.group(1)))
    flush()
    return {"suite": "syntaxcheck", "targets": targets}


def parse_phases_log(path: Path, runs: int) -> dict:
    fixtures: list[dict] = []
    current_fixture: str | None = None
    timings: list[tuple[float, float]] = []
    is_poop_output = False
    poop_runs = 0

    def flush() -> None:
        nonlocal current_fixture, timings
        if current_fixture is None or len(timings) < 2:
            current_fixture = None
            timings = []
            return
        parse_mean, parse_stddev = timings[0]
        syntax_mean, syntax_stddev = timings[1]
        fixtures.append(
            {
                "fixture": current_fixture,
                "runs": poop_runs if is_poop_output else runs,
                "parse_only": {
                    "mean_sec": parse_mean,
                    "stddev_sec": parse_stddev,
                    "measurements_sec": [],
                },
                "syntaxcheck": {
                    "mean_sec": syntax_mean,
                    "stddev_sec": syntax_stddev,
                    "measurements_sec": [],
                },
                "validator_overhead_sec": syntax_mean - parse_mean,
            }
        )
        current_fixture = None
        timings = []

    content = path.read_text(encoding="utf-8")
    
    # Check if this is poop output
    if "Benchmark" in content and "wall_time" in content:
        is_poop_output = True
        # Parse poop output
        for raw_line in content.splitlines():
            if raw_line.startswith("==> "):
                flush()
                current_fixture = clean_fixture(raw_line[4:])
                continue
            # Match poop benchmark header to get run count
            match = POOP_BENCHMARK_RE.search(raw_line)
            if match:
                poop_runs = int(match.group(1))
                continue
            # Match poop wall_time line
            match = POOP_WALL_TIME_RE.search(raw_line)
            if match:
                mean_val = to_seconds(match.group(1), match.group(2))
                stddev_val = to_seconds(match.group(3), match.group(4))
                timings.append((mean_val, stddev_val))
                continue
        flush()
        return {"suite": "realworld_phases", "fixtures": fixtures}

    # Original hyperfine parsing
    for raw_line in content.splitlines():
        if raw_line.startswith("==> "):
            flush()
            current_fixture = clean_fixture(raw_line[4:])
            continue
        match = PHASE_TIME_RE.search(raw_line)
        if match:
            timings.append((to_seconds(match.group(1), match.group(2)), to_seconds(match.group(3), match.group(4))))
            continue
        match = PHASE_ABS_RE.search(raw_line)
        if match:
            value = to_seconds(match.group(1), match.group(2))
            timings.append((value, 0.0))
    flush()
    return {"suite": "realworld_phases", "fixtures": fixtures}


def parse_resources_log(path: Path) -> dict:
    fixtures: list[dict] = []
    current_fixture: str | None = None
    current_mode: str | None = None
    current_data: dict = {}

    def flush() -> None:
        nonlocal current_fixture, current_mode, current_data
        if current_fixture is None:
            return
        fixtures.append(
            {
                "fixture": current_fixture,
                "parse_only": {
                    "peak_cpu_pct": current_data.get("parse_only_cpu"),
                    "peak_rss_kb": current_data.get("parse_only_rss"),
                },
                "syntaxcheck": {
                    "peak_cpu_pct": current_data.get("syntaxcheck_cpu"),
                    "peak_rss_kb": current_data.get("syntaxcheck_rss"),
                },
            }
        )
        current_fixture = None
        current_mode = None
        current_data = {}

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line.startswith("==>"):
            flush()
            current_fixture = clean_fixture(raw_line[4:])
            continue
        match = RESOURCE_RE.search(raw_line)
        if match:
            mode = match.group(1).lower().replace("-", "_")
            cpu = float(match.group(2).strip())
            rss = rss_to_kb(match.group(3), match.group(4))
            current_data[f"{mode}_cpu"] = cpu
            current_data[f"{mode}_rss"] = rss
    flush()
    return {"suite": "realworld_resources", "fixtures": fixtures}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--binary", required=True)
    parser.add_argument("--syntax-log", required=True)
    parser.add_argument("--phases-log", required=True)
    parser.add_argument("--resources-log", required=True)
    parser.add_argument("--phase-runs", type=int, default=5)
    parser.add_argument("--output-summary", required=True)
    args = parser.parse_args()

    result = {
        "target": args.target,
        "binary": args.binary,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "host_machine": platform.machine(),
        "host_system": platform.system(),
        "suites": {
            "syntaxcheck": parse_syntax_log(Path(args.syntax_log)),
            "realworld_phases": parse_phases_log(Path(args.phases_log), args.phase_runs),
            "realworld_resources": parse_resources_log(Path(args.resources_log)),
        },
    }

    write_json(Path(args.output_summary), result)


if __name__ == "__main__":
    main()
