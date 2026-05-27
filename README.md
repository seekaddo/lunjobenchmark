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
Generated: 2026-05-27T12:57:17.397599+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0371s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1114s | 0.1157s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0767s | 0.0806s | -0.0039s | improved |
| `lteNRRCC` | 0.1209s | 0.1240s | -0.0031s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 24.4% | 113.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0343s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0955s | 0.0924s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0657s | 0.0652s | +0.0005s | worse |
| `lteNRRCC` | 0.1193s | 0.1270s | -0.0077s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.33 MB | 36.02 MB | 12.6% | 103.8% |
| `f1ap_rel18.6_specs` | 22.21 MB | 103.46 MB | 110.7% | 103.6% |
| `ngap_rel18.6_specs` | 17.72 MB | 74.71 MB | 108.7% | 107.1% |
| `lteNRRCC` | 48.66 MB | 65.51 MB | 105.4% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0369s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.0909s | 0.0935s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0636s | 0.0653s | -0.0017s | improved |
| `lteNRRCC` | 0.1173s | 0.1265s | -0.0092s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 55.75 MB | 78.6% | 107.1% |
| `f1ap_rel18.6_specs` | 34.11 MB | 164.36 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.26 MB | 117.63 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.39 MB | 102.68 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0302s | 0.0278s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.0738s | 0.0831s | -0.0093s | improved |
| `ngap_rel18.6_specs` | 0.0482s | 0.0584s | -0.0102s | improved |
| `lteNRRCC` | 0.0838s | 0.0911s | -0.0073s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.58 MB | 12.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.81 MB | 12.72 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.19 MB | 5.55 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.59 MB | 7.19 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0423s | -0.0040s | improved |
| `f1ap_rel18.6_specs` | 0.1045s | 0.1240s | -0.0195s | improved |
| `ngap_rel18.6_specs` | 0.0732s | 0.0786s | -0.0054s | improved |
| `lteNRRCC` | 0.1357s | 0.1401s | -0.0044s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.80 MB | 7.33 MB | 119.5% | 167.2% |
| `f1ap_rel18.6_specs` | 7.93 MB | 8.54 MB | 165.1% | 188.5% |
| `ngap_rel18.6_specs` | 7.53 MB | 7.67 MB | 81.3% | 99.2% |
| `lteNRRCC` | 48.31 MB | 48.77 MB | 105.7% | 164.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0316s | 0.0364s | -0.0048s | improved |
| `f1ap_rel18.6_specs` | 0.0866s | 0.0977s | -0.0111s | improved |
| `ngap_rel18.6_specs` | 0.0614s | 0.0673s | -0.0059s | improved |
| `lteNRRCC` | 0.0926s | 0.1103s | -0.0177s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 11.66 MB | 0.0% | 101.3% |
| `f1ap_rel18.6_specs` | 19.82 MB | 18.32 MB | 90.2% | 75.3% |
| `ngap_rel18.6_specs` | 24.20 MB | 20.83 MB | 0.0% | 129.3% |
| `lteNRRCC` | 20.78 MB | 16.32 MB | 119.3% | 149.4% |
<!-- BENCH_RESULTS_END -->
