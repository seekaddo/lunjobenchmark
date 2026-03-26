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
Generated: 2026-03-26T22:39:15.702415+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0371s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1166s | 0.1139s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0811s | 0.0790s | +0.0021s | worse |
| `lteNRRCC` | 0.1239s | 0.1219s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.90 MB | 53.55 MB | 6.8% | 106.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 105.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.6% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.9% | 105.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0355s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0922s | 0.0936s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0685s | -0.0031s | improved |
| `lteNRRCC` | 0.1272s | 0.1285s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.26 MB | 25.0% | 111.1% |
| `f1ap_rel18.6_specs` | 22.23 MB | 102.84 MB | 106.2% | 105.3% |
| `ngap_rel18.6_specs` | 16.67 MB | 74.30 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.46 MB | 66.23 MB | 104.7% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0333s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1017s | 0.0890s | +0.0127s | worse |
| `ngap_rel18.6_specs` | 0.0711s | 0.0609s | +0.0102s | worse |
| `lteNRRCC` | 0.1229s | 0.1149s | +0.0080s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.21 MB | 55.77 MB | 25.6% | 107.7% |
| `f1ap_rel18.6_specs` | 34.42 MB | 164.44 MB | 107.4% | 103.4% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.49 MB | 114.3% | 102.3% |
| `lteNRRCC` | 74.77 MB | 102.97 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0203s | 0.0192s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0687s | 0.0592s | +0.0095s | worse |
| `ngap_rel18.6_specs` | 0.0453s | 0.0401s | +0.0052s | worse |
| `lteNRRCC` | 0.0728s | 0.0677s | +0.0051s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.05 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.19 MB | 1.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.00 MB | 3.58 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.97 MB | 3.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0429s | 0.0389s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1064s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0761s | +0.0029s | worse |
| `lteNRRCC` | 0.1401s | 0.1380s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.05 MB | 7.56 MB | 225.2% | 158.6% |
| `f1ap_rel18.6_specs` | 8.43 MB | 8.51 MB | 90.1% | 94.6% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.08 MB | 220.8% | 154.5% |
| `lteNRRCC` | 50.15 MB | 52.11 MB | 155.0% | 155.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0398s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1095s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0778s | -0.0023s | improved |
| `lteNRRCC` | 0.1256s | 0.1276s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.44 MB | 10.18 MB | 165.0% | 119.0% |
| `f1ap_rel18.6_specs` | 9.54 MB | 11.25 MB | 163.6% | 118.2% |
| `ngap_rel18.6_specs` | 10.55 MB | 8.82 MB | 117.1% | 83.2% |
| `lteNRRCC` | 73.75 MB | 86.71 MB | 161.5% | 160.6% |
<!-- BENCH_RESULTS_END -->
