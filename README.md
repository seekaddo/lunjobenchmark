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
Generated: 2026-05-10T11:04:29.480608+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0369s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1151s | 0.1142s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0804s | 0.0783s | +0.0021s | worse |
| `lteNRRCC` | 0.1227s | 0.1225s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 25.8% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 106.6% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0344s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0946s | 0.0922s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0671s | 0.0648s | +0.0023s | worse |
| `lteNRRCC` | 0.1298s | 0.1281s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.21 MB | 36.45 MB | 29.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.38 MB | 103.22 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.71 MB | 74.46 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.51 MB | 66.22 MB | 106.2% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0340s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1014s | 0.0984s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0702s | 0.0693s | +0.0009s | worse |
| `lteNRRCC` | 0.1184s | 0.1159s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.21 MB | 55.70 MB | 87.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.04 MB | 163.53 MB | 107.1% | 103.3% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.89 MB | 108.7% | 106.8% |
| `lteNRRCC` | 73.99 MB | 102.96 MB | 105.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0208s | +0.0142s | worse |
| `f1ap_rel18.6_specs` | 0.0683s | 0.0693s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0404s | 0.0396s | +0.0008s | worse |
| `lteNRRCC` | 0.0676s | 0.0676s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.06 MB | 4.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 3.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.47 MB | 4.17 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.03 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0416s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1148s | 0.1143s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0797s | -0.0022s | improved |
| `lteNRRCC` | 0.1394s | 0.1409s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.97 MB | 7.71 MB | 221.0% | 86.9% |
| `f1ap_rel18.6_specs` | 8.40 MB | 106.64 MB | 169.0% | 110.7% |
| `ngap_rel18.6_specs` | 7.91 MB | 8.18 MB | 95.2% | 107.1% |
| `lteNRRCC` | 51.54 MB | 70.18 MB | 104.3% | 168.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0376s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.1227s | 0.1096s | +0.0131s | worse |
| `ngap_rel18.6_specs` | 0.0841s | 0.0769s | +0.0072s | worse |
| `lteNRRCC` | 0.1375s | 0.1244s | +0.0131s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.86 MB | 8.94 MB | 82.1% | 82.0% |
| `f1ap_rel18.6_specs` | 9.99 MB | 147.54 MB | 165.5% | 107.4% |
| `ngap_rel18.6_specs` | 9.21 MB | 9.34 MB | 82.3% | 84.0% |
| `lteNRRCC` | 73.78 MB | 101.71 MB | 104.6% | 111.5% |
<!-- BENCH_RESULTS_END -->
