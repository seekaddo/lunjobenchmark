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
Generated: 2026-07-13T12:36:00.240419+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0361s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1082s | 0.1128s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0768s | -0.0018s | improved |
| `lteNRRCC` | 0.1174s | 0.1209s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 19.8% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 104.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0366s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1016s | 0.0974s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0719s | 0.0676s | +0.0043s | worse |
| `lteNRRCC` | 0.1331s | 0.1326s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.49 MB | 36.57 MB | 82.1% | 110.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.27 MB | 112.1% | 104.9% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.56 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.42 MB | 66.32 MB | 103.0% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0354s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0938s | 0.1014s | -0.0076s | improved |
| `ngap_rel18.6_specs` | 0.0656s | 0.0715s | -0.0059s | improved |
| `lteNRRCC` | 0.1196s | 0.1174s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.38 MB | 55.15 MB | 20.9% | 110.7% |
| `f1ap_rel18.6_specs` | 35.26 MB | 164.45 MB | 110.0% | 105.3% |
| `ngap_rel18.6_specs` | 24.37 MB | 117.63 MB | 112.0% | 109.1% |
| `lteNRRCC` | 74.79 MB | 102.85 MB | 105.0% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0249s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.0772s | 0.0693s | +0.0079s | worse |
| `ngap_rel18.6_specs` | 0.0586s | 0.0502s | +0.0084s | worse |
| `lteNRRCC` | 0.0884s | 0.0772s | +0.0112s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.88 MB | 4.62 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.55 MB | 3.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.30 MB | 4.56 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.53 MB | 3.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0393s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1087s | +0.0059s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0747s | +0.0053s | worse |
| `lteNRRCC` | 0.1416s | 0.1377s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.86 MB | 7.75 MB | 82.0% | 83.7% |
| `f1ap_rel18.6_specs` | 8.61 MB | 106.64 MB | 159.3% | 192.1% |
| `ngap_rel18.6_specs` | 7.99 MB | 8.00 MB | 82.7% | 162.9% |
| `lteNRRCC` | 46.27 MB | 51.21 MB | 105.9% | 107.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0383s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.1178s | 0.1080s | +0.0098s | worse |
| `ngap_rel18.6_specs` | 0.0828s | 0.0741s | +0.0087s | worse |
| `lteNRRCC` | 0.1366s | 0.1253s | +0.0113s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.41 MB | 9.01 MB | 66.9% | 81.8% |
| `f1ap_rel18.6_specs` | 10.07 MB | 144.79 MB | 80.6% | 164.9% |
| `ngap_rel18.6_specs` | 9.26 MB | 9.29 MB | 167.4% | 81.4% |
| `lteNRRCC` | 9.48 MB | 101.71 MB | 215.1% | 104.4% |
<!-- BENCH_RESULTS_END -->
