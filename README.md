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
Generated: 2026-07-08T23:14:58.123896+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0354s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1171s | 0.1099s | +0.0072s | worse |
| `ngap_rel18.6_specs` | 0.0819s | 0.0750s | +0.0069s | worse |
| `lteNRRCC` | 0.1253s | 0.1202s | +0.0051s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.75 MB | 53.55 MB | 24.0% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0279s | +0.0086s | worse |
| `f1ap_rel18.6_specs` | 0.0988s | 0.0762s | +0.0226s | worse |
| `ngap_rel18.6_specs` | 0.0674s | 0.0528s | +0.0146s | worse |
| `lteNRRCC` | 0.1315s | 0.0982s | +0.0333s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.19 MB | 36.16 MB | 13.0% | 106.9% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.40 MB | 109.1% | 105.0% |
| `ngap_rel18.6_specs` | 17.57 MB | 74.70 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.50 MB | 66.36 MB | 104.6% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0358s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0974s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0703s | 0.0679s | +0.0024s | worse |
| `lteNRRCC` | 0.1204s | 0.1236s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 55.57 MB | 92.3% | 106.9% |
| `f1ap_rel18.6_specs` | 34.68 MB | 164.57 MB | 106.2% | 105.2% |
| `ngap_rel18.6_specs` | 24.27 MB | 117.62 MB | 112.0% | 106.7% |
| `lteNRRCC` | 74.98 MB | 102.89 MB | 106.7% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0232s | 0.0392s | -0.0160s | improved |
| `f1ap_rel18.6_specs` | 0.0717s | 0.1085s | -0.0368s | improved |
| `ngap_rel18.6_specs` | 0.0566s | 0.0707s | -0.0141s | improved |
| `lteNRRCC` | 0.0894s | 0.1180s | -0.0286s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.73 MB | 8.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.17 MB | 8.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.30 MB | 8.55 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.64 MB | 7.36 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0407s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1087s | 0.1090s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0767s | +0.0023s | worse |
| `lteNRRCC` | 0.1388s | 0.1395s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.89 MB | 82.0% | 113.2% |
| `f1ap_rel18.6_specs` | 8.67 MB | 106.64 MB | 111.7% | 194.8% |
| `ngap_rel18.6_specs` | 7.67 MB | 7.67 MB | 157.9% | 161.9% |
| `lteNRRCC` | 47.31 MB | 53.07 MB | 174.3% | 108.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0393s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1100s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0758s | 0.0757s | +0.0001s | worse |
| `lteNRRCC` | 0.1279s | 0.1299s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.22 MB | 10.72 MB | 115.5% | 111.8% |
| `f1ap_rel18.6_specs` | 9.94 MB | 9.69 MB | 156.9% | 170.0% |
| `ngap_rel18.6_specs` | 9.09 MB | 10.45 MB | 168.0% | 105.0% |
| `lteNRRCC` | 9.93 MB | 72.31 MB | 222.5% | 107.2% |
<!-- BENCH_RESULTS_END -->
