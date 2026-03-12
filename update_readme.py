from __future__ import annotations

import argparse
import datetime as dt
import shutil
from pathlib import Path
from typing import Any

from _bench_common import BENCH_ROOT, load_json, write_json


README_START = "<!-- BENCH_RESULTS_START -->"
README_END = "<!-- BENCH_RESULTS_END -->"


def load_previous(latest_dir: Path, target: str) -> dict[str, Any] | None:
    path = latest_dir / f"{target}.json"
    if not path.exists():
        return None
    return load_json(path)


def phase_lookup(summary: dict[str, Any]) -> dict[str, float]:
    result: dict[str, float] = {}
    for fixture in summary["suites"]["realworld_phases"]["fixtures"]:
        result[fixture["fixture"]] = fixture["syntaxcheck"]["mean_sec"]
    return result


def format_rss_kb(value: int | None) -> str:
    if value is None:
        return "n/a"
    if value >= 1024 * 1024:
        return f"{value / (1024 * 1024):.2f} GB"
    if value >= 1024:
        return f"{value / 1024:.2f} MB"
    return f"{value} KB"


def format_cpu_pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.1f}%"


def trend(current: float, previous: float | None) -> str:
    if previous is None:
        return "new"
    delta = current - previous
    if abs(delta) < 1e-9:
        return "flat"
    return "improved" if delta < 0 else "worse"


def format_delta(current: float, previous: float | None) -> str:
    if previous is None:
        return "n/a"
    delta = current - previous
    return f"{delta:+.4f}s"


def build_readme_block(latest: list[dict[str, Any]], previous_by_target: dict[str, dict[str, Any] | None]) -> str:
    lines = [
        f"Generated: {dt.datetime.now(dt.timezone.utc).isoformat()}",
        "",
    ]
    for summary in sorted(latest, key=lambda item: item["target"]):
        target = summary["target"]
        prev = previous_by_target.get(target)
        prev_phases = phase_lookup(prev) if prev else {}
        lines.append(f"### {target}")
        lines.append("")
        lines.append("#### Timing")
        lines.append("")
        lines.append("| Fixture | Syntaxcheck mean | Previous | Delta | Trend |")
        lines.append("| --- | ---: | ---: | ---: | --- |")
        for fixture in summary["suites"]["realworld_phases"]["fixtures"]:
            name = fixture["fixture"]
            current = fixture["syntaxcheck"]["mean_sec"]
            previous = prev_phases.get(name)
            previous_text = f"{previous:.4f}s" if previous is not None else "n/a"
            lines.append(
                f"| `{name}` | {current:.4f}s | {previous_text} | {format_delta(current, previous)} | {trend(current, previous)} |"
            )
        lines.append("")
        lines.append("#### Resources")
        lines.append("")
        lines.append("| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |")
        lines.append("| --- | ---: | ---: | ---: | ---: |")
        for fixture in summary["suites"]["realworld_resources"]["fixtures"]:
            lines.append(
                "| "
                f"`{fixture['fixture']}` | "
                f"{format_rss_kb(fixture['parse_only']['peak_rss_kb'])} | "
                f"{format_rss_kb(fixture['syntaxcheck']['peak_rss_kb'])} | "
                f"{format_cpu_pct(fixture['parse_only']['peak_cpu_pct'])} | "
                f"{format_cpu_pct(fixture['syntaxcheck']['peak_cpu_pct'])} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip()


def update_readme(readme_path: Path, block: str) -> None:
    text = readme_path.read_text(encoding="utf-8")
    start = text.index(README_START) + len(README_START)
    end = text.index(README_END)
    new_text = text[:start] + "\n" + block + "\n" + text[end:]
    readme_path.write_text(new_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--incoming-dir", default=str(BENCH_ROOT / "bench_results" / "incoming"))
    parser.add_argument("--latest-dir", default=str(BENCH_ROOT / "bench_results" / "latest"))
    parser.add_argument("--history-dir", default=str(BENCH_ROOT / "bench_results" / "history"))
    parser.add_argument("--readme", default=str(BENCH_ROOT / "README.md"))
    args = parser.parse_args()

    incoming_dir = Path(args.incoming_dir)
    latest_dir = Path(args.latest_dir)
    history_dir = Path(args.history_dir)
    readme_path = Path(args.readme)

    latest_dir.mkdir(parents=True, exist_ok=True)
    history_dir.mkdir(parents=True, exist_ok=True)

    latest_summaries: list[dict[str, Any]] = []
    previous_by_target: dict[str, dict[str, Any] | None] = {}
    timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    for target_dir in sorted(incoming_dir.glob("*")):
        summary_path = target_dir / "summary.json"
        if not summary_path.exists():
            continue
        summary = load_json(summary_path)
        target = summary["target"]
        previous_by_target[target] = load_previous(latest_dir, target)
        write_json(latest_dir / f"{target}.json", summary)
        archive_dir = history_dir / target
        archive_dir.mkdir(parents=True, exist_ok=True)
        write_json(archive_dir / f"{timestamp}.json", summary)
        raw_logs_dir = target_dir / "raw_logs"
        if raw_logs_dir.exists():
            latest_raw_dir = latest_dir / "raw_logs" / target
            if latest_raw_dir.exists():
                shutil.rmtree(latest_raw_dir)
            shutil.copytree(raw_logs_dir, latest_raw_dir)

            archive_raw_dir = history_dir / target / f"{timestamp}_raw_logs"
            if archive_raw_dir.exists():
                shutil.rmtree(archive_raw_dir)
            shutil.copytree(raw_logs_dir, archive_raw_dir)
        latest_summaries.append(summary)

    if latest_summaries:
        update_readme(readme_path, build_readme_block(latest_summaries, previous_by_target))

    if incoming_dir.exists():
        shutil.rmtree(incoming_dir)


if __name__ == "__main__":
    main()
