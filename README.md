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
Generated: 2026-05-10T22:56:35.572704+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0372s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1137s | 0.1151s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0796s | 0.0804s | -0.0008s | improved |
| `lteNRRCC` | 0.1216s | 0.1227s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 10.5% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 103.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0324s | 0.0358s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0946s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0650s | 0.0671s | -0.0021s | improved |
| `lteNRRCC` | 0.1153s | 0.1298s | -0.0145s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.34 MB | 82.6% | 104.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.19 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 16.65 MB | 74.40 MB | 109.1% | 104.9% |
| `lteNRRCC` | 48.79 MB | 66.30 MB | 105.4% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0275s | 0.0350s | -0.0075s | improved |
| `f1ap_rel18.6_specs` | 0.0753s | 0.1014s | -0.0261s | improved |
| `ngap_rel18.6_specs` | 0.0520s | 0.0702s | -0.0182s | improved |
| `lteNRRCC` | 0.1015s | 0.1184s | -0.0169s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.70 MB | 55.39 MB | 19.6% | 108.7% |
| `f1ap_rel18.6_specs` | 34.09 MB | 164.46 MB | 112.0% | 106.5% |
| `ngap_rel18.6_specs` | 24.49 MB | 117.52 MB | 109.5% | 105.7% |
| `lteNRRCC` | 75.02 MB | 101.78 MB | 106.0% | 103.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0182s | 0.0350s | -0.0168s | improved |
| `f1ap_rel18.6_specs` | 0.0581s | 0.0683s | -0.0102s | improved |
| `ngap_rel18.6_specs` | 0.0390s | 0.0404s | -0.0014s | improved |
| `lteNRRCC` | 0.0676s | 0.0676s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.30 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.62 MB | 4.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 4.11 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 3.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0399s | -0.0071s | improved |
| `f1ap_rel18.6_specs` | 0.0945s | 0.1148s | -0.0203s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0775s | -0.0118s | improved |
| `lteNRRCC` | 0.1123s | 0.1394s | -0.0271s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.84 MB | 7.81 MB | 102.6% | 103.2% |
| `f1ap_rel18.6_specs` | 8.54 MB | 8.61 MB | 139.1% | 213.6% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.36 MB | 97.6% | 135.0% |
| `lteNRRCC` | 51.76 MB | 60.86 MB | 136.1% | 140.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0407s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.1036s | 0.1227s | -0.0191s | improved |
| `ngap_rel18.6_specs` | 0.0708s | 0.0841s | -0.0133s | improved |
| `lteNRRCC` | 0.1128s | 0.1375s | -0.0247s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.84 MB | 9.97 MB | 141.9% | 142.6% |
| `f1ap_rel18.6_specs` | 10.43 MB | 158.17 MB | 141.7% | 129.8% |
| `ngap_rel18.6_specs` | 9.87 MB | 10.26 MB | 140.9% | 141.5% |
| `lteNRRCC` | 73.72 MB | 76.65 MB | 140.5% | 139.2% |
<!-- BENCH_RESULTS_END -->
