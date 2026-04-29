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
Generated: 2026-04-29T23:02:19.876586+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0370s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1141s | 0.1143s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0803s | 0.0782s | +0.0021s | worse |
| `lteNRRCC` | 0.1222s | 0.1215s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.82 MB | 53.55 MB | 6.1% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 107.8% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0373s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0956s | 0.0932s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0677s | 0.0663s | +0.0014s | worse |
| `lteNRRCC` | 0.1291s | 0.1278s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.02 MB | 29.8% | 110.3% |
| `f1ap_rel18.6_specs` | 22.36 MB | 103.36 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.68 MB | 74.47 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.71 MB | 66.06 MB | 104.6% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0279s | 0.0347s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.0754s | 0.0900s | -0.0146s | improved |
| `ngap_rel18.6_specs` | 0.0526s | 0.0643s | -0.0117s | improved |
| `lteNRRCC` | 0.1018s | 0.1158s | -0.0140s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.70 MB | 55.80 MB | 95.5% | 108.7% |
| `f1ap_rel18.6_specs` | 34.44 MB | 163.61 MB | 108.0% | 104.3% |
| `ngap_rel18.6_specs` | 24.45 MB | 116.91 MB | 109.5% | 105.7% |
| `lteNRRCC` | 74.58 MB | 102.66 MB | 106.0% | 103.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0203s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0634s | 0.0586s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0433s | 0.0405s | +0.0028s | worse |
| `lteNRRCC` | 0.0729s | 0.0744s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.17 MB | 5.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.94 MB | 4.52 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.77 MB | 4.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.20 MB | 4.39 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0454s | 0.0394s | +0.0060s | worse |
| `f1ap_rel18.6_specs` | 0.1509s | 0.1056s | +0.0453s | worse |
| `ngap_rel18.6_specs` | 0.0782s | 0.0764s | +0.0018s | worse |
| `lteNRRCC` | 0.1639s | 0.1417s | +0.0222s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.75 MB | 160.5% | 137.2% |
| `f1ap_rel18.6_specs` | 8.11 MB | 106.63 MB | 79.0% | 92.0% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.30 MB | 150.9% | 113.8% |
| `lteNRRCC` | 48.56 MB | 49.57 MB | 146.2% | 105.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0416s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1186s | 0.1180s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0823s | 0.0819s | +0.0004s | worse |
| `lteNRRCC` | 0.1375s | 0.1367s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.53 MB | 9.62 MB | 90.1% | 78.8% |
| `f1ap_rel18.6_specs` | 10.05 MB | 156.60 MB | 165.9% | 164.2% |
| `ngap_rel18.6_specs` | 9.33 MB | 9.55 MB | 166.4% | 158.2% |
| `lteNRRCC` | 8.86 MB | 99.75 MB | 80.9% | 159.2% |
<!-- BENCH_RESULTS_END -->
