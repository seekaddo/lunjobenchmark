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
Generated: 2026-03-20T22:36:57.760133+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0370s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1133s | 0.1144s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0785s | 0.0790s | -0.0005s | improved |
| `lteNRRCC` | 0.1227s | 0.1218s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 105.6% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0365s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0977s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.0648s | 0.0680s | -0.0032s | improved |
| `lteNRRCC` | 0.1272s | 0.1325s | -0.0053s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 36.17 MB | 83.9% | 113.3% |
| `f1ap_rel18.6_specs` | 22.19 MB | 103.04 MB | 108.8% | 106.8% |
| `ngap_rel18.6_specs` | 16.26 MB | 73.96 MB | 113.8% | 108.9% |
| `lteNRRCC` | 48.69 MB | 66.12 MB | 106.1% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0342s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0940s | 0.0942s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0633s | +0.0024s | worse |
| `lteNRRCC` | 0.1287s | 0.1166s | +0.0121s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 55.75 MB | 93.1% | 109.4% |
| `f1ap_rel18.6_specs` | 34.69 MB | 163.79 MB | 111.8% | 104.9% |
| `ngap_rel18.6_specs` | 24.07 MB | 117.10 MB | 110.3% | 106.5% |
| `lteNRRCC` | 74.72 MB | 102.61 MB | 104.5% | 105.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0210s | 0.0224s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0655s | 0.0647s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0438s | 0.0501s | -0.0063s | improved |
| `lteNRRCC` | 0.0736s | 0.0772s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.56 MB | 5.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.52 MB | 4.53 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.80 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.92 MB | 4.44 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0428s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.1058s | 0.1082s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0737s | 0.0770s | -0.0033s | improved |
| `lteNRRCC` | 0.1380s | 0.1385s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.52 MB | 7.89 MB | 169.7% | 113.5% |
| `f1ap_rel18.6_specs` | 8.19 MB | 8.57 MB | 93.9% | 107.4% |
| `ngap_rel18.6_specs` | 8.07 MB | 7.63 MB | 107.2% | 102.4% |
| `lteNRRCC` | 48.03 MB | 49.79 MB | 103.2% | 166.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0379s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1060s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0741s | 0.0738s | +0.0003s | worse |
| `lteNRRCC` | 0.1252s | 0.1242s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.72 MB | 8.63 MB | 114.0% | 81.5% |
| `f1ap_rel18.6_specs` | 9.69 MB | 164.19 MB | 82.0% | 107.0% |
| `ngap_rel18.6_specs` | 8.96 MB | 9.09 MB | 163.8% | 81.0% |
| `lteNRRCC` | 8.69 MB | 93.44 MB | 99.7% | 159.8% |
<!-- BENCH_RESULTS_END -->
