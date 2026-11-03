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
Generated: 2026-11-03T17:40:26.853178+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0406s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1287s | 0.1258s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0887s | 0.0867s | +0.0020s | worse |
| `lteNRRCC` | 0.1326s | 0.1310s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 75.9% | 106.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.1% | 103.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 103.7% | 103.5% |
| `lteNRRCC` | 72.37 MB | 100.18 MB | 103.2% | 102.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0446s | 0.0440s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1372s | 0.1391s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0951s | 0.0939s | +0.0012s | worse |
| `lteNRRCC` | 0.1513s | 0.1526s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 34.65 MB | 88.5% | 106.1% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 102.8% | 102.5% |
| `ngap_rel18.6_specs` | 17.97 MB | 72.65 MB | 107.1% | 105.1% |
| `lteNRRCC` | 46.71 MB | 64.21 MB | 102.8% | 102.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0586s | 0.0532s | +0.0054s | worse |
| `f1ap_rel18.6_specs` | 0.1804s | 0.1641s | +0.0163s | worse |
| `ngap_rel18.6_specs` | 0.1260s | 0.1133s | +0.0127s | worse |
| `lteNRRCC` | 0.1766s | 0.1616s | +0.0150s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.81 MB | 53.73 MB | 88.0% | 102.5% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.6% | 102.0% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 103.4% | 102.8% |
| `lteNRRCC` | 72.64 MB | 100.36 MB | 102.6% | 102.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0311s | 0.0290s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0721s | 0.0810s | -0.0089s | improved |
| `ngap_rel18.6_specs` | 0.0699s | 0.0567s | +0.0132s | worse |
| `lteNRRCC` | 0.0784s | 0.1133s | -0.0349s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.78 MB | 6.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.08 MB | 8.89 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.28 MB | 8.50 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.52 MB | 7.22 MB | 0.6% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0392s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1066s | 0.1104s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0782s | -0.0026s | improved |
| `lteNRRCC` | 0.1378s | 0.1384s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.69 MB | 7.64 MB | 0.0% | 77.9% |
| `f1ap_rel18.6_specs` | 8.00 MB | 8.68 MB | 157.8% | 110.8% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.69 MB | 162.7% | 79.6% |
| `lteNRRCC` | 8.68 MB | 51.22 MB | 219.4% | 108.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0318s | 0.0397s | -0.0079s | improved |
| `f1ap_rel18.6_specs` | 0.0988s | 0.1147s | -0.0159s | improved |
| `ngap_rel18.6_specs` | 0.0605s | 0.0835s | -0.0230s | improved |
| `lteNRRCC` | 0.0899s | 0.1307s | -0.0408s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 11.73 MB | 0.0% | 138.9% |
| `f1ap_rel18.6_specs` | 11.84 MB | 11.84 MB | 144.0% | 143.5% |
| `ngap_rel18.6_specs` | 11.65 MB | 11.46 MB | 226.8% | 146.6% |
| `lteNRRCC` | 9.50 MB | 101.71 MB | 230.4% | 148.0% |
<!-- BENCH_RESULTS_END -->
