from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time


def format_output(fmt: str, elapsed: float, user: float, sys_time: float, cpu_pct: float, rss_kb: int) -> str:
    return (
        fmt.replace("%e", f"{elapsed:.6f}")
        .replace("%U", f"{user:.6f}")
        .replace("%S", f"{sys_time:.6f}")
        .replace("%P", f"{cpu_pct:.1f}%")
        .replace("%M", str(rss_kb))
    )


def run_windows(command: list[str]) -> tuple[int, float, float, float, int]:
    import ctypes
    from ctypes import wintypes

    class FILETIME(ctypes.Structure):
        _fields_ = [
            ("dwLowDateTime", wintypes.DWORD),
            ("dwHighDateTime", wintypes.DWORD),
        ]

    class PROCESS_MEMORY_COUNTERS(ctypes.Structure):
        _fields_ = [
            ("cb", wintypes.DWORD),
            ("PageFaultCount", wintypes.DWORD),
            ("PeakWorkingSetSize", ctypes.c_size_t),
            ("WorkingSetSize", ctypes.c_size_t),
            ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
            ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
            ("PagefileUsage", ctypes.c_size_t),
            ("PeakPagefileUsage", ctypes.c_size_t),
        ]

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    psapi = ctypes.WinDLL("psapi", use_last_error=True)

    proc = subprocess.Popen(command, stdout=sys.stdout, stderr=sys.stderr)
    start = time.perf_counter()
    rc = proc.wait()
    elapsed = time.perf_counter() - start

    creation = FILETIME()
    exit_time = FILETIME()
    kernel = FILETIME()
    user = FILETIME()
    if not kernel32.GetProcessTimes(int(proc._handle), ctypes.byref(creation), ctypes.byref(exit_time), ctypes.byref(kernel), ctypes.byref(user)):  # type: ignore[attr-defined]
        raise OSError(ctypes.get_last_error(), "GetProcessTimes failed")

    pmc = PROCESS_MEMORY_COUNTERS()
    pmc.cb = ctypes.sizeof(PROCESS_MEMORY_COUNTERS)
    if not psapi.GetProcessMemoryInfo(int(proc._handle), ctypes.byref(pmc), pmc.cb):  # type: ignore[attr-defined]
        raise OSError(ctypes.get_last_error(), "GetProcessMemoryInfo failed")

    def filetime_to_seconds(value: FILETIME) -> float:
        total = (value.dwHighDateTime << 32) | value.dwLowDateTime
        return total / 10_000_000.0

    user_sec = filetime_to_seconds(user)
    sys_sec = filetime_to_seconds(kernel)
    cpu_pct = ((user_sec + sys_sec) / elapsed * 100.0) if elapsed > 0 else 0.0
    rss_kb = int(pmc.PeakWorkingSetSize / 1024)
    return rc, elapsed, user_sec, sys_sec, rss_kb


def run_posix(command: list[str]) -> tuple[int, float, float, float, int]:
    import resource

    start = time.perf_counter()
    proc = subprocess.run(command, stdout=sys.stdout, stderr=sys.stderr)
    elapsed = time.perf_counter() - start
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    user_sec = usage.ru_utime
    sys_sec = usage.ru_stime
    rss_kb = int(getattr(usage, "ru_maxrss", 0))
    return proc.returncode, elapsed, user_sec, sys_sec, rss_kb


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-f", dest="fmt", default=None)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    command = args.command
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        print("time: missing command", file=sys.stderr)
        return 1

    if os.name == "nt":
        rc, elapsed, user_sec, sys_sec, rss_kb = run_windows(command)
    else:
        rc, elapsed, user_sec, sys_sec, rss_kb = run_posix(command)

    cpu_pct = ((user_sec + sys_sec) / elapsed * 100.0) if elapsed > 0 else 0.0
    if args.fmt:
        print(format_output(args.fmt, elapsed, user_sec, sys_sec, cpu_pct, rss_kb), file=sys.stderr)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
