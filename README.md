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
Generated: 2026-03-20T10:49:08.923275+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0361s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1117s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0774s | +0.0016s | worse |
| `lteNRRCC` | 0.1218s | 0.1206s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 105.6% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0358s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0977s | 0.0948s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0680s | 0.0664s | +0.0016s | worse |
| `lteNRRCC` | 0.1325s | 0.1300s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.40 MB | 36.63 MB | 89.7% | 109.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.16 MB | 108.6% | 104.9% |
| `ngap_rel18.6_specs` | 16.30 MB | 74.57 MB | 110.3% | 108.3% |
| `lteNRRCC` | 48.25 MB | 66.09 MB | 105.8% | 105.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0350s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0892s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0633s | 0.0629s | +0.0004s | worse |
| `lteNRRCC` | 0.1166s | 0.1173s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.45 MB | 55.24 MB | 20.0% | 110.7% |
| `f1ap_rel18.6_specs` | 34.22 MB | 164.59 MB | 110.0% | 107.1% |
| `ngap_rel18.6_specs` | 24.40 MB | 117.20 MB | 111.5% | 107.0% |
| `lteNRRCC` | 74.96 MB | 102.84 MB | 106.8% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0224s | 0.0288s | -0.0064s | improved |
| `f1ap_rel18.6_specs` | 0.0647s | 0.0988s | -0.0341s | improved |
| `ngap_rel18.6_specs` | 0.0501s | 0.0693s | -0.0192s | improved |
| `lteNRRCC` | 0.0772s | 0.1026s | -0.0254s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.27 MB | 4.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.88 MB | 4.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.47 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.03 MB | 3.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0428s | 0.0385s | +0.0043s | worse |
| `f1ap_rel18.6_specs` | 0.1082s | 0.1057s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0736s | +0.0034s | worse |
| `lteNRRCC` | 0.1385s | 0.1372s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.51 MB | 7.90 MB | 98.7% | 232.1% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.68 MB | 83.1% | 112.7% |
| `ngap_rel18.6_specs` | 7.59 MB | 7.92 MB | 160.9% | 177.1% |
| `lteNRRCC` | 49.72 MB | 52.27 MB | 156.9% | 107.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0387s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1060s | 0.1164s | -0.0104s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0783s | -0.0045s | improved |
| `lteNRRCC` | 0.1242s | 0.1287s | -0.0045s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.54 MB | 10.28 MB | 105.0% | 118.2% |
| `f1ap_rel18.6_specs` | 11.03 MB | 151.86 MB | 232.8% | 235.7% |
| `ngap_rel18.6_specs` | 8.92 MB | 11.13 MB | 82.8% | 223.4% |
| `lteNRRCC` | 9.68 MB | 81.27 MB | 97.3% | 106.8% |
<!-- BENCH_RESULTS_END -->
