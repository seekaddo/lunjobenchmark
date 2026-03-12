# lunjobenchmark

Benchmarking `voltcc` parser, syntaxcheck, and validator-adjacent phases across supported release binaries.

## Layout

- `test_semantic/`: copy of only the upstream fixtures used by the benchmark scripts, with Objective Systems generated headers removed where present
- `releases/`: release archives or extracted binaries produced from `build_release.sh`
- `preparebin.sh`: extracts the native binary for the current runner and places it where the copied benchmark scripts expect it
- `scripts/refresh_releases.sh`: rebuilds the parent repo releases and copies the fresh `releases/` tree into this repo
- `run_benchmarks.sh`: runs the copied upstream benchmark scripts and writes per-target JSON results
- `collect_benchmark_results.py`: parses the copied benchmark script logs into summary JSON
- `update_readme.py`: updates the results section from `bench_results`
- `bench_results/`: latest and historical benchmark output

## Assumptions

- The benchmark repo has access to release archives named like `voltcc-v<version>-<target>.tar.gz`.
- `preparebin.sh` prefers `./releases/` and falls back to `../releases/` for local nested-repo development.
- The copied upstream benchmark scripts execute the prepared binary from `./zig-out/bin/voltcc`, matching the local `test_semantic` script layout.

## Latest Results

<!-- BENCH_RESULTS_START -->
Generated: 2026-03-12T17:43:11.716078+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0980s | 0.1005s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.3062s | 0.3098s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.2180s | 0.2304s | -0.0124s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.62 MB | 5.52 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.56 MB | 471.37 MB | 0.0% | 91.6% |
| `ngap_rel18.6_specs` | 5.94 MB | 240.77 MB | 0.0% | 91.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0735s | 0.0727s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1991s | 0.2039s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.1453s | 0.1499s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.02 MB | 5.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.78 MB | 245.13 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 5.53 MB | 251.86 MB | 0.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0896s | 0.0711s | +0.0185s | worse |
| `f1ap_rel18.6_specs` | 0.2645s | 0.1902s | +0.0743s | worse |
| `ngap_rel18.6_specs` | 0.1925s | 0.1411s | +0.0514s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.23 MB | 5.70 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.82 MB | 521.41 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 6.23 MB | 247.36 MB | 0.0% | 91.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0528s | 0.0610s | -0.0082s | improved |
| `f1ap_rel18.6_specs` | 0.1650s | 0.1721s | -0.0071s | improved |
| `ngap_rel18.6_specs` | 0.1665s | 0.1223s | +0.0442s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.64 MB | 6.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.00 MB | 8.30 MB | 0.7% | 0.0% |
| `ngap_rel18.6_specs` | 9.14 MB | 9.08 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
