from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "test_semantic"
DEST = ROOT / "test_semantic"
INCLUDED_PATHS = [
    Path("_runner_common.sh"),
    Path("benchmark_syntaxcheck.sh"),
    Path("benchmark_realworld_phases.sh"),
    Path("benchmark_realworld_resources.sh"),
    Path("windows_resource_sampler.ps1"),
    Path("x681_x682_x683_protocol_ie_container.asn"),
    Path("lteNRRCC"),
    Path("e1ap_rel18.4_specs"),
    Path("f1ap_rel18.6_specs"),
    Path("ngap_rel18.6_specs"),
]


def strip_generated_header(text: str) -> str:
    lines = text.splitlines()
    idx = 0
    header_lines: list[str] = []

    while idx < len(lines):
        line = lines[idx]
        if line.startswith("--") or line.strip() == "":
            header_lines.append(line)
            idx += 1
            continue
        break

    if header_lines and any("Objective Systems" in line for line in header_lines):
        while idx < len(lines) and lines[idx].strip() == "":
            idx += 1
        stripped = "\n".join(lines[idx:])
        return (stripped + "\n") if stripped else ""

    return text if text.endswith("\n") else text + "\n"


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"missing source directory: {SOURCE}")

    if DEST.exists():
        shutil.rmtree(DEST)

    DEST.mkdir(parents=True, exist_ok=True)
    for rel_path in INCLUDED_PATHS:
        source_path = SOURCE / rel_path
        if not source_path.exists():
            raise SystemExit(f"missing benchmark fixture source: {source_path}")

        if source_path.is_file():
            dest_path = DEST / rel_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            if source_path.suffix == ".asn":
                dest_path.write_text(strip_generated_header(source_path.read_text(encoding="utf-8")), encoding="utf-8")
            else:
                shutil.copy2(source_path, dest_path)
            continue

        for child in source_path.rglob("*"):
            child_rel = child.relative_to(SOURCE)
            dest_path = DEST / child_rel
            if child.is_dir():
                dest_path.mkdir(parents=True, exist_ok=True)
                continue
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            if child.suffix == ".asn":
                dest_path.write_text(strip_generated_header(child.read_text(encoding="utf-8")), encoding="utf-8")
            else:
                shutil.copy2(child, dest_path)


if __name__ == "__main__":
    main()
