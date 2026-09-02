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
Generated: 2026-09-02T14:15:30.805285+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0361s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1122s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0784s | 0.0770s | +0.0014s | worse |
| `lteNRRCC` | 0.1213s | 0.1213s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.69 MB | 53.55 MB | 90.5% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0345s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0919s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0664s | 0.0650s | +0.0014s | worse |
| `lteNRRCC` | 0.1299s | 0.1264s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 36.69 MB | 71.4% | 103.8% |
| `f1ap_rel18.6_specs` | 22.24 MB | 103.48 MB | 103.1% | 101.8% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.71 MB | 107.7% | 102.4% |
| `lteNRRCC` | 47.96 MB | 65.72 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0373s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0904s | 0.0973s | -0.0069s | improved |
| `ngap_rel18.6_specs` | 0.0622s | 0.0681s | -0.0059s | improved |
| `lteNRRCC` | 0.1149s | 0.1302s | -0.0153s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 55.89 MB | 76.0% | 107.7% |
| `f1ap_rel18.6_specs` | 35.18 MB | 163.62 MB | 107.1% | 101.9% |
| `ngap_rel18.6_specs` | 23.79 MB | 117.89 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.27 MB | 101.98 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0244s | +0.0111s | worse |
| `f1ap_rel18.6_specs` | 0.0992s | 0.1010s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0859s | 0.0540s | +0.0319s | worse |
| `lteNRRCC` | 0.0962s | 0.1060s | -0.0098s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.75 MB | 4.70 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.86 MB | 7.45 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.80 MB | 5.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.50 MB | 3.48 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0403s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1127s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0797s | -0.0046s | improved |
| `lteNRRCC` | 0.1385s | 0.1397s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.93 MB | 7.36 MB | 0.0% | 160.8% |
| `f1ap_rel18.6_specs` | 8.11 MB | 106.64 MB | 80.7% | 177.4% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.55 MB | 158.1% | 82.7% |
| `lteNRRCC` | 50.74 MB | 50.73 MB | 158.6% | 112.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0308s | +0.0077s | worse |
| `f1ap_rel18.6_specs` | 0.1107s | 0.0830s | +0.0277s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0588s | +0.0183s | worse |
| `lteNRRCC` | 0.1240s | 0.0897s | +0.0343s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.61 MB | 12.72 MB | 127.9% | 94.5% |
| `f1ap_rel18.6_specs` | 8.68 MB | 139.05 MB | 112.3% | 134.0% |
| `ngap_rel18.6_specs` | 7.67 MB | 10.39 MB | 120.4% | 133.2% |
| `lteNRRCC` | 60.00 MB | 82.34 MB | 119.2% | 109.4% |
<!-- BENCH_RESULTS_END -->
