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
Generated: 2026-03-24T22:41:07.721798+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0386s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1165s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0792s | 0.0803s | -0.0011s | improved |
| `lteNRRCC` | 0.1222s | 0.1242s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.71 MB | 53.55 MB | 23.7% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0348s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0990s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0668s | 0.0681s | -0.0013s | improved |
| `lteNRRCC` | 0.1289s | 0.1198s | +0.0091s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 35.97 MB | 26.3% | 110.3% |
| `f1ap_rel18.6_specs` | 21.98 MB | 103.16 MB | 108.8% | 105.0% |
| `ngap_rel18.6_specs` | 16.72 MB | 74.47 MB | 114.3% | 106.4% |
| `lteNRRCC` | 48.18 MB | 66.29 MB | 103.0% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0344s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0918s | 0.1016s | -0.0098s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0703s | -0.0064s | improved |
| `lteNRRCC` | 0.1183s | 0.1183s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 55.79 MB | 86.2% | 113.8% |
| `f1ap_rel18.6_specs` | 34.63 MB | 164.16 MB | 109.7% | 105.3% |
| `ngap_rel18.6_specs` | 24.51 MB | 117.33 MB | 111.1% | 109.1% |
| `lteNRRCC` | 74.84 MB | 102.92 MB | 105.0% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0216s | 0.0310s | -0.0094s | improved |
| `f1ap_rel18.6_specs` | 0.0655s | 0.0783s | -0.0128s | improved |
| `ngap_rel18.6_specs` | 0.0448s | 0.0498s | -0.0050s | improved |
| `lteNRRCC` | 0.0734s | 0.1023s | -0.0289s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.23 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.19 MB | 4.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.38 MB | 4.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.14 MB | 3.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0386s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1057s | 0.1110s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0731s | 0.0785s | -0.0054s | improved |
| `lteNRRCC` | 0.1437s | 0.1401s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.30 MB | 83.5% | 166.6% |
| `f1ap_rel18.6_specs` | 7.96 MB | 106.62 MB | 83.7% | 163.3% |
| `ngap_rel18.6_specs` | 7.86 MB | 7.53 MB | 114.8% | 168.2% |
| `lteNRRCC` | 49.55 MB | 69.22 MB | 165.0% | 110.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0384s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1119s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0773s | 0.0753s | +0.0020s | worse |
| `lteNRRCC` | 0.1254s | 0.1273s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.93 MB | 8.93 MB | 100.6% | 96.4% |
| `f1ap_rel18.6_specs` | 9.98 MB | 10.38 MB | 79.0% | 107.0% |
| `ngap_rel18.6_specs` | 8.94 MB | 9.22 MB | 160.9% | 77.0% |
| `lteNRRCC` | 8.55 MB | 98.75 MB | 78.8% | 152.8% |
<!-- BENCH_RESULTS_END -->
