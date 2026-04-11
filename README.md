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
Generated: 2026-04-11T10:43:13.605909+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0355s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1131s | 0.1109s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0758s | +0.0031s | worse |
| `lteNRRCC` | 0.1228s | 0.1226s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 5.8% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.9% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0315s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0931s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0648s | 0.0640s | +0.0008s | worse |
| `lteNRRCC` | 0.1260s | 0.1148s | +0.0112s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 35.96 MB | 32.5% | 113.8% |
| `f1ap_rel18.6_specs` | 22.14 MB | 102.91 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.61 MB | 114.8% | 106.8% |
| `lteNRRCC` | 48.52 MB | 66.18 MB | 104.8% | 105.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0330s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.0893s | 0.0886s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0631s | 0.0620s | +0.0011s | worse |
| `lteNRRCC` | 0.1162s | 0.1156s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.24 MB | 92.0% | 110.7% |
| `f1ap_rel18.6_specs` | 35.11 MB | 164.26 MB | 106.7% | 105.4% |
| `ngap_rel18.6_specs` | 24.58 MB | 117.32 MB | 116.0% | 106.8% |
| `lteNRRCC` | 74.80 MB | 102.57 MB | 106.9% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0200s | 0.0213s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0590s | 0.0646s | -0.0056s | improved |
| `ngap_rel18.6_specs` | 0.0402s | 0.0431s | -0.0029s | improved |
| `lteNRRCC` | 0.0679s | 0.0729s | -0.0050s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.09 MB | 4.27 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.33 MB | 4.92 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.12 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.97 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0406s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1163s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0868s | 0.0791s | +0.0077s | worse |
| `lteNRRCC` | 0.1306s | 0.1402s | -0.0096s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.03 MB | 8.04 MB | 116.4% | 116.9% |
| `f1ap_rel18.6_specs` | 8.66 MB | 8.66 MB | 120.4% | 117.1% |
| `ngap_rel18.6_specs` | 8.26 MB | 8.23 MB | 118.0% | 112.4% |
| `lteNRRCC` | 8.41 MB | 8.28 MB | 116.3% | 81.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0398s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1216s | 0.1135s | +0.0081s | worse |
| `ngap_rel18.6_specs` | 0.0842s | 0.0786s | +0.0056s | worse |
| `lteNRRCC` | 0.1402s | 0.1302s | +0.0100s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.92 MB | 9.64 MB | 167.5% | 157.5% |
| `f1ap_rel18.6_specs` | 10.06 MB | 164.18 MB | 163.1% | 162.9% |
| `ngap_rel18.6_specs` | 9.29 MB | 9.41 MB | 161.1% | 80.6% |
| `lteNRRCC` | 70.17 MB | 100.58 MB | 160.9% | 159.3% |
<!-- BENCH_RESULTS_END -->
