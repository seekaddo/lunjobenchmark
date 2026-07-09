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
Generated: 2026-07-09T23:18:47.362057+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0378s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1171s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0765s | 0.0819s | -0.0054s | improved |
| `lteNRRCC` | 0.1210s | 0.1253s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 22.1% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.2% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0365s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0988s | -0.0058s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0674s | -0.0022s | improved |
| `lteNRRCC` | 0.1282s | 0.1315s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 36.69 MB | 78.6% | 107.1% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.36 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.56 MB | 73.94 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.62 MB | 66.30 MB | 104.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0353s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1142s | 0.0935s | +0.0207s | worse |
| `ngap_rel18.6_specs` | 0.0735s | 0.0703s | +0.0032s | worse |
| `lteNRRCC` | 0.1218s | 0.1204s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 55.70 MB | 76.9% | 103.6% |
| `f1ap_rel18.6_specs` | 34.63 MB | 164.52 MB | 107.1% | 104.9% |
| `ngap_rel18.6_specs` | 24.15 MB | 117.09 MB | 113.6% | 104.4% |
| `lteNRRCC` | 74.49 MB | 102.93 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0232s | +0.0147s | worse |
| `f1ap_rel18.6_specs` | 0.0765s | 0.0717s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0519s | 0.0566s | -0.0047s | improved |
| `lteNRRCC` | 0.0822s | 0.0894s | -0.0072s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.47 MB | 4.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.42 MB | 9.09 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.27 MB | 8.20 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.38 MB | 7.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0404s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1087s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0785s | 0.0790s | -0.0005s | improved |
| `lteNRRCC` | 0.1273s | 0.1388s | -0.0115s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.29 MB | 7.89 MB | 112.8% | 80.4% |
| `f1ap_rel18.6_specs` | 8.66 MB | 8.66 MB | 162.0% | 157.6% |
| `ngap_rel18.6_specs` | 8.29 MB | 8.23 MB | 162.6% | 183.9% |
| `lteNRRCC` | 8.02 MB | 8.34 MB | 160.5% | 161.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0388s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1072s | 0.1106s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0761s | 0.0758s | +0.0003s | worse |
| `lteNRRCC` | 0.1251s | 0.1279s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 10.61 MB | 157.8% | 115.5% |
| `f1ap_rel18.6_specs` | 9.82 MB | 9.82 MB | 161.8% | 161.0% |
| `ngap_rel18.6_specs` | 10.77 MB | 10.77 MB | 231.9% | 115.9% |
| `lteNRRCC` | 8.57 MB | 90.22 MB | 160.2% | 115.3% |
<!-- BENCH_RESULTS_END -->
