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
Generated: 2026-04-26T22:49:55.358801+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0368s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1183s | 0.1128s | +0.0055s | worse |
| `ngap_rel18.6_specs` | 0.0797s | 0.0776s | +0.0021s | worse |
| `lteNRRCC` | 0.1227s | 0.1241s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.94 MB | 53.55 MB | 28.2% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 105.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0337s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0988s | 0.0910s | +0.0078s | worse |
| `ngap_rel18.6_specs` | 0.0655s | 0.0633s | +0.0022s | worse |
| `lteNRRCC` | 0.1271s | 0.1221s | +0.0050s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 35.72 MB | 20.3% | 110.7% |
| `f1ap_rel18.6_specs` | 21.89 MB | 103.23 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 16.64 MB | 73.94 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.07 MB | 66.39 MB | 104.7% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0329s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0967s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0662s | 0.0676s | -0.0014s | improved |
| `lteNRRCC` | 0.1182s | 0.1140s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.29 MB | 55.63 MB | 30.7% | 114.3% |
| `f1ap_rel18.6_specs` | 34.44 MB | 164.73 MB | 110.0% | 105.2% |
| `ngap_rel18.6_specs` | 24.32 MB | 117.25 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.52 MB | 102.97 MB | 105.0% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0293s | 0.0225s | +0.0068s | worse |
| `f1ap_rel18.6_specs` | 0.0695s | 0.0671s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0452s | 0.0451s | +0.0001s | worse |
| `lteNRRCC` | 0.0689s | 0.0775s | -0.0086s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.06 MB | 3.39 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.41 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.95 MB | 4.20 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.38 MB | 3.53 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0387s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1057s | 0.1050s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0746s | 0.0738s | +0.0008s | worse |
| `lteNRRCC` | 0.1283s | 0.1379s | -0.0096s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.98 MB | 81.7% | 118.6% |
| `f1ap_rel18.6_specs` | 8.54 MB | 8.54 MB | 120.8% | 119.5% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.05 MB | 241.3% | 120.9% |
| `lteNRRCC` | 8.35 MB | 70.55 MB | 118.2% | 121.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0414s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1183s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0816s | -0.0057s | improved |
| `lteNRRCC` | 0.1286s | 0.1381s | -0.0095s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.94 MB | 8.94 MB | 103.3% | 168.2% |
| `f1ap_rel18.6_specs` | 10.28 MB | 163.95 MB | 151.4% | 152.2% |
| `ngap_rel18.6_specs` | 8.96 MB | 9.32 MB | 78.1% | 152.0% |
| `lteNRRCC` | 73.35 MB | 96.01 MB | 150.0% | 152.4% |
<!-- BENCH_RESULTS_END -->
