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
Generated: 2026-07-21T11:51:45.947610+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0388s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.1074s | 0.1161s | -0.0087s | improved |
| `ngap_rel18.6_specs` | 0.0736s | 0.0802s | -0.0066s | improved |
| `lteNRRCC` | 0.1164s | 0.1249s | -0.0085s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.73 MB | 53.55 MB | 19.2% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.6% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0364s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0992s | -0.0080s | improved |
| `ngap_rel18.6_specs` | 0.0638s | 0.0694s | -0.0056s | improved |
| `lteNRRCC` | 0.1224s | 0.1312s | -0.0088s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.31 MB | 36.25 MB | 76.7% | 110.7% |
| `f1ap_rel18.6_specs` | 22.25 MB | 103.25 MB | 109.4% | 105.4% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.44 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.80 MB | 66.04 MB | 104.8% | 104.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0347s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0941s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0660s | 0.0669s | -0.0009s | improved |
| `lteNRRCC` | 0.1306s | 0.1203s | +0.0103s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 55.17 MB | 96.0% | 110.0% |
| `f1ap_rel18.6_specs` | 34.80 MB | 164.69 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.59 MB | 107.4% | 109.1% |
| `lteNRRCC` | 74.21 MB | 102.86 MB | 104.7% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0257s | 0.0207s | +0.0050s | worse |
| `f1ap_rel18.6_specs` | 0.0757s | 0.0758s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0476s | 0.0504s | -0.0028s | improved |
| `lteNRRCC` | 0.0708s | 0.0786s | -0.0078s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.38 MB | 4.42 MB | 0.0% | 1.2% |
| `f1ap_rel18.6_specs` | 3.11 MB | 4.58 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.44 MB | 4.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.83 MB | 4.42 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0416s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1155s | 0.1133s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0782s | 0.0774s | +0.0008s | worse |
| `lteNRRCC` | 0.1270s | 0.1437s | -0.0167s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.38 MB | 8.36 MB | 117.3% | 236.2% |
| `f1ap_rel18.6_specs` | 8.10 MB | 8.29 MB | 83.0% | 81.2% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.17 MB | 164.9% | 81.0% |
| `lteNRRCC` | 8.53 MB | 8.34 MB | 106.5% | 163.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0393s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1144s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0791s | 0.0766s | +0.0025s | worse |
| `lteNRRCC` | 0.1257s | 0.1310s | -0.0053s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.79 MB | 8.65 MB | 156.5% | 155.8% |
| `f1ap_rel18.6_specs` | 9.87 MB | 11.20 MB | 157.1% | 224.7% |
| `ngap_rel18.6_specs` | 9.08 MB | 9.14 MB | 79.1% | 156.5% |
| `lteNRRCC` | 8.62 MB | 78.57 MB | 170.4% | 234.5% |
<!-- BENCH_RESULTS_END -->
