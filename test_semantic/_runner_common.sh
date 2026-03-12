#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export ZIG_GLOBAL_CACHE_DIR="${repo_root}/.zig-global-cache"
export EXEC_DIR="${repo_root}"
export VOLTCC_BIN="${EXEC_DIR}/zig-out/bin/voltcc"

ensure_built_binary() {
	if [[ ! -x "${VOLTCC_BIN}" ]]; then
		printf "error: %s is missing. Run 'zig build' first.\n" "${VOLTCC_BIN}" >&2
		exit 1
	fi
}
