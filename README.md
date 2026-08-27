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
Generated: 2026-08-27T03:02:34.655311+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0321s | 0.0353s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.1058s | 0.1097s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0725s | 0.0744s | -0.0019s | improved |
| `lteNRRCC` | 0.1160s | 0.1194s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 89.5% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.4% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.8% | 102.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0283s | 0.0343s | -0.0060s | improved |
| `f1ap_rel18.6_specs` | 0.0802s | 0.0974s | -0.0172s | improved |
| `ngap_rel18.6_specs` | 0.0523s | 0.0687s | -0.0164s | improved |
| `lteNRRCC` | 0.0989s | 0.1199s | -0.0210s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.78 MB | 36.69 MB | 51.5% | 100.0% |
| `f1ap_rel18.6_specs` | 22.09 MB | 103.33 MB | 108.3% | 102.2% |
| `ngap_rel18.6_specs` | 18.14 MB | 74.09 MB | 105.0% | 102.7% |
| `lteNRRCC` | 48.52 MB | 66.36 MB | 102.1% | 103.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0264s | 0.0334s | -0.0070s | improved |
| `f1ap_rel18.6_specs` | 0.0945s | 0.0926s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0639s | -0.0010s | improved |
| `lteNRRCC` | 0.1084s | 0.1162s | -0.0078s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.78 MB | 55.51 MB | 64.0% | 100.0% |
| `f1ap_rel18.6_specs` | 34.68 MB | 164.71 MB | 108.3% | 101.8% |
| `ngap_rel18.6_specs` | 24.01 MB | 117.82 MB | 105.0% | 100.0% |
| `lteNRRCC` | 74.94 MB | 102.66 MB | 100.0% | 101.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0229s | 0.0233s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0765s | 0.0703s | +0.0062s | worse |
| `ngap_rel18.6_specs` | 0.0476s | 0.0482s | -0.0006s | improved |
| `lteNRRCC` | 0.0778s | 0.0787s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.52 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.62 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.45 MB | 4.14 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0388s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.1152s | 0.1075s | +0.0077s | worse |
| `ngap_rel18.6_specs` | 0.0806s | 0.0755s | +0.0051s | worse |
| `lteNRRCC` | 0.1431s | 0.1425s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.14 MB | 7.96 MB | 0.0% | 220.4% |
| `f1ap_rel18.6_specs` | 8.80 MB | 99.03 MB | 215.5% | 164.3% |
| `ngap_rel18.6_specs` | 7.99 MB | 7.99 MB | 164.1% | 166.3% |
| `lteNRRCC` | 48.77 MB | 59.92 MB | 107.4% | 164.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0401s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1173s | 0.1148s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0877s | 0.0793s | +0.0084s | worse |
| `lteNRRCC` | 0.1329s | 0.1151s | +0.0178s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.29 MB | 8.79 MB | 93.9% | 91.0% |
| `f1ap_rel18.6_specs` | 9.15 MB | 158.24 MB | 94.5% | 157.7% |
| `ngap_rel18.6_specs` | 10.70 MB | 10.89 MB | 111.5% | 221.8% |
| `lteNRRCC` | 8.90 MB | 95.84 MB | 86.0% | 215.4% |
<!-- BENCH_RESULTS_END -->
