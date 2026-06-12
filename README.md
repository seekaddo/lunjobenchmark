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
Generated: 2026-06-12T13:32:00.478538+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0353s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1106s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0756s | -0.0013s | improved |
| `lteNRRCC` | 0.1187s | 0.1195s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 20.2% | 111.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 106.4% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0341s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0951s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0667s | -0.0013s | improved |
| `lteNRRCC` | 0.1250s | 0.1177s | +0.0073s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.58 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 22.17 MB | 103.49 MB | 109.4% | 103.5% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.54 MB | 111.5% | 109.3% |
| `lteNRRCC` | 48.07 MB | 64.88 MB | 106.5% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0367s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0953s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0658s | -0.0006s | improved |
| `lteNRRCC` | 0.1274s | 0.1320s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.61 MB | 95.8% | 110.3% |
| `f1ap_rel18.6_specs` | 34.20 MB | 164.60 MB | 106.2% | 105.3% |
| `ngap_rel18.6_specs` | 24.27 MB | 117.86 MB | 111.5% | 107.0% |
| `lteNRRCC` | 74.93 MB | 102.91 MB | 104.8% | 104.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0234s | +0.0093s | worse |
| `f1ap_rel18.6_specs` | 0.0826s | 0.1027s | -0.0201s | improved |
| `ngap_rel18.6_specs` | 0.0459s | 0.0486s | -0.0027s | improved |
| `lteNRRCC` | 0.0804s | 0.1021s | -0.0217s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.95 MB | 4.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.64 MB | 9.28 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.42 MB | 9.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 4.89 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0422s | 0.0400s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1090s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0819s | 0.0766s | +0.0053s | worse |
| `lteNRRCC` | 0.1426s | 0.1338s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.58 MB | 7.32 MB | 151.6% | 185.4% |
| `f1ap_rel18.6_specs` | 8.25 MB | 106.66 MB | 77.0% | 143.5% |
| `ngap_rel18.6_specs` | 8.13 MB | 8.28 MB | 75.2% | 104.8% |
| `lteNRRCC` | 8.37 MB | 55.63 MB | 90.3% | 111.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0440s | 0.0460s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1227s | 0.1263s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0844s | 0.0880s | -0.0036s | improved |
| `lteNRRCC` | 0.1311s | 0.1348s | -0.0037s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.26 MB | 9.71 MB | 80.1% | 102.4% |
| `f1ap_rel18.6_specs` | 10.42 MB | 10.57 MB | 160.0% | 115.4% |
| `ngap_rel18.6_specs` | 10.50 MB | 9.41 MB | 233.9% | 94.8% |
| `lteNRRCC` | 9.42 MB | 99.64 MB | 93.0% | 155.9% |
<!-- BENCH_RESULTS_END -->
