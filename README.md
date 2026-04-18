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
Generated: 2026-04-18T22:43:05.616900+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0371s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1138s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0777s | +0.0013s | worse |
| `lteNRRCC` | 0.1216s | 0.1222s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.84 MB | 53.55 MB | 25.3% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.9% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0362s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0974s | -0.0044s | improved |
| `ngap_rel18.6_specs` | 0.0669s | 0.0686s | -0.0017s | improved |
| `lteNRRCC` | 0.1298s | 0.1312s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.65 MB | 60.0% | 110.7% |
| `f1ap_rel18.6_specs` | 21.93 MB | 103.36 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.81 MB | 74.55 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.61 MB | 66.28 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0274s | 0.0329s | -0.0055s | improved |
| `f1ap_rel18.6_specs` | 0.0765s | 0.0889s | -0.0124s | improved |
| `ngap_rel18.6_specs` | 0.0526s | 0.0652s | -0.0126s | improved |
| `lteNRRCC` | 0.1075s | 0.1151s | -0.0076s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.74 MB | 55.57 MB | 18.0% | 113.0% |
| `f1ap_rel18.6_specs` | 34.66 MB | 164.38 MB | 112.0% | 104.2% |
| `ngap_rel18.6_specs` | 24.29 MB | 117.80 MB | 114.3% | 102.8% |
| `lteNRRCC` | 74.29 MB | 102.88 MB | 103.9% | 105.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0228s | 0.0191s | +0.0037s | worse |
| `f1ap_rel18.6_specs` | 0.0610s | 0.0747s | -0.0137s | improved |
| `ngap_rel18.6_specs` | 0.0423s | 0.0423s | +0.0000s | flat |
| `lteNRRCC` | 0.0708s | 0.0715s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.34 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 6.72 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.92 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.77 MB | 3.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0393s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1064s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0787s | 0.0756s | +0.0031s | worse |
| `lteNRRCC` | 0.1415s | 0.1387s | +0.0028s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.83 MB | 7.56 MB | 92.6% | 154.3% |
| `f1ap_rel18.6_specs` | 8.38 MB | 8.44 MB | 153.3% | 154.8% |
| `ngap_rel18.6_specs` | 7.99 MB | 7.99 MB | 155.7% | 150.8% |
| `lteNRRCC` | 8.41 MB | 50.58 MB | 92.9% | 110.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0428s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.1077s | 0.1239s | -0.0162s | improved |
| `ngap_rel18.6_specs` | 0.0799s | 0.0868s | -0.0069s | improved |
| `lteNRRCC` | 0.1266s | 0.1322s | -0.0056s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.30 MB | 10.75 MB | 113.4% | 228.8% |
| `f1ap_rel18.6_specs` | 11.07 MB | 11.32 MB | 113.2% | 235.9% |
| `ngap_rel18.6_specs` | 10.25 MB | 10.66 MB | 219.4% | 115.8% |
| `lteNRRCC` | 9.30 MB | 89.82 MB | 116.8% | 113.7% |
<!-- BENCH_RESULTS_END -->
