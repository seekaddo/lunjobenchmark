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
Generated: 2026-05-30T11:27:08.145158+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0386s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1171s | 0.1146s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0794s | 0.0792s | +0.0002s | worse |
| `lteNRRCC` | 0.1234s | 0.1231s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 28.4% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 103.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.2% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0358s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0955s | 0.0953s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0672s | 0.0671s | +0.0001s | worse |
| `lteNRRCC` | 0.1290s | 0.1283s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.38 MB | 35.87 MB | 16.1% | 106.9% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.18 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.65 MB | 74.68 MB | 111.1% | 104.4% |
| `lteNRRCC` | 48.49 MB | 66.09 MB | 102.9% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0361s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0906s | 0.1051s | -0.0145s | improved |
| `ngap_rel18.6_specs` | 0.0635s | 0.0659s | -0.0024s | improved |
| `lteNRRCC` | 0.1171s | 0.1272s | -0.0101s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.73 MB | 82.1% | 110.7% |
| `f1ap_rel18.6_specs` | 35.18 MB | 164.71 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.16 MB | 117.56 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.59 MB | 102.97 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0340s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0710s | 0.0666s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0490s | 0.0476s | +0.0014s | worse |
| `lteNRRCC` | 0.0788s | 0.0843s | -0.0055s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.22 MB | 4.80 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.86 MB | 9.25 MB | 0.0% | 0.9% |
| `ngap_rel18.6_specs` | 8.22 MB | 8.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.36 MB | 7.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0419s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1071s | +0.0035s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0752s | +0.0038s | worse |
| `lteNRRCC` | 0.1290s | 0.1356s | -0.0066s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.12 MB | 8.16 MB | 119.0% | 102.4% |
| `f1ap_rel18.6_specs` | 8.56 MB | 8.68 MB | 199.6% | 227.5% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.13 MB | 116.7% | 169.8% |
| `lteNRRCC` | 9.13 MB | 8.55 MB | 192.5% | 232.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0440s | 0.0408s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.1241s | 0.1188s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0864s | 0.0801s | +0.0063s | worse |
| `lteNRRCC` | 0.1402s | 0.1366s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.32 MB | 9.64 MB | 163.6% | 159.7% |
| `f1ap_rel18.6_specs` | 10.15 MB | 164.19 MB | 157.5% | 157.8% |
| `ngap_rel18.6_specs` | 9.33 MB | 9.41 MB | 159.2% | 160.1% |
| `lteNRRCC` | 73.77 MB | 99.76 MB | 158.9% | 156.7% |
<!-- BENCH_RESULTS_END -->
