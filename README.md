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
Generated: 2026-07-28T12:01:52.442692+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0376s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1143s | -0.0047s | improved |
| `ngap_rel18.6_specs` | 0.0742s | 0.0790s | -0.0048s | improved |
| `lteNRRCC` | 0.1186s | 0.1236s | -0.0050s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 81.8% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0272s | 0.0358s | -0.0086s | improved |
| `f1ap_rel18.6_specs` | 0.0735s | 0.0965s | -0.0230s | improved |
| `ngap_rel18.6_specs` | 0.0515s | 0.0678s | -0.0163s | improved |
| `lteNRRCC` | 0.0979s | 0.1310s | -0.0331s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.27 MB | 36.32 MB | 24.3% | 104.8% |
| `f1ap_rel18.6_specs` | 22.43 MB | 103.48 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 19.21 MB | 74.40 MB | 100.0% | 100.0% |
| `lteNRRCC` | 48.46 MB | 66.00 MB | 104.3% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0282s | 0.0364s | -0.0082s | improved |
| `f1ap_rel18.6_specs` | 0.0761s | 0.0946s | -0.0185s | improved |
| `ngap_rel18.6_specs` | 0.0524s | 0.0664s | -0.0140s | improved |
| `lteNRRCC` | 0.1012s | 0.1277s | -0.0265s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.21 MB | 55.63 MB | 85.7% | 104.5% |
| `f1ap_rel18.6_specs` | 35.25 MB | 163.81 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 24.44 MB | 116.82 MB | 105.3% | 102.9% |
| `lteNRRCC` | 74.98 MB | 102.95 MB | 102.0% | 103.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0242s | +0.0123s | worse |
| `f1ap_rel18.6_specs` | 0.0824s | 0.0671s | +0.0153s | worse |
| `ngap_rel18.6_specs` | 0.0524s | 0.0480s | +0.0044s | worse |
| `lteNRRCC` | 0.0675s | 0.0762s | -0.0087s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.75 MB | 4.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.56 MB | 4.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.12 MB | 4.20 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 4.12 MB | 0.0% | 1.3% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0412s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1069s | 0.1085s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0776s | -0.0014s | improved |
| `lteNRRCC` | 0.1413s | 0.1379s | +0.0034s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.84 MB | 7.35 MB | 108.5% | 81.4% |
| `f1ap_rel18.6_specs` | 8.17 MB | 7.97 MB | 163.4% | 82.9% |
| `ngap_rel18.6_specs` | 8.18 MB | 7.54 MB | 194.2% | 80.1% |
| `lteNRRCC` | 51.84 MB | 70.55 MB | 106.7% | 111.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0405s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1155s | 0.1170s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0832s | 0.0814s | +0.0018s | worse |
| `lteNRRCC` | 0.1302s | 0.1327s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.73 MB | 8.59 MB | 114.8% | 79.5% |
| `f1ap_rel18.6_specs` | 9.87 MB | 153.47 MB | 158.8% | 156.7% |
| `ngap_rel18.6_specs` | 9.09 MB | 9.21 MB | 76.3% | 157.5% |
| `lteNRRCC` | 73.78 MB | 96.43 MB | 159.3% | 107.8% |
<!-- BENCH_RESULTS_END -->
