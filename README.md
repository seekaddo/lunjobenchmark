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
Generated: 2026-09-15T00:25:55.602486+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0368s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1069s | 0.1157s | -0.0088s | improved |
| `ngap_rel18.6_specs` | 0.0737s | 0.0786s | -0.0049s | improved |
| `lteNRRCC` | 0.1164s | 0.1230s | -0.0066s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 62.1% | 107.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0346s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0982s | 0.0938s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0677s | 0.0659s | +0.0018s | worse |
| `lteNRRCC` | 0.1196s | 0.1293s | -0.0097s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 35.88 MB | 81.0% | 104.2% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.15 MB | 103.7% | 103.6% |
| `ngap_rel18.6_specs` | 18.08 MB | 73.95 MB | 100.0% | 100.0% |
| `lteNRRCC` | 48.39 MB | 66.54 MB | 103.6% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0365s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0957s | 0.0915s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0668s | 0.0667s | +0.0001s | worse |
| `lteNRRCC` | 0.1209s | 0.1217s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.41 MB | 80.8% | 103.4% |
| `f1ap_rel18.6_specs` | 34.48 MB | 164.20 MB | 106.7% | 103.4% |
| `ngap_rel18.6_specs` | 24.56 MB | 117.18 MB | 104.0% | 104.5% |
| `lteNRRCC` | 74.09 MB | 102.45 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0310s | 0.0345s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.0865s | 0.0998s | -0.0133s | improved |
| `ngap_rel18.6_specs` | 0.0672s | 0.0681s | -0.0009s | improved |
| `lteNRRCC` | 0.0943s | 0.1101s | -0.0158s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.25 MB | 8.88 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 688 KB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.61 MB | 9.94 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.25 MB | 7.52 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0421s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1185s | -0.0093s | improved |
| `ngap_rel18.6_specs` | 0.0772s | 0.0817s | -0.0045s | improved |
| `lteNRRCC` | 0.1378s | 0.1492s | -0.0114s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.43 MB | 7.96 MB | 221.5% | 225.9% |
| `f1ap_rel18.6_specs` | 8.76 MB | 8.54 MB | 113.8% | 224.8% |
| `ngap_rel18.6_specs` | 8.30 MB | 8.17 MB | 110.8% | 113.0% |
| `lteNRRCC` | 51.14 MB | 52.76 MB | 111.4% | 227.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0392s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1129s | 0.1098s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0769s | +0.0024s | worse |
| `lteNRRCC` | 0.1136s | 0.1273s | -0.0137s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.29 MB | 9.91 MB | 130.1% | 266.2% |
| `f1ap_rel18.6_specs` | 10.58 MB | 112.75 MB | 130.9% | 196.5% |
| `ngap_rel18.6_specs` | 10.32 MB | 10.20 MB | 132.9% | 131.3% |
| `lteNRRCC` | 9.25 MB | 74.16 MB | 135.0% | 131.4% |
<!-- BENCH_RESULTS_END -->
