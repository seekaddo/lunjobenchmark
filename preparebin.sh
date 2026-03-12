#!/usr/bin/env bash
set -euo pipefail

bench_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
target="${VOLTCC_TARGET:-}"
archive_root=""

while [[ $# -gt 0 ]]; do
	case "$1" in
		--target)
			target="$2"
			shift 2
			;;
		--archive-root)
			archive_root="$2"
			shift 2
			;;
		*)
			echo "unknown argument: $1" >&2
			exit 1
			;;
	esac
done

detect_target() {
	local os
	local arch
	os="$(uname -s | tr '[:upper:]' '[:lower:]')"
	arch="$(uname -m | tr '[:upper:]' '[:lower:]')"
	case "$os" in
		linux)
			case "$arch" in
				x86_64|amd64) echo "linux-x86_64" ;;
				i386|i686|x86) echo "linux-i386" ;;
				aarch64|arm64) echo "linux-aarch64" ;;
				*) return 1 ;;
			esac
			;;
		darwin)
			case "$arch" in
				aarch64|arm64) echo "macos-aarch64" ;;
				x86_64|amd64) echo "macos-x86_64" ;;
				*) return 1 ;;
			esac
			;;
		msys*|mingw*|cygwin*)
			case "$arch" in
				x86_64|amd64) echo "windows-x86_64" ;;
				i386|i686|x86) echo "windows-i386" ;;
				*) return 1 ;;
			esac
			;;
		*)
			return 1
			;;
	esac
}

if [[ -z "$target" ]]; then
	target="$(detect_target)"
fi

if [[ -z "$archive_root" ]]; then
	for candidate in "$bench_root/releases" "$bench_root/../releases"; do
		if [[ -d "$candidate" ]]; then
			archive_root="$candidate"
			break
		fi
	done
fi

if [[ -z "$archive_root" || ! -d "$archive_root" ]]; then
	echo "release archive directory not found" >&2
	exit 1
fi

rm -f "$bench_root/voltcc" "$bench_root/voltcc.exe"
rm -rf "$bench_root/zig-out"
tmp_dir="$bench_root/tmp_extract/$target"
rm -rf "$tmp_dir"
mkdir -p "$tmp_dir"
mkdir -p "$bench_root/zig-out/bin"

archive_path="$(find "$archive_root" -maxdepth 1 -type f -name "voltcc-v*-${target}.tar.gz" | sort | tail -n 1)"
if [[ -n "$archive_path" ]]; then
	tar -xzf "$archive_path" -C "$tmp_dir"
	case "$target" in
		windows-*)
			bin_path="$(find "$tmp_dir" -type f -name "voltcc-${target}.exe" | head -n 1)"
			if [[ -z "$bin_path" || ! -f "$bin_path" ]]; then
				echo "prepared binary not found in archive: $archive_path" >&2
				exit 1
			fi
			cp "$bin_path" "$bench_root/voltcc.exe"
			cp "$bin_path" "$bench_root/zig-out/bin/voltcc.exe"
			cp "$bin_path" "$bench_root/zig-out/bin/voltcc"
			;;
		*)
			bin_path="$(find "$tmp_dir" -type f -name "voltcc-${target}" | head -n 1)"
			if [[ -z "$bin_path" || ! -f "$bin_path" ]]; then
				echo "prepared binary not found in archive: $archive_path" >&2
				exit 1
			fi
			cp "$bin_path" "$bench_root/voltcc"
			cp "$bin_path" "$bench_root/zig-out/bin/voltcc"
			chmod +x "$bench_root/voltcc"
			chmod +x "$bench_root/zig-out/bin/voltcc"
			;;
	esac
else
	case "$target" in
		linux-*|macos-*)
			dir_name="${target%%-*}"
			bin_path="$archive_root/$dir_name/voltcc-${target}"
			cp "$bin_path" "$bench_root/voltcc"
			cp "$bin_path" "$bench_root/zig-out/bin/voltcc"
			chmod +x "$bench_root/voltcc"
			chmod +x "$bench_root/zig-out/bin/voltcc"
			;;
		windows-*)
			bin_path="$archive_root/windows/voltcc-${target}.exe"
			cp "$bin_path" "$bench_root/voltcc.exe"
			cp "$bin_path" "$bench_root/zig-out/bin/voltcc.exe"
			cp "$bin_path" "$bench_root/zig-out/bin/voltcc"
			;;
		*)
			echo "unsupported target: $target" >&2
			exit 1
			;;
	esac
	if [[ ! -f "$bin_path" ]]; then
		echo "release binary not found: $bin_path" >&2
		exit 1
	fi
fi

echo "Prepared benchmark binary for $target"
