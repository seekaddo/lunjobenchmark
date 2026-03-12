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
- `bench_results/`: latest and historical benchmark output

## Assumptions

- The benchmark repo has access to release archives named like `voltcc-v<version>-<target>.tar.gz`.
- `preparebin.sh` prefers `./releases/` and falls back to `../releases/` for local nested-repo development.
- The copied upstream benchmark scripts execute the prepared binary from `./zig-out/bin/voltcc`, matching the local `test_semantic` script layout.

## Latest Results

<!-- BENCH_RESULTS_START -->
Generated: 2026-03-12T16:56:24.788148+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0983s | 0.0973s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.3038s | 0.3009s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.2194s | 0.2197s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.48 MB | 5.54 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.43 MB | 411.57 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 5.59 MB | 210.94 MB | 0.0% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0697s | 0.0714s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.2079s | 0.2046s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.1516s | 0.1499s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.93 MB | 3.98 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.65 MB | 163.95 MB | 0.0% | 90.9% |
| `ngap_rel18.6_specs` | 4.34 MB | 195.28 MB | 0.0% | 90.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0707s | 0.0998s | -0.0291s | improved |
| `f1ap_rel18.6_specs` | 0.1948s | 0.2643s | -0.0695s | improved |
| `ngap_rel18.6_specs` | 0.1431s | 0.1925s | -0.0495s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.67 MB | 6.61 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.30 MB | 311.93 MB | 0.0% | 90.9% |
| `ngap_rel18.6_specs` | 6.87 MB | 332.75 MB | 0.0% | 90.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0610s | 0.0542s | +0.0068s | worse |
| `f1ap_rel18.6_specs` | 0.1721s | 0.1603s | +0.0119s | worse |
| `ngap_rel18.6_specs` | 0.1223s | 0.1263s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.81 MB | 4.39 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.06 MB | 564.80 MB | 0.0% | 17.1% |
| `ngap_rel18.6_specs` | 5.19 MB | 4.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0880s | 0.0844s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.2507s | 0.2469s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.1875s | 0.1782s | +0.0093s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | n/a | n/a | n/a | n/a |
| `f1ap_rel18.6_specs` | n/a | 334.25 MB | n/a | n/a |
| `ngap_rel18.6_specs` | n/a | n/a | n/a | n/a |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0941s | 0.0896s | +0.0045s | worse |
| `f1ap_rel18.6_specs` | 0.2771s | 0.2767s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.2017s | 0.2086s | -0.0069s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | n/a | n/a | n/a | n/a |
| `f1ap_rel18.6_specs` | n/a | 411.21 MB | n/a | n/a |
| `ngap_rel18.6_specs` | n/a | 421.62 MB | n/a | n/a |
<!-- BENCH_RESULTS_END -->
