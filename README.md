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
Generated: 2026-08-29T14:59:17.342914+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0332s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1062s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0772s | 0.0726s | +0.0046s | worse |
| `lteNRRCC` | 0.1205s | 0.1149s | +0.0056s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 82.6% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0238s | 0.0347s | -0.0109s | improved |
| `f1ap_rel18.6_specs` | 0.0709s | 0.0939s | -0.0230s | improved |
| `ngap_rel18.6_specs` | 0.0476s | 0.0668s | -0.0192s | improved |
| `lteNRRCC` | 0.0883s | 0.1295s | -0.0412s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.75 MB | 36.69 MB | 62.5% | 105.3% |
| `f1ap_rel18.6_specs` | 22.38 MB | 103.44 MB | 104.5% | 102.3% |
| `ngap_rel18.6_specs` | 18.06 MB | 74.46 MB | 105.6% | 103.1% |
| `lteNRRCC` | 48.55 MB | 66.53 MB | 102.2% | 101.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0239s | +0.0110s | worse |
| `f1ap_rel18.6_specs` | 0.0929s | 0.0829s | +0.0100s | worse |
| `ngap_rel18.6_specs` | 0.0646s | 0.0545s | +0.0101s | worse |
| `lteNRRCC` | 0.1278s | 0.0849s | +0.0429s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.17 MB | 18.3% | 107.4% |
| `f1ap_rel18.6_specs` | 34.79 MB | 164.56 MB | 106.7% | 101.8% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.27 MB | 104.0% | 104.8% |
| `lteNRRCC` | 74.79 MB | 102.14 MB | 101.6% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0256s | 0.0224s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0671s | 0.0685s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0475s | 0.0564s | -0.0089s | improved |
| `lteNRRCC` | 0.0783s | 0.0813s | -0.0030s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.39 MB | 4.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 4.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.94 MB | 9.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.12 MB | 5.14 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0393s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1073s | 0.1075s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0748s | 0.0749s | -0.0001s | improved |
| `lteNRRCC` | 0.1389s | 0.1379s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.91 MB | 7.45 MB | 0.0% | 161.2% |
| `f1ap_rel18.6_specs` | 8.05 MB | 8.12 MB | 80.5% | 93.5% |
| `ngap_rel18.6_specs` | 9.31 MB | 8.12 MB | 196.6% | 100.4% |
| `lteNRRCC` | 46.77 MB | 49.27 MB | 160.5% | 160.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0371s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1041s | +0.0071s | worse |
| `ngap_rel18.6_specs` | 0.0806s | 0.0733s | +0.0073s | worse |
| `lteNRRCC` | 0.1282s | 0.1265s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.87 MB | 0.0% | 157.0% |
| `f1ap_rel18.6_specs` | 11.27 MB | 11.16 MB | 105.3% | 100.9% |
| `ngap_rel18.6_specs` | 11.45 MB | 11.07 MB | 82.4% | 108.9% |
| `lteNRRCC` | 73.78 MB | 79.77 MB | 152.8% | 107.2% |
<!-- BENCH_RESULTS_END -->
