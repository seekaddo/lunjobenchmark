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
Generated: 2026-06-03T23:50:37.353165+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0349s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.1148s | 0.1101s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0756s | +0.0030s | worse |
| `lteNRRCC` | 0.1223s | 0.1206s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 21.7% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0333s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0941s | 0.0993s | -0.0052s | improved |
| `ngap_rel18.6_specs` | 0.0668s | 0.0661s | +0.0007s | worse |
| `lteNRRCC` | 0.1301s | 0.1165s | +0.0136s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.35 MB | 78.1% | 110.3% |
| `f1ap_rel18.6_specs` | 21.70 MB | 103.43 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.12 MB | 111.1% | 104.4% |
| `lteNRRCC` | 48.48 MB | 66.39 MB | 103.0% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0360s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0937s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0652s | +0.0002s | worse |
| `lteNRRCC` | 0.1165s | 0.1274s | -0.0109s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.25 MB | 55.33 MB | 16.3% | 111.1% |
| `f1ap_rel18.6_specs` | 34.52 MB | 164.70 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.74 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.98 MB | 102.78 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0248s | 0.0464s | -0.0216s | improved |
| `f1ap_rel18.6_specs` | 0.0842s | 0.0681s | +0.0161s | worse |
| `ngap_rel18.6_specs` | 0.0518s | 0.0471s | +0.0047s | worse |
| `lteNRRCC` | 0.0855s | 0.0784s | +0.0071s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.31 MB | 4.50 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 4.64 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.91 MB | 4.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.03 MB | 3.61 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0398s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1143s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0803s | -0.0040s | improved |
| `lteNRRCC` | 0.1391s | 0.1430s | -0.0039s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.82 MB | 167.4% | 82.7% |
| `f1ap_rel18.6_specs` | 8.43 MB | 106.66 MB | 166.6% | 109.5% |
| `ngap_rel18.6_specs` | 7.98 MB | 8.38 MB | 88.7% | 109.8% |
| `lteNRRCC` | 49.33 MB | 54.14 MB | 162.2% | 106.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0438s | 0.0416s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1274s | 0.1179s | +0.0095s | worse |
| `ngap_rel18.6_specs` | 0.0876s | 0.0809s | +0.0067s | worse |
| `lteNRRCC` | 0.1349s | 0.1301s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.64 MB | 10.02 MB | 171.8% | 119.1% |
| `f1ap_rel18.6_specs` | 10.23 MB | 9.68 MB | 81.6% | 164.9% |
| `ngap_rel18.6_specs` | 9.48 MB | 9.55 MB | 158.7% | 83.7% |
| `lteNRRCC` | 8.14 MB | 8.86 MB | 238.7% | 166.7% |
<!-- BENCH_RESULTS_END -->
