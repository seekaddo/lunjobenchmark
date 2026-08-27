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
Generated: 2026-08-27T20:16:06.137911+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0321s | +0.0043s | worse |
| `f1ap_rel18.6_specs` | 0.1131s | 0.1058s | +0.0073s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0725s | +0.0044s | worse |
| `lteNRRCC` | 0.1210s | 0.1160s | +0.0050s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 79.2% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0264s | 0.0283s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0762s | 0.0802s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0498s | 0.0523s | -0.0025s | improved |
| `lteNRRCC` | 0.0964s | 0.0989s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.78 MB | 36.66 MB | 13.0% | 100.0% |
| `f1ap_rel18.6_specs` | 21.95 MB | 103.35 MB | 104.3% | 102.3% |
| `ngap_rel18.6_specs` | 18.14 MB | 73.91 MB | 105.3% | 102.9% |
| `lteNRRCC` | 48.52 MB | 65.94 MB | 102.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0289s | 0.0264s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.0764s | 0.0945s | -0.0181s | improved |
| `ngap_rel18.6_specs` | 0.0536s | 0.0629s | -0.0093s | improved |
| `lteNRRCC` | 0.1021s | 0.1084s | -0.0063s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 55.61 MB | 29.8% | 104.5% |
| `f1ap_rel18.6_specs` | 34.71 MB | 164.68 MB | 104.2% | 102.1% |
| `ngap_rel18.6_specs` | 23.64 MB | 117.80 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.86 MB | 102.48 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0229s | 0.0229s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0690s | 0.0765s | -0.0075s | improved |
| `ngap_rel18.6_specs` | 0.0517s | 0.0476s | +0.0041s | worse |
| `lteNRRCC` | 0.0774s | 0.0778s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.31 MB | 4.05 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 5.72 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.80 MB | 4.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.73 MB | 3.86 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0429s | 0.0419s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1059s | 0.1152s | -0.0093s | improved |
| `ngap_rel18.6_specs` | 0.0747s | 0.0806s | -0.0059s | improved |
| `lteNRRCC` | 0.1554s | 0.1431s | +0.0123s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.63 MB | 7.33 MB | 112.6% | 81.9% |
| `f1ap_rel18.6_specs` | 8.24 MB | 106.65 MB | 108.1% | 107.9% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.68 MB | 162.5% | 86.6% |
| `lteNRRCC` | 51.84 MB | 51.46 MB | 153.3% | 158.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0398s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1210s | 0.1173s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0844s | 0.0877s | -0.0033s | improved |
| `lteNRRCC` | 0.1202s | 0.1329s | -0.0127s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.18 MB | 10.11 MB | 0.0% | 133.3% |
| `f1ap_rel18.6_specs` | 10.45 MB | 130.43 MB | 178.3% | 128.5% |
| `ngap_rel18.6_specs` | 9.57 MB | 10.38 MB | 129.6% | 117.3% |
| `lteNRRCC` | 73.79 MB | 79.34 MB | 182.4% | 132.1% |
<!-- BENCH_RESULTS_END -->
