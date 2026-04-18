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
Generated: 2026-04-18T10:50:43.448178+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0362s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1138s | 0.1113s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0778s | -0.0001s | improved |
| `lteNRRCC` | 0.1222s | 0.1207s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 24.7% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0347s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0974s | 0.0937s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0686s | 0.0663s | +0.0023s | worse |
| `lteNRRCC` | 0.1312s | 0.1317s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.38 MB | 36.51 MB | 96.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.19 MB | 103.38 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.50 MB | 74.29 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.73 MB | 66.25 MB | 106.2% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0355s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0889s | 0.0939s | -0.0050s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0649s | +0.0003s | worse |
| `lteNRRCC` | 0.1151s | 0.1274s | -0.0123s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.47 MB | 92.3% | 110.7% |
| `f1ap_rel18.6_specs` | 34.54 MB | 163.67 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 24.10 MB | 117.20 MB | 108.0% | 107.1% |
| `lteNRRCC` | 75.00 MB | 102.89 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0191s | 0.0202s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0747s | 0.0663s | +0.0084s | worse |
| `ngap_rel18.6_specs` | 0.0423s | 0.0463s | -0.0040s | improved |
| `lteNRRCC` | 0.0715s | 0.0748s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.48 MB | 4.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.56 MB | 3.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.34 MB | 1.00 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.83 MB | 4.61 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0382s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1064s | 0.1062s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0756s | 0.0735s | +0.0021s | worse |
| `lteNRRCC` | 0.1387s | 0.1361s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.33 MB | 109.3% | 163.1% |
| `f1ap_rel18.6_specs` | 8.61 MB | 8.04 MB | 225.1% | 159.9% |
| `ngap_rel18.6_specs` | 7.49 MB | 7.68 MB | 80.5% | 162.0% |
| `lteNRRCC` | 49.32 MB | 69.93 MB | 108.1% | 106.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0428s | 0.0387s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1239s | 0.1104s | +0.0135s | worse |
| `ngap_rel18.6_specs` | 0.0868s | 0.0809s | +0.0059s | worse |
| `lteNRRCC` | 0.1322s | 0.1260s | +0.0062s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.54 MB | 10.20 MB | 147.9% | 120.2% |
| `f1ap_rel18.6_specs` | 10.35 MB | 10.90 MB | 191.4% | 118.7% |
| `ngap_rel18.6_specs` | 9.26 MB | 9.50 MB | 164.0% | 82.8% |
| `lteNRRCC` | 8.61 MB | 100.87 MB | 157.6% | 108.8% |
<!-- BENCH_RESULTS_END -->
