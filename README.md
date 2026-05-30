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
Generated: 2026-05-30T23:05:35.514511+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0363s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1171s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0795s | 0.0794s | +0.0001s | worse |
| `lteNRRCC` | 0.1206s | 0.1234s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.83 MB | 53.55 MB | 7.9% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0347s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.0914s | 0.0955s | -0.0041s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0672s | -0.0023s | improved |
| `lteNRRCC` | 0.1230s | 0.1290s | -0.0060s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.30 MB | 36.70 MB | 100.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.43 MB | 112.5% | 107.0% |
| `ngap_rel18.6_specs` | 17.66 MB | 74.39 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.68 MB | 66.22 MB | 103.2% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0350s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.1233s | 0.0906s | +0.0327s | worse |
| `ngap_rel18.6_specs` | 0.0854s | 0.0635s | +0.0219s | worse |
| `lteNRRCC` | 0.1313s | 0.1171s | +0.0142s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.65 MB | 18.5% | 109.7% |
| `f1ap_rel18.6_specs` | 34.75 MB | 164.42 MB | 110.0% | 102.8% |
| `ngap_rel18.6_specs` | 24.23 MB | 117.53 MB | 112.5% | 105.7% |
| `lteNRRCC` | 74.65 MB | 102.15 MB | 103.3% | 102.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0281s | 0.0361s | -0.0080s | improved |
| `f1ap_rel18.6_specs` | 0.0908s | 0.0710s | +0.0198s | worse |
| `ngap_rel18.6_specs` | 0.0626s | 0.0490s | +0.0136s | worse |
| `lteNRRCC` | 0.1195s | 0.0788s | +0.0407s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 5.11 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.45 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.66 MB | 3.69 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.06 MB | 3.41 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0401s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1068s | 0.1106s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0754s | 0.0790s | -0.0036s | improved |
| `lteNRRCC` | 0.1376s | 0.1290s | +0.0086s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.35 MB | 7.74 MB | 92.7% | 114.2% |
| `f1ap_rel18.6_specs` | 8.47 MB | 8.55 MB | 228.6% | 211.9% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.61 MB | 161.8% | 163.4% |
| `lteNRRCC` | 49.13 MB | 69.22 MB | 176.1% | 162.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0434s | 0.0440s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1263s | 0.1241s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0866s | 0.0864s | +0.0002s | worse |
| `lteNRRCC` | 0.1415s | 0.1402s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.57 MB | 9.64 MB | 155.0% | 78.1% |
| `f1ap_rel18.6_specs` | 10.48 MB | 164.19 MB | 156.0% | 103.8% |
| `ngap_rel18.6_specs` | 9.41 MB | 10.25 MB | 155.2% | 153.9% |
| `lteNRRCC` | 73.58 MB | 101.71 MB | 108.9% | 106.3% |
<!-- BENCH_RESULTS_END -->
