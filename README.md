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
Generated: 2026-07-27T23:10:50.321990+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0351s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1089s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0740s | +0.0050s | worse |
| `lteNRRCC` | 0.1236s | 0.1188s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 80.0% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 103.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0346s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0965s | 0.0961s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0678s | 0.0671s | +0.0007s | worse |
| `lteNRRCC` | 0.1310s | 0.1300s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.37 MB | 80.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.39 MB | 103.41 MB | 103.1% | 101.8% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.14 MB | 104.0% | 102.3% |
| `lteNRRCC` | 47.96 MB | 66.53 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0296s | +0.0068s | worse |
| `f1ap_rel18.6_specs` | 0.0946s | 0.0764s | +0.0182s | worse |
| `ngap_rel18.6_specs` | 0.0664s | 0.0528s | +0.0136s | worse |
| `lteNRRCC` | 0.1277s | 0.1008s | +0.0269s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 55.81 MB | 14.9% | 107.1% |
| `f1ap_rel18.6_specs` | 34.57 MB | 163.65 MB | 106.7% | 103.5% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.50 MB | 104.0% | 102.3% |
| `lteNRRCC` | 74.91 MB | 102.40 MB | 103.2% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0242s | 0.0228s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0671s | 0.0680s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0480s | 0.0466s | +0.0014s | worse |
| `lteNRRCC` | 0.0762s | 0.0764s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.95 MB | 4.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 2.73 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0429s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1200s | -0.0115s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0838s | -0.0062s | improved |
| `lteNRRCC` | 0.1379s | 0.1610s | -0.0231s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.07 MB | 7.43 MB | 178.7% | 168.2% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.11 MB | 81.6% | 80.2% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.61 MB | 82.6% | 86.5% |
| `lteNRRCC` | 49.26 MB | 69.10 MB | 108.4% | 108.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0376s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.1170s | 0.1097s | +0.0073s | worse |
| `ngap_rel18.6_specs` | 0.0814s | 0.0769s | +0.0045s | worse |
| `lteNRRCC` | 0.1327s | 0.1274s | +0.0053s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 11.41 MB | 0.0% | 107.0% |
| `f1ap_rel18.6_specs` | 10.31 MB | 164.20 MB | 170.0% | 109.5% |
| `ngap_rel18.6_specs` | 11.14 MB | 9.36 MB | 107.2% | 151.9% |
| `lteNRRCC` | 8.82 MB | 85.63 MB | 73.7% | 213.3% |
<!-- BENCH_RESULTS_END -->
