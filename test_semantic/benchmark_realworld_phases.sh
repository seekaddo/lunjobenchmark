#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_runner_common.sh"
cd "$repo_root"
ensure_built_binary

if [[ "$(detect_host_os)" == "windows" ]]; then
	if ! command -v hyperfine >/dev/null 2>&1; then
		printf "error: hyperfine is not installed or not on PATH.\n" >&2
		exit 1
	fi
fi

fixture_dirs=(
	"test_semantic/e1ap_rel18.4_specs"
	"test_semantic/f1ap_rel18.6_specs"
	"test_semantic/ngap_rel18.6_specs"
)

while [[ $# -gt 0 ]]; do
	case "$1" in
		--runs)
			runs="$2"
			shift 2
			;;
		*)
			fixture_dirs=("$@")
			break
			;;
	esac
done

printf 'Benchmarking parser-only and full syntaxcheck on real-world directories.\n'
printf 'Note: there is no --validate-only mode yet, so validator cost is approximated by comparing parse-only with syntaxcheck.\n\n'

for fixture_dir in "${fixture_dirs[@]}"; do
	printf '==> %s\n' "$fixture_dir"
	fixture_path="$(normalize_path_for_voltcc "$fixture_dir")"
	if [[ "$(detect_host_os)" == "windows" ]]; then
		parse_cmd="$VOLTCC_BIN --parse-only --no-warnings --dir $fixture_path"
		syntax_cmd="$VOLTCC_BIN --syntaxcheck --no-warnings --dir $fixture_path"
		hyperfine \
			--shell=none \
			--warmup 1 \
			--runs 5 \
			"$parse_cmd" \
			"$syntax_cmd"
	elif [[ "$(detect_host_os)" == "linux" ]] && [[ -n "${POOP_BIN:-}" ]]; then
		# Warmup run
		"${VOLTCC_BIN}" --parse-only --no-warnings --dir "${fixture_path}" >/dev/null 2>&1 || true
		"${VOLTCC_BIN}" --syntaxcheck --no-warnings --dir "${fixture_path}" >/dev/null 2>&1 || true
		# Benchmark - use eval to properly expand the command
		eval "${POOP_BIN}" "'${VOLTCC_BIN} --parse-only --no-warnings --dir ${fixture_path}'"
		eval "${POOP_BIN}" "'${VOLTCC_BIN} --syntaxcheck --no-warnings --dir ${fixture_path}'"
	else
		# macOS or no poop - use hyperfine
		if ! command -v hyperfine >/dev/null 2>&1; then
			printf "error: hyperfine is not installed or not on PATH.\n" >&2
			exit 1
		fi
		parse_cmd="$(shell_join "$VOLTCC_BIN" --parse-only --no-warnings --dir "$fixture_path") >/dev/null 2>&1"
		syntax_cmd="$(shell_join "$VOLTCC_BIN" --syntaxcheck --no-warnings --dir "$fixture_path") >/dev/null 2>&1"
		hyperfine \
			--warmup 1 \
			--runs 5 \
			"$parse_cmd" \
			"$syntax_cmd"
	fi
	printf '\n'
done
