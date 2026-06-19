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
Generated: 2026-06-19T23:05:17.282583+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0356s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1109s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0775s | -0.0037s | improved |
| `lteNRRCC` | 0.1186s | 0.1207s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.81 MB | 53.55 MB | 20.7% | 111.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 106.4% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0317s | 0.0203s | +0.0114s | worse |
| `f1ap_rel18.6_specs` | 0.0924s | 0.0558s | +0.0366s | worse |
| `ngap_rel18.6_specs` | 0.0644s | 0.0392s | +0.0252s | worse |
| `lteNRRCC` | 0.1143s | 0.0705s | +0.0438s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 36.14 MB | 75.0% | 108.3% |
| `f1ap_rel18.6_specs` | 22.01 MB | 103.31 MB | 103.6% | 103.6% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.66 MB | 104.3% | 105.0% |
| `lteNRRCC` | 48.84 MB | 66.43 MB | 103.6% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0351s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0971s | 0.0900s | +0.0071s | worse |
| `ngap_rel18.6_specs` | 0.0666s | 0.0639s | +0.0027s | worse |
| `lteNRRCC` | 0.1280s | 0.1187s | +0.0093s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 55.11 MB | 96.0% | 106.9% |
| `f1ap_rel18.6_specs` | 35.23 MB | 164.75 MB | 109.4% | 106.9% |
| `ngap_rel18.6_specs` | 24.50 MB | 117.41 MB | 107.4% | 106.8% |
| `lteNRRCC` | 74.96 MB | 102.74 MB | 104.8% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0196s | 0.0244s | -0.0048s | improved |
| `f1ap_rel18.6_specs` | 0.0732s | 0.0712s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0432s | 0.0490s | -0.0058s | improved |
| `lteNRRCC` | 0.1168s | 0.0794s | +0.0374s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.36 MB | 4.12 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.33 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 4.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.19 MB | 5.05 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0398s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1093s | +0.0043s | worse |
| `ngap_rel18.6_specs` | 0.0787s | 0.0804s | -0.0017s | improved |
| `lteNRRCC` | 0.1283s | 0.1396s | -0.0113s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.83 MB | 7.97 MB | 164.8% | 161.0% |
| `f1ap_rel18.6_specs` | 8.86 MB | 8.64 MB | 81.8% | 81.5% |
| `ngap_rel18.6_specs` | 8.24 MB | 8.18 MB | 169.0% | 162.0% |
| `lteNRRCC` | 8.36 MB | 69.74 MB | 107.7% | 110.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0599s | -0.0253s | improved |
| `f1ap_rel18.6_specs` | 0.1028s | 0.1367s | -0.0339s | improved |
| `ngap_rel18.6_specs` | 0.0705s | 0.0952s | -0.0247s | improved |
| `lteNRRCC` | 0.1127s | 0.1340s | -0.0213s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.72 MB | 10.16 MB | 0.0% | 129.5% |
| `f1ap_rel18.6_specs` | 10.44 MB | 158.11 MB | 140.9% | 139.5% |
| `ngap_rel18.6_specs` | 10.25 MB | 10.11 MB | 105.1% | 141.7% |
| `lteNRRCC` | 8.98 MB | 74.07 MB | 140.9% | 140.2% |
<!-- BENCH_RESULTS_END -->
