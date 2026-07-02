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
Generated: 2026-07-02T23:15:19.681760+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0359s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1133s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0782s | -0.0030s | improved |
| `lteNRRCC` | 0.1195s | 0.1224s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 20.8% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 106.1% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0213s | 0.0364s | -0.0151s | improved |
| `f1ap_rel18.6_specs` | 0.0594s | 0.0931s | -0.0337s | improved |
| `ngap_rel18.6_specs` | 0.0390s | 0.0657s | -0.0267s | improved |
| `lteNRRCC` | 0.0727s | 0.1275s | -0.0548s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.21 MB | 36.25 MB | 80.0% | 111.8% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.19 MB | 110.5% | 105.7% |
| `ngap_rel18.6_specs` | 19.20 MB | 74.53 MB | 112.5% | 107.7% |
| `lteNRRCC` | 48.73 MB | 66.14 MB | 105.6% | 102.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0367s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.0904s | 0.1066s | -0.0162s | improved |
| `ngap_rel18.6_specs` | 0.0632s | 0.0741s | -0.0109s | improved |
| `lteNRRCC` | 0.1194s | 0.1242s | -0.0048s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.50 MB | 55.64 MB | 88.0% | 107.4% |
| `f1ap_rel18.6_specs` | 35.27 MB | 163.44 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 23.92 MB | 117.85 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.68 MB | 102.59 MB | 105.2% | 102.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0223s | 0.0318s | -0.0095s | improved |
| `f1ap_rel18.6_specs` | 0.0699s | 0.0893s | -0.0194s | improved |
| `ngap_rel18.6_specs` | 0.0458s | 0.0596s | -0.0138s | improved |
| `lteNRRCC` | 0.0821s | 0.1014s | -0.0193s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.62 MB | 3.64 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.98 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.78 MB | 4.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.03 MB | 4.20 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0408s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1189s | -0.0062s | improved |
| `ngap_rel18.6_specs` | 0.0782s | 0.0813s | -0.0031s | improved |
| `lteNRRCC` | 0.1409s | 0.1414s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.34 MB | 118.6% | 154.8% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.43 MB | 159.7% | 148.8% |
| `ngap_rel18.6_specs` | 8.02 MB | 8.36 MB | 149.8% | 223.8% |
| `lteNRRCC` | 8.06 MB | 69.98 MB | 171.2% | 113.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0475s | 0.0425s | +0.0050s | worse |
| `f1ap_rel18.6_specs` | 0.1459s | 0.1158s | +0.0301s | worse |
| `ngap_rel18.6_specs` | 0.1013s | 0.0857s | +0.0156s | worse |
| `lteNRRCC` | 0.1461s | 0.1315s | +0.0146s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.09 MB | 10.52 MB | 106.0% | 129.3% |
| `f1ap_rel18.6_specs` | 11.05 MB | 11.05 MB | 152.0% | 146.4% |
| `ngap_rel18.6_specs` | 10.31 MB | 10.50 MB | 155.4% | 145.4% |
| `lteNRRCC` | 9.36 MB | 99.39 MB | 141.2% | 131.5% |
<!-- BENCH_RESULTS_END -->
