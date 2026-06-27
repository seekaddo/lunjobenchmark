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
Generated: 2026-06-27T23:10:03.804726+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0368s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1086s | 0.1124s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0754s | 0.0779s | -0.0025s | improved |
| `lteNRRCC` | 0.1184s | 0.1212s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 20.8% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 104.2% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 103.5% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0344s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0979s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0659s | 0.0644s | +0.0015s | worse |
| `lteNRRCC` | 0.1301s | 0.1234s | +0.0067s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.49 MB | 85.2% | 111.1% |
| `f1ap_rel18.6_specs` | 22.21 MB | 103.38 MB | 106.2% | 105.4% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.47 MB | 111.5% | 107.0% |
| `lteNRRCC` | 47.49 MB | 66.53 MB | 104.6% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0356s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.0904s | 0.0947s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0660s | -0.0042s | improved |
| `lteNRRCC` | 0.1169s | 0.1296s | -0.0127s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 55.84 MB | 78.6% | 111.1% |
| `f1ap_rel18.6_specs` | 35.13 MB | 164.54 MB | 106.7% | 103.6% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.14 MB | 108.0% | 107.1% |
| `lteNRRCC` | 74.73 MB | 102.27 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0242s | 0.0185s | +0.0057s | worse |
| `f1ap_rel18.6_specs` | 0.0661s | 0.0611s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0518s | 0.0464s | +0.0054s | worse |
| `lteNRRCC` | 0.0778s | 0.0693s | +0.0085s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.25 MB | 4.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.92 MB | 3.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.39 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.41 MB | 7.33 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0415s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1107s | 0.1121s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0774s | -0.0004s | improved |
| `lteNRRCC` | 0.1401s | 0.1409s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.52 MB | 7.62 MB | 153.6% | 76.2% |
| `f1ap_rel18.6_specs` | 8.04 MB | 106.64 MB | 80.0% | 158.1% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.61 MB | 158.2% | 172.2% |
| `lteNRRCC` | 46.65 MB | 53.01 MB | 156.1% | 107.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0430s | 0.0385s | +0.0045s | worse |
| `f1ap_rel18.6_specs` | 0.1195s | 0.1134s | +0.0061s | worse |
| `ngap_rel18.6_specs` | 0.0842s | 0.0791s | +0.0051s | worse |
| `lteNRRCC` | 0.1379s | 0.1287s | +0.0092s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.53 MB | 9.72 MB | 180.1% | 172.8% |
| `f1ap_rel18.6_specs` | 10.00 MB | 160.33 MB | 168.8% | 110.1% |
| `ngap_rel18.6_specs` | 10.39 MB | 9.49 MB | 218.0% | 162.4% |
| `lteNRRCC` | 73.16 MB | 76.77 MB | 159.8% | 107.8% |
<!-- BENCH_RESULTS_END -->
