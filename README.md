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
Generated: 2026-10-11T00:47:03.997714+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0362s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1134s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0771s | -0.0019s | improved |
| `lteNRRCC` | 0.1183s | 0.1211s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.92 MB | 53.55 MB | 70.8% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 104.3% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0348s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0948s | 0.0947s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0671s | 0.0673s | -0.0002s | improved |
| `lteNRRCC` | 0.1287s | 0.1291s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.51 MB | 74.1% | 107.4% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.29 MB | 103.2% | 103.4% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.65 MB | 103.6% | 104.8% |
| `lteNRRCC` | 47.52 MB | 66.29 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0368s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1014s | 0.0963s | +0.0051s | worse |
| `ngap_rel18.6_specs` | 0.0722s | 0.0651s | +0.0071s | worse |
| `lteNRRCC` | 0.1189s | 0.1207s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 55.67 MB | 85.0% | 108.0% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.61 MB | 103.8% | 100.0% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.86 MB | 105.0% | 102.3% |
| `lteNRRCC` | 74.98 MB | 102.95 MB | 101.8% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0272s | 0.0275s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0718s | 0.0968s | -0.0250s | improved |
| `ngap_rel18.6_specs` | 0.0496s | 0.0589s | -0.0093s | improved |
| `lteNRRCC` | 0.0901s | 0.0926s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.84 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.66 MB | 3.77 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.02 MB | 4.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.41 MB | 4.12 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0403s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1115s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0773s | -0.0011s | improved |
| `lteNRRCC` | 0.1459s | 0.1402s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.29 MB | 7.54 MB | 0.0% | 156.3% |
| `f1ap_rel18.6_specs` | 8.34 MB | 8.71 MB | 79.5% | 198.4% |
| `ngap_rel18.6_specs` | 7.78 MB | 7.66 MB | 79.3% | 79.2% |
| `lteNRRCC` | 51.00 MB | 70.53 MB | 153.9% | 113.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0346s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.1216s | 0.0987s | +0.0229s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0719s | +0.0069s | worse |
| `lteNRRCC` | 0.1285s | 0.1116s | +0.0169s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.07 MB | 8.46 MB | 0.0% | 176.0% |
| `f1ap_rel18.6_specs` | 10.31 MB | 11.30 MB | 97.8% | 117.6% |
| `ngap_rel18.6_specs` | 8.74 MB | 10.60 MB | 80.6% | 114.7% |
| `lteNRRCC` | 72.68 MB | 74.12 MB | 156.6% | 159.9% |
<!-- BENCH_RESULTS_END -->
