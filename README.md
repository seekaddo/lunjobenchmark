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
Generated: 2026-04-23T11:15:48.661813+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0372s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1165s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0796s | 0.0794s | +0.0002s | worse |
| `lteNRRCC` | 0.1231s | 0.1236s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 12.3% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 105.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 107.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0347s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0930s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0656s | 0.0651s | +0.0005s | worse |
| `lteNRRCC` | 0.1281s | 0.1237s | +0.0044s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.62 MB | 36.52 MB | 17.9% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.34 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.59 MB | 74.29 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.55 MB | 65.96 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0333s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0899s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0626s | +0.0003s | worse |
| `lteNRRCC` | 0.1181s | 0.1171s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.51 MB | 92.3% | 110.7% |
| `f1ap_rel18.6_specs` | 34.25 MB | 164.45 MB | 110.0% | 105.3% |
| `ngap_rel18.6_specs` | 24.07 MB | 117.82 MB | 116.0% | 107.0% |
| `lteNRRCC` | 74.68 MB | 102.59 MB | 105.2% | 105.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0197s | 0.0251s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.0593s | 0.1097s | -0.0504s | improved |
| `ngap_rel18.6_specs` | 0.0415s | 0.0471s | -0.0056s | improved |
| `lteNRRCC` | 0.0682s | 0.1117s | -0.0435s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.03 MB | 3.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.05 MB | 3.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.94 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0413s | 0.0339s | +0.0074s | worse |
| `f1ap_rel18.6_specs` | 0.1129s | 0.0926s | +0.0203s | worse |
| `ngap_rel18.6_specs` | 0.0801s | 0.0659s | +0.0142s | worse |
| `lteNRRCC` | 0.1415s | 0.1132s | +0.0283s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.38 MB | 7.73 MB | 127.5% | 80.8% |
| `f1ap_rel18.6_specs` | 8.55 MB | 8.86 MB | 166.9% | 78.6% |
| `ngap_rel18.6_specs` | 8.43 MB | 8.24 MB | 156.6% | 80.3% |
| `lteNRRCC` | 51.84 MB | 51.96 MB | 162.6% | 111.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0389s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1076s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0749s | +0.0054s | worse |
| `lteNRRCC` | 0.1282s | 0.1274s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.59 MB | 8.93 MB | 159.1% | 150.9% |
| `f1ap_rel18.6_specs` | 9.87 MB | 158.62 MB | 155.3% | 151.9% |
| `ngap_rel18.6_specs` | 10.32 MB | 9.14 MB | 172.9% | 77.6% |
| `lteNRRCC` | 9.49 MB | 73.53 MB | 95.9% | 154.8% |
<!-- BENCH_RESULTS_END -->
