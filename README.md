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
Generated: 2026-04-16T11:12:09.798458+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0357s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.1223s | 0.1130s | +0.0093s | worse |
| `ngap_rel18.6_specs` | 0.0852s | 0.0759s | +0.0093s | worse |
| `lteNRRCC` | 0.1297s | 0.1208s | +0.0089s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 10.8% | 111.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 111.8% | 105.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 110.7% | 106.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.8% | 105.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0358s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0928s | 0.0971s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0660s | 0.0675s | -0.0015s | improved |
| `lteNRRCC` | 0.1292s | 0.1305s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.73 MB | 88.5% | 107.1% |
| `f1ap_rel18.6_specs` | 22.28 MB | 103.39 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.70 MB | 73.92 MB | 107.4% | 107.0% |
| `lteNRRCC` | 48.56 MB | 66.37 MB | 104.7% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0361s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.0890s | 0.1021s | -0.0131s | improved |
| `ngap_rel18.6_specs` | 0.0614s | 0.0716s | -0.0102s | improved |
| `lteNRRCC` | 0.1183s | 0.1189s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.21 MB | 55.82 MB | 92.3% | 111.1% |
| `f1ap_rel18.6_specs` | 34.61 MB | 164.74 MB | 106.7% | 105.5% |
| `ngap_rel18.6_specs` | 24.21 MB | 117.58 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.29 MB | 102.90 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0260s | 0.0135s | +0.0125s | worse |
| `f1ap_rel18.6_specs` | 0.0712s | 0.0861s | -0.0149s | improved |
| `ngap_rel18.6_specs` | 0.0425s | 0.0588s | -0.0163s | improved |
| `lteNRRCC` | 0.0671s | 0.0790s | -0.0119s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.27 MB | 4.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.80 MB | 5.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.94 MB | 4.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.47 MB | 7.09 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0383s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1051s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0772s | 0.0739s | +0.0033s | worse |
| `lteNRRCC` | 0.1276s | 0.1368s | -0.0092s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.74 MB | 7.97 MB | 81.9% | 78.7% |
| `f1ap_rel18.6_specs` | 8.73 MB | 8.73 MB | 79.6% | 106.2% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.23 MB | 89.2% | 172.9% |
| `lteNRRCC` | 8.59 MB | 69.16 MB | 115.4% | 103.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0385s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1086s | 0.1091s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0771s | +0.0000s | flat |
| `lteNRRCC` | 0.1253s | 0.1275s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 8.79 MB | 79.5% | 149.5% |
| `f1ap_rel18.6_specs` | 9.74 MB | 164.19 MB | 154.0% | 157.2% |
| `ngap_rel18.6_specs` | 8.88 MB | 8.98 MB | 156.9% | 162.8% |
| `lteNRRCC` | 8.37 MB | 86.65 MB | 78.9% | 160.7% |
<!-- BENCH_RESULTS_END -->
