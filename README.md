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
Generated: 2026-08-24T22:33:05.530257+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0371s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1171s | -0.0066s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0785s | -0.0027s | improved |
| `lteNRRCC` | 0.1211s | 0.1236s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.85 MB | 53.55 MB | 82.6% | 103.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 101.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0345s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0935s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0647s | 0.0648s | -0.0001s | improved |
| `lteNRRCC` | 0.1269s | 0.1281s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.14 MB | 80.0% | 103.8% |
| `f1ap_rel18.6_specs` | 22.04 MB | 103.23 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.45 MB | 104.0% | 102.4% |
| `lteNRRCC` | 48.71 MB | 66.21 MB | 101.6% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0305s | 0.0333s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.0797s | 0.0917s | -0.0120s | improved |
| `ngap_rel18.6_specs` | 0.0552s | 0.0635s | -0.0083s | improved |
| `lteNRRCC` | 0.1043s | 0.1197s | -0.0154s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.63 MB | 55.82 MB | 68.0% | 104.3% |
| `f1ap_rel18.6_specs` | 34.47 MB | 164.54 MB | 108.3% | 102.1% |
| `ngap_rel18.6_specs` | 24.61 MB | 116.77 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.97 MB | 102.38 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0239s | 0.0248s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0660s | 0.0829s | -0.0169s | improved |
| `ngap_rel18.6_specs` | 0.0473s | 0.0496s | -0.0023s | improved |
| `lteNRRCC` | 0.0787s | 0.0784s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.92 MB | 4.48 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.31 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.75 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.05 MB | 4.73 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0433s | 0.0351s | +0.0082s | worse |
| `f1ap_rel18.6_specs` | 0.1201s | 0.1000s | +0.0201s | worse |
| `ngap_rel18.6_specs` | 0.0799s | 0.0692s | +0.0107s | worse |
| `lteNRRCC` | 0.1418s | 0.1152s | +0.0266s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.04 MB | 8.38 MB | 203.9% | 158.1% |
| `f1ap_rel18.6_specs` | 8.68 MB | 9.12 MB | 98.5% | 93.0% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.12 MB | 81.8% | 169.7% |
| `lteNRRCC` | 8.42 MB | 61.80 MB | 169.3% | 105.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0398s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1086s | 0.1115s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0762s | -0.0011s | improved |
| `lteNRRCC` | 0.1254s | 0.1267s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.83 MB | 8.66 MB | 0.0% | 160.4% |
| `f1ap_rel18.6_specs` | 9.57 MB | 164.20 MB | 80.2% | 168.1% |
| `ngap_rel18.6_specs` | 8.68 MB | 9.50 MB | 231.4% | 101.2% |
| `lteNRRCC` | 73.77 MB | 88.77 MB | 103.5% | 105.6% |
<!-- BENCH_RESULTS_END -->
