from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from _bench_common import DEFAULT_BINARY, ensure_binary, fixture_args, fixture_path, run_elapsed, write_json


DEFAULT_TARGETS = [
    "x681_x682_x683_protocol_ie_container.asn",
    "lteNRRCC",
    "e1ap_rel18.4_specs",
    "f1ap_rel18.6_specs",
    "ngap_rel18.6_specs",
]


def run_suite(binary: Path, repeat: int, targets: list[str]) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for target in targets:
        fixture = fixture_path(target)
        command = [str(binary), "--syntaxcheck", *fixture_args(fixture)]

        measurements = [run_elapsed(command)["elapsed_sec"] for _ in range(repeat)]
        results.append(
            {
                "fixture": target,
                "kind": "dir" if fixture.is_dir() else "file",
                "repeat": repeat,
                "measurements_sec": measurements,
                "mean_sec": sum(measurements) / len(measurements),
            }
        )

    return {"suite": "syntaxcheck", "targets": results}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", default=str(DEFAULT_BINARY))
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument("--output-json", required=True)
    parser.add_argument("targets", nargs="*")
    args = parser.parse_args()

    binary = ensure_binary(Path(args.binary))
    data = run_suite(binary, args.repeat, args.targets or DEFAULT_TARGETS)
    write_json(Path(args.output_json), data)


if __name__ == "__main__":
    main()
