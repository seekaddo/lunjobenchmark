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
Generated: 2026-08-24T10:42:29.757966+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0384s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1171s | 0.1178s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0785s | 0.0806s | -0.0021s | improved |
| `lteNRRCC` | 0.1236s | 0.1250s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 87.0% | 103.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 103.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0242s | +0.0103s | worse |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0741s | +0.0194s | worse |
| `ngap_rel18.6_specs` | 0.0648s | 0.0487s | +0.0161s | worse |
| `lteNRRCC` | 0.1281s | 0.0845s | +0.0436s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.56 MB | 36.68 MB | 18.0% | 107.7% |
| `f1ap_rel18.6_specs` | 22.35 MB | 103.26 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.67 MB | 104.0% | 100.0% |
| `lteNRRCC` | 48.57 MB | 66.17 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0330s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0917s | 0.0904s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0635s | 0.0617s | +0.0018s | worse |
| `lteNRRCC` | 0.1197s | 0.1163s | +0.0034s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.42 MB | 55.83 MB | 74.1% | 103.8% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.25 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.27 MB | 117.74 MB | 104.2% | 102.4% |
| `lteNRRCC` | 75.03 MB | 102.63 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0248s | 0.0303s | -0.0055s | improved |
| `f1ap_rel18.6_specs` | 0.0829s | 0.0782s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0496s | 0.0743s | -0.0247s | improved |
| `lteNRRCC` | 0.0784s | 0.1089s | -0.0305s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.41 MB | 4.89 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.50 MB | 5.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.14 MB | 4.36 MB | 1.2% | 0.0% |
| `lteNRRCC` | 3.78 MB | 4.06 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0332s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1000s | 0.0879s | +0.0121s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0660s | +0.0032s | worse |
| `lteNRRCC` | 0.1152s | 0.0944s | +0.0208s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.39 MB | 8.51 MB | 122.9% | 123.2% |
| `f1ap_rel18.6_specs` | 8.92 MB | 106.65 MB | 188.9% | 105.6% |
| `ngap_rel18.6_specs` | 8.49 MB | 8.94 MB | 94.5% | 94.6% |
| `lteNRRCC` | 8.66 MB | 62.61 MB | 94.3% | 108.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0401s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1135s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0824s | -0.0062s | improved |
| `lteNRRCC` | 0.1267s | 0.1283s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.98 MB | 9.01 MB | 0.0% | 167.3% |
| `f1ap_rel18.6_specs` | 11.39 MB | 164.20 MB | 88.3% | 114.3% |
| `ngap_rel18.6_specs` | 9.49 MB | 9.21 MB | 104.5% | 158.1% |
| `lteNRRCC` | 73.77 MB | 97.83 MB | 157.6% | 231.5% |
<!-- BENCH_RESULTS_END -->
