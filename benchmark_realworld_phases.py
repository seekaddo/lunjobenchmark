from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from _bench_common import DEFAULT_BINARY, ensure_binary, fixture_path, mean, run_elapsed, stddev, write_json


DEFAULT_FIXTURES = [
    "e1ap_rel18.4_specs",
    "f1ap_rel18.6_specs",
    "ngap_rel18.6_specs",
]


def timed_repeats(command: list[str], runs: int) -> list[float]:
    return [run_elapsed(command)["elapsed_sec"] for _ in range(runs)]


def run_suite(binary: Path, runs: int, fixtures: list[str]) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for fixture_name in fixtures:
        fixture = fixture_path(fixture_name)
        parse_cmd = [str(binary), "--parse-only", "--no-warnings", "--dir", str(fixture)]
        syntax_cmd = [str(binary), "--syntaxcheck", "--no-warnings", "--dir", str(fixture)]
        parse_times = timed_repeats(parse_cmd, runs)
        syntax_times = timed_repeats(syntax_cmd, runs)
        results.append(
            {
                "fixture": fixture_name,
                "runs": runs,
                "parse_only": {
                    "mean_sec": mean(parse_times),
                    "stddev_sec": stddev(parse_times),
                    "measurements_sec": parse_times,
                },
                "syntaxcheck": {
                    "mean_sec": mean(syntax_times),
                    "stddev_sec": stddev(syntax_times),
                    "measurements_sec": syntax_times,
                },
                "validator_overhead_sec": mean(syntax_times) - mean(parse_times),
            }
        )
    return {"suite": "realworld_phases", "fixtures": results}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", default=str(DEFAULT_BINARY))
    parser.add_argument("--runs", type=int, default=5)
    parser.add_argument("--output-json", required=True)
    parser.add_argument("fixtures", nargs="*")
    args = parser.parse_args()

    binary = ensure_binary(Path(args.binary))
    data = run_suite(binary, args.runs, args.fixtures or DEFAULT_FIXTURES)
    write_json(Path(args.output_json), data)


if __name__ == "__main__":
    main()
