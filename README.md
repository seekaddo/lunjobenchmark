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
Generated: 2026-05-15T12:00:26.195545+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0369s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1139s | 0.1120s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0784s | 0.0769s | +0.0015s | worse |
| `lteNRRCC` | 0.1236s | 0.1204s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 8.4% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 116.0% | 105.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 105.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0354s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0962s | 0.0937s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0665s | 0.0662s | +0.0003s | worse |
| `lteNRRCC` | 0.1179s | 0.1290s | -0.0111s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.32 MB | 36.54 MB | 83.3% | 112.0% |
| `f1ap_rel18.6_specs` | 21.68 MB | 102.95 MB | 106.9% | 103.5% |
| `ngap_rel18.6_specs` | 16.62 MB | 74.21 MB | 108.7% | 107.1% |
| `lteNRRCC` | 48.66 MB | 66.27 MB | 103.6% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0343s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0989s | 0.0988s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0682s | 0.0692s | -0.0010s | improved |
| `lteNRRCC` | 0.1163s | 0.1150s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.35 MB | 55.49 MB | 90.5% | 107.7% |
| `f1ap_rel18.6_specs` | 35.18 MB | 164.53 MB | 111.1% | 103.4% |
| `ngap_rel18.6_specs` | 23.93 MB | 117.82 MB | 109.5% | 102.3% |
| `lteNRRCC` | 74.71 MB | 102.55 MB | 103.6% | 104.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0131s | 0.0353s | -0.0222s | improved |
| `f1ap_rel18.6_specs` | 0.0679s | 0.0657s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0457s | 0.0438s | +0.0019s | worse |
| `lteNRRCC` | 0.0850s | 0.0780s | +0.0070s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.77 MB | 4.31 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.59 MB | 4.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.78 MB | 7.31 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.47 MB | 3.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0407s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1138s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0762s | +0.0000s | flat |
| `lteNRRCC` | 0.1423s | 0.1398s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.70 MB | 7.74 MB | 165.6% | 168.2% |
| `f1ap_rel18.6_specs` | 8.68 MB | 106.65 MB | 100.8% | 167.7% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.06 MB | 83.6% | 83.6% |
| `lteNRRCC` | 51.53 MB | 69.18 MB | 173.6% | 165.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0453s | 0.0390s | +0.0063s | worse |
| `f1ap_rel18.6_specs` | 0.1216s | 0.1082s | +0.0134s | worse |
| `ngap_rel18.6_specs` | 0.0848s | 0.0825s | +0.0023s | worse |
| `lteNRRCC` | 0.1410s | 0.1281s | +0.0129s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.66 MB | 9.56 MB | 148.8% | 79.8% |
| `f1ap_rel18.6_specs` | 10.25 MB | 142.86 MB | 79.9% | 107.1% |
| `ngap_rel18.6_specs` | 9.35 MB | 10.20 MB | 158.5% | 156.6% |
| `lteNRRCC` | 68.18 MB | 101.72 MB | 160.0% | 159.8% |
<!-- BENCH_RESULTS_END -->
