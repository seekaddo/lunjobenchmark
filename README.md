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
Generated: 2026-08-03T12:57:36.800701+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0345s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1081s | 0.1117s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0754s | -0.0011s | improved |
| `lteNRRCC` | 0.1189s | 0.1196s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 78.3% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.3% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0349s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0962s | 0.0931s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0677s | 0.0658s | +0.0019s | worse |
| `lteNRRCC` | 0.1302s | 0.1245s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 36.42 MB | 75.0% | 107.1% |
| `f1ap_rel18.6_specs` | 22.39 MB | 103.46 MB | 106.2% | 101.7% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.06 MB | 107.7% | 104.5% |
| `lteNRRCC` | 48.82 MB | 66.42 MB | 103.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0366s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0933s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0651s | 0.0658s | -0.0007s | improved |
| `lteNRRCC` | 0.1187s | 0.1180s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.25 MB | 55.57 MB | 13.3% | 107.4% |
| `f1ap_rel18.6_specs` | 34.65 MB | 164.34 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.23 MB | 117.80 MB | 104.2% | 102.4% |
| `lteNRRCC` | 74.32 MB | 102.95 MB | 101.7% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0183s | 0.0217s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.0774s | 0.0657s | +0.0117s | worse |
| `ngap_rel18.6_specs` | 0.0516s | 0.0453s | +0.0063s | worse |
| `lteNRRCC` | 0.0917s | 0.0758s | +0.0159s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.59 MB | 4.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.02 MB | 11.08 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.78 MB | 8.45 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.58 MB | 4.25 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0411s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1118s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0780s | +0.0010s | worse |
| `lteNRRCC` | 0.1394s | 0.1396s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.62 MB | 7.57 MB | 107.8% | 156.4% |
| `f1ap_rel18.6_specs` | 8.67 MB | 8.18 MB | 215.5% | 78.6% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.99 MB | 79.1% | 155.5% |
| `lteNRRCC` | 8.04 MB | 70.55 MB | 89.4% | 154.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0378s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.1215s | 0.1072s | +0.0143s | worse |
| `ngap_rel18.6_specs` | 0.0849s | 0.0739s | +0.0110s | worse |
| `lteNRRCC` | 0.1370s | 0.1252s | +0.0118s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.93 MB | 9.65 MB | 0.0% | 161.2% |
| `f1ap_rel18.6_specs` | 10.11 MB | 164.18 MB | 80.2% | 107.8% |
| `ngap_rel18.6_specs` | 9.45 MB | 10.09 MB | 161.9% | 157.5% |
| `lteNRRCC` | 9.21 MB | 81.18 MB | 90.0% | 208.4% |
<!-- BENCH_RESULTS_END -->
