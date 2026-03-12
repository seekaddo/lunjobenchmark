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
Generated: 2026-03-12T17:45:55.663884+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0984s | 0.0980s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.3057s | 0.3062s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.2196s | 0.2180s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.75 MB | 5.54 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.61 MB | 466.18 MB | 0.0% | 95.6% |
| `ngap_rel18.6_specs` | 5.82 MB | 233.40 MB | 0.0% | 91.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0685s | 0.0735s | -0.0050s | improved |
| `f1ap_rel18.6_specs` | 0.1943s | 0.1991s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.1421s | 0.1453s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.54 MB | 4.96 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.17 MB | 201.26 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 4.97 MB | 248.73 MB | 0.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0709s | 0.0896s | -0.0187s | improved |
| `f1ap_rel18.6_specs` | 0.1971s | 0.2645s | -0.0674s | improved |
| `ngap_rel18.6_specs` | 0.1430s | 0.1925s | -0.0495s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.23 MB | 6.51 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.20 MB | 354.50 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 7.39 MB | 383.66 MB | 0.0% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0459s | 0.0528s | -0.0069s | improved |
| `f1ap_rel18.6_specs` | 0.1381s | 0.1650s | -0.0269s | improved |
| `ngap_rel18.6_specs` | 0.1003s | 0.1665s | -0.0662s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.34 MB | 4.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.86 MB | 4.11 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.91 MB | 3.98 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
