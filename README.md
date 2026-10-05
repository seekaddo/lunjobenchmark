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
Generated: 2026-10-05T19:11:02.071350+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0359s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1164s | -0.0073s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0776s | -0.0025s | improved |
| `lteNRRCC` | 0.1185s | 0.1226s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 85.7% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 100.0% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0251s | 0.0273s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0708s | 0.0750s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0491s | 0.0521s | -0.0030s | improved |
| `lteNRRCC` | 0.0900s | 0.0998s | -0.0098s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 36.29 MB | 16.3% | 105.3% |
| `f1ap_rel18.6_specs` | 22.35 MB | 103.25 MB | 104.8% | 102.4% |
| `ngap_rel18.6_specs` | 18.20 MB | 74.58 MB | 105.9% | 103.0% |
| `lteNRRCC` | 48.55 MB | 66.48 MB | 102.2% | 101.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0342s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0971s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0666s | 0.0657s | +0.0009s | worse |
| `lteNRRCC` | 0.1215s | 0.1115s | +0.0100s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.67 MB | 55.87 MB | 84.0% | 107.4% |
| `f1ap_rel18.6_specs` | 34.13 MB | 164.49 MB | 103.4% | 103.6% |
| `ngap_rel18.6_specs` | 24.50 MB | 117.66 MB | 104.2% | 102.4% |
| `lteNRRCC` | 74.80 MB | 102.31 MB | 101.7% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0315s | 0.0388s | -0.0073s | improved |
| `f1ap_rel18.6_specs` | 0.1053s | 0.0948s | +0.0105s | worse |
| `ngap_rel18.6_specs` | 0.0689s | 0.0826s | -0.0137s | improved |
| `lteNRRCC` | 0.1218s | 0.1156s | +0.0062s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.77 MB | 6.61 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.06 MB | 8.53 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.81 MB | 5.91 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.02 MB | 8.06 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0345s | +0.0053s | worse |
| `f1ap_rel18.6_specs` | 0.1092s | 0.0938s | +0.0154s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0651s | +0.0115s | worse |
| `lteNRRCC` | 0.1295s | 0.1116s | +0.0179s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.43 MB | 8.06 MB | 0.0% | 121.8% |
| `f1ap_rel18.6_specs` | 8.63 MB | 8.63 MB | 120.4% | 119.2% |
| `ngap_rel18.6_specs` | 8.26 MB | 8.01 MB | 121.4% | 195.3% |
| `lteNRRCC` | 8.00 MB | 69.19 MB | 228.7% | 240.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0409s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1129s | 0.1136s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0825s | 0.0810s | +0.0015s | worse |
| `lteNRRCC` | 0.1275s | 0.1300s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 8.91 MB | 0.0% | 150.5% |
| `f1ap_rel18.6_specs` | 11.43 MB | 164.16 MB | 170.6% | 108.0% |
| `ngap_rel18.6_specs` | 9.21 MB | 9.12 MB | 154.5% | 153.9% |
| `lteNRRCC` | 8.59 MB | 92.61 MB | 77.0% | 210.8% |
<!-- BENCH_RESULTS_END -->
