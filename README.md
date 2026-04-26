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
Generated: 2026-04-26T10:53:23.166709+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0354s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1113s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0754s | +0.0022s | worse |
| `lteNRRCC` | 0.1241s | 0.1199s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 13.9% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0323s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0910s | 0.0943s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0633s | 0.0646s | -0.0013s | improved |
| `lteNRRCC` | 0.1221s | 0.1244s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 35.71 MB | 96.0% | 106.9% |
| `f1ap_rel18.6_specs` | 21.71 MB | 103.43 MB | 112.5% | 105.3% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.64 MB | 107.4% | 107.0% |
| `lteNRRCC` | 48.68 MB | 66.27 MB | 104.8% | 105.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0359s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.0967s | 0.1046s | -0.0079s | improved |
| `ngap_rel18.6_specs` | 0.0676s | 0.0734s | -0.0058s | improved |
| `lteNRRCC` | 0.1140s | 0.1195s | -0.0055s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.76 MB | 95.0% | 108.0% |
| `f1ap_rel18.6_specs` | 34.62 MB | 164.42 MB | 107.7% | 103.5% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.51 MB | 109.5% | 104.8% |
| `lteNRRCC` | 74.97 MB | 102.47 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0225s | 0.0198s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.0671s | 0.0668s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0451s | 0.0428s | +0.0023s | worse |
| `lteNRRCC` | 0.0775s | 0.0708s | +0.0067s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.17 MB | 4.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.88 MB | 2.73 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.27 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.95 MB | 4.20 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0323s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.1050s | 0.0901s | +0.0149s | worse |
| `ngap_rel18.6_specs` | 0.0738s | 0.0623s | +0.0115s | worse |
| `lteNRRCC` | 0.1379s | 0.1113s | +0.0266s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.31 MB | 7.50 MB | 81.2% | 104.8% |
| `f1ap_rel18.6_specs` | 7.96 MB | 8.43 MB | 103.5% | 110.2% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.88 MB | 162.0% | 104.0% |
| `lteNRRCC` | 51.52 MB | 51.65 MB | 160.4% | 160.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0388s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1183s | 0.1105s | +0.0078s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0784s | +0.0032s | worse |
| `lteNRRCC` | 0.1381s | 0.1270s | +0.0111s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.20 MB | 9.53 MB | 82.1% | 160.6% |
| `f1ap_rel18.6_specs` | 11.05 MB | 164.19 MB | 204.0% | 217.8% |
| `ngap_rel18.6_specs` | 9.41 MB | 9.32 MB | 81.6% | 163.2% |
| `lteNRRCC` | 70.20 MB | 77.83 MB | 157.4% | 160.9% |
<!-- BENCH_RESULTS_END -->
