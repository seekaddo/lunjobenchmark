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
Generated: 2026-09-20T00:01:11.556804+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0356s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1089s | 0.1098s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0734s | 0.0753s | -0.0019s | improved |
| `lteNRRCC` | 0.1171s | 0.1182s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 15.8% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0347s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0937s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0674s | 0.0662s | +0.0012s | worse |
| `lteNRRCC` | 0.1286s | 0.1286s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.06 MB | 70.0% | 103.6% |
| `f1ap_rel18.6_specs` | 21.95 MB | 103.32 MB | 106.2% | 103.4% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.20 MB | 107.7% | 102.2% |
| `lteNRRCC` | 48.07 MB | 66.54 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0301s | 0.0353s | -0.0052s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0929s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0626s | 0.0658s | -0.0032s | improved |
| `lteNRRCC` | 0.0944s | 0.1189s | -0.0245s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.86 MB | 55.77 MB | 50.0% | 100.0% |
| `f1ap_rel18.6_specs` | 35.19 MB | 163.74 MB | 104.3% | 100.0% |
| `ngap_rel18.6_specs` | 24.42 MB | 117.71 MB | 105.3% | 102.6% |
| `lteNRRCC` | 74.86 MB | 102.82 MB | 102.3% | 101.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0550s | 0.0241s | +0.0309s | worse |
| `f1ap_rel18.6_specs` | 0.0837s | 0.0701s | +0.0136s | worse |
| `ngap_rel18.6_specs` | 0.0895s | 0.0479s | +0.0416s | worse |
| `lteNRRCC` | 0.1049s | 0.0750s | +0.0299s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.58 MB | 2.34 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.42 MB | 9.69 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.80 MB | 7.53 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.52 MB | 8.45 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0443s | 0.0406s | +0.0037s | worse |
| `f1ap_rel18.6_specs` | 0.1310s | 0.1134s | +0.0176s | worse |
| `ngap_rel18.6_specs` | 0.0841s | 0.0779s | +0.0062s | worse |
| `lteNRRCC` | 0.1609s | 0.1413s | +0.0196s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.61 MB | 0.0% | 103.8% |
| `f1ap_rel18.6_specs` | 7.88 MB | 9.06 MB | 87.4% | 104.6% |
| `ngap_rel18.6_specs` | 8.16 MB | 8.82 MB | 164.9% | 213.7% |
| `lteNRRCC` | 48.30 MB | 51.32 MB | 209.9% | 111.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0384s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1128s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0797s | 0.0801s | -0.0004s | improved |
| `lteNRRCC` | 0.1244s | 0.1277s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.59 MB | 0.0% | 164.0% |
| `f1ap_rel18.6_specs` | 9.62 MB | 9.75 MB | 160.5% | 81.5% |
| `ngap_rel18.6_specs` | 8.74 MB | 9.02 MB | 160.6% | 159.2% |
| `lteNRRCC` | 8.56 MB | 95.64 MB | 79.9% | 156.2% |
<!-- BENCH_RESULTS_END -->
