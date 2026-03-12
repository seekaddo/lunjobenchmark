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
Generated: 2026-03-12T22:34:39.085374+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0385s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1207s | 0.1233s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0824s | 0.0847s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.54 MB | 55.92 MB | 82.6% | 106.9% |
| `f1ap_rel18.6_specs` | 32.42 MB | 176.92 MB | 106.9% | 102.9% |
| `ngap_rel18.6_specs` | 22.29 MB | 125.92 MB | 108.7% | 103.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0369s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0991s | 0.0992s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0682s | 0.0697s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.75 MB | 38.04 MB | 24.4% | 107.7% |
| `f1ap_rel18.6_specs` | 22.04 MB | 111.56 MB | 106.9% | 103.4% |
| `ngap_rel18.6_specs` | 16.93 MB | 80.34 MB | 108.7% | 104.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0372s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0927s | 0.0977s | -0.0050s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0693s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.75 MB | 57.92 MB | 88.9% | 113.8% |
| `f1ap_rel18.6_specs` | 34.27 MB | 178.96 MB | 112.9% | 106.9% |
| `ngap_rel18.6_specs` | 24.25 MB | 128.01 MB | 111.5% | 106.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0220s | 0.0216s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0738s | 0.0655s | +0.0083s | worse |
| `ngap_rel18.6_specs` | 0.0584s | 0.0443s | +0.0141s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.92 MB | 4.89 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.14 MB | 4.11 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 192 KB | 2.36 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0405s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1113s | 0.1180s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0779s | 0.0816s | -0.0037s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.38 MB | 7.31 MB | 183.7% | 81.3% |
| `f1ap_rel18.6_specs` | 7.91 MB | 114.88 MB | 84.9% | 107.1% |
| `ngap_rel18.6_specs` | 7.43 MB | 7.43 MB | 168.1% | 166.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0457s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1369s | -0.0239s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0959s | -0.0169s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.21 MB | 9.64 MB | 226.8% | 102.7% |
| `f1ap_rel18.6_specs` | 11.03 MB | 147.99 MB | 234.3% | 106.6% |
| `ngap_rel18.6_specs` | 10.25 MB | 9.14 MB | 118.0% | 105.8% |
<!-- BENCH_RESULTS_END -->
