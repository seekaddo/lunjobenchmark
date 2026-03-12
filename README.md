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
Generated: 2026-03-12T17:36:25.865692+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.1005s | 0.0983s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.3098s | 0.3038s | +0.0060s | worse |
| `ngap_rel18.6_specs` | 0.2304s | 0.2194s | +0.0110s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.50 MB | 5.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.51 MB | 426.23 MB | 0.0% | 95.6% |
| `ngap_rel18.6_specs` | 6.00 MB | 216.30 MB | 0.0% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0727s | 0.0697s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.2039s | 0.2079s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.1499s | 0.1516s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.41 MB | 4.82 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.09 MB | 206.68 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 4.84 MB | 238.23 MB | 0.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0711s | 0.0707s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1902s | 0.1948s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.1411s | 0.1431s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.34 MB | 6.25 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.58 MB | 362.90 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 7.44 MB | 385.38 MB | 0.0% | 100.0% |
<!-- BENCH_RESULTS_END -->
