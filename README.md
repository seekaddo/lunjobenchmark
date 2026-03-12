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
Generated: 2026-03-12T22:11:21.800741+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0397s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1233s | 0.1264s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0847s | 0.0863s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.54 MB | 55.92 MB | 58.8% | 110.3% |
| `f1ap_rel18.6_specs` | 32.42 MB | 176.92 MB | 106.9% | 104.2% |
| `ngap_rel18.6_specs` | 22.29 MB | 125.92 MB | 108.3% | 103.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0349s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0992s | 0.1009s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0697s | 0.0707s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.79 MB | 38.04 MB | 89.3% | 113.3% |
| `f1ap_rel18.6_specs` | 22.17 MB | 111.94 MB | 108.6% | 106.6% |
| `ngap_rel18.6_specs` | 16.55 MB | 80.32 MB | 110.3% | 106.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0353s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0977s | 0.0928s | +0.0049s | worse |
| `ngap_rel18.6_specs` | 0.0693s | 0.0656s | +0.0037s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.78 MB | 58.11 MB | 22.8% | 109.7% |
| `f1ap_rel18.6_specs` | 34.77 MB | 179.09 MB | 112.5% | 106.6% |
| `ngap_rel18.6_specs` | 24.50 MB | 128.01 MB | 110.7% | 108.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0216s | 0.0243s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.0655s | 0.0668s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0443s | 0.0487s | -0.0044s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.31 MB | 4.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.12 MB | 4.28 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.53 MB | 3.95 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0422s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1180s | 0.1144s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0797s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.72 MB | 7.39 MB | 103.7% | 163.6% |
| `f1ap_rel18.6_specs` | 8.01 MB | 110.06 MB | 80.7% | 162.7% |
| `ngap_rel18.6_specs` | 7.43 MB | 7.58 MB | 165.1% | 82.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0457s | 0.0401s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.1369s | 0.1236s | +0.0133s | worse |
| `ngap_rel18.6_specs` | 0.0959s | 0.0841s | +0.0118s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.61 MB | 7.97 MB | 161.3% | 105.2% |
| `f1ap_rel18.6_specs` | 10.51 MB | 179.21 MB | 115.4% | 117.4% |
| `ngap_rel18.6_specs` | 9.39 MB | 9.60 MB | 96.2% | 160.5% |
<!-- BENCH_RESULTS_END -->
