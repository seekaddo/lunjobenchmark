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
Generated: 2026-06-01T16:13:02.468761+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0362s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1153s | 0.1128s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0778s | +0.0011s | worse |
| `lteNRRCC` | 0.1227s | 0.1182s | +0.0045s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 25.6% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 107.7% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0329s | +0.0039s | worse |
| `f1ap_rel18.6_specs` | 0.0990s | 0.0939s | +0.0051s | worse |
| `ngap_rel18.6_specs` | 0.0698s | 0.0649s | +0.0049s | worse |
| `lteNRRCC` | 0.1326s | 0.1154s | +0.0172s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.63 MB | 77.4% | 113.3% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.19 MB | 111.8% | 104.9% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.55 MB | 110.7% | 108.7% |
| `lteNRRCC` | 48.79 MB | 66.41 MB | 104.5% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0331s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0922s | 0.0893s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0637s | 0.0624s | +0.0013s | worse |
| `lteNRRCC` | 0.1184s | 0.1149s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 54.73 MB | 76.7% | 114.3% |
| `f1ap_rel18.6_specs` | 34.77 MB | 163.53 MB | 110.0% | 105.2% |
| `ngap_rel18.6_specs` | 24.12 MB | 117.44 MB | 112.0% | 104.5% |
| `lteNRRCC` | 75.02 MB | 102.62 MB | 106.8% | 102.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0312s | 0.0285s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.0661s | 0.0799s | -0.0138s | improved |
| `ngap_rel18.6_specs` | 0.0434s | 0.0488s | -0.0054s | improved |
| `lteNRRCC` | 0.0684s | 0.0796s | -0.0112s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 4.06 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.89 MB | 4.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.83 MB | 3.64 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.84 MB | 3.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0428s | 0.0397s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1044s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0748s | 0.0738s | +0.0010s | worse |
| `lteNRRCC` | 0.1260s | 0.1370s | -0.0110s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.96 MB | 7.81 MB | 117.6% | 119.2% |
| `f1ap_rel18.6_specs` | 8.54 MB | 8.79 MB | 242.2% | 235.0% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.29 MB | 243.4% | 236.1% |
| `lteNRRCC` | 8.47 MB | 8.03 MB | 116.1% | 236.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0410s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1158s | 0.1192s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0805s | 0.0820s | -0.0015s | improved |
| `lteNRRCC` | 0.1319s | 0.1376s | -0.0057s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.88 MB | 8.95 MB | 77.6% | 153.7% |
| `f1ap_rel18.6_specs` | 9.91 MB | 10.01 MB | 151.1% | 154.8% |
| `ngap_rel18.6_specs` | 9.28 MB | 9.22 MB | 153.0% | 76.0% |
| `lteNRRCC` | 8.88 MB | 90.15 MB | 75.3% | 148.3% |
<!-- BENCH_RESULTS_END -->
