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
Generated: 2026-03-12T18:11:17.240611+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.1013s | 0.0979s | +0.0034s | worse |
| `f1ap_rel18.6_specs` | 0.3156s | 0.3015s | +0.0141s | worse |
| `ngap_rel18.6_specs` | 0.2278s | 0.2243s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.43 MB | 5.38 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.94 MB | 446.86 MB | 0.0% | 95.8% |
| `ngap_rel18.6_specs` | 5.78 MB | 232.14 MB | 0.0% | 91.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0714s | 0.0691s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1959s | 0.1933s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.1433s | 0.1417s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.73 MB | 4.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.33 MB | 220.55 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 5.11 MB | 246.47 MB | 0.0% | 109.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0681s | 0.0693s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1914s | 0.1958s | -0.0044s | improved |
| `ngap_rel18.6_specs` | 0.1408s | 0.1462s | -0.0054s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.61 MB | 6.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.44 MB | 375.38 MB | 0.0% | 84.6% |
| `ngap_rel18.6_specs` | 7.73 MB | 390.23 MB | 0.0% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0650s | 0.0721s | -0.0071s | improved |
| `f1ap_rel18.6_specs` | 0.2384s | 0.1975s | +0.0409s | worse |
| `ngap_rel18.6_specs` | 0.1614s | 0.2170s | -0.0556s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.36 MB | 11.55 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.72 MB | 410.67 MB | 0.0% | 20.7% |
| `ngap_rel18.6_specs` | 5.97 MB | 6.08 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
