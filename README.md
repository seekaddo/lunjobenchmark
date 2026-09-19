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
Generated: 2026-09-19T13:49:20.451487+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0361s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1109s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0753s | 0.0785s | -0.0032s | improved |
| `lteNRRCC` | 0.1182s | 0.1204s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 81.8% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0331s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0956s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0662s | 0.0658s | +0.0004s | worse |
| `lteNRRCC` | 0.1286s | 0.1175s | +0.0111s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.70 MB | 75.0% | 103.7% |
| `f1ap_rel18.6_specs` | 22.24 MB | 102.20 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 18.02 MB | 74.71 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.56 MB | 66.46 MB | 103.1% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0342s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0929s | 0.0901s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0622s | +0.0036s | worse |
| `lteNRRCC` | 0.1189s | 0.1159s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.38 MB | 55.09 MB | 75.0% | 103.6% |
| `f1ap_rel18.6_specs` | 35.10 MB | 164.53 MB | 103.4% | 103.6% |
| `ngap_rel18.6_specs` | 24.33 MB | 117.65 MB | 108.3% | 104.5% |
| `lteNRRCC` | 75.00 MB | 102.82 MB | 101.7% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0241s | 0.0464s | -0.0223s | improved |
| `f1ap_rel18.6_specs` | 0.0701s | 0.0720s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0479s | 0.0497s | -0.0018s | improved |
| `lteNRRCC` | 0.0750s | 0.0701s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.00 MB | 8.08 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.06 MB | 8.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.72 MB | 4.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.31 MB | 7.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0409s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1103s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0779s | 0.0778s | +0.0001s | worse |
| `lteNRRCC` | 0.1413s | 0.1408s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.91 MB | 7.34 MB | 0.0% | 159.9% |
| `f1ap_rel18.6_specs` | 7.95 MB | 7.95 MB | 163.9% | 97.5% |
| `ngap_rel18.6_specs` | 7.52 MB | 7.97 MB | 160.7% | 211.9% |
| `lteNRRCC` | 48.98 MB | 50.92 MB | 203.6% | 107.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0417s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1179s | -0.0051s | improved |
| `ngap_rel18.6_specs` | 0.0801s | 0.0818s | -0.0017s | improved |
| `lteNRRCC` | 0.1277s | 0.1328s | -0.0051s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.77 MB | 0.0% | 73.0% |
| `f1ap_rel18.6_specs` | 10.89 MB | 164.17 MB | 101.4% | 103.0% |
| `ngap_rel18.6_specs` | 8.93 MB | 9.25 MB | 78.2% | 78.7% |
| `lteNRRCC` | 9.21 MB | 98.73 MB | 88.7% | 109.4% |
<!-- BENCH_RESULTS_END -->
