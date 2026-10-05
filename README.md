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
Generated: 2026-10-05T00:39:16.308749+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0355s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1164s | 0.1101s | +0.0063s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0772s | +0.0004s | worse |
| `lteNRRCC` | 0.1226s | 0.1192s | +0.0034s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 85.7% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0273s | 0.0345s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.0750s | 0.0935s | -0.0185s | improved |
| `ngap_rel18.6_specs` | 0.0521s | 0.0652s | -0.0131s | improved |
| `lteNRRCC` | 0.0998s | 0.1284s | -0.0286s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 36.27 MB | 25.4% | 104.8% |
| `f1ap_rel18.6_specs` | 21.62 MB | 103.34 MB | 104.3% | 102.2% |
| `ngap_rel18.6_specs` | 18.14 MB | 74.34 MB | 105.0% | 102.9% |
| `lteNRRCC` | 48.76 MB | 66.30 MB | 102.1% | 103.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0341s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0971s | 0.0899s | +0.0072s | worse |
| `ngap_rel18.6_specs` | 0.0657s | 0.0618s | +0.0039s | worse |
| `lteNRRCC` | 0.1115s | 0.1189s | -0.0074s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 55.21 MB | 73.9% | 104.2% |
| `f1ap_rel18.6_specs` | 34.66 MB | 163.77 MB | 104.0% | 101.8% |
| `ngap_rel18.6_specs` | 24.18 MB | 117.26 MB | 104.8% | 102.4% |
| `lteNRRCC` | 74.92 MB | 102.69 MB | 100.0% | 101.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0306s | +0.0082s | worse |
| `f1ap_rel18.6_specs` | 0.0948s | 0.1277s | -0.0329s | improved |
| `ngap_rel18.6_specs` | 0.0826s | 0.0732s | +0.0094s | worse |
| `lteNRRCC` | 0.1156s | 0.0985s | +0.0171s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.95 MB | 6.06 MB | 0.0% | 1.2% |
| `f1ap_rel18.6_specs` | 7.55 MB | 3.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.52 MB | 5.64 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.09 MB | 4.52 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0408s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0938s | 0.1081s | -0.0143s | improved |
| `ngap_rel18.6_specs` | 0.0651s | 0.0762s | -0.0111s | improved |
| `lteNRRCC` | 0.1116s | 0.1395s | -0.0279s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.28 MB | 8.47 MB | 115.2% | 96.7% |
| `f1ap_rel18.6_specs` | 9.02 MB | 9.02 MB | 112.1% | 97.9% |
| `ngap_rel18.6_specs` | 8.34 MB | 8.52 MB | 193.3% | 195.4% |
| `lteNRRCC` | 8.72 MB | 66.02 MB | 128.2% | 126.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0426s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1167s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0810s | 0.0807s | +0.0003s | worse |
| `lteNRRCC` | 0.1300s | 0.1361s | -0.0061s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 9.12 MB | 0.0% | 92.5% |
| `f1ap_rel18.6_specs` | 9.79 MB | 11.81 MB | 153.6% | 221.1% |
| `ngap_rel18.6_specs` | 8.94 MB | 9.25 MB | 153.4% | 153.0% |
| `lteNRRCC` | 9.97 MB | 93.62 MB | 221.4% | 105.7% |
<!-- BENCH_RESULTS_END -->
