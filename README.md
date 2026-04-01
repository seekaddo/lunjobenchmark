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
Generated: 2026-04-01T22:48:36.448530+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0390s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1237s | -0.0128s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0845s | -0.0075s | improved |
| `lteNRRCC` | 0.1193s | 0.1290s | -0.0097s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 19.0% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 116.7% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 105.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0364s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0988s | 0.0942s | +0.0046s | worse |
| `ngap_rel18.6_specs` | 0.0697s | 0.0658s | +0.0039s | worse |
| `lteNRRCC` | 0.1338s | 0.1259s | +0.0079s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.00 MB | 89.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.36 MB | 111.8% | 104.8% |
| `ngap_rel18.6_specs` | 16.47 MB | 74.58 MB | 114.8% | 106.4% |
| `lteNRRCC` | 48.58 MB | 66.23 MB | 103.0% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0323s | 0.0354s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.0883s | 0.1014s | -0.0131s | improved |
| `ngap_rel18.6_specs` | 0.0615s | 0.0698s | -0.0083s | improved |
| `lteNRRCC` | 0.1148s | 0.1165s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.15 MB | 55.80 MB | 15.3% | 111.5% |
| `f1ap_rel18.6_specs` | 35.16 MB | 164.24 MB | 106.9% | 105.6% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.66 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.59 MB | 102.91 MB | 105.2% | 104.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0194s | 0.0236s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.0591s | 0.0589s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0404s | 0.0403s | +0.0001s | worse |
| `lteNRRCC` | 0.0677s | 0.0680s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 3.89 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.12 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.95 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.80 MB | 3.73 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0392s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1043s | 0.1083s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0725s | 0.0751s | -0.0026s | improved |
| `lteNRRCC` | 0.1346s | 0.1370s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.28 MB | 7.43 MB | 165.8% | 164.7% |
| `f1ap_rel18.6_specs` | 7.96 MB | 8.03 MB | 82.8% | 165.9% |
| `ngap_rel18.6_specs` | 7.46 MB | 7.54 MB | 170.8% | 82.8% |
| `lteNRRCC` | 49.76 MB | 70.55 MB | 116.1% | 107.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0496s | -0.0118s | improved |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1393s | -0.0259s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.1013s | -0.0237s | improved |
| `lteNRRCC` | 0.1249s | 0.1506s | -0.0257s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.51 MB | 8.64 MB | 160.8% | 172.1% |
| `f1ap_rel18.6_specs` | 9.48 MB | 9.80 MB | 161.8% | 163.1% |
| `ngap_rel18.6_specs` | 8.82 MB | 10.68 MB | 160.0% | 235.6% |
| `lteNRRCC` | 9.35 MB | 73.00 MB | 115.9% | 160.5% |
<!-- BENCH_RESULTS_END -->
