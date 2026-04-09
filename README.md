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
Generated: 2026-04-09T11:06:45.914794+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0358s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1112s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0758s | +0.0005s | worse |
| `lteNRRCC` | 0.1189s | 0.1194s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 53.55 MB | 7.9% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 106.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0354s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1060s | 0.0955s | +0.0105s | worse |
| `ngap_rel18.6_specs` | 0.0724s | 0.0661s | +0.0063s | worse |
| `lteNRRCC` | 0.1268s | 0.1292s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.28 MB | 36.62 MB | 25.9% | 107.1% |
| `f1ap_rel18.6_specs` | 22.43 MB | 103.33 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 16.70 MB | 74.38 MB | 108.0% | 104.4% |
| `lteNRRCC` | 48.29 MB | 65.62 MB | 103.4% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0320s | +0.0065s | worse |
| `f1ap_rel18.6_specs` | 0.0899s | 0.0884s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0596s | +0.0033s | worse |
| `lteNRRCC` | 0.1169s | 0.1102s | +0.0067s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.28 MB | 55.54 MB | 92.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.80 MB | 164.55 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.49 MB | 117.72 MB | 112.0% | 104.7% |
| `lteNRRCC` | 75.04 MB | 102.71 MB | 105.1% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0238s | 0.0206s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0974s | 0.0636s | +0.0338s | worse |
| `ngap_rel18.6_specs` | 0.0593s | 0.0442s | +0.0151s | worse |
| `lteNRRCC` | 0.1323s | 0.0776s | +0.0547s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 7.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.95 MB | 6.95 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.84 MB | 8.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.31 MB | 4.09 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0396s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1048s | 0.1101s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0727s | 0.0769s | -0.0042s | improved |
| `lteNRRCC` | 0.1369s | 0.1395s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.80 MB | 7.68 MB | 119.6% | 96.8% |
| `f1ap_rel18.6_specs` | 8.43 MB | 106.64 MB | 107.7% | 117.3% |
| `ngap_rel18.6_specs` | 7.98 MB | 7.47 MB | 236.5% | 166.3% |
| `lteNRRCC` | 46.06 MB | 51.86 MB | 105.3% | 117.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0437s | 0.0432s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1219s | 0.1170s | +0.0049s | worse |
| `ngap_rel18.6_specs` | 0.0859s | 0.0822s | +0.0037s | worse |
| `lteNRRCC` | 0.1422s | 0.1299s | +0.0123s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.89 MB | 9.96 MB | 91.4% | 96.8% |
| `f1ap_rel18.6_specs` | 10.30 MB | 162.10 MB | 154.7% | 169.3% |
| `ngap_rel18.6_specs` | 9.33 MB | 9.54 MB | 92.3% | 157.8% |
| `lteNRRCC` | 72.64 MB | 80.75 MB | 161.9% | 109.5% |
<!-- BENCH_RESULTS_END -->
