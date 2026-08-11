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
Generated: 2026-08-11T10:55:54.228267+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0351s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1093s | 0.1088s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0741s | 0.0743s | -0.0002s | improved |
| `lteNRRCC` | 0.1188s | 0.1185s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 21.4% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.6% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0339s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0965s | 0.0954s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0671s | 0.0660s | +0.0011s | worse |
| `lteNRRCC` | 0.1177s | 0.1182s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 36.13 MB | 18.4% | 104.0% |
| `f1ap_rel18.6_specs` | 22.27 MB | 103.45 MB | 103.7% | 101.8% |
| `ngap_rel18.6_specs` | 17.65 MB | 74.26 MB | 109.5% | 102.4% |
| `lteNRRCC` | 48.45 MB | 66.19 MB | 101.8% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0353s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0900s | 0.0942s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0623s | 0.0649s | -0.0026s | improved |
| `lteNRRCC` | 0.1223s | 0.1204s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.29 MB | 55.70 MB | 80.0% | 103.8% |
| `f1ap_rel18.6_specs` | 34.04 MB | 163.71 MB | 103.6% | 103.7% |
| `ngap_rel18.6_specs` | 24.21 MB | 117.69 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.89 MB | 102.87 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0297s | 0.0218s | +0.0079s | worse |
| `f1ap_rel18.6_specs` | 0.0845s | 0.0772s | +0.0073s | worse |
| `ngap_rel18.6_specs` | 0.0574s | 0.0579s | -0.0005s | improved |
| `lteNRRCC` | 0.0861s | 0.0921s | -0.0060s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.36 MB | 4.31 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.80 MB | 7.83 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.47 MB | 8.20 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.67 MB | 9.58 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0426s | 0.0379s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.1150s | 0.1050s | +0.0100s | worse |
| `ngap_rel18.6_specs` | 0.0799s | 0.0727s | +0.0072s | worse |
| `lteNRRCC` | 0.1425s | 0.1398s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.89 MB | 0.0% | 79.9% |
| `f1ap_rel18.6_specs` | 8.45 MB | 105.55 MB | 162.5% | 165.2% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.17 MB | 101.7% | 181.4% |
| `lteNRRCC` | 51.83 MB | 69.16 MB | 156.3% | 107.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0437s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1153s | 0.1337s | -0.0184s | improved |
| `ngap_rel18.6_specs` | 0.0800s | 0.0902s | -0.0102s | improved |
| `lteNRRCC` | 0.1344s | 0.1413s | -0.0069s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.93 MB | 0.0% | 74.0% |
| `f1ap_rel18.6_specs` | 10.11 MB | 164.19 MB | 150.6% | 108.5% |
| `ngap_rel18.6_specs` | 9.33 MB | 11.25 MB | 148.2% | 89.3% |
| `lteNRRCC` | 7.87 MB | 96.00 MB | 177.4% | 104.0% |
<!-- BENCH_RESULTS_END -->
