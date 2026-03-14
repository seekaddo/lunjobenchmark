#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_runner_common.sh"
cd "$repo_root"
ensure_built_binary

duration=5
linux_repeat=5
linux_time_bin=""
fixture_dirs=(
	"test_semantic/e1ap_rel18.4_specs"
	"test_semantic/f1ap_rel18.6_specs"
	"test_semantic/ngap_rel18.6_specs"
	"test_semantic/lteNRRCC"
)

while [[ $# -gt 0 ]]; do
	case "$1" in
		--seconds)
			duration="$2"
			shift 2
			;;
		--linux-repeat)
			linux_repeat="$2"
			shift 2
			;;
		*)
			fixture_dirs=("$@")
			break
			;;
	esac
done

if [[ "$(detect_host_os)" == "linux" ]]; then
	if command -v gtime >/dev/null 2>&1; then
		linux_time_bin="$(command -v gtime)"
	elif [[ -x /usr/bin/time ]]; then
		linux_time_bin="/usr/bin/time"
	elif [[ -x /bin/time ]]; then
		linux_time_bin="/bin/time"
	fi
fi

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

sample_resources_linux_time() {
	local mode="$1"
	local fixture_dir="$2"
	local label="$3"
	local fixture_path
	local time_file
	local target_rc
	local cpu_pct="n/a"
	local max_rss_kb="0"
	local user_sec="0"
	local sys_sec="0"
	local elapsed_sec="0"

	fixture_path="$(normalize_path_for_voltcc "$fixture_dir")"
	time_file="$(mktemp)"

	set +e
	timeout "${duration}s" "$linux_time_bin" -f 'user_sec=%U\nsys_sec=%S\nmax_rss_kb=%M\nelapsed_sec=%e' -o "$time_file" \
		bash -lc '
			repeat="$1"
			bin="$2"
			mode="$3"
			fixture="$4"
			for ((i=0; i<repeat; ++i)); do
				"$bin" "$mode" --no-warnings --dir "$fixture" >/dev/null 2>&1
			done
		' _ "$linux_repeat" "$VOLTCC_BIN" "$mode" "$fixture_path"
	target_rc=$?
	set -e

	if [[ -f "$time_file" ]]; then
		while IFS='=' read -r key value; do
			case "$key" in
				user_sec) user_sec="$value" ;;
				sys_sec) sys_sec="$value" ;;
				max_rss_kb) max_rss_kb="$value" ;;
				elapsed_sec) elapsed_sec="$value" ;;
			esac
		done <"$time_file"
	fi
	rm -f "$time_file"

	if [[ "$elapsed_sec" != "0" && "$elapsed_sec" != "0.00" ]]; then
		cpu_pct="$(awk -v u="$user_sec" -v s="$sys_sec" -v e="$elapsed_sec" 'BEGIN { printf "%.1f", ((u + s) / e) * 100 }')"
	fi

	local formatted_rss
	formatted_rss="$(format_memory "${max_rss_kb:-0}")"

	if [[ "$target_rc" -eq 124 ]]; then
		printf '  %-12s timed out after %ss (cpu=%s%% max rss=%s repeats=%s)\n' "$label" "$duration" "$cpu_pct" "$formatted_rss" "$linux_repeat"
	elif [[ "$target_rc" -eq 0 ]]; then
		printf '  %-12s cpu=%s%% max rss=%s repeats=%s\n' "$label" "$cpu_pct" "$formatted_rss" "$linux_repeat"
	else
		printf '  %-12s failed (exit=%s cpu=%s%% max rss=%s repeats=%s)\n' "$label" "$target_rc" "$cpu_pct" "$formatted_rss" "$linux_repeat" >&2
		return "$target_rc"
	fi
}

sample_resources_windows() {
	local mode="$1"
	local fixture_path="$2"
	local label="$3"
	local helper_script
	local helper_output
	local peak_cpu="0"
	local peak_rss="0"
	local target_rc="1"
	local timed_out="false"

	helper_script="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/windows_resource_sampler.ps1"
	helper_output="$(
		powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$helper_script" \
			-BinaryPath "$VOLTCC_BIN" \
			-Mode "$mode" \
			-FixturePath "$fixture_path" \
			-Seconds "$duration"
	)"

	for token in $helper_output; do
		case "$token" in
			peak_cpu=*) peak_cpu="${token#peak_cpu=}" ;;
			peak_rss_kb=*) peak_rss="${token#peak_rss_kb=}" ;;
			exit_code=*) target_rc="${token#exit_code=}" ;;
			timed_out=*) timed_out="${token#timed_out=}" ;;
		esac
	done

	local formatted_rss
	formatted_rss="$(format_memory "$peak_rss")"

	if [[ "$timed_out" == "true" ]]; then
		printf '  %-12s timed out after %ss (peak cpu=%s%% peak rss=%s)\n' "$label" "$duration" "$peak_cpu" "$formatted_rss"
	elif [[ "$target_rc" -eq 0 ]]; then
		printf '  %-12s peak cpu=%s%% peak rss=%s\n' "$label" "$peak_cpu" "$formatted_rss"
	else
		printf '  %-12s failed (exit=%s peak cpu=%s%% peak rss=%s)\n' "$label" "$target_rc" "$peak_cpu" "$formatted_rss" >&2
		return "$target_rc"
	fi
}

sample_resources() {
	local mode="$1"
	local fixture_dir="$2"
	local label="$3"
	local fixture_path
	local target_pid
	local killer_pid
	local peak_cpu="0"
	local peak_rss="0"
	local ps_line=""

	fixture_path="$(normalize_path_for_voltcc "$fixture_dir")"
	if [[ "$(detect_host_os)" == "windows" ]]; then
		sample_resources_windows "$mode" "$fixture_path" "$label"
		return
	fi
	if [[ "$(detect_host_os)" == "linux" ]] && [[ -n "$linux_time_bin" ]]; then
		sample_resources_linux_time "$mode" "$fixture_dir" "$label"
		return
	fi

	set +e
	"$VOLTCC_BIN" "$mode" --no-warnings --dir "$fixture_path" >/dev/null 2>&1 &
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
printf 'On Linux, this uses GNU time for max RSS and average CPU over repeated runs.\n'
printf 'On other platforms, it samples peak CPU and RSS during the run window.\n\n'

for fixture_dir in "${fixture_dirs[@]}"; do
	printf '==> %s\n' "$fixture_dir"
	sample_resources --parse-only "$fixture_dir" "parse-only"
	sample_resources --syntaxcheck "$fixture_dir" "syntaxcheck"
	printf '\n'
done
