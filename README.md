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
Generated: 2026-08-12T22:49:24.355859+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0354s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1066s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0760s | 0.0741s | +0.0019s | worse |
| `lteNRRCC` | 0.1191s | 0.1180s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.44 MB | 53.55 MB | 77.3% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0284s | 0.0267s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0762s | 0.0755s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0550s | 0.0514s | +0.0036s | worse |
| `lteNRRCC` | 0.1019s | 0.0961s | +0.0058s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.39 MB | 36.62 MB | 48.6% | 105.0% |
| `f1ap_rel18.6_specs` | 22.41 MB | 102.96 MB | 108.7% | 100.0% |
| `ngap_rel18.6_specs` | 19.42 MB | 73.72 MB | 105.3% | 103.0% |
| `lteNRRCC` | 48.66 MB | 66.18 MB | 102.1% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0283s | 0.0284s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0760s | 0.0761s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0529s | 0.0587s | -0.0058s | improved |
| `lteNRRCC` | 0.1010s | 0.1015s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.20 MB | 55.66 MB | 12.8% | 100.0% |
| `f1ap_rel18.6_specs` | 34.58 MB | 163.63 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.66 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.80 MB | 102.93 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0212s | 0.0359s | -0.0147s | improved |
| `f1ap_rel18.6_specs` | 0.0662s | 0.0799s | -0.0137s | improved |
| `ngap_rel18.6_specs` | 0.0473s | 0.0446s | +0.0027s | worse |
| `lteNRRCC` | 0.0765s | 0.0764s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.27 MB | 4.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.53 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.55 MB | 4.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.83 MB | 4.25 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0385s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.0951s | 0.1060s | -0.0109s | improved |
| `ngap_rel18.6_specs` | 0.0660s | 0.0732s | -0.0072s | improved |
| `lteNRRCC` | 0.1160s | 0.1363s | -0.0203s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 8.06 MB | 0.0% | 198.7% |
| `f1ap_rel18.6_specs` | 9.41 MB | 106.62 MB | 249.4% | 196.9% |
| `ngap_rel18.6_specs` | 8.00 MB | 8.37 MB | 138.1% | 117.2% |
| `lteNRRCC` | 8.61 MB | 68.28 MB | 193.4% | 118.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0424s | 0.0415s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1242s | 0.1293s | -0.0051s | improved |
| `ngap_rel18.6_specs` | 0.0854s | 0.0839s | +0.0015s | worse |
| `lteNRRCC` | 0.1378s | 0.1406s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 9.26 MB | 0.0% | 164.6% |
| `f1ap_rel18.6_specs` | 9.93 MB | 156.23 MB | 175.4% | 164.7% |
| `ngap_rel18.6_specs` | 9.34 MB | 9.33 MB | 80.0% | 82.3% |
| `lteNRRCC` | 69.05 MB | 73.70 MB | 161.9% | 163.1% |
<!-- BENCH_RESULTS_END -->
