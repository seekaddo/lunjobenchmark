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
Generated: 2026-06-18T13:34:03.564264+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0340s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1120s | 0.1086s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0783s | 0.0743s | +0.0040s | worse |
| `lteNRRCC` | 0.1207s | 0.1175s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.91 MB | 53.55 MB | 22.3% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0343s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0958s | 0.0932s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0675s | 0.0666s | +0.0009s | worse |
| `lteNRRCC` | 0.1304s | 0.1278s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.17 MB | 36.55 MB | 82.1% | 107.1% |
| `f1ap_rel18.6_specs` | 21.82 MB | 102.96 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.47 MB | 111.5% | 106.8% |
| `lteNRRCC` | 48.47 MB | 66.53 MB | 103.1% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0349s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0907s | +0.0035s | worse |
| `ngap_rel18.6_specs` | 0.0640s | 0.0634s | +0.0006s | worse |
| `lteNRRCC` | 0.1178s | 0.1180s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.40 MB | 55.82 MB | 16.8% | 111.1% |
| `f1ap_rel18.6_specs` | 34.44 MB | 164.74 MB | 110.3% | 103.6% |
| `ngap_rel18.6_specs` | 24.57 MB | 117.64 MB | 108.0% | 107.1% |
| `lteNRRCC` | 74.46 MB | 102.00 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0236s | 0.0213s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0803s | 0.0770s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0529s | +0.0138s | worse |
| `lteNRRCC` | 0.0829s | 0.0911s | -0.0082s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.70 MB | 6.08 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.73 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.45 MB | 5.89 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.45 MB | 3.45 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0339s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.1093s | 0.0942s | +0.0151s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0677s | +0.0099s | worse |
| `lteNRRCC` | 0.1377s | 0.1143s | +0.0234s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.57 MB | 7.37 MB | 104.8% | 164.5% |
| `f1ap_rel18.6_specs` | 8.44 MB | 106.64 MB | 101.7% | 164.5% |
| `ngap_rel18.6_specs` | 7.38 MB | 7.62 MB | 165.2% | 79.4% |
| `lteNRRCC` | 49.12 MB | 69.23 MB | 107.0% | 156.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0437s | 0.0385s | +0.0052s | worse |
| `f1ap_rel18.6_specs` | 0.1275s | 0.1126s | +0.0149s | worse |
| `ngap_rel18.6_specs` | 0.0913s | 0.0752s | +0.0161s | worse |
| `lteNRRCC` | 0.1349s | 0.1295s | +0.0054s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.01 MB | 9.53 MB | 169.0% | 162.4% |
| `f1ap_rel18.6_specs` | 10.17 MB | 10.00 MB | 162.8% | 92.3% |
| `ngap_rel18.6_specs` | 10.62 MB | 10.25 MB | 105.9% | 101.0% |
| `lteNRRCC` | 8.98 MB | 8.75 MB | 157.4% | 101.6% |
<!-- BENCH_RESULTS_END -->
