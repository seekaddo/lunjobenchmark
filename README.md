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
Generated: 2026-04-11T22:40:28.554506+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0361s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1137s | 0.1131s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0789s | -0.0013s | improved |
| `lteNRRCC` | 0.1234s | 0.1228s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 28.0% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.1% | 105.6% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0342s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.0929s | 0.0925s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0661s | 0.0648s | +0.0013s | worse |
| `lteNRRCC` | 0.1251s | 0.1260s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 35.42 MB | 76.5% | 106.7% |
| `f1ap_rel18.6_specs` | 22.09 MB | 102.72 MB | 112.1% | 105.0% |
| `ngap_rel18.6_specs` | 16.51 MB | 74.63 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.15 MB | 66.22 MB | 104.7% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0340s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0948s | 0.0893s | +0.0055s | worse |
| `ngap_rel18.6_specs` | 0.0650s | 0.0631s | +0.0019s | worse |
| `lteNRRCC` | 0.1259s | 0.1162s | +0.0097s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.84 MB | 69.4% | 110.0% |
| `f1ap_rel18.6_specs` | 35.13 MB | 164.73 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 23.83 MB | 117.64 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.65 MB | 102.40 MB | 104.6% | 102.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0192s | 0.0200s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0598s | 0.0590s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0408s | 0.0402s | +0.0006s | worse |
| `lteNRRCC` | 0.0751s | 0.0679s | +0.0072s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.98 MB | 4.17 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 4.09 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.02 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.95 MB | 3.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0409s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1065s | 0.1110s | -0.0045s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0868s | -0.0100s | improved |
| `lteNRRCC` | 0.1409s | 0.1306s | +0.0103s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.32 MB | 161.7% | 163.3% |
| `f1ap_rel18.6_specs` | 8.37 MB | 106.63 MB | 156.6% | 144.4% |
| `ngap_rel18.6_specs` | 7.38 MB | 7.54 MB | 92.5% | 166.2% |
| `lteNRRCC` | 51.39 MB | 55.12 MB | 159.5% | 103.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0419s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1216s | -0.0133s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0842s | -0.0074s | improved |
| `lteNRRCC` | 0.1278s | 0.1402s | -0.0124s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.57 MB | 8.85 MB | 94.6% | 156.4% |
| `f1ap_rel18.6_specs` | 9.65 MB | 11.38 MB | 170.5% | 115.6% |
| `ngap_rel18.6_specs` | 9.26 MB | 8.95 MB | 94.1% | 160.2% |
| `lteNRRCC` | 8.73 MB | 70.99 MB | 77.2% | 154.6% |
<!-- BENCH_RESULTS_END -->
