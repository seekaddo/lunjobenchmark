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
Generated: 2026-10-26T00:01:40.262079+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0344s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1080s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0747s | 0.0750s | -0.0003s | improved |
| `lteNRRCC` | 0.1188s | 0.1190s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 85.7% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0218s | 0.0263s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.0597s | 0.0720s | -0.0123s | improved |
| `ngap_rel18.6_specs` | 0.0434s | 0.0502s | -0.0068s | improved |
| `lteNRRCC` | 0.0773s | 0.0966s | -0.0193s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.60 MB | 36.63 MB | 56.0% | 105.9% |
| `f1ap_rel18.6_specs` | 21.71 MB | 103.09 MB | 105.3% | 105.6% |
| `ngap_rel18.6_specs` | 18.12 MB | 74.66 MB | 106.2% | 100.0% |
| `lteNRRCC` | 48.81 MB | 65.92 MB | 102.6% | 102.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0334s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0890s | 0.0976s | -0.0086s | improved |
| `ngap_rel18.6_specs` | 0.0630s | 0.0666s | -0.0036s | improved |
| `lteNRRCC` | 0.1172s | 0.1123s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.58 MB | 55.62 MB | 84.0% | 103.8% |
| `f1ap_rel18.6_specs` | 35.17 MB | 163.73 MB | 103.7% | 101.9% |
| `ngap_rel18.6_specs` | 24.49 MB | 117.89 MB | 104.5% | 105.1% |
| `lteNRRCC` | 74.21 MB | 102.48 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0217s | 0.0233s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0772s | 0.0974s | -0.0202s | improved |
| `ngap_rel18.6_specs` | 0.0487s | 0.0486s | +0.0001s | worse |
| `lteNRRCC` | 0.0774s | 0.0885s | -0.0111s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.77 MB | 4.42 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.17 MB | 13.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.95 MB | 5.89 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.69 MB | 4.08 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0423s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1095s | 0.1127s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0784s | 0.0792s | -0.0008s | improved |
| `lteNRRCC` | 0.1397s | 0.1288s | +0.0109s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.75 MB | 7.60 MB | 219.9% | 194.0% |
| `f1ap_rel18.6_specs` | 8.18 MB | 8.05 MB | 155.4% | 163.5% |
| `ngap_rel18.6_specs` | 7.62 MB | 8.31 MB | 78.4% | 224.4% |
| `lteNRRCC` | 51.32 MB | 49.40 MB | 115.8% | 156.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0373s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.1188s | 0.1101s | +0.0087s | worse |
| `ngap_rel18.6_specs` | 0.0838s | 0.0756s | +0.0082s | worse |
| `lteNRRCC` | 0.1324s | 0.1264s | +0.0060s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.98 MB | 10.92 MB | 107.3% | 107.0% |
| `f1ap_rel18.6_specs` | 11.84 MB | 11.96 MB | 214.6% | 105.5% |
| `ngap_rel18.6_specs` | 11.08 MB | 10.96 MB | 107.8% | 105.1% |
| `lteNRRCC` | 9.75 MB | 79.41 MB | 109.9% | 109.0% |
<!-- BENCH_RESULTS_END -->
