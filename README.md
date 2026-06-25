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
Generated: 2026-06-25T12:27:29.709098+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0342s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1089s | 0.1089s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0759s | 0.0743s | +0.0016s | worse |
| `lteNRRCC` | 0.1198s | 0.1183s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 20.8% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.3% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0320s | 0.0348s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0930s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0655s | 0.0653s | +0.0002s | worse |
| `lteNRRCC` | 0.1166s | 0.1281s | -0.0115s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 36.64 MB | 75.0% | 108.3% |
| `f1ap_rel18.6_specs` | 21.77 MB | 103.15 MB | 111.1% | 103.6% |
| `ngap_rel18.6_specs` | 17.79 MB | 74.47 MB | 109.1% | 104.9% |
| `lteNRRCC` | 48.11 MB | 66.26 MB | 105.5% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0351s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0903s | 0.0922s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0654s | -0.0015s | improved |
| `lteNRRCC` | 0.1160s | 0.1171s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.89 MB | 91.7% | 110.7% |
| `f1ap_rel18.6_specs` | 34.47 MB | 164.58 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 24.41 MB | 116.96 MB | 112.5% | 104.8% |
| `lteNRRCC` | 74.79 MB | 102.83 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0321s | 0.0211s | +0.0110s | worse |
| `f1ap_rel18.6_specs` | 0.0952s | 0.1134s | -0.0182s | improved |
| `ngap_rel18.6_specs` | 0.0614s | 0.0790s | -0.0176s | improved |
| `lteNRRCC` | 0.1137s | 0.0762s | +0.0375s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.84 MB | 2.53 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.94 MB | 9.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.45 MB | 5.89 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.48 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0388s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1153s | 0.1088s | +0.0065s | worse |
| `ngap_rel18.6_specs` | 0.0819s | 0.0751s | +0.0068s | worse |
| `lteNRRCC` | 0.1413s | 0.1372s | +0.0041s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.74 MB | 7.80 MB | 163.7% | 83.4% |
| `f1ap_rel18.6_specs` | 8.24 MB | 106.64 MB | 165.0% | 107.3% |
| `ngap_rel18.6_specs` | 8.06 MB | 8.12 MB | 83.2% | 214.1% |
| `lteNRRCC` | 48.21 MB | 52.00 MB | 107.7% | 109.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0351s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.1087s | 0.1037s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0754s | 0.0729s | +0.0025s | worse |
| `lteNRRCC` | 0.1251s | 0.1126s | +0.0125s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.52 MB | 8.66 MB | 160.2% | 159.7% |
| `f1ap_rel18.6_specs` | 9.49 MB | 164.19 MB | 182.9% | 224.9% |
| `ngap_rel18.6_specs` | 10.50 MB | 9.14 MB | 223.8% | 156.4% |
| `lteNRRCC` | 8.56 MB | 87.40 MB | 159.2% | 157.1% |
<!-- BENCH_RESULTS_END -->
