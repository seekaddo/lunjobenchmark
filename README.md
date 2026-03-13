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
Generated: 2026-03-13T16:08:44.124534+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0393s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1225s | 0.1253s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0856s | 0.0861s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | n/a | n/a | n/a | n/a |
| `f1ap_rel18.6_specs` | n/a | n/a | n/a | n/a |
| `ngap_rel18.6_specs` | n/a | n/a | n/a | n/a |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0368s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1016s | 0.1020s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0724s | 0.0701s | +0.0023s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | n/a | n/a | n/a | n/a |
| `f1ap_rel18.6_specs` | n/a | n/a | n/a | n/a |
| `ngap_rel18.6_specs` | n/a | n/a | n/a | n/a |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0361s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0941s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0677s | 0.0667s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | n/a | n/a | n/a | n/a |
| `f1ap_rel18.6_specs` | n/a | n/a | n/a | n/a |
| `ngap_rel18.6_specs` | n/a | n/a | n/a | n/a |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0223s | 0.0225s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0725s | 0.0838s | -0.0113s | improved |
| `ngap_rel18.6_specs` | 0.0525s | 0.0531s | -0.0006s | improved |

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
| `e1ap_rel18.4_specs` | 0.0422s | 0.0419s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1184s | 0.1195s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0831s | 0.0822s | +0.0009s | worse |

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
| `e1ap_rel18.4_specs` | 0.0390s | 0.0389s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1160s | 0.1165s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0803s | 0.0804s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | n/a | n/a | n/a | n/a |
| `f1ap_rel18.6_specs` | n/a | n/a | n/a | n/a |
| `ngap_rel18.6_specs` | n/a | n/a | n/a | n/a |
<!-- BENCH_RESULTS_END -->
