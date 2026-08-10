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
Generated: 2026-08-10T11:13:32.325071+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0355s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1104s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0780s | 0.0771s | +0.0009s | worse |
| `lteNRRCC` | 0.1220s | 0.1198s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 79.2% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0349s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0909s | 0.0954s | -0.0045s | improved |
| `ngap_rel18.6_specs` | 0.0634s | 0.0692s | -0.0058s | improved |
| `lteNRRCC` | 0.1223s | 0.1305s | -0.0082s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.24 MB | 36.71 MB | 19.3% | 107.4% |
| `f1ap_rel18.6_specs` | 22.22 MB | 102.93 MB | 106.5% | 103.6% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.58 MB | 108.0% | 104.7% |
| `lteNRRCC` | 47.77 MB | 65.72 MB | 103.3% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0348s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0905s | 0.0927s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0648s | 0.0636s | +0.0012s | worse |
| `lteNRRCC` | 0.1169s | 0.1199s | -0.0030s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.26 MB | 54.38 MB | 15.2% | 107.7% |
| `f1ap_rel18.6_specs` | 34.62 MB | 164.66 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.19 MB | 117.69 MB | 104.2% | 102.4% |
| `lteNRRCC` | 74.70 MB | 102.54 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0484s | 0.0237s | +0.0247s | worse |
| `f1ap_rel18.6_specs` | 0.1005s | 0.0777s | +0.0228s | worse |
| `ngap_rel18.6_specs` | 0.0727s | 0.0490s | +0.0237s | worse |
| `lteNRRCC` | 0.1089s | 0.0762s | +0.0327s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.09 MB | 6.27 MB | 0.0% | 0.6% |
| `f1ap_rel18.6_specs` | 5.53 MB | 3.81 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.31 MB | 9.72 MB | 0.0% | 1.2% |
| `lteNRRCC` | 4.42 MB | 5.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0453s | -0.0073s | improved |
| `f1ap_rel18.6_specs` | 0.1049s | 0.1283s | -0.0234s | improved |
| `ngap_rel18.6_specs` | 0.0767s | 0.0872s | -0.0105s | improved |
| `lteNRRCC` | 0.1378s | 0.1589s | -0.0211s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.37 MB | 0.0% | 81.6% |
| `f1ap_rel18.6_specs` | 7.91 MB | 8.67 MB | 162.8% | 112.9% |
| `ngap_rel18.6_specs` | 8.12 MB | 7.55 MB | 232.2% | 163.5% |
| `lteNRRCC` | 49.78 MB | 52.00 MB | 107.2% | 162.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0403s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1117s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0823s | 0.0751s | +0.0072s | worse |
| `lteNRRCC` | 0.1313s | 0.1264s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.46 MB | 0.0% | 78.4% |
| `f1ap_rel18.6_specs` | 10.00 MB | 153.92 MB | 158.3% | 109.2% |
| `ngap_rel18.6_specs` | 8.84 MB | 9.12 MB | 157.2% | 92.2% |
| `lteNRRCC` | 8.81 MB | 91.57 MB | 95.2% | 150.8% |
<!-- BENCH_RESULTS_END -->
