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
Generated: 2026-09-29T16:26:23.295121+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0357s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1122s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0758s | +0.0001s | worse |
| `lteNRRCC` | 0.1206s | 0.1206s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 15.0% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0312s | 0.0341s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.0826s | 0.0931s | -0.0105s | improved |
| `ngap_rel18.6_specs` | 0.0586s | 0.0655s | -0.0069s | improved |
| `lteNRRCC` | 0.1035s | 0.1287s | -0.0252s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 36.19 MB | 25.0% | 108.7% |
| `f1ap_rel18.6_specs` | 22.41 MB | 102.96 MB | 107.7% | 100.0% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.64 MB | 104.5% | 102.8% |
| `lteNRRCC` | 48.40 MB | 66.52 MB | 101.9% | 103.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0266s | 0.0351s | -0.0085s | improved |
| `f1ap_rel18.6_specs` | 0.0845s | 0.0998s | -0.0153s | improved |
| `ngap_rel18.6_specs` | 0.0571s | 0.0687s | -0.0116s | improved |
| `lteNRRCC` | 0.0868s | 0.1168s | -0.0300s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 55.00 MB | 9.0% | 104.3% |
| `f1ap_rel18.6_specs` | 34.45 MB | 163.80 MB | 100.0% | 101.9% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.74 MB | 100.0% | 102.7% |
| `lteNRRCC` | 73.89 MB | 102.91 MB | 100.0% | 101.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0356s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.0946s | 0.1069s | -0.0123s | improved |
| `ngap_rel18.6_specs` | 0.0721s | 0.0750s | -0.0029s | improved |
| `lteNRRCC` | 0.1095s | 0.1201s | -0.0106s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.20 MB | 4.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.22 MB | 11.64 MB | 0.0% | 0.9% |
| `ngap_rel18.6_specs` | 4.38 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.94 MB | 7.33 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0502s | 0.0402s | +0.0100s | worse |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1077s | +0.0080s | worse |
| `ngap_rel18.6_specs` | 0.0811s | 0.0756s | +0.0055s | worse |
| `lteNRRCC` | 0.1445s | 0.1378s | +0.0067s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.78 MB | 8.00 MB | 94.9% | 154.9% |
| `f1ap_rel18.6_specs` | 8.86 MB | 8.95 MB | 151.9% | 154.1% |
| `ngap_rel18.6_specs` | 8.27 MB | 8.40 MB | 99.9% | 160.9% |
| `lteNRRCC` | 51.80 MB | 60.51 MB | 153.0% | 155.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0394s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1072s | 0.1105s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0737s | 0.0768s | -0.0031s | improved |
| `lteNRRCC` | 0.1267s | 0.1291s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.39 MB | 10.64 MB | 0.0% | 226.7% |
| `f1ap_rel18.6_specs` | 10.43 MB | 10.63 MB | 106.4% | 101.5% |
| `ngap_rel18.6_specs` | 9.41 MB | 9.07 MB | 99.2% | 157.4% |
| `lteNRRCC` | 8.49 MB | 73.77 MB | 153.8% | 155.3% |
<!-- BENCH_RESULTS_END -->
