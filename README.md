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
Generated: 2026-03-24T10:58:41.394338+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0374s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1165s | 0.1151s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0799s | +0.0004s | worse |
| `lteNRRCC` | 0.1242s | 0.1209s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.72 MB | 53.55 MB | 28.0% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 105.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 114.8% | 105.6% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.8% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0369s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.0990s | 0.0952s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0681s | 0.0677s | +0.0004s | worse |
| `lteNRRCC` | 0.1198s | 0.1306s | -0.0108s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.52 MB | 36.07 MB | 90.9% | 111.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.18 MB | 110.3% | 105.1% |
| `ngap_rel18.6_specs` | 16.77 MB | 73.68 MB | 108.3% | 104.4% |
| `lteNRRCC` | 48.60 MB | 66.24 MB | 105.2% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0351s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1016s | 0.0902s | +0.0114s | worse |
| `ngap_rel18.6_specs` | 0.0703s | 0.0617s | +0.0086s | worse |
| `lteNRRCC` | 0.1183s | 0.1223s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.52 MB | 55.48 MB | 90.9% | 110.3% |
| `f1ap_rel18.6_specs` | 34.75 MB | 164.41 MB | 107.1% | 105.0% |
| `ngap_rel18.6_specs` | 24.40 MB | 117.71 MB | 108.7% | 106.8% |
| `lteNRRCC` | 74.99 MB | 102.88 MB | 105.4% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0310s | 0.0204s | +0.0106s | worse |
| `f1ap_rel18.6_specs` | 0.0783s | 0.0621s | +0.0162s | worse |
| `ngap_rel18.6_specs` | 0.0498s | 0.0403s | +0.0095s | worse |
| `lteNRRCC` | 0.1023s | 0.0683s | +0.0340s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.89 MB | 6.70 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.69 MB | 2.91 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 5.61 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.25 MB | 3.52 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0385s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1047s | +0.0063s | worse |
| `ngap_rel18.6_specs` | 0.0785s | 0.0732s | +0.0053s | worse |
| `lteNRRCC` | 0.1401s | 0.1369s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.33 MB | 7.64 MB | 83.0% | 103.9% |
| `f1ap_rel18.6_specs` | 8.38 MB | 8.56 MB | 226.6% | 109.8% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.88 MB | 103.0% | 92.6% |
| `lteNRRCC` | 51.85 MB | 70.57 MB | 107.7% | 156.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0384s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1062s | +0.0057s | worse |
| `ngap_rel18.6_specs` | 0.0753s | 0.0750s | +0.0003s | worse |
| `lteNRRCC` | 0.1273s | 0.1241s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.65 MB | 8.45 MB | 102.0% | 159.7% |
| `f1ap_rel18.6_specs` | 9.75 MB | 10.93 MB | 160.1% | 99.7% |
| `ngap_rel18.6_specs` | 9.27 MB | 10.30 MB | 94.2% | 106.3% |
| `lteNRRCC` | 9.36 MB | 93.70 MB | 210.4% | 106.2% |
<!-- BENCH_RESULTS_END -->
