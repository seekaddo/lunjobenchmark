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
Generated: 2026-05-20T12:30:24.049292+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0364s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1141s | 0.1153s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0783s | 0.0797s | -0.0014s | improved |
| `lteNRRCC` | 0.1217s | 0.1228s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.90 MB | 53.55 MB | 25.3% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0355s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1005s | 0.0943s | +0.0062s | worse |
| `ngap_rel18.6_specs` | 0.0664s | 0.0665s | -0.0001s | improved |
| `lteNRRCC` | 0.1303s | 0.1292s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.79 MB | 36.52 MB | 23.5% | 110.7% |
| `f1ap_rel18.6_specs` | 21.94 MB | 103.46 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.62 MB | 73.61 MB | 111.1% | 107.0% |
| `lteNRRCC` | 48.64 MB | 66.46 MB | 103.1% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0335s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0897s | 0.0898s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0626s | 0.0624s | +0.0002s | worse |
| `lteNRRCC` | 0.1160s | 0.1168s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 55.63 MB | 20.2% | 110.7% |
| `f1ap_rel18.6_specs` | 34.14 MB | 164.50 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.24 MB | 112.0% | 104.8% |
| `lteNRRCC` | 74.69 MB | 102.39 MB | 103.4% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0205s | 0.0362s | -0.0157s | improved |
| `f1ap_rel18.6_specs` | 0.0722s | 0.1016s | -0.0294s | improved |
| `ngap_rel18.6_specs` | 0.0522s | 0.0595s | -0.0073s | improved |
| `lteNRRCC` | 0.0935s | 0.0886s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 192 KB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 3.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 1.34 MB | 1.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.28 MB | 4.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0395s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1087s | 0.1091s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0741s | +0.0018s | worse |
| `lteNRRCC` | 0.1371s | 0.1362s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.69 MB | 165.5% | 237.1% |
| `f1ap_rel18.6_specs` | 8.17 MB | 8.55 MB | 89.3% | 104.0% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.61 MB | 158.7% | 162.4% |
| `lteNRRCC` | 50.87 MB | 69.11 MB | 157.3% | 105.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0424s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.1076s | 0.1243s | -0.0167s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0871s | -0.0101s | improved |
| `lteNRRCC` | 0.1283s | 0.1416s | -0.0133s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.72 MB | 9.77 MB | 159.3% | 97.3% |
| `f1ap_rel18.6_specs` | 11.45 MB | 164.19 MB | 113.9% | 177.1% |
| `ngap_rel18.6_specs` | 8.95 MB | 10.54 MB | 80.4% | 227.5% |
| `lteNRRCC` | 8.62 MB | 75.75 MB | 79.0% | 157.0% |
<!-- BENCH_RESULTS_END -->
