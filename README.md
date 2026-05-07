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
Generated: 2026-05-07T23:04:56.216264+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0365s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1138s | 0.1143s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0793s | 0.0790s | +0.0003s | worse |
| `lteNRRCC` | 0.1232s | 0.1226s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 8.9% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0374s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0943s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0677s | 0.0671s | +0.0006s | worse |
| `lteNRRCC` | 0.1291s | 0.1288s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.22 MB | 36.36 MB | 62.5% | 114.3% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.13 MB | 109.1% | 106.8% |
| `ngap_rel18.6_specs` | 16.54 MB | 73.67 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.72 MB | 66.27 MB | 103.1% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0320s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0898s | 0.0769s | +0.0129s | worse |
| `ngap_rel18.6_specs` | 0.0625s | 0.0544s | +0.0081s | worse |
| `lteNRRCC` | 0.1167s | 0.1033s | +0.0134s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.99 MB | 55.67 MB | 27.2% | 107.1% |
| `f1ap_rel18.6_specs` | 33.80 MB | 164.56 MB | 110.0% | 105.5% |
| `ngap_rel18.6_specs` | 24.57 MB | 117.50 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.95 MB | 102.89 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0263s | 0.0272s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0857s | 0.0832s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0553s | 0.0629s | -0.0076s | improved |
| `lteNRRCC` | 0.1153s | 0.0823s | +0.0330s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 704 KB | 4.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.50 MB | 4.58 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.34 MB | 4.00 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.27 MB | 4.19 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0395s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1119s | -0.0057s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0766s | -0.0003s | improved |
| `lteNRRCC` | 0.1384s | 0.1384s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.56 MB | 7.68 MB | 105.3% | 117.2% |
| `f1ap_rel18.6_specs` | 8.10 MB | 8.17 MB | 80.4% | 159.9% |
| `ngap_rel18.6_specs` | 7.86 MB | 7.61 MB | 79.2% | 160.7% |
| `lteNRRCC` | 51.07 MB | 64.23 MB | 159.0% | 158.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0442s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.1185s | 0.1265s | -0.0080s | improved |
| `ngap_rel18.6_specs` | 0.0832s | 0.0905s | -0.0073s | improved |
| `lteNRRCC` | 0.1311s | 0.1347s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.86 MB | 8.79 MB | 138.1% | 149.4% |
| `f1ap_rel18.6_specs` | 10.61 MB | 164.20 MB | 101.4% | 148.2% |
| `ngap_rel18.6_specs` | 10.50 MB | 9.38 MB | 93.6% | 147.4% |
| `lteNRRCC` | 8.68 MB | 99.08 MB | 147.8% | 104.8% |
<!-- BENCH_RESULTS_END -->
