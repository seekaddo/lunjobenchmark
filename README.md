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
Generated: 2026-05-19T23:11:18.327903+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0363s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1153s | 0.1155s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0797s | 0.0788s | +0.0009s | worse |
| `lteNRRCC` | 0.1228s | 0.1234s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 4.8% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0359s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0956s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0665s | 0.0686s | -0.0021s | improved |
| `lteNRRCC` | 0.1292s | 0.1304s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.69 MB | 36.43 MB | 92.3% | 106.9% |
| `f1ap_rel18.6_specs` | 21.96 MB | 102.61 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.75 MB | 73.73 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.50 MB | 66.18 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0390s | -0.0055s | improved |
| `f1ap_rel18.6_specs` | 0.0898s | 0.1002s | -0.0104s | improved |
| `ngap_rel18.6_specs` | 0.0624s | 0.0715s | -0.0091s | improved |
| `lteNRRCC` | 0.1168s | 0.1355s | -0.0187s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.79 MB | 55.85 MB | 33.3% | 110.7% |
| `f1ap_rel18.6_specs` | 34.28 MB | 164.57 MB | 106.7% | 105.4% |
| `ngap_rel18.6_specs` | 24.04 MB | 117.73 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.74 MB | 102.86 MB | 103.4% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0273s | +0.0089s | worse |
| `f1ap_rel18.6_specs` | 0.1016s | 0.0935s | +0.0081s | worse |
| `ngap_rel18.6_specs` | 0.0595s | 0.0499s | +0.0096s | worse |
| `lteNRRCC` | 0.0886s | 0.1086s | -0.0200s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.33 MB | 4.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.12 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.92 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.73 MB | 1.59 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0452s | -0.0057s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1251s | -0.0160s | improved |
| `ngap_rel18.6_specs` | 0.0741s | 0.0868s | -0.0127s | improved |
| `lteNRRCC` | 0.1362s | 0.1495s | -0.0133s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.38 MB | 81.2% | 162.0% |
| `f1ap_rel18.6_specs` | 7.98 MB | 100.44 MB | 84.2% | 164.1% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.55 MB | 95.5% | 163.0% |
| `lteNRRCC` | 49.39 MB | 51.09 MB | 104.1% | 163.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0424s | 0.0431s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1243s | 0.1257s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0871s | 0.0868s | +0.0003s | worse |
| `lteNRRCC` | 0.1416s | 0.1410s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.65 MB | 9.01 MB | 109.0% | 164.4% |
| `f1ap_rel18.6_specs` | 10.06 MB | 154.84 MB | 166.4% | 108.8% |
| `ngap_rel18.6_specs` | 10.32 MB | 9.27 MB | 205.2% | 163.4% |
| `lteNRRCC` | 8.75 MB | 77.08 MB | 163.7% | 162.8% |
<!-- BENCH_RESULTS_END -->
