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
Generated: 2026-06-06T11:39:24.932648+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0363s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1134s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0789s | -0.0023s | improved |
| `lteNRRCC` | 0.1221s | 0.1207s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 6.9% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0339s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0915s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0637s | 0.0641s | -0.0004s | improved |
| `lteNRRCC` | 0.1228s | 0.1228s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 36.39 MB | 96.0% | 110.7% |
| `f1ap_rel18.6_specs` | 22.33 MB | 103.27 MB | 106.1% | 107.0% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.64 MB | 111.1% | 107.0% |
| `lteNRRCC` | 48.75 MB | 66.49 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0336s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0905s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0670s | 0.0633s | +0.0037s | worse |
| `lteNRRCC` | 0.1280s | 0.1187s | +0.0093s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.71 MB | 92.6% | 113.3% |
| `f1ap_rel18.6_specs` | 35.12 MB | 163.66 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.63 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.27 MB | 101.79 MB | 104.7% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0326s | 0.0393s | -0.0067s | improved |
| `f1ap_rel18.6_specs` | 0.0692s | 0.0648s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0468s | 0.0594s | -0.0126s | improved |
| `lteNRRCC` | 0.0779s | 0.0777s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 4.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.02 MB | 8.89 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.45 MB | 3.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.88 MB | 3.95 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0448s | -0.0051s | improved |
| `f1ap_rel18.6_specs` | 0.1079s | 0.1226s | -0.0147s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0902s | -0.0146s | improved |
| `lteNRRCC` | 0.1381s | 0.1470s | -0.0089s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.36 MB | 79.1% | 78.8% |
| `f1ap_rel18.6_specs` | 8.38 MB | 8.17 MB | 157.1% | 146.2% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.57 MB | 157.8% | 163.8% |
| `lteNRRCC` | 51.32 MB | 51.57 MB | 153.8% | 104.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0360s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1072s | +0.0058s | worse |
| `ngap_rel18.6_specs` | 0.0761s | 0.0742s | +0.0019s | worse |
| `lteNRRCC` | 0.1265s | 0.1141s | +0.0124s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.01 MB | 8.87 MB | 152.5% | 76.9% |
| `f1ap_rel18.6_specs` | 9.75 MB | 11.05 MB | 167.5% | 228.9% |
| `ngap_rel18.6_specs` | 9.07 MB | 9.14 MB | 166.2% | 158.7% |
| `lteNRRCC` | 9.61 MB | 95.58 MB | 113.2% | 105.8% |
<!-- BENCH_RESULTS_END -->
