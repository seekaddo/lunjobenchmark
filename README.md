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
Generated: 2026-03-12T21:52:58.809475+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.1010s | -0.0613s | improved |
| `f1ap_rel18.6_specs` | 0.1264s | 0.3087s | -0.1823s | improved |
| `ngap_rel18.6_specs` | 0.0863s | 0.2237s | -0.1374s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.54 MB | 55.92 MB | 95.5% | 109.7% |
| `f1ap_rel18.6_specs` | 32.42 MB | 176.92 MB | 110.0% | 104.1% |
| `ngap_rel18.6_specs` | 22.29 MB | 125.92 MB | 108.3% | 103.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0709s | -0.0360s | improved |
| `f1ap_rel18.6_specs` | 0.1009s | 0.1947s | -0.0938s | improved |
| `ngap_rel18.6_specs` | 0.0707s | 0.1430s | -0.0723s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.66 MB | 37.67 MB | 20.2% | 107.7% |
| `f1ap_rel18.6_specs` | 22.04 MB | 111.68 MB | 110.3% | 105.1% |
| `ngap_rel18.6_specs` | 16.92 MB | 80.44 MB | 108.7% | 104.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0714s | -0.0361s | improved |
| `f1ap_rel18.6_specs` | 0.0928s | 0.1951s | -0.1023s | improved |
| `ngap_rel18.6_specs` | 0.0656s | 0.1442s | -0.0786s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.78 MB | 57.91 MB | 92.3% | 110.3% |
| `f1ap_rel18.6_specs` | 33.89 MB | 179.21 MB | 109.7% | 105.2% |
| `ngap_rel18.6_specs` | 24.00 MB | 127.16 MB | 111.5% | 106.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0243s | 0.0584s | -0.0341s | improved |
| `f1ap_rel18.6_specs` | 0.0668s | 0.1988s | -0.1320s | improved |
| `ngap_rel18.6_specs` | 0.0487s | 0.1289s | -0.0802s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.86 MB | 3.81 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.45 MB | 4.27 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.55 MB | 3.95 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0422s | 0.0825s | -0.0403s | improved |
| `f1ap_rel18.6_specs` | 0.1144s | 0.2438s | -0.1294s | improved |
| `ngap_rel18.6_specs` | 0.0797s | 0.1737s | -0.0940s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.65 MB | 7.98 MB | 79.6% | 108.6% |
| `f1ap_rel18.6_specs` | 8.00 MB | 8.25 MB | 148.0% | 159.5% |
| `ngap_rel18.6_specs` | 7.65 MB | 7.71 MB | 159.1% | 154.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0935s | -0.0534s | improved |
| `f1ap_rel18.6_specs` | 0.1236s | 0.2677s | -0.1441s | improved |
| `ngap_rel18.6_specs` | 0.0841s | 0.1965s | -0.1124s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.66 MB | 8.75 MB | 111.1% | 153.0% |
| `f1ap_rel18.6_specs` | 9.76 MB | 179.27 MB | 161.7% | 107.8% |
| `ngap_rel18.6_specs` | 8.95 MB | 8.82 MB | 157.2% | 95.6% |
<!-- BENCH_RESULTS_END -->
