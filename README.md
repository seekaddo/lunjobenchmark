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
Generated: 2026-09-17T00:17:30.028818+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0353s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1095s | 0.1097s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0750s | +0.0013s | worse |
| `lteNRRCC` | 0.1200s | 0.1188s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 75.0% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0386s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.0971s | 0.1055s | -0.0084s | improved |
| `ngap_rel18.6_specs` | 0.0680s | 0.0753s | -0.0073s | improved |
| `lteNRRCC` | 0.1306s | 0.1419s | -0.0113s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.03 MB | 76.7% | 103.6% |
| `f1ap_rel18.6_specs` | 22.31 MB | 102.65 MB | 103.1% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.65 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.77 MB | 66.26 MB | 103.1% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0358s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0921s | 0.0970s | -0.0049s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0672s | -0.0033s | improved |
| `lteNRRCC` | 0.1270s | 0.1308s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.70 MB | 60.0% | 103.6% |
| `f1ap_rel18.6_specs` | 34.41 MB | 164.20 MB | 106.7% | 103.6% |
| `ngap_rel18.6_specs` | 24.13 MB | 117.71 MB | 108.0% | 102.4% |
| `lteNRRCC` | 74.36 MB | 102.79 MB | 103.2% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0318s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.0742s | 0.0903s | -0.0161s | improved |
| `ngap_rel18.6_specs` | 0.0502s | 0.0654s | -0.0152s | improved |
| `lteNRRCC` | 0.0943s | 0.0873s | +0.0070s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.78 MB | 8.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.61 MB | 9.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.19 MB | 8.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.56 MB | 7.22 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
