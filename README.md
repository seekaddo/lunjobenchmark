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
Generated: 2026-05-07T11:55:06.066075+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0375s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1149s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0782s | +0.0008s | worse |
| `lteNRRCC` | 0.1226s | 0.1234s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 27.0% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 107.7% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.3% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0377s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0887s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0671s | 0.0635s | +0.0036s | worse |
| `lteNRRCC` | 0.1288s | 0.1228s | +0.0060s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.29 MB | 36.23 MB | 104.2% | 110.7% |
| `f1ap_rel18.6_specs` | 22.12 MB | 103.23 MB | 106.1% | 103.4% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.57 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.57 MB | 66.29 MB | 104.6% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0320s | 0.0340s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0769s | 0.0908s | -0.0139s | improved |
| `ngap_rel18.6_specs` | 0.0544s | 0.0626s | -0.0082s | improved |
| `lteNRRCC` | 0.1033s | 0.1210s | -0.0177s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.74 MB | 55.61 MB | 44.7% | 108.3% |
| `f1ap_rel18.6_specs` | 34.38 MB | 164.36 MB | 108.0% | 106.2% |
| `ngap_rel18.6_specs` | 23.71 MB | 116.97 MB | 109.5% | 105.6% |
| `lteNRRCC` | 74.80 MB | 102.96 MB | 106.0% | 105.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0272s | 0.0230s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.0832s | 0.0710s | +0.0122s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0499s | +0.0130s | worse |
| `lteNRRCC` | 0.0823s | 0.0844s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 192 KB | 8.42 MB | 0.6% | 0.0% |
| `f1ap_rel18.6_specs` | 8.42 MB | 8.45 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.05 MB | 1.94 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.70 MB | 1.55 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0379s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1073s | +0.0046s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0745s | +0.0021s | worse |
| `lteNRRCC` | 0.1384s | 0.1382s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.51 MB | 158.2% | 158.7% |
| `f1ap_rel18.6_specs` | 8.24 MB | 106.64 MB | 156.6% | 106.6% |
| `ngap_rel18.6_specs` | 7.96 MB | 7.99 MB | 92.1% | 93.4% |
| `lteNRRCC` | 47.43 MB | 53.27 MB | 106.9% | 108.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0442s | 0.0394s | +0.0048s | worse |
| `f1ap_rel18.6_specs` | 0.1265s | 0.1115s | +0.0150s | worse |
| `ngap_rel18.6_specs` | 0.0905s | 0.0796s | +0.0109s | worse |
| `lteNRRCC` | 0.1347s | 0.1279s | +0.0068s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.28 MB | 9.08 MB | 233.6% | 161.4% |
| `f1ap_rel18.6_specs` | 10.30 MB | 11.27 MB | 159.8% | 233.7% |
| `ngap_rel18.6_specs` | 10.19 MB | 10.06 MB | 232.8% | 82.1% |
| `lteNRRCC` | 8.89 MB | 9.24 MB | 157.5% | 115.8% |
<!-- BENCH_RESULTS_END -->
