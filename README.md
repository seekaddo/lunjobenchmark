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
Generated: 2026-03-12T19:33:05.208725+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.1010s | 0.0999s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.3087s | 0.3077s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.2237s | 0.2231s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.54 MB | 184.54 MB | 105.6% | 103.3% |
| `f1ap_rel18.6_specs` | 32.41 MB | 563.04 MB | 106.7% | 101.2% |
| `ngap_rel18.6_specs` | 22.29 MB | 419.29 MB | 112.5% | 102.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0709s | 0.0683s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1947s | 0.1969s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.1430s | 0.1433s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.78 MB | 123.57 MB | 89.3% | 106.4% |
| `f1ap_rel18.6_specs` | 22.29 MB | 370.14 MB | 111.4% | 102.8% |
| `ngap_rel18.6_specs` | 16.17 MB | 276.81 MB | 110.3% | 104.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0714s | 0.0708s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1951s | 0.1918s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.1442s | 0.1438s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.79 MB | 186.79 MB | 82.8% | 104.2% |
| `f1ap_rel18.6_specs` | 34.77 MB | 564.93 MB | 109.7% | 102.8% |
| `ngap_rel18.6_specs` | 24.25 MB | 421.24 MB | 111.5% | 103.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0584s | 0.0464s | +0.0120s | worse |
| `f1ap_rel18.6_specs` | 0.1988s | 0.1447s | +0.0541s | worse |
| `ngap_rel18.6_specs` | 0.1289s | 0.1316s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.47 MB | 5.05 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.89 MB | 5.75 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.08 MB | 421.00 MB | 0.0% | 35.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0825s | 0.0848s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.2438s | 0.2462s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.1737s | 0.1802s | -0.0065s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.39 MB | 7.41 MB | 166.8% | 104.3% |
| `f1ap_rel18.6_specs` | 7.89 MB | 376.50 MB | 164.6% | 105.0% |
| `ngap_rel18.6_specs` | 7.36 MB | 280.45 MB | 169.0% | 166.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0935s | 0.0906s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.2677s | 0.2784s | -0.0107s | improved |
| `ngap_rel18.6_specs` | 0.1965s | 0.1971s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.84 MB | 8.57 MB | 119.2% | 162.0% |
| `f1ap_rel18.6_specs` | 9.83 MB | 565.44 MB | 95.4% | 163.6% |
| `ngap_rel18.6_specs` | 9.05 MB | 421.56 MB | 156.0% | 158.8% |
<!-- BENCH_RESULTS_END -->
