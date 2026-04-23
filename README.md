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
Generated: 2026-04-23T22:56:27.903609+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0370s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1153s | 0.1144s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0792s | 0.0796s | -0.0004s | improved |
| `lteNRRCC` | 0.1230s | 0.1231s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 22.4% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 107.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0338s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0932s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0662s | 0.0656s | +0.0006s | worse |
| `lteNRRCC` | 0.1290s | 0.1281s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.39 MB | 36.63 MB | 96.0% | 114.3% |
| `f1ap_rel18.6_specs` | 22.32 MB | 102.90 MB | 106.1% | 103.4% |
| `ngap_rel18.6_specs` | 16.65 MB | 74.35 MB | 110.3% | 106.8% |
| `lteNRRCC` | 48.76 MB | 66.46 MB | 103.1% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0339s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0915s | 0.0918s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0629s | +0.0011s | worse |
| `lteNRRCC` | 0.1176s | 0.1181s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.72 MB | 100.0% | 110.7% |
| `f1ap_rel18.6_specs` | 34.68 MB | 164.37 MB | 110.0% | 107.0% |
| `ngap_rel18.6_specs` | 23.93 MB | 117.36 MB | 116.0% | 106.8% |
| `lteNRRCC` | 74.94 MB | 102.24 MB | 105.2% | 102.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0186s | 0.0197s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0597s | 0.0593s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0402s | 0.0415s | -0.0013s | improved |
| `lteNRRCC` | 0.0679s | 0.0682s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 4.38 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.38 MB | 5.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.50 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.81 MB | 4.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0413s | -0.0078s | improved |
| `f1ap_rel18.6_specs` | 0.0935s | 0.1129s | -0.0194s | improved |
| `ngap_rel18.6_specs` | 0.0666s | 0.0801s | -0.0135s | improved |
| `lteNRRCC` | 0.1118s | 0.1415s | -0.0297s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.43 MB | 8.04 MB | 134.1% | 119.9% |
| `f1ap_rel18.6_specs` | 8.80 MB | 106.60 MB | 101.9% | 105.2% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.30 MB | 102.7% | 135.4% |
| `lteNRRCC` | 51.84 MB | 58.86 MB | 135.3% | 202.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0392s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1160s | 0.1116s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0810s | 0.0803s | +0.0007s | worse |
| `lteNRRCC` | 0.1321s | 0.1282s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.32 MB | 8.79 MB | 149.2% | 153.7% |
| `f1ap_rel18.6_specs` | 9.66 MB | 10.43 MB | 151.2% | 150.7% |
| `ngap_rel18.6_specs` | 10.66 MB | 11.65 MB | 107.4% | 172.5% |
| `lteNRRCC` | 8.74 MB | 80.39 MB | 160.2% | 106.9% |
<!-- BENCH_RESULTS_END -->
