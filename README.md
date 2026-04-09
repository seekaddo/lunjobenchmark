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
Generated: 2026-04-09T22:51:47.761417+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0354s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1142s | 0.1111s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0778s | 0.0763s | +0.0015s | worse |
| `lteNRRCC` | 0.1219s | 0.1189s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.83 MB | 53.55 MB | 9.2% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.3% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0354s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0938s | 0.1060s | -0.0122s | improved |
| `ngap_rel18.6_specs` | 0.0659s | 0.0724s | -0.0065s | improved |
| `lteNRRCC` | 0.1284s | 0.1268s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.26 MB | 36.18 MB | 100.0% | 110.7% |
| `f1ap_rel18.6_specs` | 22.03 MB | 102.50 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.63 MB | 74.59 MB | 107.4% | 106.8% |
| `lteNRRCC` | 47.88 MB | 66.54 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0385s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0899s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0625s | 0.0629s | -0.0004s | improved |
| `lteNRRCC` | 0.1155s | 0.1169s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.51 MB | 96.0% | 110.7% |
| `f1ap_rel18.6_specs` | 34.73 MB | 164.29 MB | 113.8% | 105.5% |
| `ngap_rel18.6_specs` | 23.75 MB | 117.62 MB | 112.5% | 107.1% |
| `lteNRRCC` | 74.75 MB | 102.14 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0187s | 0.0238s | -0.0051s | improved |
| `f1ap_rel18.6_specs` | 0.0626s | 0.0974s | -0.0348s | improved |
| `ngap_rel18.6_specs` | 0.0405s | 0.0593s | -0.0188s | improved |
| `lteNRRCC` | 0.0755s | 0.1323s | -0.0568s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.25 MB | 3.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.28 MB | 4.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 3.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.98 MB | 3.80 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0378s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1145s | 0.1048s | +0.0097s | worse |
| `ngap_rel18.6_specs` | 0.0815s | 0.0727s | +0.0088s | worse |
| `lteNRRCC` | 0.1418s | 0.1369s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.89 MB | 7.86 MB | 159.6% | 97.5% |
| `f1ap_rel18.6_specs` | 8.57 MB | 106.13 MB | 79.0% | 156.4% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.11 MB | 82.8% | 97.7% |
| `lteNRRCC` | 48.12 MB | 54.19 MB | 173.1% | 107.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0437s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.1059s | 0.1219s | -0.0160s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0859s | -0.0114s | improved |
| `lteNRRCC` | 0.1234s | 0.1422s | -0.0188s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.78 MB | 9.54 MB | 179.6% | 174.4% |
| `f1ap_rel18.6_specs` | 9.68 MB | 9.96 MB | 158.1% | 161.2% |
| `ngap_rel18.6_specs` | 8.89 MB | 9.13 MB | 80.5% | 91.7% |
| `lteNRRCC` | 72.57 MB | 87.69 MB | 164.4% | 160.0% |
<!-- BENCH_RESULTS_END -->
