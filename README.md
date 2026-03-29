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
Generated: 2026-03-29T10:42:35.062200+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0364s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1204s | -0.0058s | improved |
| `ngap_rel18.6_specs` | 0.0794s | 0.0777s | +0.0017s | worse |
| `lteNRRCC` | 0.1218s | 0.1200s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 28.9% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 103.8% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0312s | 0.0337s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.0922s | 0.0927s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0634s | 0.0650s | -0.0016s | improved |
| `lteNRRCC` | 0.1151s | 0.1266s | -0.0115s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.37 MB | 36.71 MB | 86.4% | 112.5% |
| `f1ap_rel18.6_specs` | 22.11 MB | 102.87 MB | 107.4% | 103.7% |
| `ngap_rel18.6_specs` | 16.59 MB | 74.66 MB | 109.1% | 104.9% |
| `lteNRRCC` | 48.33 MB | 66.43 MB | 103.6% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0354s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.0897s | 0.1014s | -0.0117s | improved |
| `ngap_rel18.6_specs` | 0.0615s | 0.0695s | -0.0080s | improved |
| `lteNRRCC` | 0.1157s | 0.1168s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.63 MB | 100.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.69 MB | 164.69 MB | 110.3% | 105.6% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.32 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.93 MB | 102.80 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0204s | 0.0194s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.0601s | 0.0626s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0401s | 0.0400s | +0.0001s | worse |
| `lteNRRCC` | 0.0701s | 0.0675s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.72 MB | 4.31 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 4.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.88 MB | 4.84 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.75 MB | 3.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0395s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1093s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0795s | 0.0762s | +0.0033s | worse |
| `lteNRRCC` | 0.1283s | 0.1394s | -0.0111s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.62 MB | 8.59 MB | 111.7% | 228.8% |
| `f1ap_rel18.6_specs` | 8.86 MB | 9.04 MB | 209.9% | 110.9% |
| `ngap_rel18.6_specs` | 8.42 MB | 8.93 MB | 112.0% | 221.6% |
| `lteNRRCC` | 8.46 MB | 8.72 MB | 96.7% | 216.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0382s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1131s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0764s | 0.0773s | -0.0009s | improved |
| `lteNRRCC` | 0.1254s | 0.1262s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.53 MB | 10.41 MB | 115.0% | 118.1% |
| `f1ap_rel18.6_specs` | 11.07 MB | 11.34 MB | 116.6% | 115.7% |
| `ngap_rel18.6_specs` | 9.56 MB | 10.82 MB | 176.9% | 230.5% |
| `lteNRRCC` | 73.79 MB | 99.02 MB | 243.9% | 115.3% |
<!-- BENCH_RESULTS_END -->
