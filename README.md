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
Generated: 2026-03-12T18:07:17.704015+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0979s | 0.0979s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.3015s | 0.3021s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.2243s | 0.2191s | +0.0052s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.30 MB | 5.30 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.38 MB | 471.40 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 5.68 MB | 238.05 MB | 0.0% | 91.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0691s | 0.0726s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.1933s | 0.2235s | -0.0302s | improved |
| `ngap_rel18.6_specs` | 0.1417s | 0.1503s | -0.0086s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.39 MB | 4.68 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.11 MB | 220.13 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 5.52 MB | 248.85 MB | 0.0% | 92.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0693s | 0.0713s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1958s | 0.1982s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.1462s | 0.1480s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.61 MB | 6.68 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.29 MB | 348.38 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 7.11 MB | 363.63 MB | 0.0% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0721s | 0.0628s | +0.0093s | worse |
| `f1ap_rel18.6_specs` | 0.1975s | 0.1783s | +0.0192s | worse |
| `ngap_rel18.6_specs` | 0.2170s | 0.1177s | +0.0993s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.72 MB | 6.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.92 MB | 6.56 MB | 0.0% | 0.4% |
| `ngap_rel18.6_specs` | 8.42 MB | 4.91 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
