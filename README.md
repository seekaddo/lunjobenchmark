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
Generated: 2026-07-31T23:08:56.132671+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0356s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1117s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0778s | 0.0767s | +0.0011s | worse |
| `lteNRRCC` | 0.1217s | 0.1210s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 90.5% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 100.0% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0259s | 0.0351s | -0.0092s | improved |
| `f1ap_rel18.6_specs` | 0.0729s | 0.0939s | -0.0210s | improved |
| `ngap_rel18.6_specs` | 0.0557s | 0.0655s | -0.0098s | improved |
| `lteNRRCC` | 0.0971s | 0.1286s | -0.0315s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.20 MB | 36.25 MB | 68.0% | 100.0% |
| `f1ap_rel18.6_specs` | 21.94 MB | 102.74 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 19.11 MB | 74.57 MB | 105.6% | 102.8% |
| `lteNRRCC` | 48.59 MB | 66.52 MB | 100.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0351s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0917s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0656s | 0.0645s | +0.0011s | worse |
| `lteNRRCC` | 0.1284s | 0.1184s | +0.0100s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.49 MB | 55.42 MB | 17.3% | 103.6% |
| `f1ap_rel18.6_specs` | 34.49 MB | 164.33 MB | 106.7% | 101.8% |
| `ngap_rel18.6_specs` | 24.58 MB | 116.72 MB | 103.8% | 102.3% |
| `lteNRRCC` | 74.95 MB | 102.62 MB | 103.2% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0239s | +0.0088s | worse |
| `f1ap_rel18.6_specs` | 0.0785s | 0.0680s | +0.0105s | worse |
| `ngap_rel18.6_specs` | 0.0565s | 0.0471s | +0.0094s | worse |
| `lteNRRCC` | 0.1010s | 0.0773s | +0.0237s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.64 MB | 6.81 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.39 MB | 6.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.78 MB | 7.36 MB | 1.3% | 0.0% |
| `lteNRRCC` | 3.98 MB | 7.34 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0292s | +0.0113s | worse |
| `f1ap_rel18.6_specs` | 0.1098s | 0.0826s | +0.0272s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0594s | +0.0192s | worse |
| `lteNRRCC` | 0.1405s | 0.0909s | +0.0496s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.80 MB | 0.0% | 105.5% |
| `f1ap_rel18.6_specs` | 7.88 MB | 106.64 MB | 162.1% | 164.5% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.88 MB | 160.0% | 104.8% |
| `lteNRRCC` | 51.71 MB | 51.33 MB | 162.1% | 158.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0389s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1153s | 0.1106s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0778s | 0.0766s | +0.0012s | worse |
| `lteNRRCC` | 0.1300s | 0.1273s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.31 MB | 0.0% | 225.6% |
| `f1ap_rel18.6_specs` | 10.05 MB | 164.16 MB | 155.6% | 161.2% |
| `ngap_rel18.6_specs` | 8.95 MB | 8.95 MB | 80.3% | 78.5% |
| `lteNRRCC` | 8.68 MB | 73.09 MB | 154.6% | 154.0% |
<!-- BENCH_RESULTS_END -->
