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
Generated: 2026-05-08T23:01:48.854939+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0347s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1133s | 0.1106s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0771s | +0.0002s | worse |
| `lteNRRCC` | 0.1234s | 0.1198s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 25.9% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0349s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1037s | 0.0942s | +0.0095s | worse |
| `ngap_rel18.6_specs` | 0.0720s | 0.0663s | +0.0057s | worse |
| `lteNRRCC` | 0.1322s | 0.1282s | +0.0040s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 36.50 MB | 89.3% | 110.0% |
| `f1ap_rel18.6_specs` | 22.34 MB | 103.20 MB | 109.1% | 104.8% |
| `ngap_rel18.6_specs` | 16.85 MB | 74.71 MB | 110.7% | 106.4% |
| `lteNRRCC` | 48.37 MB | 66.06 MB | 104.5% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0325s | 0.0328s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0889s | 0.0883s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0618s | 0.0621s | -0.0003s | improved |
| `lteNRRCC` | 0.1159s | 0.1148s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.51 MB | 71.9% | 111.1% |
| `f1ap_rel18.6_specs` | 34.64 MB | 164.24 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.43 MB | 117.77 MB | 116.7% | 107.1% |
| `lteNRRCC` | 74.75 MB | 102.73 MB | 106.9% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0244s | 0.0206s | +0.0038s | worse |
| `f1ap_rel18.6_specs` | 0.0765s | 0.0644s | +0.0121s | worse |
| `ngap_rel18.6_specs` | 0.0549s | 0.0434s | +0.0115s | worse |
| `lteNRRCC` | 0.0738s | 0.0724s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.44 MB | 2.61 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 5.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 4.77 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.98 MB | 4.00 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0413s | 0.0407s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1176s | 0.1134s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0800s | +0.0016s | worse |
| `lteNRRCC` | 0.1432s | 0.1293s | +0.0139s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.36 MB | 7.89 MB | 152.1% | 100.5% |
| `f1ap_rel18.6_specs` | 8.87 MB | 106.65 MB | 202.6% | 109.1% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.56 MB | 163.5% | 202.1% |
| `lteNRRCC` | 8.54 MB | 70.55 MB | 158.9% | 213.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0490s | 0.0337s | +0.0153s | worse |
| `f1ap_rel18.6_specs` | 0.1349s | 0.1030s | +0.0319s | worse |
| `ngap_rel18.6_specs` | 0.0918s | 0.0732s | +0.0186s | worse |
| `lteNRRCC` | 0.1375s | 0.1124s | +0.0251s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.85 MB | 9.07 MB | 77.2% | 160.6% |
| `f1ap_rel18.6_specs` | 11.39 MB | 10.30 MB | 234.8% | 117.5% |
| `ngap_rel18.6_specs` | 9.48 MB | 9.80 MB | 81.0% | 146.7% |
| `lteNRRCC` | 8.80 MB | 99.58 MB | 116.2% | 157.1% |
<!-- BENCH_RESULTS_END -->
