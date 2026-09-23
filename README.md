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
Generated: 2026-09-23T00:13:56.023845+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0353s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1096s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0755s | 0.0753s | +0.0002s | worse |
| `lteNRRCC` | 0.1196s | 0.1192s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 12.2% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0365s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.0958s | 0.0982s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0655s | 0.0696s | -0.0041s | improved |
| `lteNRRCC` | 0.1179s | 0.1317s | -0.0138s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 36.37 MB | 81.0% | 104.2% |
| `f1ap_rel18.6_specs` | 21.93 MB | 103.00 MB | 103.7% | 101.8% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.71 MB | 104.8% | 102.4% |
| `lteNRRCC` | 48.70 MB | 66.53 MB | 101.8% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0311s | 0.0337s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0941s | 0.0905s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0643s | 0.0630s | +0.0013s | worse |
| `lteNRRCC` | 0.0958s | 0.1179s | -0.0221s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 55.12 MB | 21.4% | 100.0% |
| `f1ap_rel18.6_specs` | 34.79 MB | 164.66 MB | 100.0% | 100.0% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.43 MB | 105.9% | 102.6% |
| `lteNRRCC` | 74.79 MB | 102.55 MB | 102.2% | 101.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0310s | +0.0052s | worse |
| `f1ap_rel18.6_specs` | 0.0950s | 0.1063s | -0.0113s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0717s | -0.0077s | improved |
| `lteNRRCC` | 0.1141s | 0.0860s | +0.0281s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.77 MB | 7.08 MB | 0.0% | 1.2% |
| `f1ap_rel18.6_specs` | 3.12 MB | 768 KB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.41 MB | 3.72 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.97 MB | 6.55 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0411s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.1066s | 0.1150s | -0.0084s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0800s | -0.0057s | improved |
| `lteNRRCC` | 0.1363s | 0.1431s | -0.0068s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.65 MB | 7.36 MB | 0.0% | 162.2% |
| `f1ap_rel18.6_specs` | 8.07 MB | 7.94 MB | 99.7% | 161.1% |
| `ngap_rel18.6_specs` | 8.01 MB | 7.44 MB | 119.0% | 167.2% |
| `lteNRRCC` | 51.80 MB | 54.79 MB | 164.0% | 109.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0385s | +0.0038s | worse |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1142s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0828s | 0.0756s | +0.0072s | worse |
| `lteNRRCC` | 0.1321s | 0.1263s | +0.0058s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 9.50 MB | 0.0% | 150.9% |
| `f1ap_rel18.6_specs` | 10.48 MB | 164.16 MB | 139.0% | 189.2% |
| `ngap_rel18.6_specs` | 9.18 MB | 9.18 MB | 143.7% | 149.0% |
| `lteNRRCC` | 8.66 MB | 95.12 MB | 152.9% | 144.4% |
<!-- BENCH_RESULTS_END -->
