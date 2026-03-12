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
Generated: 2026-03-12T17:53:19.475429+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0979s | 0.0984s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.3021s | 0.3057s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.2191s | 0.2196s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.49 MB | 5.52 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.58 MB | 461.41 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 5.94 MB | 232.93 MB | 0.0% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0726s | 0.0685s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.2235s | 0.1943s | +0.0292s | worse |
| `ngap_rel18.6_specs` | 0.1503s | 0.1421s | +0.0082s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.80 MB | 4.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.07 MB | 206.27 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 5.27 MB | 198.36 MB | 0.0% | 92.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0713s | 0.0709s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1982s | 0.1971s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.1480s | 0.1430s | +0.0050s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.81 MB | 6.93 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.79 MB | 348.44 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 7.99 MB | 376.51 MB | 0.0% | 92.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0628s | 0.0459s | +0.0169s | worse |
| `f1ap_rel18.6_specs` | 0.1783s | 0.1381s | +0.0402s | worse |
| `ngap_rel18.6_specs` | 0.1177s | 0.1003s | +0.0174s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.77 MB | 4.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.86 MB | 4.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 272 KB | 3.98 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
