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
Generated: 2026-07-10T12:29:29.639735+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0362s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1118s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0765s | +0.0025s | worse |
| `lteNRRCC` | 0.1230s | 0.1210s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 21.7% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0293s | 0.0340s | -0.0047s | improved |
| `f1ap_rel18.6_specs` | 0.0765s | 0.0930s | -0.0165s | improved |
| `ngap_rel18.6_specs` | 0.0539s | 0.0652s | -0.0113s | improved |
| `lteNRRCC` | 0.0984s | 0.1282s | -0.0298s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.25 MB | 35.90 MB | 14.9% | 108.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.19 MB | 107.7% | 104.3% |
| `ngap_rel18.6_specs` | 19.11 MB | 73.95 MB | 109.1% | 105.6% |
| `lteNRRCC` | 48.66 MB | 66.41 MB | 106.1% | 105.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0363s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0925s | 0.1142s | -0.0217s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0735s | -0.0081s | improved |
| `lteNRRCC` | 0.1213s | 0.1218s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.29 MB | 55.90 MB | 20.7% | 110.3% |
| `f1ap_rel18.6_specs` | 34.23 MB | 164.78 MB | 106.7% | 103.4% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.57 MB | 112.0% | 109.3% |
| `lteNRRCC` | 74.57 MB | 102.43 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0379s | -0.0153s | improved |
| `f1ap_rel18.6_specs` | 0.0635s | 0.0765s | -0.0130s | improved |
| `ngap_rel18.6_specs` | 0.0424s | 0.0519s | -0.0095s | improved |
| `lteNRRCC` | 0.0737s | 0.0822s | -0.0085s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.56 MB | 3.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.56 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.44 MB | 4.17 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.33 MB | 4.12 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0432s | 0.0403s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1143s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0789s | 0.0785s | +0.0004s | worse |
| `lteNRRCC` | 0.1425s | 0.1273s | +0.0152s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.83 MB | 7.64 MB | 141.7% | 75.9% |
| `f1ap_rel18.6_specs` | 8.62 MB | 8.63 MB | 149.1% | 146.4% |
| `ngap_rel18.6_specs` | 7.59 MB | 8.00 MB | 159.6% | 75.2% |
| `lteNRRCC` | 51.85 MB | 52.01 MB | 195.0% | 106.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0380s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1206s | 0.1072s | +0.0134s | worse |
| `ngap_rel18.6_specs` | 0.0833s | 0.0761s | +0.0072s | worse |
| `lteNRRCC` | 0.1304s | 0.1251s | +0.0053s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.09 MB | 9.65 MB | 105.0% | 163.5% |
| `f1ap_rel18.6_specs` | 10.24 MB | 11.14 MB | 80.4% | 117.5% |
| `ngap_rel18.6_specs` | 9.33 MB | 9.48 MB | 161.3% | 162.0% |
| `lteNRRCC` | 8.91 MB | 100.84 MB | 81.2% | 105.7% |
<!-- BENCH_RESULTS_END -->
