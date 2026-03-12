#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_runner_common.sh"
cd "$repo_root"
ensure_built_binary

TIME_BIN="$(type -P time || true)"
if [[ -z "${TIME_BIN}" ]]; then
	printf "error: a standalone 'time' binary is required for benchmark_syntaxcheck.sh\n" >&2
	exit 1
fi

repeat=1
targets=()

while [[ $# -gt 0 ]]; do
	case "$1" in
		--repeat)
			repeat="$2"
			shift 2
			;;
		*)
			targets+=("$1")
			shift
			;;
	esac
done

if [[ "${#targets[@]}" -eq 0 ]]; then
	targets=(
		"test_semantic/x681_x682_x683_protocol_ie_container.asn"
		"test_semantic/lteNRRCC"
		"test_semantic/e1ap_rel18.4_specs"
		"test_semantic/f1ap_rel18.6_specs"
	)
fi

for target in "${targets[@]}"; do
	if [[ -d "${target}" ]]; then
		target_path="$(normalize_path_for_voltcc "${target}")"
		args=(--syntaxcheck --dir "${target_path}")
	else
		target_path="$(normalize_path_for_voltcc "${target}")"
		args=(--syntaxcheck "${target_path}")
	fi

	printf '==> %s\n' "${target}"
	for run_idx in $(seq 1 "${repeat}"); do
		printf '  run %d: ' "${run_idx}"
		"${TIME_BIN}" -f 'elapsed=%e sec user=%U sys=%S cpu=%P rss=%M KB' \
			"${VOLTCC_BIN}" "${args[@]}" >/dev/null
	done
done
