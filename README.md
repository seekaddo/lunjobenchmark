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
Generated: 2026-08-15T22:28:08.690132+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0370s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1068s | 0.1134s | -0.0066s | improved |
| `ngap_rel18.6_specs` | 0.0730s | 0.0761s | -0.0031s | improved |
| `lteNRRCC` | 0.1158s | 0.1207s | -0.0049s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.64 MB | 53.55 MB | 85.0% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.4% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 100.0% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0256s | 0.0367s | -0.0111s | improved |
| `f1ap_rel18.6_specs` | 0.0776s | 0.0975s | -0.0199s | improved |
| `ngap_rel18.6_specs` | 0.0519s | 0.0691s | -0.0172s | improved |
| `lteNRRCC` | 0.0985s | 0.1337s | -0.0352s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.39 MB | 36.51 MB | 66.7% | 105.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.39 MB | 104.5% | 102.3% |
| `ngap_rel18.6_specs` | 19.42 MB | 74.59 MB | 105.6% | 100.0% |
| `lteNRRCC` | 48.62 MB | 66.32 MB | 104.3% | 101.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0372s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1062s | 0.0907s | +0.0155s | worse |
| `ngap_rel18.6_specs` | 0.0695s | 0.0645s | +0.0050s | worse |
| `lteNRRCC` | 0.1164s | 0.1171s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.67 MB | 55.77 MB | 56.2% | 107.7% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.66 MB | 103.7% | 101.7% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.65 MB | 109.1% | 102.3% |
| `lteNRRCC` | 74.69 MB | 102.39 MB | 103.6% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0217s | 0.0344s | -0.0127s | improved |
| `f1ap_rel18.6_specs` | 0.0697s | 0.1043s | -0.0346s | improved |
| `ngap_rel18.6_specs` | 0.0431s | 0.0670s | -0.0239s | improved |
| `lteNRRCC` | 0.0747s | 0.1078s | -0.0331s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.36 MB | 7.88 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.09 MB | 3.77 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.86 MB | 8.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.41 MB | 4.30 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0325s | 0.0393s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.0933s | 0.1104s | -0.0171s | improved |
| `ngap_rel18.6_specs` | 0.0676s | 0.0773s | -0.0097s | improved |
| `lteNRRCC` | 0.0996s | 0.1410s | -0.0414s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 8.40 MB | 0.0% | 109.2% |
| `f1ap_rel18.6_specs` | 8.86 MB | 99.37 MB | 104.1% | 107.8% |
| `ngap_rel18.6_specs` | 8.39 MB | 8.18 MB | 119.8% | 143.2% |
| `lteNRRCC` | 8.36 MB | 61.86 MB | 0.0% | 139.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0408s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1268s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0794s | 0.0864s | -0.0070s | improved |
| `lteNRRCC` | 0.1308s | 0.1264s | +0.0044s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.15 MB | 10.58 MB | 0.0% | 228.7% |
| `f1ap_rel18.6_specs` | 9.68 MB | 164.19 MB | 160.7% | 168.3% |
| `ngap_rel18.6_specs` | 9.01 MB | 8.95 MB | 80.8% | 158.2% |
| `lteNRRCC` | 8.61 MB | 79.45 MB | 78.2% | 108.6% |
<!-- BENCH_RESULTS_END -->
