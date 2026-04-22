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
Generated: 2026-04-22T22:55:44.779085+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0396s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.1165s | 0.1216s | -0.0051s | improved |
| `ngap_rel18.6_specs` | 0.0794s | 0.0843s | -0.0049s | improved |
| `lteNRRCC` | 0.1236s | 0.1275s | -0.0039s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 24.5% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0345s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0930s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0651s | 0.0654s | -0.0003s | improved |
| `lteNRRCC` | 0.1237s | 0.1278s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.80 MB | 36.70 MB | 25.8% | 110.3% |
| `f1ap_rel18.6_specs` | 22.37 MB | 103.38 MB | 112.1% | 106.9% |
| `ngap_rel18.6_specs` | 16.77 MB | 74.65 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.75 MB | 66.54 MB | 104.8% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0325s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0899s | 0.0895s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0626s | 0.0616s | +0.0010s | worse |
| `lteNRRCC` | 0.1171s | 0.1166s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.23 MB | 88.5% | 110.7% |
| `f1ap_rel18.6_specs` | 34.65 MB | 164.64 MB | 106.7% | 105.4% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.54 MB | 108.0% | 107.1% |
| `lteNRRCC` | 74.20 MB | 102.00 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0251s | 0.0322s | -0.0071s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1115s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0471s | 0.0847s | -0.0376s | improved |
| `lteNRRCC` | 0.1117s | 0.1027s | +0.0090s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.38 MB | 3.62 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.55 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.78 MB | 4.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 128 KB | 4.23 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0386s | -0.0047s | improved |
| `f1ap_rel18.6_specs` | 0.0926s | 0.1085s | -0.0159s | improved |
| `ngap_rel18.6_specs` | 0.0659s | 0.0755s | -0.0096s | improved |
| `lteNRRCC` | 0.1132s | 0.1378s | -0.0246s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.89 MB | 8.04 MB | 103.4% | 107.3% |
| `f1ap_rel18.6_specs` | 8.79 MB | 8.54 MB | 138.7% | 205.6% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.14 MB | 104.6% | 102.8% |
| `lteNRRCC` | 51.83 MB | 54.07 MB | 133.1% | 200.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0388s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1076s | 0.1115s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0749s | 0.0799s | -0.0050s | improved |
| `lteNRRCC` | 0.1274s | 0.1261s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.03 MB | 8.46 MB | 102.9% | 160.2% |
| `f1ap_rel18.6_specs` | 9.69 MB | 9.62 MB | 160.3% | 159.4% |
| `ngap_rel18.6_specs` | 10.63 MB | 9.15 MB | 221.9% | 94.7% |
| `lteNRRCC` | 73.38 MB | 72.90 MB | 110.5% | 158.0% |
<!-- BENCH_RESULTS_END -->
