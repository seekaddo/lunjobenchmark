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
Generated: 2026-06-18T23:50:56.595700+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0363s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1094s | 0.1120s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0783s | -0.0027s | improved |
| `lteNRRCC` | 0.1193s | 0.1207s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 17.5% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.3% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0355s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0948s | 0.0958s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0669s | 0.0675s | -0.0006s | improved |
| `lteNRRCC` | 0.1257s | 0.1304s | -0.0047s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 35.97 MB | 23.4% | 110.3% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.07 MB | 112.5% | 105.2% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.27 MB | 110.7% | 106.8% |
| `lteNRRCC` | 48.72 MB | 65.82 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0350s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0942s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0668s | 0.0640s | +0.0028s | worse |
| `lteNRRCC` | 0.1290s | 0.1178s | +0.0112s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.71 MB | 92.3% | 106.7% |
| `f1ap_rel18.6_specs` | 35.17 MB | 164.71 MB | 109.4% | 105.0% |
| `ngap_rel18.6_specs` | 24.18 MB | 117.03 MB | 111.5% | 106.8% |
| `lteNRRCC` | 74.78 MB | 102.44 MB | 104.8% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0236s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0684s | 0.0803s | -0.0119s | improved |
| `ngap_rel18.6_specs` | 0.0479s | 0.0667s | -0.0188s | improved |
| `lteNRRCC` | 0.0782s | 0.0829s | -0.0047s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.56 MB | 4.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.19 MB | 4.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.17 MB | 4.48 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.33 MB | 4.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0395s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1093s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0776s | +0.0024s | worse |
| `lteNRRCC` | 0.1492s | 0.1377s | +0.0115s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.62 MB | 7.61 MB | 155.1% | 90.6% |
| `f1ap_rel18.6_specs` | 8.43 MB | 8.92 MB | 145.8% | 143.5% |
| `ngap_rel18.6_specs` | 7.98 MB | 7.86 MB | 153.5% | 155.0% |
| `lteNRRCC` | 48.00 MB | 51.33 MB | 153.2% | 155.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0437s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1275s | -0.0143s | improved |
| `ngap_rel18.6_specs` | 0.0779s | 0.0913s | -0.0134s | improved |
| `lteNRRCC` | 0.1298s | 0.1349s | -0.0051s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.78 MB | 8.58 MB | 221.2% | 79.6% |
| `f1ap_rel18.6_specs` | 9.68 MB | 11.20 MB | 93.0% | 111.6% |
| `ngap_rel18.6_specs` | 8.95 MB | 8.83 MB | 161.4% | 80.5% |
| `lteNRRCC` | 8.68 MB | 85.23 MB | 150.9% | 159.4% |
<!-- BENCH_RESULTS_END -->
