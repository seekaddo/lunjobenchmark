from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from _bench_common import DEFAULT_BINARY, ensure_binary, fixture_path, sample_process, write_json


DEFAULT_FIXTURES = [
    "e1ap_rel18.4_specs",
    "f1ap_rel18.6_specs",
    "ngap_rel18.6_specs",
]


def run_suite(binary: Path, fixtures: list[str]) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for fixture_name in fixtures:
        fixture = fixture_path(fixture_name)
        parse_cmd = [str(binary), "--parse-only", "--no-warnings", "--dir", str(fixture)]
        syntax_cmd = [str(binary), "--syntaxcheck", "--no-warnings", "--dir", str(fixture)]
        results.append(
            {
                "fixture": fixture_name,
                "parse_only": sample_process(parse_cmd),
                "syntaxcheck": sample_process(syntax_cmd),
            }
        )
    return {"suite": "realworld_resources", "fixtures": results}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", default=str(DEFAULT_BINARY))
    parser.add_argument("--output-json", required=True)
    parser.add_argument("fixtures", nargs="*")
    args = parser.parse_args()

    binary = ensure_binary(Path(args.binary))
    data = run_suite(binary, args.fixtures or DEFAULT_FIXTURES)
    write_json(Path(args.output_json), data)


if __name__ == "__main__":
    main()
