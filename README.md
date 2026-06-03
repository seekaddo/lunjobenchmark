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
Generated: 2026-06-03T14:48:23.019096+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0352s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1106s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0764s | -0.0008s | improved |
| `lteNRRCC` | 0.1206s | 0.1199s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 20.0% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0352s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0993s | 0.0950s | +0.0043s | worse |
| `ngap_rel18.6_specs` | 0.0661s | 0.0673s | -0.0012s | improved |
| `lteNRRCC` | 0.1165s | 0.1293s | -0.0128s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 36.25 MB | 82.6% | 108.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.42 MB | 110.3% | 103.5% |
| `ngap_rel18.6_specs` | 17.73 MB | 74.61 MB | 108.7% | 104.8% |
| `lteNRRCC` | 48.63 MB | 66.22 MB | 105.4% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0334s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0902s | +0.0035s | worse |
| `ngap_rel18.6_specs` | 0.0652s | 0.0632s | +0.0020s | worse |
| `lteNRRCC` | 0.1274s | 0.1179s | +0.0095s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 55.34 MB | 85.7% | 110.3% |
| `f1ap_rel18.6_specs` | 34.21 MB | 163.83 MB | 112.5% | 105.2% |
| `ngap_rel18.6_specs` | 24.35 MB | 117.83 MB | 111.1% | 106.7% |
| `lteNRRCC` | 74.59 MB | 102.32 MB | 104.7% | 105.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0464s | 0.0273s | +0.0191s | worse |
| `f1ap_rel18.6_specs` | 0.0681s | 0.1034s | -0.0353s | improved |
| `ngap_rel18.6_specs` | 0.0471s | 0.0687s | -0.0216s | improved |
| `lteNRRCC` | 0.0784s | 0.1019s | -0.0235s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 3.81 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.19 MB | 9.30 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.98 MB | 3.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.17 MB | 3.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0321s | +0.0077s | worse |
| `f1ap_rel18.6_specs` | 0.1143s | 0.0934s | +0.0209s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0664s | +0.0139s | worse |
| `lteNRRCC` | 0.1430s | 0.1149s | +0.0281s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.82 MB | 7.88 MB | 162.9% | 158.1% |
| `f1ap_rel18.6_specs` | 8.55 MB | 105.38 MB | 98.3% | 164.6% |
| `ngap_rel18.6_specs` | 8.05 MB | 7.99 MB | 164.8% | 164.0% |
| `lteNRRCC` | 51.46 MB | 55.27 MB | 215.8% | 106.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0438s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1179s | 0.1241s | -0.0062s | improved |
| `ngap_rel18.6_specs` | 0.0809s | 0.0929s | -0.0120s | improved |
| `lteNRRCC` | 0.1301s | 0.1371s | -0.0070s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.86 MB | 9.00 MB | 154.9% | 152.8% |
| `f1ap_rel18.6_specs` | 9.93 MB | 164.19 MB | 149.3% | 154.7% |
| `ngap_rel18.6_specs` | 9.55 MB | 10.56 MB | 145.2% | 104.5% |
| `lteNRRCC` | 8.80 MB | 83.81 MB | 153.9% | 162.8% |
<!-- BENCH_RESULTS_END -->
