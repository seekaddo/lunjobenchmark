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
Generated: 2026-08-25T10:38:57.714505+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0356s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1141s | 0.1105s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0780s | 0.0758s | +0.0022s | worse |
| `lteNRRCC` | 0.1216s | 0.1211s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 18.8% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0338s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0918s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0659s | 0.0647s | +0.0012s | worse |
| `lteNRRCC` | 0.1288s | 0.1269s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 36.64 MB | 76.9% | 107.7% |
| `f1ap_rel18.6_specs` | 22.39 MB | 103.33 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.62 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.13 MB | 66.30 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0305s | +0.0050s | worse |
| `f1ap_rel18.6_specs` | 0.1018s | 0.0797s | +0.0221s | worse |
| `ngap_rel18.6_specs` | 0.0706s | 0.0552s | +0.0154s | worse |
| `lteNRRCC` | 0.1171s | 0.1043s | +0.0128s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 55.60 MB | 73.9% | 104.0% |
| `f1ap_rel18.6_specs` | 34.79 MB | 164.68 MB | 103.8% | 101.7% |
| `ngap_rel18.6_specs` | 24.42 MB | 117.69 MB | 100.0% | 100.0% |
| `lteNRRCC` | 74.98 MB | 102.94 MB | 100.0% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0262s | 0.0239s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0660s | +0.0282s | worse |
| `ngap_rel18.6_specs` | 0.0548s | 0.0473s | +0.0075s | worse |
| `lteNRRCC` | 0.0978s | 0.0787s | +0.0191s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 3.48 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.44 MB | 5.17 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.41 MB | 6.89 MB | 0.6% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0433s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1201s | -0.0073s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0799s | -0.0023s | improved |
| `lteNRRCC` | 0.1397s | 0.1418s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.50 MB | 7.84 MB | 96.4% | 180.5% |
| `f1ap_rel18.6_specs` | 8.48 MB | 106.64 MB | 80.7% | 161.7% |
| `ngap_rel18.6_specs` | 8.27 MB | 8.18 MB | 102.1% | 161.7% |
| `lteNRRCC` | 51.84 MB | 60.73 MB | 218.5% | 157.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0386s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1086s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0779s | 0.0751s | +0.0028s | worse |
| `lteNRRCC` | 0.1282s | 0.1254s | +0.0028s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.66 MB | 8.66 MB | 218.7% | 160.3% |
| `f1ap_rel18.6_specs` | 11.33 MB | 10.58 MB | 94.2% | 102.8% |
| `ngap_rel18.6_specs` | 9.14 MB | 9.23 MB | 149.0% | 76.6% |
| `lteNRRCC` | 73.78 MB | 72.96 MB | 152.9% | 146.6% |
<!-- BENCH_RESULTS_END -->
