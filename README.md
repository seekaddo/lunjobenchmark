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
Generated: 2026-08-09T10:42:17.610059+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0368s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.1069s | 0.1156s | -0.0087s | improved |
| `ngap_rel18.6_specs` | 0.0732s | 0.0795s | -0.0063s | improved |
| `lteNRRCC` | 0.1160s | 0.1228s | -0.0068s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.60 MB | 53.55 MB | 77.3% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.4% | 103.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 100.0% | 104.4% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0340s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0921s | 0.0918s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0650s | 0.0644s | +0.0006s | worse |
| `lteNRRCC` | 0.1249s | 0.1277s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.22 MB | 36.62 MB | 84.0% | 106.9% |
| `f1ap_rel18.6_specs` | 22.24 MB | 103.38 MB | 106.5% | 103.5% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.54 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.74 MB | 65.39 MB | 103.3% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0316s | 0.0361s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.0949s | 0.0960s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0637s | 0.0669s | -0.0032s | improved |
| `lteNRRCC` | 0.1089s | 0.1292s | -0.0203s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.11 MB | 55.75 MB | 37.5% | 104.5% |
| `f1ap_rel18.6_specs` | 34.01 MB | 163.49 MB | 104.2% | 101.8% |
| `ngap_rel18.6_specs` | 22.63 MB | 117.72 MB | 105.0% | 102.6% |
| `lteNRRCC` | 74.93 MB | 102.97 MB | 101.9% | 103.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0215s | 0.0241s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0675s | 0.0710s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0468s | 0.0489s | -0.0021s | improved |
| `lteNRRCC` | 0.0759s | 0.0775s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.05 MB | 3.80 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 4.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.17 MB | 3.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.03 MB | 4.23 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0391s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1082s | 0.1089s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0780s | 0.0765s | +0.0015s | worse |
| `lteNRRCC` | 0.1408s | 0.1387s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.68 MB | 0.0% | 150.7% |
| `f1ap_rel18.6_specs` | 8.18 MB | 8.18 MB | 157.7% | 155.7% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.99 MB | 80.5% | 87.4% |
| `lteNRRCC` | 46.89 MB | 51.99 MB | 153.9% | 110.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0395s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1138s | 0.1129s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0779s | 0.0767s | +0.0012s | worse |
| `lteNRRCC` | 0.1297s | 0.1275s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 8.66 MB | 0.0% | 94.7% |
| `f1ap_rel18.6_specs` | 9.62 MB | 11.21 MB | 78.8% | 98.5% |
| `ngap_rel18.6_specs` | 9.09 MB | 10.51 MB | 157.8% | 226.4% |
| `lteNRRCC` | 73.66 MB | 73.89 MB | 154.7% | 156.2% |
<!-- BENCH_RESULTS_END -->
