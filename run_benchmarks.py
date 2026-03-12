from __future__ import annotations

import argparse
import datetime as dt
import platform
from pathlib import Path

import benchmark_realworld_phases
import benchmark_realworld_resources
import benchmark_syntaxcheck
from _bench_common import DEFAULT_BINARY, BENCH_ROOT, detect_target, ensure_binary, write_json


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

    print(f"Benchmark target: {args.target}", flush=True)
    print(f"Using binary: {binary}", flush=True)
    print("Running syntaxcheck suite...", flush=True)
    syntax_data = benchmark_syntaxcheck.run_suite(binary, args.syntax_repeat, benchmark_syntaxcheck.DEFAULT_TARGETS)
    print("Running realworld phase suite...", flush=True)
    phases_data = benchmark_realworld_phases.run_suite(binary, args.phase_runs, benchmark_realworld_phases.DEFAULT_FIXTURES)
    print("Running realworld resource suite...", flush=True)
    resources_data = benchmark_realworld_resources.run_suite(binary, benchmark_realworld_resources.DEFAULT_FIXTURES)

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
