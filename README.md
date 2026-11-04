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
Generated: 2026-11-04T17:54:16.184483+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0403s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1249s | 0.1222s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0850s | 0.0855s | -0.0005s | improved |
| `lteNRRCC` | 0.1305s | 0.1276s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 80.8% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 101.9% |
| `lteNRRCC` | 72.37 MB | 100.18 MB | 103.2% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0461s | -0.0075s | improved |
| `f1ap_rel18.6_specs` | 0.1171s | 0.1420s | -0.0249s | improved |
| `ngap_rel18.6_specs` | 0.0809s | 0.0998s | -0.0189s | improved |
| `lteNRRCC` | 0.1312s | 0.1576s | -0.0264s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 34.65 MB | 64.3% | 103.6% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 106.7% | 101.5% |
| `ngap_rel18.6_specs` | 18.00 MB | 72.65 MB | 108.7% | 102.0% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 103.3% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0539s | 0.0593s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.1668s | 0.1743s | -0.0075s | improved |
| `ngap_rel18.6_specs` | 0.1153s | 0.1225s | -0.0072s | improved |
| `lteNRRCC` | 0.1625s | 0.1682s | -0.0057s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.69 MB | 53.73 MB | 16.0% | 102.6% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.6% | 102.2% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 103.6% | 102.9% |
| `lteNRRCC` | 72.58 MB | 100.36 MB | 102.7% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0240s | 0.0188s | +0.0052s | worse |
| `f1ap_rel18.6_specs` | 0.0756s | 0.0739s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0655s | 0.0740s | -0.0085s | improved |
| `lteNRRCC` | 0.0919s | 0.0908s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.67 MB | 5.70 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.94 MB | 15.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.20 MB | 7.72 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.77 MB | 5.72 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0398s | -0.0057s | improved |
| `f1ap_rel18.6_specs` | 0.0931s | 0.1097s | -0.0166s | improved |
| `ngap_rel18.6_specs` | 0.0643s | 0.0819s | -0.0176s | improved |
| `lteNRRCC` | 0.1118s | 0.1372s | -0.0254s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.31 MB | 0.0% | 136.1% |
| `f1ap_rel18.6_specs` | 8.86 MB | 8.39 MB | 135.7% | 206.2% |
| `ngap_rel18.6_specs` | 8.34 MB | 8.38 MB | 140.1% | 202.0% |
| `lteNRRCC` | 8.80 MB | 68.20 MB | 134.3% | 134.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0396s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1124s | 0.1152s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0843s | 0.0767s | +0.0076s | worse |
| `lteNRRCC` | 0.1282s | 0.1270s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.67 MB | 0.0% | 159.6% |
| `f1ap_rel18.6_specs` | 9.57 MB | 161.30 MB | 77.2% | 158.8% |
| `ngap_rel18.6_specs` | 10.56 MB | 10.51 MB | 220.7% | 109.7% |
| `lteNRRCC` | 8.57 MB | 74.77 MB | 153.7% | 172.3% |
<!-- BENCH_RESULTS_END -->
