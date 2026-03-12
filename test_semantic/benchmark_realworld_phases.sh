#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_runner_common.sh"
cd "$repo_root"
ensure_built_binary

if ! command -v hyperfine >/dev/null 2>&1; then
	printf "error: hyperfine is not installed or not on PATH.\n" >&2
	exit 1
fi

runs=5
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

hyperfine_shell_args=()
if [[ "$(detect_host_os)" == "windows" ]]; then
	hyperfine_shell_args=(--shell bash)
fi

for fixture_dir in "${fixture_dirs[@]}"; do
	printf '==> %s\n' "$fixture_dir"
	fixture_path="$(normalize_path_for_voltcc "$fixture_dir")"
	parse_cmd="$(shell_join "$VOLTCC_BIN" --parse-only --no-warnings --dir "$fixture_path") >/dev/null 2>&1"
	syntax_cmd="$(shell_join "$VOLTCC_BIN" --syntaxcheck --no-warnings --dir "$fixture_path") >/dev/null 2>&1"
	hyperfine \
		"${hyperfine_shell_args[@]}" \
		--warmup 1 \
		--runs "$runs" \
		"$parse_cmd" \
		"$syntax_cmd"
	printf '\n'
done
