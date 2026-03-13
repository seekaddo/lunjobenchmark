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
Generated: 2026-03-13T16:05:18.355397+00:00

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0225s | 0.0206s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0838s | 0.0621s | +0.0217s | worse |
| `ngap_rel18.6_specs` | 0.0531s | 0.0427s | +0.0104s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | n/a | n/a | n/a | n/a |
| `f1ap_rel18.6_specs` | n/a | n/a | n/a | n/a |
| `ngap_rel18.6_specs` | n/a | n/a | n/a | n/a |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0401s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1195s | 0.1137s | +0.0058s | worse |
| `ngap_rel18.6_specs` | 0.0822s | 0.0800s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | n/a | n/a | n/a | n/a |
| `f1ap_rel18.6_specs` | n/a | n/a | n/a | n/a |
| `ngap_rel18.6_specs` | n/a | n/a | n/a | n/a |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0431s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.1165s | 0.1226s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0804s | 0.0838s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | n/a | n/a | n/a | n/a |
| `f1ap_rel18.6_specs` | n/a | n/a | n/a | n/a |
| `ngap_rel18.6_specs` | n/a | n/a | n/a | n/a |
<!-- BENCH_RESULTS_END -->
