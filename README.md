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
Generated: 2026-08-19T10:35:15.010176+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0354s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1117s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0759s | +0.0010s | worse |
| `lteNRRCC` | 0.1210s | 0.1199s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 69.2% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0364s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0937s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0658s | -0.0004s | improved |
| `lteNRRCC` | 0.1276s | 0.1281s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 36.12 MB | 66.7% | 107.7% |
| `f1ap_rel18.6_specs` | 22.26 MB | 103.30 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.68 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.48 MB | 66.29 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0343s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0915s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0626s | 0.0653s | -0.0027s | improved |
| `lteNRRCC` | 0.1162s | 0.1187s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 55.19 MB | 76.0% | 107.7% |
| `f1ap_rel18.6_specs` | 34.62 MB | 163.86 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 24.46 MB | 116.73 MB | 104.3% | 102.4% |
| `lteNRRCC` | 74.34 MB | 102.70 MB | 103.5% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0442s | 0.0507s | -0.0065s | improved |
| `f1ap_rel18.6_specs` | 0.0833s | 0.1049s | -0.0216s | improved |
| `ngap_rel18.6_specs` | 0.0644s | 0.1032s | -0.0388s | improved |
| `lteNRRCC` | 0.1117s | 0.1039s | +0.0078s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.14 MB | 4.19 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 496 KB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.80 MB | 4.00 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.53 MB | 4.03 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0382s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1077s | 0.1049s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0761s | 0.0755s | +0.0006s | worse |
| `lteNRRCC` | 0.1380s | 0.1418s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.50 MB | 0.0% | 162.4% |
| `f1ap_rel18.6_specs` | 7.97 MB | 106.65 MB | 163.2% | 108.6% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.55 MB | 161.1% | 161.6% |
| `lteNRRCC` | 47.32 MB | 51.99 MB | 109.7% | 158.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0425s | 0.0380s | +0.0045s | worse |
| `f1ap_rel18.6_specs` | 0.1256s | 0.1101s | +0.0155s | worse |
| `ngap_rel18.6_specs` | 0.0821s | 0.0753s | +0.0068s | worse |
| `lteNRRCC` | 0.1304s | 0.1261s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.65 MB | 0.0% | 160.9% |
| `f1ap_rel18.6_specs` | 10.43 MB | 10.58 MB | 179.1% | 115.3% |
| `ngap_rel18.6_specs` | 9.62 MB | 10.63 MB | 163.1% | 224.7% |
| `lteNRRCC` | 9.43 MB | 101.71 MB | 104.1% | 105.9% |
<!-- BENCH_RESULTS_END -->
