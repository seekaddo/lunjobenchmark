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
Generated: 2026-05-29T23:20:23.258208+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0364s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1171s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0792s | 0.0788s | +0.0004s | worse |
| `lteNRRCC` | 0.1231s | 0.1253s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 27.0% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 103.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0347s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0935s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0671s | 0.0654s | +0.0017s | worse |
| `lteNRRCC` | 0.1283s | 0.1253s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.54 MB | 86.2% | 113.8% |
| `f1ap_rel18.6_specs` | 22.38 MB | 102.93 MB | 109.1% | 106.9% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.69 MB | 114.8% | 106.7% |
| `lteNRRCC` | 47.90 MB | 66.32 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0364s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1051s | 0.0961s | +0.0090s | worse |
| `ngap_rel18.6_specs` | 0.0659s | 0.0674s | -0.0015s | improved |
| `lteNRRCC` | 0.1272s | 0.1292s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.62 MB | 20.0% | 110.0% |
| `f1ap_rel18.6_specs` | 34.68 MB | 164.71 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.68 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.97 MB | 102.57 MB | 106.2% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0408s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.0666s | 0.0673s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0476s | 0.0380s | +0.0096s | worse |
| `lteNRRCC` | 0.0843s | 0.0698s | +0.0145s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.23 MB | 8.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.50 MB | 4.66 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.00 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.25 MB | 4.08 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0406s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1071s | 0.1098s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0776s | -0.0024s | improved |
| `lteNRRCC` | 0.1356s | 0.1394s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.62 MB | 7.32 MB | 117.9% | 93.9% |
| `f1ap_rel18.6_specs` | 8.04 MB | 7.97 MB | 103.3% | 83.0% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.98 MB | 90.7% | 227.3% |
| `lteNRRCC` | 48.94 MB | 65.61 MB | 107.2% | 108.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0447s | -0.0039s | improved |
| `f1ap_rel18.6_specs` | 0.1188s | 0.1319s | -0.0131s | improved |
| `ngap_rel18.6_specs` | 0.0801s | 0.0904s | -0.0103s | improved |
| `lteNRRCC` | 0.1366s | 0.1462s | -0.0096s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.14 MB | 9.01 MB | 110.6% | 179.2% |
| `f1ap_rel18.6_specs` | 11.26 MB | 162.23 MB | 110.9% | 165.2% |
| `ngap_rel18.6_specs` | 10.56 MB | 9.38 MB | 226.6% | 161.8% |
| `lteNRRCC` | 8.87 MB | 75.14 MB | 163.6% | 104.5% |
<!-- BENCH_RESULTS_END -->
