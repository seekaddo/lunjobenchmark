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
Generated: 2026-09-01T23:55:36.277930+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0361s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1122s | 0.1112s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0761s | +0.0009s | worse |
| `lteNRRCC` | 0.1213s | 0.1214s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 16.5% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.0% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0338s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0919s | 0.0906s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0650s | 0.0639s | +0.0011s | worse |
| `lteNRRCC` | 0.1264s | 0.1228s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.38 MB | 80.8% | 107.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.36 MB | 106.2% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.70 MB | 107.7% | 104.3% |
| `lteNRRCC` | 48.61 MB | 66.54 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0354s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0973s | 0.0945s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0681s | 0.0658s | +0.0023s | worse |
| `lteNRRCC` | 0.1302s | 0.1293s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.43 MB | 17.7% | 107.1% |
| `f1ap_rel18.6_specs` | 34.73 MB | 164.64 MB | 106.2% | 103.4% |
| `ngap_rel18.6_specs` | 24.42 MB | 117.20 MB | 103.8% | 104.5% |
| `lteNRRCC` | 74.64 MB | 102.95 MB | 101.6% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0244s | 0.0347s | -0.0103s | improved |
| `f1ap_rel18.6_specs` | 0.1010s | 0.0882s | +0.0128s | worse |
| `ngap_rel18.6_specs` | 0.0540s | 0.0657s | -0.0117s | improved |
| `lteNRRCC` | 0.1060s | 0.1181s | -0.0121s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.19 MB | 5.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 11.53 MB | 6.98 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 1.91 MB | 8.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.11 MB | 6.64 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0352s | +0.0051s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.0965s | +0.0162s | worse |
| `ngap_rel18.6_specs` | 0.0797s | 0.0666s | +0.0131s | worse |
| `lteNRRCC` | 0.1397s | 0.1133s | +0.0264s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.20 MB | 7.76 MB | 0.0% | 99.8% |
| `f1ap_rel18.6_specs` | 8.42 MB | 8.45 MB | 165.8% | 84.2% |
| `ngap_rel18.6_specs` | 7.93 MB | 8.06 MB | 167.4% | 193.0% |
| `lteNRRCC` | 48.64 MB | 54.07 MB | 111.1% | 177.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0308s | 0.0392s | -0.0084s | improved |
| `f1ap_rel18.6_specs` | 0.0830s | 0.1108s | -0.0278s | improved |
| `ngap_rel18.6_specs` | 0.0588s | 0.0769s | -0.0181s | improved |
| `lteNRRCC` | 0.0897s | 0.1281s | -0.0384s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 22.45 MB | 0.0% | 100.1% |
| `f1ap_rel18.6_specs` | 29.04 MB | 18.20 MB | 130.8% | 104.2% |
| `ngap_rel18.6_specs` | 24.21 MB | 15.07 MB | 70.5% | 115.4% |
| `lteNRRCC` | 11.22 MB | 16.03 MB | 136.6% | 77.4% |
<!-- BENCH_RESULTS_END -->
