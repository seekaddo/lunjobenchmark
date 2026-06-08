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
Generated: 2026-06-08T14:15:03.803402+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0359s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1120s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0721s | 0.0767s | -0.0046s | improved |
| `lteNRRCC` | 0.1174s | 0.1206s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 20.0% | 111.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 106.4% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.3% | 104.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0348s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0951s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0664s | 0.0661s | +0.0003s | worse |
| `lteNRRCC` | 0.1293s | 0.1267s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.17 MB | 36.16 MB | 19.1% | 110.7% |
| `f1ap_rel18.6_specs` | 21.84 MB | 103.31 MB | 109.1% | 103.4% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.22 MB | 110.7% | 106.7% |
| `lteNRRCC` | 48.77 MB | 66.42 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0375s | -0.0039s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0995s | -0.0083s | improved |
| `ngap_rel18.6_specs` | 0.0634s | 0.0712s | -0.0078s | improved |
| `lteNRRCC` | 0.1185s | 0.1323s | -0.0138s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.43 MB | 55.66 MB | 79.3% | 107.1% |
| `f1ap_rel18.6_specs` | 35.22 MB | 164.30 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.39 MB | 116.99 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.71 MB | 102.87 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0246s | 0.0391s | -0.0145s | improved |
| `f1ap_rel18.6_specs` | 0.0915s | 0.0690s | +0.0225s | worse |
| `ngap_rel18.6_specs` | 0.0650s | 0.0508s | +0.0142s | worse |
| `lteNRRCC` | 0.1135s | 0.0829s | +0.0306s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.34 MB | 3.59 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.39 MB | 2.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.62 MB | 2.94 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.92 MB | 4.61 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0444s | 0.0394s | +0.0050s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1097s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0796s | 0.0750s | +0.0046s | worse |
| `lteNRRCC` | 0.1395s | 0.1370s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.63 MB | 7.75 MB | 154.0% | 152.3% |
| `f1ap_rel18.6_specs` | 8.24 MB | 8.44 MB | 156.4% | 75.6% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.12 MB | 146.4% | 153.3% |
| `lteNRRCC` | 49.58 MB | 69.24 MB | 155.9% | 170.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0391s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1107s | 0.1140s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0804s | 0.0768s | +0.0036s | worse |
| `lteNRRCC` | 0.1272s | 0.1277s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.65 MB | 8.55 MB | 160.6% | 79.7% |
| `f1ap_rel18.6_specs` | 11.57 MB | 9.68 MB | 96.7% | 155.0% |
| `ngap_rel18.6_specs` | 9.14 MB | 9.14 MB | 153.5% | 152.8% |
| `lteNRRCC` | 8.49 MB | 98.58 MB | 152.3% | 111.8% |
<!-- BENCH_RESULTS_END -->
