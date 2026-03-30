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
Generated: 2026-03-30T22:45:35.609380+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0372s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1157s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0787s | 0.0789s | -0.0002s | improved |
| `lteNRRCC` | 0.1238s | 0.1218s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 27.7% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.2% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0353s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0966s | 0.0942s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0699s | 0.0674s | +0.0025s | worse |
| `lteNRRCC` | 0.1281s | 0.1300s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.15 MB | 36.65 MB | 29.4% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.04 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.84 MB | 74.27 MB | 111.1% | 109.3% |
| `lteNRRCC` | 47.73 MB | 66.12 MB | 104.5% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0351s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0956s | 0.0906s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0668s | 0.0645s | +0.0023s | worse |
| `lteNRRCC` | 0.1293s | 0.1165s | +0.0128s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.23 MB | 55.72 MB | 83.3% | 106.7% |
| `f1ap_rel18.6_specs` | 34.54 MB | 164.64 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 24.24 MB | 117.86 MB | 111.1% | 106.7% |
| `lteNRRCC` | 74.57 MB | 102.96 MB | 104.6% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0192s | 0.0259s | -0.0067s | improved |
| `f1ap_rel18.6_specs` | 0.0675s | 0.1094s | -0.0419s | improved |
| `ngap_rel18.6_specs` | 0.0457s | 0.0436s | +0.0021s | worse |
| `lteNRRCC` | 0.0853s | 0.0965s | -0.0112s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.80 MB | 8.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.27 MB | 9.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.78 MB | 18.67 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.80 MB | 7.34 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0387s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1071s | +0.0039s | worse |
| `ngap_rel18.6_specs` | 0.0760s | 0.0753s | +0.0007s | worse |
| `lteNRRCC` | 0.1387s | 0.1365s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.33 MB | 7.34 MB | 161.8% | 164.5% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.61 MB | 167.2% | 232.2% |
| `ngap_rel18.6_specs` | 7.55 MB | 8.18 MB | 164.1% | 229.5% |
| `lteNRRCC` | 8.04 MB | 50.87 MB | 94.6% | 160.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0445s | 0.0375s | +0.0070s | worse |
| `f1ap_rel18.6_specs` | 0.1290s | 0.1075s | +0.0215s | worse |
| `ngap_rel18.6_specs` | 0.0899s | 0.0728s | +0.0171s | worse |
| `lteNRRCC` | 0.1322s | 0.1233s | +0.0089s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.00 MB | 9.00 MB | 167.7% | 164.6% |
| `f1ap_rel18.6_specs` | 10.50 MB | 10.02 MB | 119.8% | 161.1% |
| `ngap_rel18.6_specs` | 9.14 MB | 9.55 MB | 164.2% | 118.1% |
| `lteNRRCC` | 8.55 MB | 99.39 MB | 164.6% | 107.4% |
<!-- BENCH_RESULTS_END -->
