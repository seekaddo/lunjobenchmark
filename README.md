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
Generated: 2026-09-03T14:18:25.727946+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0355s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1149s | 0.1101s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0757s | +0.0013s | worse |
| `lteNRRCC` | 0.1204s | 0.1192s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 85.7% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0352s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0967s | 0.0952s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0683s | 0.0652s | +0.0031s | worse |
| `lteNRRCC` | 0.1322s | 0.1259s | +0.0063s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.60 MB | 16.1% | 103.6% |
| `f1ap_rel18.6_specs` | 22.31 MB | 103.07 MB | 103.1% | 103.4% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.60 MB | 103.8% | 104.7% |
| `lteNRRCC` | 48.69 MB | 66.30 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0285s | 0.0366s | -0.0081s | improved |
| `f1ap_rel18.6_specs` | 0.0889s | 0.0961s | -0.0072s | improved |
| `ngap_rel18.6_specs` | 0.0604s | 0.0678s | -0.0074s | improved |
| `lteNRRCC` | 0.0890s | 0.1292s | -0.0402s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 55.76 MB | 26.4% | 104.5% |
| `f1ap_rel18.6_specs` | 34.77 MB | 163.76 MB | 100.0% | 100.0% |
| `ngap_rel18.6_specs` | 24.21 MB | 117.32 MB | 106.2% | 102.8% |
| `lteNRRCC` | 74.43 MB | 102.87 MB | 102.4% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0235s | 0.0231s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0712s | 0.0676s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0495s | 0.0467s | +0.0028s | worse |
| `lteNRRCC` | 0.0801s | 0.0772s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 3.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.50 MB | 4.41 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.75 MB | 3.59 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.09 MB | 4.16 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0395s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1094s | 0.1065s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0768s | 0.0745s | +0.0023s | worse |
| `lteNRRCC` | 0.1398s | 0.1384s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.05 MB | 7.44 MB | 220.6% | 99.3% |
| `f1ap_rel18.6_specs` | 8.05 MB | 7.92 MB | 162.5% | 163.0% |
| `ngap_rel18.6_specs` | 7.49 MB | 7.56 MB | 81.5% | 163.9% |
| `lteNRRCC` | 49.79 MB | 52.38 MB | 228.1% | 105.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0434s | 0.0432s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1246s | 0.1162s | +0.0084s | worse |
| `ngap_rel18.6_specs` | 0.0853s | 0.0812s | +0.0041s | worse |
| `lteNRRCC` | 0.1386s | 0.1383s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 9.24 MB | 0.0% | 94.6% |
| `f1ap_rel18.6_specs` | 9.46 MB | 164.20 MB | 167.1% | 113.8% |
| `ngap_rel18.6_specs` | 8.96 MB | 9.49 MB | 152.4% | 94.1% |
| `lteNRRCC` | 73.78 MB | 74.15 MB | 151.9% | 111.1% |
<!-- BENCH_RESULTS_END -->
