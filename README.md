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
Generated: 2026-06-17T23:44:17.853010+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0377s | -0.0037s | improved |
| `f1ap_rel18.6_specs` | 0.1086s | 0.1163s | -0.0077s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0777s | -0.0034s | improved |
| `lteNRRCC` | 0.1175s | 0.1229s | -0.0054s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 20.6% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.7% | 104.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 104.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0361s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0921s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0666s | 0.0659s | +0.0007s | worse |
| `lteNRRCC` | 0.1278s | 0.1258s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.67 MB | 82.1% | 111.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.00 MB | 106.1% | 103.5% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.58 MB | 107.7% | 107.0% |
| `lteNRRCC` | 48.27 MB | 66.09 MB | 104.7% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0338s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0907s | 0.0936s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0634s | 0.0641s | -0.0007s | improved |
| `lteNRRCC` | 0.1180s | 0.1183s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.27 MB | 55.28 MB | 75.9% | 110.7% |
| `f1ap_rel18.6_specs` | 35.19 MB | 163.78 MB | 110.0% | 103.5% |
| `ngap_rel18.6_specs` | 24.55 MB | 116.70 MB | 108.0% | 107.0% |
| `lteNRRCC` | 74.82 MB | 102.11 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0213s | 0.0413s | -0.0200s | improved |
| `f1ap_rel18.6_specs` | 0.0770s | 0.0824s | -0.0054s | improved |
| `ngap_rel18.6_specs` | 0.0529s | 0.0791s | -0.0262s | improved |
| `lteNRRCC` | 0.0911s | 0.0945s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.73 MB | 4.38 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.14 MB | 7.66 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.12 MB | 4.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.67 MB | 5.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0426s | -0.0087s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.1185s | -0.0243s | improved |
| `ngap_rel18.6_specs` | 0.0677s | 0.0827s | -0.0150s | improved |
| `lteNRRCC` | 0.1143s | 0.1428s | -0.0285s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.18 MB | 7.88 MB | 199.3% | 142.7% |
| `f1ap_rel18.6_specs` | 8.61 MB | 106.64 MB | 138.7% | 104.8% |
| `ngap_rel18.6_specs` | 8.24 MB | 8.43 MB | 105.9% | 134.8% |
| `lteNRRCC` | 51.40 MB | 57.44 MB | 131.2% | 107.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0414s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1209s | -0.0083s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0847s | -0.0095s | improved |
| `lteNRRCC` | 0.1295s | 0.1388s | -0.0093s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.39 MB | 8.46 MB | 80.2% | 162.6% |
| `f1ap_rel18.6_specs` | 10.83 MB | 9.81 MB | 114.7% | 103.5% |
| `ngap_rel18.6_specs` | 8.83 MB | 10.50 MB | 158.8% | 115.8% |
| `lteNRRCC` | 73.77 MB | 85.77 MB | 161.2% | 159.5% |
<!-- BENCH_RESULTS_END -->
