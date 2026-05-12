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
Generated: 2026-05-12T12:04:27.038440+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0363s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1172s | 0.1139s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0769s | +0.0024s | worse |
| `lteNRRCC` | 0.1247s | 0.1215s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.84 MB | 53.55 MB | 30.8% | 112.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.5% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 115.4% | 107.5% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0335s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0911s | 0.0905s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0637s | 0.0644s | -0.0007s | improved |
| `lteNRRCC` | 0.1230s | 0.1245s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.24 MB | 36.57 MB | 89.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.33 MB | 102.96 MB | 109.1% | 107.0% |
| `ngap_rel18.6_specs` | 16.83 MB | 74.53 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.12 MB | 66.40 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0337s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0890s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0628s | 0.0619s | +0.0009s | worse |
| `lteNRRCC` | 0.1182s | 0.1163s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.24 MB | 55.48 MB | 100.0% | 114.8% |
| `f1ap_rel18.6_specs` | 34.81 MB | 164.64 MB | 110.0% | 105.5% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.83 MB | 112.0% | 104.8% |
| `lteNRRCC` | 74.83 MB | 102.79 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0193s | 0.0256s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0586s | 0.0733s | -0.0147s | improved |
| `ngap_rel18.6_specs` | 0.0406s | 0.0391s | +0.0015s | worse |
| `lteNRRCC` | 0.0671s | 0.0684s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.94 MB | 3.88 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.06 MB | 3.92 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.45 MB | 3.73 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0394s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.0962s | 0.1071s | -0.0109s | improved |
| `ngap_rel18.6_specs` | 0.0671s | 0.0752s | -0.0081s | improved |
| `lteNRRCC` | 0.1146s | 0.1399s | -0.0253s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.69 MB | 7.87 MB | 104.6% | 99.1% |
| `f1ap_rel18.6_specs` | 8.36 MB | 8.73 MB | 103.0% | 266.8% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.24 MB | 203.9% | 98.3% |
| `lteNRRCC` | 51.84 MB | 51.64 MB | 197.3% | 104.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0387s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1176s | 0.1124s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0832s | 0.0775s | +0.0057s | worse |
| `lteNRRCC` | 0.1321s | 0.1293s | +0.0028s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.86 MB | 10.65 MB | 150.1% | 109.2% |
| `f1ap_rel18.6_specs` | 10.44 MB | 164.13 MB | 94.7% | 154.6% |
| `ngap_rel18.6_specs` | 9.02 MB | 9.48 MB | 151.7% | 90.3% |
| `lteNRRCC` | 8.91 MB | 78.21 MB | 159.3% | 213.7% |
<!-- BENCH_RESULTS_END -->
