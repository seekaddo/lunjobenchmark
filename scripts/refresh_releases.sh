#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bench_root="$(cd "$script_dir/.." && pwd)"
source_root="$(cd "$bench_root/.." && pwd)"

if [[ ! -x "$source_root/build_release.sh" ]]; then
	echo "missing build script: $source_root/build_release.sh" >&2
	exit 1
fi

(
	cd "$source_root"
	./build_release.sh "$@"
)

rm -rf "$bench_root/releases"
cp -R "$source_root/releases" "$bench_root/releases"

echo "Copied fresh releases into $bench_root/releases"
