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
Generated: 2026-07-16T11:45:48.125634+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0355s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1120s | 0.1111s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0764s | 0.0771s | -0.0007s | improved |
| `lteNRRCC` | 0.1208s | 0.1207s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 17.4% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0354s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0966s | 0.0931s | +0.0035s | worse |
| `ngap_rel18.6_specs` | 0.0678s | 0.0663s | +0.0015s | worse |
| `lteNRRCC` | 0.1304s | 0.1284s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.25 MB | 36.59 MB | 75.0% | 110.7% |
| `f1ap_rel18.6_specs` | 22.34 MB | 103.07 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.00 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.15 MB | 66.39 MB | 104.7% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0366s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0913s | 0.0959s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.0646s | 0.0688s | -0.0042s | improved |
| `lteNRRCC` | 0.1175s | 0.1212s | -0.0037s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.35 MB | 55.13 MB | 78.6% | 110.7% |
| `f1ap_rel18.6_specs` | 34.60 MB | 163.70 MB | 106.7% | 105.4% |
| `ngap_rel18.6_specs` | 24.58 MB | 117.26 MB | 112.0% | 104.8% |
| `lteNRRCC` | 74.98 MB | 102.36 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0464s | 0.0187s | +0.0277s | worse |
| `f1ap_rel18.6_specs` | 0.0770s | 0.0705s | +0.0065s | worse |
| `ngap_rel18.6_specs` | 0.0490s | 0.0527s | -0.0037s | improved |
| `lteNRRCC` | 0.0794s | 0.0975s | -0.0181s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.58 MB | 5.98 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.33 MB | 6.73 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.61 MB | 6.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.06 MB | 4.64 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0431s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1178s | -0.0086s | improved |
| `ngap_rel18.6_specs` | 0.0786s | 0.0822s | -0.0036s | improved |
| `lteNRRCC` | 0.1408s | 0.1426s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.63 MB | 7.55 MB | 96.6% | 157.0% |
| `f1ap_rel18.6_specs` | 8.37 MB | 8.45 MB | 154.6% | 152.8% |
| `ngap_rel18.6_specs` | 7.87 MB | 8.11 MB | 77.3% | 151.8% |
| `lteNRRCC` | 51.84 MB | 50.88 MB | 213.0% | 151.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0450s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.1151s | 0.1267s | -0.0116s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0858s | -0.0106s | improved |
| `lteNRRCC` | 0.1348s | 0.1413s | -0.0065s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.91 MB | 8.59 MB | 110.7% | 79.8% |
| `f1ap_rel18.6_specs` | 9.75 MB | 9.88 MB | 161.6% | 99.6% |
| `ngap_rel18.6_specs` | 8.90 MB | 8.90 MB | 161.9% | 79.9% |
| `lteNRRCC` | 8.56 MB | 81.27 MB | 158.5% | 157.9% |
<!-- BENCH_RESULTS_END -->
