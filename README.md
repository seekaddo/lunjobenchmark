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
Generated: 2026-06-11T23:42:42.813877+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0354s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1107s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0760s | -0.0004s | improved |
| `lteNRRCC` | 0.1195s | 0.1202s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 18.3% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 104.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0344s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0924s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0655s | +0.0012s | worse |
| `lteNRRCC` | 0.1177s | 0.1274s | -0.0097s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.42 MB | 36.23 MB | 16.2% | 108.0% |
| `f1ap_rel18.6_specs` | 22.22 MB | 103.38 MB | 103.6% | 103.6% |
| `ngap_rel18.6_specs` | 17.73 MB | 74.42 MB | 109.1% | 104.8% |
| `lteNRRCC` | 48.73 MB | 66.29 MB | 103.6% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0346s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0997s | -0.0044s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0694s | -0.0036s | improved |
| `lteNRRCC` | 0.1320s | 0.1184s | +0.0136s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 55.50 MB | 66.7% | 110.3% |
| `f1ap_rel18.6_specs` | 34.74 MB | 163.11 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 23.74 MB | 117.35 MB | 111.1% | 106.7% |
| `lteNRRCC` | 74.66 MB | 102.45 MB | 103.1% | 102.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0234s | 0.0222s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1027s | 0.0645s | +0.0382s | worse |
| `ngap_rel18.6_specs` | 0.0486s | 0.0449s | +0.0037s | worse |
| `lteNRRCC` | 0.1021s | 0.0789s | +0.0232s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.09 MB | 8.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 8.58 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.16 MB | 8.89 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.41 MB | 8.66 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0388s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1090s | 0.1053s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0734s | +0.0032s | worse |
| `lteNRRCC` | 0.1338s | 0.1364s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.11 MB | 7.75 MB | 230.7% | 187.6% |
| `f1ap_rel18.6_specs` | 8.10 MB | 8.86 MB | 119.5% | 111.6% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.18 MB | 107.8% | 164.3% |
| `lteNRRCC` | 8.66 MB | 70.55 MB | 117.7% | 159.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0460s | 0.0411s | +0.0049s | worse |
| `f1ap_rel18.6_specs` | 0.1263s | 0.1242s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0880s | 0.0857s | +0.0023s | worse |
| `lteNRRCC` | 0.1348s | 0.1405s | -0.0057s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.70 MB | 9.00 MB | 159.2% | 96.9% |
| `f1ap_rel18.6_specs` | 10.42 MB | 10.42 MB | 78.4% | 154.1% |
| `ngap_rel18.6_specs` | 9.34 MB | 9.91 MB | 154.5% | 79.4% |
| `lteNRRCC` | 8.80 MB | 9.15 MB | 78.4% | 79.4% |
<!-- BENCH_RESULTS_END -->
