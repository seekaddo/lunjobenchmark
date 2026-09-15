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
Generated: 2026-09-15T14:48:30.614127+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0345s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1069s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0742s | 0.0737s | +0.0005s | worse |
| `lteNRRCC` | 0.1191s | 0.1164s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 78.3% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0277s | 0.0334s | -0.0057s | improved |
| `f1ap_rel18.6_specs` | 0.0752s | 0.0982s | -0.0230s | improved |
| `ngap_rel18.6_specs` | 0.0523s | 0.0677s | -0.0154s | improved |
| `lteNRRCC` | 0.0992s | 0.1196s | -0.0204s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.73 MB | 36.19 MB | 13.9% | 100.0% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.38 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 18.06 MB | 74.55 MB | 105.0% | 102.9% |
| `lteNRRCC` | 48.38 MB | 65.77 MB | 104.2% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0364s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0945s | 0.0957s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0668s | -0.0010s | improved |
| `lteNRRCC` | 0.1200s | 0.1209s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.53 MB | 84.0% | 107.4% |
| `f1ap_rel18.6_specs` | 34.65 MB | 164.24 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.37 MB | 117.78 MB | 108.3% | 102.3% |
| `lteNRRCC` | 74.75 MB | 102.43 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0489s | 0.0310s | +0.0179s | worse |
| `f1ap_rel18.6_specs` | 0.0880s | 0.0865s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0672s | +0.0103s | worse |
| `lteNRRCC` | 0.1048s | 0.0943s | +0.0105s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.83 MB | 4.44 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.73 MB | 3.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.97 MB | 7.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.11 MB | 3.50 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0391s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1102s | 0.1092s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0809s | 0.0772s | +0.0037s | worse |
| `lteNRRCC` | 0.1397s | 0.1378s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.88 MB | 7.56 MB | 208.2% | 76.2% |
| `f1ap_rel18.6_specs` | 8.44 MB | 8.61 MB | 159.4% | 151.1% |
| `ngap_rel18.6_specs` | 7.68 MB | 7.99 MB | 156.3% | 79.4% |
| `lteNRRCC` | 51.08 MB | 51.98 MB | 107.2% | 217.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0449s | 0.0392s | +0.0057s | worse |
| `f1ap_rel18.6_specs` | 0.1306s | 0.1129s | +0.0177s | worse |
| `ngap_rel18.6_specs` | 0.0892s | 0.0793s | +0.0099s | worse |
| `lteNRRCC` | 0.1342s | 0.1136s | +0.0206s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.23 MB | 10.29 MB | 103.2% | 94.5% |
| `f1ap_rel18.6_specs` | 11.21 MB | 121.90 MB | 156.9% | 113.2% |
| `ngap_rel18.6_specs` | 10.89 MB | 10.64 MB | 99.2% | 155.0% |
| `lteNRRCC` | 73.79 MB | 77.47 MB | 154.8% | 158.1% |
<!-- BENCH_RESULTS_END -->
