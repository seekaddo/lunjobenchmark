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
Generated: 2026-07-31T12:05:26.113041+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0346s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1078s | +0.0039s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0749s | +0.0018s | worse |
| `lteNRRCC` | 0.1210s | 0.1190s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 15.3% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0362s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0978s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0655s | 0.0675s | -0.0020s | improved |
| `lteNRRCC` | 0.1286s | 0.1409s | -0.0123s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.32 MB | 76.9% | 103.8% |
| `f1ap_rel18.6_specs` | 22.16 MB | 103.23 MB | 106.5% | 103.6% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.66 MB | 108.0% | 102.4% |
| `lteNRRCC` | 47.66 MB | 66.33 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0360s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0917s | 0.0954s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0645s | 0.0672s | -0.0027s | improved |
| `lteNRRCC` | 0.1184s | 0.1302s | -0.0118s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.35 MB | 55.86 MB | 83.3% | 103.7% |
| `f1ap_rel18.6_specs` | 33.90 MB | 163.57 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.23 MB | 117.20 MB | 104.2% | 102.4% |
| `lteNRRCC` | 74.71 MB | 102.53 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0239s | 0.0305s | -0.0066s | improved |
| `f1ap_rel18.6_specs` | 0.0680s | 0.1039s | -0.0359s | improved |
| `ngap_rel18.6_specs` | 0.0471s | 0.0756s | -0.0285s | improved |
| `lteNRRCC` | 0.0773s | 0.1141s | -0.0368s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.20 MB | 4.50 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.66 MB | 4.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.78 MB | 4.17 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.39 MB | 5.06 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0292s | 0.0378s | -0.0086s | improved |
| `f1ap_rel18.6_specs` | 0.0826s | 0.1041s | -0.0215s | improved |
| `ngap_rel18.6_specs` | 0.0594s | 0.0728s | -0.0134s | improved |
| `lteNRRCC` | 0.0909s | 0.1366s | -0.0457s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.62 MB | 0.0% | 119.1% |
| `f1ap_rel18.6_specs` | 13.00 MB | 15.90 MB | 101.7% | 159.2% |
| `ngap_rel18.6_specs` | 17.92 MB | 9.36 MB | 62.0% | 141.5% |
| `lteNRRCC` | 16.30 MB | 19.24 MB | 136.3% | 114.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0461s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1311s | -0.0205s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0906s | -0.0140s | improved |
| `lteNRRCC` | 0.1273s | 0.1377s | -0.0104s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.65 MB | 0.0% | 78.7% |
| `f1ap_rel18.6_specs` | 11.39 MB | 161.36 MB | 226.9% | 106.9% |
| `ngap_rel18.6_specs` | 9.27 MB | 9.55 MB | 158.4% | 100.7% |
| `lteNRRCC` | 8.74 MB | 101.68 MB | 77.0% | 155.8% |
<!-- BENCH_RESULTS_END -->
