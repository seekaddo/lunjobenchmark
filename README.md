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
Generated: 2026-03-12T18:15:35.106031+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0984s | 0.1013s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.3055s | 0.3156s | -0.0101s | improved |
| `ngap_rel18.6_specs` | 0.2270s | 0.2278s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.39 MB | 5.32 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.25 MB | 456.03 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 5.68 MB | 232.43 MB | 0.0% | 91.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0702s | 0.0714s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1944s | 0.1959s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.1425s | 0.1433s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.66 MB | 4.87 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.55 MB | 209.12 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 5.16 MB | 252.23 MB | 0.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0708s | 0.0681s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1919s | 0.1914s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.1411s | 0.1408s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.70 MB | 6.29 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.39 MB | 360.50 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 7.22 MB | 392.36 MB | 0.0% | 92.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0462s | 0.0650s | -0.0188s | improved |
| `f1ap_rel18.6_specs` | 0.1644s | 0.2384s | -0.0740s | improved |
| `ngap_rel18.6_specs` | 0.1146s | 0.1614s | -0.0468s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.30 MB | 8.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.70 MB | 4.70 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.47 MB | 2.17 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
