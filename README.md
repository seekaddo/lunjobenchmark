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
Generated: 2026-09-16T14:45:29.034389+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0360s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1104s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0744s | +0.0006s | worse |
| `lteNRRCC` | 0.1188s | 0.1214s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 16.4% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0345s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1055s | 0.0946s | +0.0109s | worse |
| `ngap_rel18.6_specs` | 0.0753s | 0.0656s | +0.0097s | worse |
| `lteNRRCC` | 0.1419s | 0.1277s | +0.0142s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.49 MB | 80.0% | 103.0% |
| `f1ap_rel18.6_specs` | 22.21 MB | 103.35 MB | 102.9% | 103.0% |
| `ngap_rel18.6_specs` | 18.02 MB | 74.58 MB | 103.4% | 101.9% |
| `lteNRRCC` | 48.66 MB | 66.34 MB | 102.9% | 103.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0343s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0970s | 0.0922s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0672s | 0.0643s | +0.0029s | worse |
| `lteNRRCC` | 0.1308s | 0.1177s | +0.0131s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.26 MB | 87.5% | 103.4% |
| `f1ap_rel18.6_specs` | 35.25 MB | 164.74 MB | 102.9% | 101.6% |
| `ngap_rel18.6_specs` | 23.93 MB | 117.00 MB | 108.0% | 102.3% |
| `lteNRRCC` | 74.81 MB | 102.34 MB | 103.2% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0318s | 0.0384s | -0.0066s | improved |
| `f1ap_rel18.6_specs` | 0.0903s | 0.1273s | -0.0370s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0767s | -0.0113s | improved |
| `lteNRRCC` | 0.0873s | 0.1201s | -0.0328s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.98 MB | 800 KB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.42 MB | 8.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.59 MB | 7.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.33 MB | 9.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0274s | 0.0332s | -0.0058s | improved |
| `f1ap_rel18.6_specs` | 0.0737s | 0.0927s | -0.0190s | improved |
| `ngap_rel18.6_specs` | 0.0530s | 0.0645s | -0.0115s | improved |
| `lteNRRCC` | 0.0883s | 0.1163s | -0.0280s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 10.39 MB | 0.0% | 118.1% |
| `f1ap_rel18.6_specs` | 14.28 MB | 12.70 MB | 94.7% | 97.7% |
| `ngap_rel18.6_specs` | 14.12 MB | 28.84 MB | 83.2% | 111.1% |
| `lteNRRCC` | 21.12 MB | 14.49 MB | 122.8% | 87.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0272s | +0.0138s | worse |
| `f1ap_rel18.6_specs` | 0.1157s | 0.0795s | +0.0362s | worse |
| `ngap_rel18.6_specs` | 0.0813s | 0.0559s | +0.0254s | worse |
| `lteNRRCC` | 0.1379s | 0.0835s | +0.0544s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.72 MB | 9.72 MB | 85.4% | 92.7% |
| `f1ap_rel18.6_specs` | 11.35 MB | 164.20 MB | 217.2% | 104.2% |
| `ngap_rel18.6_specs` | 9.35 MB | 9.56 MB | 178.2% | 164.3% |
| `lteNRRCC` | 70.30 MB | 76.28 MB | 107.9% | 157.9% |
<!-- BENCH_RESULTS_END -->
