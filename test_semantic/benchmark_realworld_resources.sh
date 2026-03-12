#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_runner_common.sh"
cd "$repo_root"
ensure_built_binary

duration=5
fixture_dirs=(
	"test_semantic/e1ap_rel18.4_specs"
	"test_semantic/f1ap_rel18.6_specs"
	"test_semantic/ngap_rel18.6_specs"
)

while [[ $# -gt 0 ]]; do
	case "$1" in
		--seconds)
			duration="$2"
			shift 2
			;;
		*)
			fixture_dirs=("$@")
			break
			;;
	esac
done

format_memory() {
	local rss_kb=$1
	if (( rss_kb >= 1024 * 1024 )); then
		awk "BEGIN { printf \"%.2f GB\", $rss_kb / (1024 * 1024) }"
	elif (( rss_kb >= 1024 )); then
		awk "BEGIN { printf \"%.2f MB\", $rss_kb / 1024 }"
	else
		printf "%s KB" "$rss_kb"
	fi
}

sample_resources() {
	local mode="$1"
	local fixture_dir="$2"
	local label="$3"
	local target_pid
	local killer_pid
	local peak_cpu="0"
	local peak_rss="0"
	local ps_line=""

	set +e
	"$VOLTCC_BIN" "$mode" --no-warnings --dir "$fixture_dir" >/dev/null 2>&1 &
	target_pid=$!
	(
		sleep "$duration"
		kill -TERM "$target_pid" 2>/dev/null || true
	) &
	killer_pid=$!

	while kill -0 "$target_pid" 2>/dev/null; do
		ps_line="$(ps -p "$target_pid" -o %cpu=,rss= 2>/dev/null | awk 'NF == 2 { print $1, $2 }')"
		if [[ -n "$ps_line" ]]; then
			local current_cpu
			local current_rss
			current_cpu="$(awk '{ print $1 }' <<<"$ps_line")"
			current_rss="$(awk '{ print $2 }' <<<"$ps_line")"
			peak_cpu="$(awk -v a="$peak_cpu" -v b="$current_cpu" 'BEGIN { if (b > a) print b; else print a }')"
			peak_rss="$(awk -v a="$peak_rss" -v b="$current_rss" 'BEGIN { if (b > a) print b; else print a }')"
		fi
		sleep 0.1
	done

	wait "$target_pid"
	local target_rc=$?
	kill -TERM "$killer_pid" 2>/dev/null || true
	wait "$killer_pid" 2>/dev/null || true
	set -e

	local formatted_rss
	formatted_rss="$(format_memory "$peak_rss")"

	if [[ "$target_rc" -eq 143 ]]; then
		printf '  %-12s timed out after %ss (peak cpu=%s%% peak rss=%s)\n' "$label" "$duration" "$peak_cpu" "$formatted_rss"
	else
		printf '  %-12s peak cpu=%s%% peak rss=%s\n' "$label" "$peak_cpu" "$formatted_rss"
	fi
}

printf 'Sampling CPU and RSS on real-world directories.\n'
printf 'This samples peak CPU and RSS during the run window.\n\n'

for fixture_dir in "${fixture_dirs[@]}"; do
	printf '==> %s\n' "$fixture_dir"
	sample_resources --parse-only "$fixture_dir" "parse-only"
	sample_resources --syntaxcheck "$fixture_dir" "syntaxcheck"
	printf '\n'
done
