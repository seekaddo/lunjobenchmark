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
Generated: 2026-03-27T22:41:27.721740+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0385s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1166s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0785s | 0.0811s | -0.0026s | improved |
| `lteNRRCC` | 0.1218s | 0.1239s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 8.5% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0356s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0969s | 0.0979s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0681s | 0.0698s | -0.0017s | improved |
| `lteNRRCC` | 0.1309s | 0.1312s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.24 MB | 36.54 MB | 83.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.44 MB | 102.68 MB | 108.8% | 105.0% |
| `ngap_rel18.6_specs` | 16.85 MB | 74.40 MB | 111.1% | 104.3% |
| `lteNRRCC` | 48.20 MB | 66.37 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0340s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0893s | 0.0887s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0607s | 0.0615s | -0.0008s | improved |
| `lteNRRCC` | 0.1134s | 0.1149s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.15 MB | 54.90 MB | 100.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.04 MB | 164.64 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.41 MB | 117.66 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.92 MB | 102.82 MB | 105.3% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0234s | 0.0315s | -0.0081s | improved |
| `f1ap_rel18.6_specs` | 0.0608s | 0.0976s | -0.0368s | improved |
| `ngap_rel18.6_specs` | 0.0400s | 0.0558s | -0.0158s | improved |
| `lteNRRCC` | 0.0682s | 0.1347s | -0.0665s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.38 MB | 4.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 6.48 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.55 MB | 5.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.81 MB | 3.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0380s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1046s | +0.0072s | worse |
| `ngap_rel18.6_specs` | 0.0845s | 0.0728s | +0.0117s | worse |
| `lteNRRCC` | 0.1286s | 0.1355s | -0.0069s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.86 MB | 8.04 MB | 158.5% | 158.9% |
| `f1ap_rel18.6_specs` | 8.46 MB | 8.73 MB | 159.7% | 165.8% |
| `ngap_rel18.6_specs` | 9.48 MB | 8.23 MB | 84.0% | 160.4% |
| `lteNRRCC` | 8.21 MB | 70.54 MB | 157.8% | 230.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0395s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1122s | 0.1075s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0743s | +0.0033s | worse |
| `lteNRRCC` | 0.1315s | 0.1244s | +0.0071s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.77 MB | 8.71 MB | 157.3% | 80.5% |
| `f1ap_rel18.6_specs` | 9.80 MB | 164.18 MB | 188.8% | 169.9% |
| `ngap_rel18.6_specs` | 9.01 MB | 9.01 MB | 163.6% | 159.3% |
| `lteNRRCC` | 67.47 MB | 88.94 MB | 104.7% | 106.2% |
<!-- BENCH_RESULTS_END -->
