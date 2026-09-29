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
Generated: 2026-09-29T01:43:13.224183+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0370s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1122s | 0.1115s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0758s | 0.0774s | -0.0016s | improved |
| `lteNRRCC` | 0.1206s | 0.1199s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 14.5% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0346s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0964s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0655s | 0.0706s | -0.0051s | improved |
| `lteNRRCC` | 0.1287s | 0.1301s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.58 MB | 80.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.38 MB | 103.50 MB | 103.1% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.15 MB | 108.0% | 104.8% |
| `lteNRRCC` | 48.76 MB | 66.38 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0305s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.0998s | 0.0811s | +0.0187s | worse |
| `ngap_rel18.6_specs` | 0.0687s | 0.0589s | +0.0098s | worse |
| `lteNRRCC` | 0.1168s | 0.1044s | +0.0124s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 55.79 MB | 72.7% | 104.0% |
| `f1ap_rel18.6_specs` | 35.19 MB | 164.64 MB | 103.8% | 101.8% |
| `ngap_rel18.6_specs` | 23.60 MB | 117.25 MB | 105.0% | 102.3% |
| `lteNRRCC` | 74.83 MB | 102.79 MB | 101.9% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0388s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.1069s | 0.0961s | +0.0108s | worse |
| `ngap_rel18.6_specs` | 0.0750s | 0.0550s | +0.0200s | worse |
| `lteNRRCC` | 0.1201s | 0.0926s | +0.0275s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.03 MB | 7.22 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.78 MB | 8.69 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.17 MB | 7.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.89 MB | 3.98 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0409s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1077s | 0.1112s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0782s | -0.0026s | improved |
| `lteNRRCC` | 0.1378s | 0.1508s | -0.0130s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 7.79 MB | 158.4% | 99.8% |
| `f1ap_rel18.6_specs` | 8.14 MB | 8.52 MB | 161.2% | 104.0% |
| `ngap_rel18.6_specs` | 8.14 MB | 7.89 MB | 91.1% | 156.2% |
| `lteNRRCC` | 51.80 MB | 70.52 MB | 155.5% | 110.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0409s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1212s | -0.0107s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0813s | -0.0045s | improved |
| `lteNRRCC` | 0.1291s | 0.1360s | -0.0069s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.13 MB | 8.63 MB | 0.0% | 163.8% |
| `f1ap_rel18.6_specs` | 9.59 MB | 9.78 MB | 155.7% | 78.2% |
| `ngap_rel18.6_specs` | 10.66 MB | 10.16 MB | 108.1% | 99.5% |
| `lteNRRCC` | 9.21 MB | 83.18 MB | 107.6% | 168.2% |
<!-- BENCH_RESULTS_END -->
