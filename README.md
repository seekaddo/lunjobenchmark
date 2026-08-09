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
Generated: 2026-08-09T22:37:35.535699+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0343s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1069s | +0.0035s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0732s | +0.0039s | worse |
| `lteNRRCC` | 0.1198s | 0.1160s | +0.0038s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 15.7% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0337s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0954s | 0.0921s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0650s | +0.0042s | worse |
| `lteNRRCC` | 0.1305s | 0.1249s | +0.0056s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 36.01 MB | 74.1% | 107.4% |
| `f1ap_rel18.6_specs` | 22.42 MB | 103.36 MB | 103.1% | 101.8% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.45 MB | 103.8% | 102.4% |
| `lteNRRCC` | 48.73 MB | 66.31 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0316s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0927s | 0.0949s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0636s | 0.0637s | -0.0001s | improved |
| `lteNRRCC` | 0.1199s | 0.1089s | +0.0110s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 55.84 MB | 15.8% | 103.7% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.72 MB | 106.9% | 103.6% |
| `ngap_rel18.6_specs` | 24.23 MB | 117.36 MB | 108.3% | 104.9% |
| `lteNRRCC` | 74.98 MB | 102.14 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0237s | 0.0215s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0777s | 0.0675s | +0.0102s | worse |
| `ngap_rel18.6_specs` | 0.0490s | 0.0468s | +0.0022s | worse |
| `lteNRRCC` | 0.0762s | 0.0759s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.06 MB | 3.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.27 MB | 4.62 MB | 0.0% | 0.6% |
| `ngap_rel18.6_specs` | 4.73 MB | 5.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.78 MB | 3.72 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0453s | 0.0390s | +0.0063s | worse |
| `f1ap_rel18.6_specs` | 0.1283s | 0.1082s | +0.0201s | worse |
| `ngap_rel18.6_specs` | 0.0872s | 0.0780s | +0.0092s | worse |
| `lteNRRCC` | 0.1589s | 0.1408s | +0.0181s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.81 MB | 0.0% | 150.0% |
| `f1ap_rel18.6_specs` | 9.04 MB | 8.72 MB | 92.5% | 138.3% |
| `ngap_rel18.6_specs` | 8.32 MB | 7.88 MB | 212.3% | 154.7% |
| `lteNRRCC` | 51.83 MB | 51.86 MB | 106.9% | 151.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0385s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1138s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0779s | -0.0028s | improved |
| `lteNRRCC` | 0.1264s | 0.1297s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.52 MB | 0.0% | 160.8% |
| `f1ap_rel18.6_specs` | 9.68 MB | 164.14 MB | 175.0% | 105.3% |
| `ngap_rel18.6_specs` | 10.08 MB | 8.96 MB | 108.0% | 80.4% |
| `lteNRRCC` | 8.43 MB | 94.95 MB | 159.1% | 115.6% |
<!-- BENCH_RESULTS_END -->
