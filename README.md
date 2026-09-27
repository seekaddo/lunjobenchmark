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
Generated: 2026-09-27T00:24:02.220725+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0362s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1120s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0760s | 0.0771s | -0.0011s | improved |
| `lteNRRCC` | 0.1207s | 0.1219s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 85.7% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0364s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0977s | 0.0970s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0676s | 0.0684s | -0.0008s | improved |
| `lteNRRCC` | 0.1198s | 0.1308s | -0.0110s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 36.55 MB | 78.3% | 104.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.45 MB | 107.4% | 101.8% |
| `ngap_rel18.6_specs` | 17.99 MB | 74.62 MB | 104.5% | 100.0% |
| `lteNRRCC` | 48.80 MB | 66.16 MB | 103.6% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0358s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0919s | 0.1023s | -0.0104s | improved |
| `ngap_rel18.6_specs` | 0.0651s | 0.0716s | -0.0065s | improved |
| `lteNRRCC` | 0.1262s | 0.1187s | +0.0075s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.67 MB | 91.3% | 103.6% |
| `f1ap_rel18.6_specs` | 34.43 MB | 164.45 MB | 106.2% | 103.5% |
| `ngap_rel18.6_specs` | 24.12 MB | 117.61 MB | 104.0% | 104.8% |
| `lteNRRCC` | 74.66 MB | 102.88 MB | 101.6% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0239s | 0.0289s | -0.0050s | improved |
| `f1ap_rel18.6_specs` | 0.0987s | 0.0708s | +0.0279s | worse |
| `ngap_rel18.6_specs` | 0.0436s | 0.0439s | -0.0003s | improved |
| `lteNRRCC` | 0.0858s | 0.0990s | -0.0132s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.58 MB | 4.33 MB | 0.0% | 0.6% |
| `f1ap_rel18.6_specs` | 8.72 MB | 8.98 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.44 MB | 8.27 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.36 MB | 7.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0401s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1086s | 0.1092s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0760s | 0.0791s | -0.0031s | improved |
| `lteNRRCC` | 0.1396s | 0.1400s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.59 MB | 7.86 MB | 107.2% | 234.6% |
| `f1ap_rel18.6_specs` | 8.41 MB | 8.13 MB | 231.1% | 169.7% |
| `ngap_rel18.6_specs` | 8.07 MB | 7.51 MB | 230.9% | 164.1% |
| `lteNRRCC` | 51.11 MB | 52.47 MB | 105.9% | 160.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0432s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1286s | -0.0181s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0880s | -0.0128s | improved |
| `lteNRRCC` | 0.1279s | 0.1343s | -0.0064s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.84 MB | 11.03 MB | 104.9% | 106.7% |
| `f1ap_rel18.6_specs` | 11.71 MB | 11.51 MB | 112.0% | 108.1% |
| `ngap_rel18.6_specs` | 11.12 MB | 9.26 MB | 110.5% | 153.7% |
| `lteNRRCC` | 9.73 MB | 99.13 MB | 110.6% | 103.8% |
<!-- BENCH_RESULTS_END -->
