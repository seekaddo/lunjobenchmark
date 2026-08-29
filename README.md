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
- `bench_results/`: latest and historical benchmark output, including raw console logs for each benchmark suite alongside the JSON summaries

## Assumptions

- The benchmark repo has access to release archives named like `voltcc-v<version>-<target>.tar.gz`.
- `preparebin.sh` prefers `./releases/` and falls back to `../releases/` for local nested-repo development.
- The copied upstream benchmark scripts execute the prepared binary from `./zig-out/bin/voltcc`, matching the local `test_semantic` script layout.

## Latest Results

<!-- BENCH_RESULTS_START -->
Generated: 2026-08-29T03:36:42.843239+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0356s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1134s | -0.0072s | improved |
| `ngap_rel18.6_specs` | 0.0726s | 0.0777s | -0.0051s | improved |
| `lteNRRCC` | 0.1149s | 0.1219s | -0.0070s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 19.5% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.4% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.8% | 102.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0373s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0978s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0668s | 0.0696s | -0.0028s | improved |
| `lteNRRCC` | 0.1295s | 0.1319s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.64 MB | 23.2% | 103.7% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.01 MB | 106.5% | 103.6% |
| `ngap_rel18.6_specs` | 18.02 MB | 74.65 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.75 MB | 66.03 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0239s | 0.0349s | -0.0110s | improved |
| `f1ap_rel18.6_specs` | 0.0829s | 0.0918s | -0.0089s | improved |
| `ngap_rel18.6_specs` | 0.0545s | 0.0643s | -0.0098s | improved |
| `lteNRRCC` | 0.0849s | 0.1179s | -0.0330s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.70 MB | 55.16 MB | 16.0% | 105.3% |
| `f1ap_rel18.6_specs` | 34.63 MB | 164.55 MB | 105.0% | 100.0% |
| `ngap_rel18.6_specs` | 24.14 MB | 117.22 MB | 105.9% | 100.0% |
| `lteNRRCC` | 74.05 MB | 102.45 MB | 102.5% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0224s | 0.0236s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0685s | 0.0998s | -0.0313s | improved |
| `ngap_rel18.6_specs` | 0.0564s | 0.0471s | +0.0093s | worse |
| `lteNRRCC` | 0.0813s | 0.0780s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.62 MB | 8.03 MB | 0.0% | 1.6% |
| `f1ap_rel18.6_specs` | 9.03 MB | 8.95 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.61 MB | 8.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.36 MB | 7.55 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0387s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1063s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0749s | 0.0737s | +0.0012s | worse |
| `lteNRRCC` | 0.1379s | 0.1371s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.45 MB | 7.57 MB | 0.0% | 159.5% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.04 MB | 163.9% | 164.8% |
| `ngap_rel18.6_specs` | 7.68 MB | 7.55 MB | 101.2% | 162.1% |
| `lteNRRCC` | 51.84 MB | 52.02 MB | 106.4% | 163.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0416s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.1041s | 0.1174s | -0.0133s | improved |
| `ngap_rel18.6_specs` | 0.0733s | 0.0844s | -0.0111s | improved |
| `lteNRRCC` | 0.1265s | 0.1306s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 8.66 MB | 0.0% | 161.4% |
| `f1ap_rel18.6_specs` | 10.31 MB | 11.27 MB | 112.2% | 234.3% |
| `ngap_rel18.6_specs` | 8.78 MB | 8.96 MB | 162.3% | 160.4% |
| `lteNRRCC` | 8.50 MB | 72.25 MB | 79.2% | 159.9% |
<!-- BENCH_RESULTS_END -->
