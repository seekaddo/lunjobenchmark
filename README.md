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
Generated: 2026-09-06T23:41:39.344784+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0340s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1081s | 0.1093s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0732s | 0.0757s | -0.0025s | improved |
| `lteNRRCC` | 0.1164s | 0.1195s | -0.0031s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 90.0% | 107.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0229s | +0.0124s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0653s | +0.0294s | worse |
| `ngap_rel18.6_specs` | 0.0665s | 0.0469s | +0.0196s | worse |
| `lteNRRCC` | 0.1328s | 0.0762s | +0.0566s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.49 MB | 36.59 MB | 75.0% | 103.6% |
| `f1ap_rel18.6_specs` | 21.34 MB | 103.14 MB | 106.5% | 103.5% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.62 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.75 MB | 66.40 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0333s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0919s | 0.0900s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0649s | 0.0633s | +0.0016s | worse |
| `lteNRRCC` | 0.1191s | 0.1180s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.11 MB | 69.0% | 107.4% |
| `f1ap_rel18.6_specs` | 34.66 MB | 164.59 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.38 MB | 117.79 MB | 104.2% | 102.4% |
| `lteNRRCC` | 74.83 MB | 102.21 MB | 103.5% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0296s | 0.0246s | +0.0050s | worse |
| `f1ap_rel18.6_specs` | 0.1024s | 0.0720s | +0.0304s | worse |
| `ngap_rel18.6_specs` | 0.0681s | 0.0610s | +0.0071s | worse |
| `lteNRRCC` | 0.1190s | 0.0805s | +0.0385s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.53 MB | 8.08 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.78 MB | 9.23 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.30 MB | 8.20 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.34 MB | 7.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0378s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1063s | 0.1073s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0734s | +0.0025s | worse |
| `lteNRRCC` | 0.1368s | 0.1369s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.05 MB | 7.32 MB | 176.8% | 165.9% |
| `f1ap_rel18.6_specs` | 7.97 MB | 8.03 MB | 173.1% | 82.9% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.54 MB | 162.1% | 96.7% |
| `lteNRRCC` | 46.32 MB | 49.51 MB | 163.5% | 106.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0446s | -0.0056s | improved |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1114s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0782s | 0.0779s | +0.0003s | worse |
| `lteNRRCC` | 0.1288s | 0.1271s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.54 MB | 7.29 MB | 0.0% | 232.5% |
| `f1ap_rel18.6_specs` | 9.56 MB | 11.23 MB | 80.7% | 117.9% |
| `ngap_rel18.6_specs` | 9.49 MB | 8.95 MB | 111.2% | 163.0% |
| `lteNRRCC` | 73.77 MB | 81.65 MB | 159.2% | 159.2% |
<!-- BENCH_RESULTS_END -->
