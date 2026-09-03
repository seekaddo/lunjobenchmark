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
Generated: 2026-09-03T23:53:57.448931+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0358s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1073s | 0.1149s | -0.0076s | improved |
| `ngap_rel18.6_specs` | 0.0735s | 0.0770s | -0.0035s | improved |
| `lteNRRCC` | 0.1172s | 0.1204s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 85.7% | 107.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.7% | 103.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 100.0% | 102.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0365s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0967s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0673s | 0.0683s | -0.0010s | improved |
| `lteNRRCC` | 0.1297s | 0.1322s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.66 MB | 62.5% | 103.7% |
| `f1ap_rel18.6_specs` | 22.32 MB | 102.74 MB | 106.5% | 103.6% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.32 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.30 MB | 66.01 MB | 103.1% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0285s | +0.0076s | worse |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0889s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0672s | 0.0604s | +0.0068s | worse |
| `lteNRRCC` | 0.1320s | 0.0890s | +0.0430s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 55.40 MB | 17.7% | 103.6% |
| `f1ap_rel18.6_specs` | 35.19 MB | 164.30 MB | 106.5% | 101.7% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.86 MB | 103.8% | 104.7% |
| `lteNRRCC` | 75.03 MB | 102.58 MB | 101.6% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0235s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1022s | 0.0712s | +0.0310s | worse |
| `ngap_rel18.6_specs` | 0.0997s | 0.0495s | +0.0502s | worse |
| `lteNRRCC` | 0.1019s | 0.0801s | +0.0218s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.97 MB | 6.86 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.62 MB | 8.39 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 12.05 MB | 8.20 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.02 MB | 9.06 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0398s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.1153s | 0.1094s | +0.0059s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0768s | +0.0003s | worse |
| `lteNRRCC` | 0.1395s | 0.1398s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.57 MB | 7.51 MB | 169.2% | 162.2% |
| `f1ap_rel18.6_specs` | 8.05 MB | 8.41 MB | 92.1% | 156.7% |
| `ngap_rel18.6_specs` | 7.89 MB | 7.96 MB | 158.6% | 156.4% |
| `lteNRRCC` | 49.52 MB | 54.09 MB | 156.2% | 107.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0418s | 0.0434s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1186s | 0.1246s | -0.0060s | improved |
| `ngap_rel18.6_specs` | 0.0836s | 0.0853s | -0.0017s | improved |
| `lteNRRCC` | 0.1366s | 0.1386s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 9.21 MB | 0.0% | 171.1% |
| `f1ap_rel18.6_specs` | 10.07 MB | 155.91 MB | 177.1% | 167.3% |
| `ngap_rel18.6_specs` | 9.16 MB | 9.42 MB | 177.3% | 161.5% |
| `lteNRRCC` | 8.88 MB | 73.79 MB | 163.3% | 106.7% |
<!-- BENCH_RESULTS_END -->
