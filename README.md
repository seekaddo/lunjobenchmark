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
Generated: 2026-07-19T11:13:24.901935+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0360s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1117s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0765s | +0.0003s | worse |
| `lteNRRCC` | 0.1205s | 0.1211s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 22.6% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.32 MB | 100.11 MB | 103.4% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0279s | +0.0061s | worse |
| `f1ap_rel18.6_specs` | 0.0914s | 0.0761s | +0.0153s | worse |
| `ngap_rel18.6_specs` | 0.0635s | 0.0545s | +0.0090s | worse |
| `lteNRRCC` | 0.1243s | 0.0989s | +0.0254s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 36.59 MB | 22.6% | 110.7% |
| `f1ap_rel18.6_specs` | 21.94 MB | 102.62 MB | 109.7% | 105.3% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.39 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.72 MB | 66.34 MB | 104.8% | 104.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0302s | 0.0340s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.0875s | 0.0914s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0553s | 0.0652s | -0.0099s | improved |
| `lteNRRCC` | 0.0994s | 0.1177s | -0.0183s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.11 MB | 54.91 MB | 70.4% | 109.5% |
| `f1ap_rel18.6_specs` | 34.56 MB | 164.49 MB | 112.5% | 105.9% |
| `ngap_rel18.6_specs` | 24.37 MB | 117.75 MB | 110.0% | 105.4% |
| `lteNRRCC` | 74.86 MB | 101.75 MB | 104.0% | 103.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0314s | 0.0359s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.0861s | 0.0938s | -0.0077s | improved |
| `ngap_rel18.6_specs` | 0.0552s | 0.0566s | -0.0014s | improved |
| `lteNRRCC` | 0.0863s | 0.1235s | -0.0372s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.72 MB | 4.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.52 MB | 3.28 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.23 MB | 4.84 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.95 MB | 6.09 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0394s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1113s | 0.1060s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0782s | 0.0751s | +0.0031s | worse |
| `lteNRRCC` | 0.1455s | 0.1401s | +0.0054s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.36 MB | 91.5% | 169.4% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.11 MB | 164.2% | 80.2% |
| `ngap_rel18.6_specs` | 7.88 MB | 7.88 MB | 160.0% | 157.4% |
| `lteNRRCC` | 50.74 MB | 70.55 MB | 107.8% | 114.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0336s | +0.0057s | worse |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1006s | +0.0130s | worse |
| `ngap_rel18.6_specs` | 0.0804s | 0.0773s | +0.0031s | worse |
| `lteNRRCC` | 0.1375s | 0.1115s | +0.0260s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.73 MB | 8.80 MB | 157.3% | 156.2% |
| `f1ap_rel18.6_specs` | 9.43 MB | 164.20 MB | 150.6% | 107.5% |
| `ngap_rel18.6_specs` | 10.26 MB | 8.96 MB | 98.5% | 157.0% |
| `lteNRRCC` | 8.69 MB | 82.02 MB | 152.7% | 156.8% |
<!-- BENCH_RESULTS_END -->
