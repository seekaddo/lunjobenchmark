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
Generated: 2026-06-25T23:24:01.108711+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0355s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1089s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0759s | +0.0007s | worse |
| `lteNRRCC` | 0.1201s | 0.1198s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 20.2% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0320s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.0985s | 0.0943s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0690s | 0.0655s | +0.0035s | worse |
| `lteNRRCC` | 0.1310s | 0.1166s | +0.0144s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 36.46 MB | 67.6% | 110.7% |
| `f1ap_rel18.6_specs` | 22.16 MB | 102.71 MB | 106.1% | 105.1% |
| `ngap_rel18.6_specs` | 17.76 MB | 74.66 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.35 MB | 66.19 MB | 104.6% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0348s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0903s | +0.0039s | worse |
| `ngap_rel18.6_specs` | 0.0662s | 0.0639s | +0.0023s | worse |
| `lteNRRCC` | 0.1281s | 0.1160s | +0.0121s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.49 MB | 54.92 MB | 96.0% | 110.7% |
| `f1ap_rel18.6_specs` | 34.36 MB | 164.71 MB | 109.7% | 105.3% |
| `ngap_rel18.6_specs` | 24.57 MB | 117.50 MB | 111.5% | 107.0% |
| `lteNRRCC` | 74.86 MB | 102.53 MB | 104.8% | 104.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0275s | 0.0321s | -0.0046s | improved |
| `f1ap_rel18.6_specs` | 0.1001s | 0.0952s | +0.0049s | worse |
| `ngap_rel18.6_specs` | 0.0578s | 0.0614s | -0.0036s | improved |
| `lteNRRCC` | 0.0933s | 0.1137s | -0.0204s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.84 MB | 4.27 MB | 0.5% | 0.0% |
| `f1ap_rel18.6_specs` | 2.94 MB | 6.84 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.83 MB | 9.06 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.14 MB | 4.70 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0412s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1089s | 0.1153s | -0.0064s | improved |
| `ngap_rel18.6_specs` | 0.0773s | 0.0819s | -0.0046s | improved |
| `lteNRRCC` | 0.1393s | 0.1413s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.35 MB | 7.35 MB | 165.9% | 166.1% |
| `f1ap_rel18.6_specs` | 7.91 MB | 8.04 MB | 88.1% | 166.4% |
| `ngap_rel18.6_specs` | 7.88 MB | 7.47 MB | 233.2% | 166.5% |
| `lteNRRCC` | 51.83 MB | 51.99 MB | 113.7% | 164.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0386s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1087s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0754s | +0.0021s | worse |
| `lteNRRCC` | 0.1275s | 0.1251s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.09 MB | 10.31 MB | 110.0% | 118.7% |
| `f1ap_rel18.6_specs` | 9.75 MB | 11.03 MB | 164.0% | 116.2% |
| `ngap_rel18.6_specs` | 8.77 MB | 8.89 MB | 82.8% | 80.4% |
| `lteNRRCC` | 9.61 MB | 96.07 MB | 118.9% | 116.8% |
<!-- BENCH_RESULTS_END -->
