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
Generated: 2026-05-22T23:09:33.954379+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0371s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1151s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0779s | 0.0794s | -0.0015s | improved |
| `lteNRRCC` | 0.1233s | 0.1243s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.90 MB | 53.55 MB | 26.2% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 105.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0354s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0951s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0660s | 0.0664s | -0.0004s | improved |
| `lteNRRCC` | 0.1260s | 0.1294s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.73 MB | 21.2% | 110.3% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.02 MB | 108.8% | 105.2% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.13 MB | 114.3% | 106.5% |
| `lteNRRCC` | 48.11 MB | 66.34 MB | 104.8% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0365s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0949s | 0.1003s | -0.0054s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0701s | -0.0044s | improved |
| `lteNRRCC` | 0.1281s | 0.1177s | +0.0104s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 55.78 MB | 96.2% | 113.8% |
| `f1ap_rel18.6_specs` | 34.42 MB | 164.46 MB | 109.1% | 105.0% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.64 MB | 111.1% | 106.7% |
| `lteNRRCC` | 75.02 MB | 102.93 MB | 103.1% | 105.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0366s | +0.0051s | worse |
| `f1ap_rel18.6_specs` | 0.0698s | 0.0950s | -0.0252s | improved |
| `ngap_rel18.6_specs` | 0.0508s | 0.0712s | -0.0204s | improved |
| `lteNRRCC` | 0.0735s | 0.1085s | -0.0350s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.20 MB | 4.38 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.36 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.61 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.12 MB | 4.16 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0397s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1057s | 0.1128s | -0.0071s | improved |
| `ngap_rel18.6_specs` | 0.0740s | 0.0773s | -0.0033s | improved |
| `lteNRRCC` | 0.1382s | 0.1388s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.33 MB | 7.81 MB | 164.6% | 231.5% |
| `f1ap_rel18.6_specs` | 8.62 MB | 106.64 MB | 110.9% | 109.2% |
| `ngap_rel18.6_specs` | 8.25 MB | 7.55 MB | 114.2% | 82.2% |
| `lteNRRCC` | 45.77 MB | 51.53 MB | 161.8% | 230.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0431s | 0.0428s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1197s | 0.1201s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0839s | 0.0828s | +0.0011s | worse |
| `lteNRRCC` | 0.1381s | 0.1379s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.93 MB | 10.27 MB | 193.1% | 221.2% |
| `f1ap_rel18.6_specs` | 9.86 MB | 157.60 MB | 90.0% | 163.5% |
| `ngap_rel18.6_specs` | 10.87 MB | 10.50 MB | 110.3% | 220.6% |
| `lteNRRCC` | 70.43 MB | 74.13 MB | 109.3% | 106.4% |
<!-- BENCH_RESULTS_END -->
