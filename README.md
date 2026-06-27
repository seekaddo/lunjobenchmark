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
Generated: 2026-06-27T11:40:35.014145+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0357s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1124s | 0.1098s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0779s | 0.0748s | +0.0031s | worse |
| `lteNRRCC` | 0.1212s | 0.1193s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 21.4% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0338s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0979s | 0.0912s | +0.0067s | worse |
| `ngap_rel18.6_specs` | 0.0644s | 0.0632s | +0.0012s | worse |
| `lteNRRCC` | 0.1234s | 0.1225s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.18 MB | 36.64 MB | 92.3% | 110.7% |
| `f1ap_rel18.6_specs` | 21.98 MB | 103.50 MB | 109.4% | 103.5% |
| `ngap_rel18.6_specs` | 17.73 MB | 74.58 MB | 115.4% | 106.8% |
| `lteNRRCC` | 48.16 MB | 66.52 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0350s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0930s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0660s | 0.0648s | +0.0012s | worse |
| `lteNRRCC` | 0.1296s | 0.1292s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 55.62 MB | 79.3% | 110.3% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.68 MB | 109.4% | 103.4% |
| `ngap_rel18.6_specs` | 24.35 MB | 117.74 MB | 111.5% | 106.8% |
| `lteNRRCC` | 74.99 MB | 102.49 MB | 104.8% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0185s | 0.0323s | -0.0138s | improved |
| `f1ap_rel18.6_specs` | 0.0611s | 0.0896s | -0.0285s | improved |
| `ngap_rel18.6_specs` | 0.0464s | 0.0615s | -0.0151s | improved |
| `lteNRRCC` | 0.0693s | 0.1047s | -0.0354s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.53 MB | 3.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.97 MB | 4.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.31 MB | 8.42 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.92 MB | 3.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0412s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1121s | 0.1098s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0774s | 0.0776s | -0.0002s | improved |
| `lteNRRCC` | 0.1409s | 0.1385s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.70 MB | 7.89 MB | 162.7% | 97.8% |
| `f1ap_rel18.6_specs` | 8.43 MB | 8.54 MB | 156.2% | 75.1% |
| `ngap_rel18.6_specs` | 8.55 MB | 8.17 MB | 210.1% | 146.8% |
| `lteNRRCC` | 51.57 MB | 65.29 MB | 107.5% | 104.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0440s | -0.0055s | improved |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1288s | -0.0154s | improved |
| `ngap_rel18.6_specs` | 0.0791s | 0.0893s | -0.0102s | improved |
| `lteNRRCC` | 0.1287s | 0.1362s | -0.0075s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.46 MB | 8.66 MB | 164.6% | 161.0% |
| `f1ap_rel18.6_specs` | 9.50 MB | 164.20 MB | 163.0% | 109.5% |
| `ngap_rel18.6_specs` | 8.90 MB | 10.57 MB | 163.5% | 111.8% |
| `lteNRRCC` | 8.56 MB | 91.63 MB | 170.3% | 154.9% |
<!-- BENCH_RESULTS_END -->
