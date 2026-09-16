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
Generated: 2026-09-16T00:07:24.930890+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0353s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1084s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0744s | 0.0742s | +0.0002s | worse |
| `lteNRRCC` | 0.1214s | 0.1191s | +0.0023s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 82.6% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0277s | +0.0068s | worse |
| `f1ap_rel18.6_specs` | 0.0946s | 0.0752s | +0.0194s | worse |
| `ngap_rel18.6_specs` | 0.0656s | 0.0523s | +0.0133s | worse |
| `lteNRRCC` | 0.1277s | 0.0992s | +0.0285s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.55 MB | 36.50 MB | 77.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.37 MB | 103.34 MB | 106.5% | 103.6% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.24 MB | 104.0% | 102.3% |
| `lteNRRCC` | 48.59 MB | 66.48 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0381s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.0922s | 0.0945s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0643s | 0.0658s | -0.0015s | improved |
| `lteNRRCC` | 0.1177s | 0.1200s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 55.65 MB | 71.4% | 103.8% |
| `f1ap_rel18.6_specs` | 34.77 MB | 163.49 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 24.01 MB | 117.76 MB | 104.2% | 104.9% |
| `lteNRRCC` | 74.77 MB | 101.80 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0489s | -0.0105s | improved |
| `f1ap_rel18.6_specs` | 0.1273s | 0.0880s | +0.0393s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0775s | -0.0008s | improved |
| `lteNRRCC` | 0.1201s | 0.1048s | +0.0153s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.45 MB | 8.34 MB | 0.0% | 2.0% |
| `f1ap_rel18.6_specs` | 8.09 MB | 10.55 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.09 MB | 7.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.34 MB | 8.12 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0407s | -0.0075s | improved |
| `f1ap_rel18.6_specs` | 0.0927s | 0.1102s | -0.0175s | improved |
| `ngap_rel18.6_specs` | 0.0645s | 0.0809s | -0.0164s | improved |
| `lteNRRCC` | 0.1163s | 0.1397s | -0.0234s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.57 MB | 7.99 MB | 125.5% | 139.1% |
| `f1ap_rel18.6_specs` | 8.55 MB | 106.64 MB | 101.6% | 142.0% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.30 MB | 140.1% | 143.3% |
| `lteNRRCC` | 8.29 MB | 50.81 MB | 141.0% | 139.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0272s | 0.0449s | -0.0177s | improved |
| `f1ap_rel18.6_specs` | 0.0795s | 0.1306s | -0.0511s | improved |
| `ngap_rel18.6_specs` | 0.0559s | 0.0892s | -0.0333s | improved |
| `lteNRRCC` | 0.0835s | 0.1342s | -0.0507s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 50.61 MB | 0.0% | 123.7% |
| `f1ap_rel18.6_specs` | 13.37 MB | 27.43 MB | 143.2% | 140.8% |
| `ngap_rel18.6_specs` | 13.15 MB | 31.19 MB | 133.6% | 135.7% |
| `lteNRRCC` | 14.71 MB | 101.72 MB | 111.6% | 157.0% |
<!-- BENCH_RESULTS_END -->
