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
Generated: 2026-04-27T11:51:07.428296+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0383s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1121s | 0.1183s | -0.0062s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0797s | -0.0031s | improved |
| `lteNRRCC` | 0.1209s | 0.1227s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 28.9% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 105.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0344s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0969s | 0.0988s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0677s | 0.0655s | +0.0022s | worse |
| `lteNRRCC` | 0.1316s | 0.1271s | +0.0045s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 35.87 MB | 30.2% | 110.3% |
| `f1ap_rel18.6_specs` | 22.07 MB | 103.30 MB | 108.8% | 103.3% |
| `ngap_rel18.6_specs` | 16.86 MB | 74.39 MB | 110.7% | 106.5% |
| `lteNRRCC` | 48.61 MB | 66.36 MB | 104.5% | 103.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0345s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0929s | 0.0937s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0634s | 0.0662s | -0.0028s | improved |
| `lteNRRCC` | 0.1188s | 0.1182s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.09 MB | 55.56 MB | 95.8% | 110.7% |
| `f1ap_rel18.6_specs` | 34.76 MB | 164.21 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 24.36 MB | 117.50 MB | 108.0% | 107.1% |
| `lteNRRCC` | 74.70 MB | 102.09 MB | 105.2% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0286s | 0.0293s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1032s | 0.0695s | +0.0337s | worse |
| `ngap_rel18.6_specs` | 0.0723s | 0.0452s | +0.0271s | worse |
| `lteNRRCC` | 0.1038s | 0.0689s | +0.0349s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.69 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 5.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.75 MB | 8.53 MB | 1.3% | 0.0% |
| `lteNRRCC` | 3.77 MB | 992 KB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0397s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1057s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0733s | 0.0746s | -0.0013s | improved |
| `lteNRRCC` | 0.1361s | 0.1283s | +0.0078s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.55 MB | 162.0% | 109.1% |
| `f1ap_rel18.6_specs` | 7.96 MB | 106.64 MB | 82.6% | 162.3% |
| `ngap_rel18.6_specs` | 7.67 MB | 8.30 MB | 96.7% | 232.4% |
| `lteNRRCC` | 47.38 MB | 69.22 MB | 161.0% | 107.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0406s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.0995s | 0.1116s | -0.0121s | improved |
| `ngap_rel18.6_specs` | 0.0726s | 0.0759s | -0.0033s | improved |
| `lteNRRCC` | 0.1128s | 0.1286s | -0.0158s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.71 MB | 9.65 MB | 200.8% | 101.0% |
| `f1ap_rel18.6_specs` | 11.18 MB | 164.18 MB | 138.3% | 105.9% |
| `ngap_rel18.6_specs` | 10.69 MB | 10.44 MB | 128.8% | 139.3% |
| `lteNRRCC` | 9.92 MB | 74.80 MB | 120.1% | 108.7% |
<!-- BENCH_RESULTS_END -->
