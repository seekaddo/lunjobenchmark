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
Generated: 2026-07-16T23:03:00.240048+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0360s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1120s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0764s | -0.0012s | improved |
| `lteNRRCC` | 0.1198s | 0.1208s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.61 MB | 53.55 MB | 6.2% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 106.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0361s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0966s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0665s | 0.0678s | -0.0013s | improved |
| `lteNRRCC` | 0.1296s | 0.1304s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.36 MB | 36.60 MB | 76.7% | 107.1% |
| `f1ap_rel18.6_specs` | 22.42 MB | 103.48 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.51 MB | 111.5% | 107.0% |
| `lteNRRCC` | 47.98 MB | 66.15 MB | 103.1% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0366s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0885s | 0.0913s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0621s | 0.0646s | -0.0025s | improved |
| `lteNRRCC` | 0.1150s | 0.1175s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.38 MB | 55.52 MB | 16.9% | 111.5% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.32 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.58 MB | 117.34 MB | 108.3% | 106.7% |
| `lteNRRCC` | 74.65 MB | 102.88 MB | 105.3% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0191s | 0.0464s | -0.0273s | improved |
| `f1ap_rel18.6_specs` | 0.0581s | 0.0770s | -0.0189s | improved |
| `ngap_rel18.6_specs` | 0.0397s | 0.0490s | -0.0093s | improved |
| `lteNRRCC` | 0.0672s | 0.0794s | -0.0122s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 4.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.88 MB | 3.73 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.88 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0409s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1041s | 0.1092s | -0.0051s | improved |
| `ngap_rel18.6_specs` | 0.0733s | 0.0786s | -0.0053s | improved |
| `lteNRRCC` | 0.1362s | 0.1408s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.44 MB | 162.7% | 163.3% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.45 MB | 163.8% | 104.8% |
| `ngap_rel18.6_specs` | 8.11 MB | 7.52 MB | 116.5% | 82.1% |
| `lteNRRCC` | 51.34 MB | 49.64 MB | 162.6% | 104.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0378s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1051s | 0.1151s | -0.0100s | improved |
| `ngap_rel18.6_specs` | 0.0725s | 0.0752s | -0.0027s | improved |
| `lteNRRCC` | 0.1240s | 0.1348s | -0.0108s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.58 MB | 8.52 MB | 165.0% | 160.9% |
| `f1ap_rel18.6_specs` | 9.46 MB | 164.19 MB | 161.6% | 235.9% |
| `ngap_rel18.6_specs` | 8.89 MB | 10.69 MB | 174.6% | 115.1% |
| `lteNRRCC` | 73.23 MB | 75.52 MB | 160.5% | 158.3% |
<!-- BENCH_RESULTS_END -->
