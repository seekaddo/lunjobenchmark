#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export ZIG_GLOBAL_CACHE_DIR="${repo_root}/.zig-global-cache"
export EXEC_DIR="${repo_root}"
export VOLTCC_BIN="${EXEC_DIR}/zig-out/bin/voltcc"

detect_host_os() {
	local os
	os="$(uname -s | tr '[:upper:]' '[:lower:]')"
	case "$os" in
		msys*|mingw*|cygwin*) echo "windows" ;;
		*) echo "$os" ;;
	esac
}

normalize_path_for_voltcc() {
	local path="$1"
	if [[ "$(detect_host_os)" == "windows" ]] && command -v cygpath >/dev/null 2>&1; then
		cygpath -w "$path"
	else
		printf "%s\n" "$path"
	fi
}

shell_join() {
	local out=()
	local arg
	for arg in "$@"; do
		printf -v quoted '%q' "$arg"
		out+=("$quoted")
	done
	local joined=""
	if [[ "${#out[@]}" -gt 0 ]]; then
		joined="${out[0]}"
		for arg in "${out[@]:1}"; do
			joined+=" ${arg}"
		done
	fi
	printf "%s" "$joined"
}

ensure_built_binary() {
	if [[ ! -x "${VOLTCC_BIN}" ]]; then
		printf "error: %s is missing. Run 'zig build' first.\n" "${VOLTCC_BIN}" >&2
		exit 1
	fi
}
