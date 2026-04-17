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
Generated: 2026-04-17T11:05:01.041792+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0354s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1167s | 0.1125s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0745s | +0.0058s | worse |
| `lteNRRCC` | 0.1234s | 0.1168s | +0.0066s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 9.1% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0326s | 0.0367s | -0.0041s | improved |
| `f1ap_rel18.6_specs` | 0.1006s | 0.0921s | +0.0085s | worse |
| `ngap_rel18.6_specs` | 0.0699s | 0.0653s | +0.0046s | worse |
| `lteNRRCC` | 0.1208s | 0.1288s | -0.0080s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.31 MB | 36.67 MB | 87.0% | 108.0% |
| `f1ap_rel18.6_specs` | 22.10 MB | 103.12 MB | 107.1% | 103.3% |
| `ngap_rel18.6_specs` | 16.78 MB | 74.27 MB | 113.6% | 104.5% |
| `lteNRRCC` | 48.62 MB | 66.49 MB | 103.5% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0327s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0904s | 0.0905s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0638s | 0.0653s | -0.0015s | improved |
| `lteNRRCC` | 0.1181s | 0.1168s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.77 MB | 88.5% | 110.7% |
| `f1ap_rel18.6_specs` | 34.46 MB | 164.29 MB | 110.0% | 107.1% |
| `ngap_rel18.6_specs` | 24.15 MB | 117.71 MB | 112.0% | 109.5% |
| `lteNRRCC` | 74.22 MB | 102.79 MB | 105.2% | 105.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0517s | 0.0190s | +0.0327s | worse |
| `f1ap_rel18.6_specs` | 0.1084s | 0.0619s | +0.0465s | worse |
| `ngap_rel18.6_specs` | 0.0811s | 0.0484s | +0.0327s | worse |
| `lteNRRCC` | 0.1158s | 0.0682s | +0.0476s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.44 MB | 6.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.02 MB | 8.14 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.33 MB | 9.03 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.66 MB | 6.09 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0386s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1061s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0781s | 0.0738s | +0.0043s | worse |
| `lteNRRCC` | 0.1273s | 0.1374s | -0.0101s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.55 MB | 7.96 MB | 165.0% | 242.2% |
| `f1ap_rel18.6_specs` | 8.73 MB | 8.39 MB | 120.6% | 93.6% |
| `ngap_rel18.6_specs` | 8.23 MB | 8.23 MB | 106.9% | 118.7% |
| `lteNRRCC` | 8.16 MB | 8.03 MB | 119.3% | 240.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0420s | 0.0393s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1154s | 0.1144s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0801s | 0.0794s | +0.0007s | worse |
| `lteNRRCC` | 0.1357s | 0.1294s | +0.0063s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.93 MB | 8.93 MB | 83.3% | 83.5% |
| `f1ap_rel18.6_specs` | 9.80 MB | 164.16 MB | 166.5% | 108.3% |
| `ngap_rel18.6_specs` | 9.14 MB | 9.20 MB | 165.4% | 83.4% |
| `lteNRRCC` | 68.36 MB | 99.64 MB | 110.0% | 112.3% |
<!-- BENCH_RESULTS_END -->
