#!/usr/bin/env bash
set -euo pipefail

bench_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
target="${VOLTCC_TARGET:-}"
output_dir="bench_results/incoming"
syntax_repeat=3
phase_runs=5
resource_seconds=5

while [[ $# -gt 0 ]]; do
	case "$1" in
		--target)
			target="$2"
			shift 2
			;;
		--output-dir)
			output_dir="$2"
			shift 2
			;;
		--syntax-repeat)
			syntax_repeat="$2"
			shift 2
			;;
		--phase-runs)
			phase_runs="$2"
			shift 2
			;;
		--resource-seconds)
			resource_seconds="$2"
			shift 2
			;;
		*)
			printf "unknown argument: %s\n" "$1" >&2
			exit 1
			;;
	esac
done

if [[ -z "$target" ]]; then
	target="unknown-target"
fi

if [[ "$output_dir" == /* || "$output_dir" =~ ^[A-Za-z]:[\\/] ]]; then
	target_dir="${output_dir}/${target}"
else
	target_dir="${bench_root}/${output_dir}/${target}"
fi
log_dir="${target_dir}/raw_logs"
mkdir -p "$log_dir"

printf 'Benchmark target: %s\n' "$target"
printf 'Using binary: %s\n' "${bench_root}/zig-out/bin/voltcc"

printf 'Running syntaxcheck suite...\n'
"${bench_root}/test_semantic/benchmark_syntaxcheck.sh" --repeat "$syntax_repeat" 2>&1 | tee "${log_dir}/syntaxcheck.log"

printf 'Running realworld phase suite...\n'
"${bench_root}/test_semantic/benchmark_realworld_phases.sh" --runs "$phase_runs" 2>&1 | tee "${log_dir}/realworld_phases.log"

printf 'Running realworld resource suite...\n'
"${bench_root}/test_semantic/benchmark_realworld_resources.sh" --seconds "$resource_seconds" 2>&1 | tee "${log_dir}/realworld_resources.log"

python3 "${bench_root}/collect_benchmark_results.py" \
	--target "$target" \
	--binary "${bench_root}/zig-out/bin/voltcc" \
	--syntax-log "${log_dir}/syntaxcheck.log" \
	--phases-log "${log_dir}/realworld_phases.log" \
	--resources-log "${log_dir}/realworld_resources.log" \
	--phase-runs "$phase_runs" \
	--output-summary "${target_dir}/summary.json"

printf 'Wrote benchmark summary: %s\n' "${target_dir}/summary.json"
