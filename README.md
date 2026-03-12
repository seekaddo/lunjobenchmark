# lunjobenchmark

Benchmarking `voltcc` parser, syntaxcheck, and validator-adjacent phases across supported release binaries.

## Layout

- `test_semantic/`: copy of only the upstream fixtures used by the benchmark scripts, with Objective Systems generated headers removed where present
- `releases/`: release archives or extracted binaries produced from `build_release.sh`
- `preparebin.sh`: extracts the native binary for the current runner into the repo root
- `scripts/refresh_releases.sh`: rebuilds the parent repo releases and copies the fresh `releases/` tree into this repo
- `run_benchmarks.py`: runs all benchmark suites and writes per-target JSON results
- `update_readme.py`: updates the results section from `bench_results`
- `bench_results/`: latest and historical benchmark output

## Assumptions

- The benchmark repo has access to release archives named like `voltcc-v<version>-<target>.tar.gz`.
- `preparebin.sh` prefers `./releases/` and falls back to `../releases/` for local nested-repo development.
- The benchmark scripts always execute the extracted binary from the current repo root: `./voltcc` or `./voltcc.exe`.

## Latest Results

<!-- BENCH_RESULTS_START -->
Generated: 2026-03-12T16:40:17.608018+00:00

### linux-aarch64

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0973s | n/a | n/a | new |
| `f1ap_rel18.6_specs` | 0.3009s | n/a | n/a | new |
| `ngap_rel18.6_specs` | 0.2197s | n/a | n/a | new |

### linux-i386

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0714s | n/a | n/a | new |
| `f1ap_rel18.6_specs` | 0.2046s | n/a | n/a | new |
| `ngap_rel18.6_specs` | 0.1499s | n/a | n/a | new |

### linux-x86_64

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0998s | n/a | n/a | new |
| `f1ap_rel18.6_specs` | 0.2643s | n/a | n/a | new |
| `ngap_rel18.6_specs` | 0.1925s | n/a | n/a | new |

### macos-aarch64

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0542s | n/a | n/a | new |
| `f1ap_rel18.6_specs` | 0.1603s | n/a | n/a | new |
| `ngap_rel18.6_specs` | 0.1263s | n/a | n/a | new |

### windows-i386

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0844s | n/a | n/a | new |
| `f1ap_rel18.6_specs` | 0.2469s | n/a | n/a | new |
| `ngap_rel18.6_specs` | 0.1782s | n/a | n/a | new |

### windows-x86_64

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0896s | n/a | n/a | new |
| `f1ap_rel18.6_specs` | 0.2767s | n/a | n/a | new |
| `ngap_rel18.6_specs` | 0.2086s | n/a | n/a | new |
<!-- BENCH_RESULTS_END -->
