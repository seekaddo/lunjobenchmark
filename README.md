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
Generated: 2026-07-02T12:13:36.654027+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0363s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1133s | 0.1113s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0782s | 0.0765s | +0.0017s | worse |
| `lteNRRCC` | 0.1224s | 0.1204s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 22.1% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 105.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0352s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0937s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0662s | -0.0005s | improved |
| `lteNRRCC` | 0.1275s | 0.1297s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.33 MB | 36.59 MB | 18.7% | 106.5% |
| `f1ap_rel18.6_specs` | 21.85 MB | 103.28 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.66 MB | 107.7% | 107.0% |
| `lteNRRCC` | 48.70 MB | 66.35 MB | 104.7% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0345s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1066s | 0.0915s | +0.0151s | worse |
| `ngap_rel18.6_specs` | 0.0741s | 0.0639s | +0.0102s | worse |
| `lteNRRCC` | 0.1242s | 0.1166s | +0.0076s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.43 MB | 55.40 MB | 35.1% | 107.4% |
| `f1ap_rel18.6_specs` | 34.66 MB | 164.23 MB | 107.1% | 105.0% |
| `ngap_rel18.6_specs` | 24.21 MB | 117.62 MB | 109.1% | 106.8% |
| `lteNRRCC` | 74.47 MB | 102.94 MB | 105.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0318s | 0.0234s | +0.0084s | worse |
| `f1ap_rel18.6_specs` | 0.0893s | 0.0682s | +0.0211s | worse |
| `ngap_rel18.6_specs` | 0.0596s | 0.0472s | +0.0124s | worse |
| `lteNRRCC` | 0.1014s | 0.0782s | +0.0232s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.34 MB | 7.50 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.12 MB | 9.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.41 MB | 8.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 11.56 MB | 1.31 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0405s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1189s | 0.1069s | +0.0120s | worse |
| `ngap_rel18.6_specs` | 0.0813s | 0.0741s | +0.0072s | worse |
| `lteNRRCC` | 0.1414s | 0.1378s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.84 MB | 7.62 MB | 218.4% | 169.4% |
| `f1ap_rel18.6_specs` | 8.18 MB | 106.64 MB | 166.8% | 167.0% |
| `ngap_rel18.6_specs` | 7.89 MB | 7.96 MB | 83.5% | 164.6% |
| `lteNRRCC` | 48.45 MB | 51.96 MB | 167.8% | 165.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0425s | 0.0377s | +0.0048s | worse |
| `f1ap_rel18.6_specs` | 0.1158s | 0.1091s | +0.0067s | worse |
| `ngap_rel18.6_specs` | 0.0857s | 0.0732s | +0.0125s | worse |
| `lteNRRCC` | 0.1315s | 0.1267s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.55 MB | 8.87 MB | 73.9% | 73.1% |
| `f1ap_rel18.6_specs` | 10.58 MB | 164.20 MB | 153.3% | 109.7% |
| `ngap_rel18.6_specs` | 9.27 MB | 9.35 MB | 148.4% | 143.6% |
| `lteNRRCC` | 10.05 MB | 79.40 MB | 101.0% | 143.0% |
<!-- BENCH_RESULTS_END -->
