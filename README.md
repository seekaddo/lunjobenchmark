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
Generated: 2026-08-20T10:37:05.775038+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0373s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1135s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0764s | 0.0771s | -0.0007s | improved |
| `lteNRRCC` | 0.1205s | 0.1219s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.73 MB | 53.55 MB | 64.3% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0356s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0956s | 0.0964s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0660s | 0.0693s | -0.0033s | improved |
| `lteNRRCC` | 0.1295s | 0.1318s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.71 MB | 71.4% | 107.7% |
| `f1ap_rel18.6_specs` | 22.13 MB | 103.41 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.55 MB | 108.0% | 104.8% |
| `lteNRRCC` | 48.19 MB | 66.03 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0374s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0971s | 0.1036s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0688s | 0.0712s | -0.0024s | improved |
| `lteNRRCC` | 0.1307s | 0.1187s | +0.0120s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 54.76 MB | 23.0% | 106.9% |
| `f1ap_rel18.6_specs` | 34.77 MB | 163.36 MB | 106.5% | 103.4% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.84 MB | 107.7% | 104.5% |
| `lteNRRCC` | 74.28 MB | 102.95 MB | 101.6% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0243s | 0.0188s | +0.0055s | worse |
| `f1ap_rel18.6_specs` | 0.0683s | 0.0693s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0474s | 0.0471s | +0.0003s | worse |
| `lteNRRCC` | 0.0776s | 0.0832s | -0.0056s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.28 MB | 3.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.48 MB | 5.50 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.47 MB | 4.53 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.02 MB | 3.75 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0399s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1094s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0771s | -0.0005s | improved |
| `lteNRRCC` | 0.1390s | 0.1415s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.50 MB | 0.0% | 157.9% |
| `f1ap_rel18.6_specs` | 8.17 MB | 8.17 MB | 115.0% | 77.5% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.18 MB | 154.8% | 98.3% |
| `lteNRRCC` | 51.09 MB | 69.23 MB | 157.2% | 155.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0391s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1191s | -0.0095s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0831s | -0.0068s | improved |
| `lteNRRCC` | 0.1269s | 0.1170s | +0.0099s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.75 MB | 8.46 MB | 113.2% | 81.7% |
| `f1ap_rel18.6_specs` | 11.04 MB | 11.28 MB | 116.3% | 118.1% |
| `ngap_rel18.6_specs` | 10.57 MB | 10.94 MB | 114.4% | 114.6% |
| `lteNRRCC` | 8.37 MB | 73.88 MB | 79.8% | 231.1% |
<!-- BENCH_RESULTS_END -->
