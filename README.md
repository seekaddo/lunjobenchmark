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
Generated: 2026-07-14T11:36:29.412686+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0364s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1122s | 0.1127s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0762s | +0.0008s | worse |
| `lteNRRCC` | 0.1204s | 0.1207s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 20.6% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0279s | 0.0355s | -0.0076s | improved |
| `f1ap_rel18.6_specs` | 0.0744s | 0.0977s | -0.0233s | improved |
| `ngap_rel18.6_specs` | 0.0525s | 0.0684s | -0.0159s | improved |
| `lteNRRCC` | 0.0983s | 0.1268s | -0.0285s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.20 MB | 36.53 MB | 87.0% | 113.6% |
| `f1ap_rel18.6_specs` | 22.07 MB | 103.28 MB | 108.0% | 104.3% |
| `ngap_rel18.6_specs` | 19.21 MB | 74.34 MB | 109.5% | 102.9% |
| `lteNRRCC` | 48.73 MB | 65.91 MB | 106.2% | 103.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0274s | +0.0055s | worse |
| `f1ap_rel18.6_specs` | 0.0898s | 0.0884s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0585s | +0.0044s | worse |
| `lteNRRCC` | 0.1171s | 0.0998s | +0.0173s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.05 MB | 55.50 MB | 95.7% | 111.1% |
| `f1ap_rel18.6_specs` | 33.88 MB | 163.71 MB | 106.9% | 105.5% |
| `ngap_rel18.6_specs` | 24.32 MB | 117.30 MB | 108.3% | 107.1% |
| `lteNRRCC` | 74.22 MB | 102.95 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0249s | 0.0459s | -0.0210s | improved |
| `f1ap_rel18.6_specs` | 0.0749s | 0.0693s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0502s | 0.0493s | +0.0009s | worse |
| `lteNRRCC` | 0.0764s | 0.0812s | -0.0048s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 4.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.95 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.45 MB | 3.86 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.77 MB | 7.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0334s | +0.0067s | worse |
| `f1ap_rel18.6_specs` | 0.1074s | 0.0916s | +0.0158s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0622s | +0.0149s | worse |
| `lteNRRCC` | 0.1389s | 0.1104s | +0.0285s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.97 MB | 153.6% | 224.9% |
| `f1ap_rel18.6_specs` | 8.38 MB | 8.61 MB | 159.2% | 226.9% |
| `ngap_rel18.6_specs` | 7.98 MB | 7.88 MB | 106.4% | 158.3% |
| `lteNRRCC` | 48.63 MB | 52.04 MB | 160.3% | 107.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0436s | -0.0041s | improved |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1214s | -0.0109s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0871s | -0.0113s | improved |
| `lteNRRCC` | 0.1307s | 0.1409s | -0.0102s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.45 MB | 10.16 MB | 78.7% | 104.5% |
| `f1ap_rel18.6_specs` | 9.74 MB | 164.16 MB | 177.1% | 159.4% |
| `ngap_rel18.6_specs` | 9.14 MB | 9.27 MB | 155.1% | 149.7% |
| `lteNRRCC` | 9.80 MB | 86.82 MB | 111.6% | 112.0% |
<!-- BENCH_RESULTS_END -->
