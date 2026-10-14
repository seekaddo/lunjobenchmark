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
Generated: 2026-10-14T01:03:08.915552+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0354s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1165s | 0.1112s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0801s | 0.0759s | +0.0042s | worse |
| `lteNRRCC` | 0.1241s | 0.1192s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.98 MB | 53.55 MB | 74.1% | 103.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0334s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0948s | 0.0912s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0657s | 0.0636s | +0.0021s | worse |
| `lteNRRCC` | 0.1292s | 0.1227s | +0.0065s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.45 MB | 16.7% | 107.7% |
| `f1ap_rel18.6_specs` | 22.29 MB | 103.11 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.91 MB | 73.84 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.46 MB | 66.43 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0235s | 0.0368s | -0.0133s | improved |
| `f1ap_rel18.6_specs` | 0.0642s | 0.0976s | -0.0334s | improved |
| `ngap_rel18.6_specs` | 0.0441s | 0.0663s | -0.0222s | improved |
| `lteNRRCC` | 0.0790s | 0.1289s | -0.0499s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.75 MB | 55.23 MB | 77.8% | 105.3% |
| `f1ap_rel18.6_specs` | 34.47 MB | 163.36 MB | 110.5% | 102.6% |
| `ngap_rel18.6_specs` | 24.30 MB | 117.61 MB | 106.2% | 103.4% |
| `lteNRRCC` | 74.60 MB | 102.91 MB | 102.7% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0300s | 0.0413s | -0.0113s | improved |
| `f1ap_rel18.6_specs` | 0.1367s | 0.1083s | +0.0284s | worse |
| `ngap_rel18.6_specs` | 0.0741s | 0.0726s | +0.0015s | worse |
| `lteNRRCC` | 0.1015s | 0.0985s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.64 MB | 5.98 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.78 MB | 7.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.36 MB | 2.95 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.28 MB | 3.45 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0311s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.1069s | 0.0838s | +0.0231s | worse |
| `ngap_rel18.6_specs` | 0.0752s | 0.0611s | +0.0141s | worse |
| `lteNRRCC` | 0.1378s | 0.0958s | +0.0420s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.96 MB | 7.47 MB | 199.8% | 175.0% |
| `f1ap_rel18.6_specs` | 8.01 MB | 8.00 MB | 81.6% | 162.4% |
| `ngap_rel18.6_specs` | 7.51 MB | 7.64 MB | 159.3% | 116.1% |
| `lteNRRCC` | 7.77 MB | 59.14 MB | 80.3% | 109.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0392s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1152s | 0.1130s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0806s | -0.0013s | improved |
| `lteNRRCC` | 0.1361s | 0.1261s | +0.0100s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 8.84 MB | 0.0% | 102.3% |
| `f1ap_rel18.6_specs` | 9.40 MB | 164.17 MB | 239.5% | 159.9% |
| `ngap_rel18.6_specs` | 8.75 MB | 9.00 MB | 158.1% | 78.6% |
| `lteNRRCC` | 9.16 MB | 87.19 MB | 114.2% | 138.5% |
<!-- BENCH_RESULTS_END -->
