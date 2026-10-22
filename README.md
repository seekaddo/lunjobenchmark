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
Generated: 2026-10-22T14:59:51.810817+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0392s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1217s | -0.0113s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0845s | -0.0075s | improved |
| `lteNRRCC` | 0.1197s | 0.1264s | -0.0067s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 79.2% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0294s | 0.0383s | -0.0089s | improved |
| `f1ap_rel18.6_specs` | 0.0909s | 0.1157s | -0.0248s | improved |
| `ngap_rel18.6_specs` | 0.0643s | 0.0804s | -0.0161s | improved |
| `lteNRRCC` | 0.0955s | 0.1303s | -0.0348s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 34.65 MB | 71.4% | 104.3% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 104.3% | 101.8% |
| `ngap_rel18.6_specs` | 18.04 MB | 72.65 MB | 105.3% | 102.4% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 100.0% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0431s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0968s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0646s | 0.0671s | -0.0025s | improved |
| `lteNRRCC` | 0.1204s | 0.1297s | -0.0093s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.55 MB | 77.8% | 107.4% |
| `f1ap_rel18.6_specs` | 35.11 MB | 164.37 MB | 106.9% | 100.0% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.79 MB | 104.2% | 102.3% |
| `lteNRRCC` | 74.14 MB | 102.45 MB | 103.4% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0270s | 0.0518s | -0.0248s | improved |
| `f1ap_rel18.6_specs` | 0.0752s | 0.0917s | -0.0165s | improved |
| `ngap_rel18.6_specs` | 0.0502s | 0.0704s | -0.0202s | improved |
| `lteNRRCC` | 0.0826s | 0.0760s | +0.0066s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.02 MB | 5.17 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.72 MB | 2.44 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.12 MB | 2.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.33 MB | 912 KB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0334s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.0981s | 0.0955s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0655s | +0.0012s | worse |
| `lteNRRCC` | 0.1065s | 0.1133s | -0.0068s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.30 MB | 7.94 MB | 0.0% | 134.4% |
| `f1ap_rel18.6_specs` | 8.55 MB | 106.61 MB | 133.6% | 133.8% |
| `ngap_rel18.6_specs` | 8.16 MB | 8.20 MB | 133.6% | 133.4% |
| `lteNRRCC` | 8.40 MB | 55.29 MB | 195.5% | 134.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0393s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1171s | 0.1128s | +0.0043s | worse |
| `ngap_rel18.6_specs` | 0.0807s | 0.0771s | +0.0036s | worse |
| `lteNRRCC` | 0.1311s | 0.1291s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.01 MB | 0.0% | 95.3% |
| `f1ap_rel18.6_specs` | 10.35 MB | 12.06 MB | 148.9% | 194.0% |
| `ngap_rel18.6_specs` | 9.46 MB | 9.53 MB | 152.0% | 148.4% |
| `lteNRRCC` | 8.79 MB | 81.88 MB | 147.9% | 143.1% |
<!-- BENCH_RESULTS_END -->
