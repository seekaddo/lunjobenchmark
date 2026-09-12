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
Generated: 2026-09-12T23:53:41.773986+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0367s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1156s | -0.0064s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0804s | -0.0049s | improved |
| `lteNRRCC` | 0.1187s | 0.1233s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 47.4% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.6% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0344s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0923s | 0.0926s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0646s | +0.0011s | worse |
| `lteNRRCC` | 0.1251s | 0.1274s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.24 MB | 81.5% | 107.4% |
| `f1ap_rel18.6_specs` | 22.43 MB | 103.23 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.70 MB | 108.0% | 104.8% |
| `lteNRRCC` | 48.33 MB | 66.22 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0324s | 0.0277s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.0890s | 0.0876s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0617s | 0.0589s | +0.0028s | worse |
| `lteNRRCC` | 0.1164s | 0.0987s | +0.0177s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.65 MB | 76.9% | 103.8% |
| `f1ap_rel18.6_specs` | 34.49 MB | 163.50 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.21 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.82 MB | 102.80 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0514s | 0.0316s | +0.0198s | worse |
| `f1ap_rel18.6_specs` | 0.0704s | 0.0902s | -0.0198s | improved |
| `ngap_rel18.6_specs` | 0.0487s | 0.0595s | -0.0108s | improved |
| `lteNRRCC` | 0.0790s | 0.1019s | -0.0229s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.64 MB | 4.28 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.45 MB | 4.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.23 MB | 5.34 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.59 MB | 7.39 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0324s | +0.0079s | worse |
| `f1ap_rel18.6_specs` | 0.1126s | 0.0938s | +0.0188s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0655s | +0.0131s | worse |
| `lteNRRCC` | 0.1410s | 0.1123s | +0.0287s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.84 MB | 7.52 MB | 107.4% | 157.0% |
| `f1ap_rel18.6_specs` | 8.05 MB | 8.49 MB | 91.2% | 155.4% |
| `ngap_rel18.6_specs` | 7.63 MB | 7.70 MB | 157.9% | 160.7% |
| `lteNRRCC` | 8.18 MB | 52.01 MB | 155.2% | 154.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0414s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1135s | 0.1176s | -0.0041s | improved |
| `ngap_rel18.6_specs` | 0.0782s | 0.0804s | -0.0022s | improved |
| `lteNRRCC` | 0.1310s | 0.1300s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.73 MB | 0.0% | 157.4% |
| `f1ap_rel18.6_specs` | 9.82 MB | 164.18 MB | 161.2% | 226.0% |
| `ngap_rel18.6_specs` | 8.92 MB | 9.03 MB | 158.9% | 158.1% |
| `lteNRRCC` | 9.43 MB | 96.09 MB | 229.3% | 106.0% |
<!-- BENCH_RESULTS_END -->
