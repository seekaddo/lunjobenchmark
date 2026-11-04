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
Generated: 2026-11-04T02:04:21.667677+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0415s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1222s | 0.1287s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0855s | 0.0887s | -0.0032s | improved |
| `lteNRRCC` | 0.1276s | 0.1326s | -0.0050s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 90.9% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 101.9% |
| `lteNRRCC` | 72.37 MB | 100.18 MB | 103.3% | 101.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0461s | 0.0446s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1420s | 0.1372s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0998s | 0.0951s | +0.0047s | worse |
| `lteNRRCC` | 0.1576s | 0.1513s | +0.0063s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 34.65 MB | 79.3% | 105.9% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.6% | 102.4% |
| `ngap_rel18.6_specs` | 17.92 MB | 72.65 MB | 107.1% | 103.3% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 101.4% | 101.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0593s | 0.0586s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1743s | 0.1804s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.1225s | 0.1260s | -0.0035s | improved |
| `lteNRRCC` | 0.1682s | 0.1766s | -0.0084s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 53.73 MB | 20.7% | 104.9% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.6% | 102.0% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 106.9% | 102.8% |
| `lteNRRCC` | 72.66 MB | 100.36 MB | 102.7% | 103.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0188s | 0.0311s | -0.0123s | improved |
| `f1ap_rel18.6_specs` | 0.0739s | 0.0721s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0740s | 0.0699s | +0.0041s | worse |
| `lteNRRCC` | 0.0908s | 0.0784s | +0.0124s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.17 MB | 8.02 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.67 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.44 MB | 7.81 MB | 1.3% | 0.0% |
| `lteNRRCC` | 7.62 MB | 7.41 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0386s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1066s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0819s | 0.0756s | +0.0063s | worse |
| `lteNRRCC` | 0.1372s | 0.1378s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.62 MB | 7.87 MB | 0.0% | 116.4% |
| `f1ap_rel18.6_specs` | 8.24 MB | 106.65 MB | 110.7% | 166.6% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.62 MB | 162.3% | 161.9% |
| `lteNRRCC` | 49.07 MB | 51.57 MB | 165.2% | 168.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0318s | +0.0078s | worse |
| `f1ap_rel18.6_specs` | 0.1152s | 0.0988s | +0.0164s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0605s | +0.0162s | worse |
| `lteNRRCC` | 0.1270s | 0.0899s | +0.0371s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 10.16 MB | 0.0% | 102.0% |
| `f1ap_rel18.6_specs` | 11.59 MB | 9.47 MB | 108.9% | 95.8% |
| `ngap_rel18.6_specs` | 9.03 MB | 11.13 MB | 153.2% | 220.3% |
| `lteNRRCC` | 73.77 MB | 97.02 MB | 109.2% | 107.0% |
<!-- BENCH_RESULTS_END -->
