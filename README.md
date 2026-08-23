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
Generated: 2026-08-23T22:28:20.531043+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0343s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1178s | 0.1081s | +0.0097s | worse |
| `ngap_rel18.6_specs` | 0.0806s | 0.0738s | +0.0068s | worse |
| `lteNRRCC` | 0.1250s | 0.1182s | +0.0068s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 25.3% | 103.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 103.8% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0242s | 0.0319s | -0.0077s | improved |
| `f1ap_rel18.6_specs` | 0.0741s | 0.0939s | -0.0198s | improved |
| `ngap_rel18.6_specs` | 0.0487s | 0.0645s | -0.0158s | improved |
| `lteNRRCC` | 0.0845s | 0.1159s | -0.0314s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.78 MB | 36.58 MB | 6.3% | 105.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.46 MB | 100.0% | 100.0% |
| `ngap_rel18.6_specs` | 18.06 MB | 74.69 MB | 100.0% | 103.1% |
| `lteNRRCC` | 48.50 MB | 65.33 MB | 100.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0372s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.0904s | 0.0978s | -0.0074s | improved |
| `ngap_rel18.6_specs` | 0.0617s | 0.0695s | -0.0078s | improved |
| `lteNRRCC` | 0.1163s | 0.1296s | -0.0133s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.89 MB | 73.1% | 107.7% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.70 MB | 103.6% | 103.7% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.59 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.73 MB | 102.97 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0303s | 0.0215s | +0.0088s | worse |
| `f1ap_rel18.6_specs` | 0.0782s | 0.0842s | -0.0060s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0677s | +0.0066s | worse |
| `lteNRRCC` | 0.1089s | 0.0854s | +0.0235s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.16 MB | 5.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.95 MB | 5.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.53 MB | 7.55 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.22 MB | 4.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0392s | -0.0060s | improved |
| `f1ap_rel18.6_specs` | 0.0879s | 0.1083s | -0.0204s | improved |
| `ngap_rel18.6_specs` | 0.0660s | 0.0744s | -0.0084s | improved |
| `lteNRRCC` | 0.0944s | 0.1388s | -0.0444s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.39 MB | 8.19 MB | 142.4% | 155.0% |
| `f1ap_rel18.6_specs` | 8.30 MB | 102.01 MB | 149.5% | 132.5% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.06 MB | 113.2% | 151.8% |
| `lteNRRCC` | 8.24 MB | 63.54 MB | 155.3% | 143.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0457s | -0.0056s | improved |
| `f1ap_rel18.6_specs` | 0.1135s | 0.1353s | -0.0218s | improved |
| `ngap_rel18.6_specs` | 0.0824s | 0.0912s | -0.0088s | improved |
| `lteNRRCC` | 0.1283s | 0.1437s | -0.0154s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.48 MB | 8.59 MB | 104.8% | 179.1% |
| `f1ap_rel18.6_specs` | 11.14 MB | 118.96 MB | 101.3% | 197.2% |
| `ngap_rel18.6_specs` | 9.15 MB | 9.21 MB | 88.7% | 156.6% |
| `lteNRRCC` | 9.43 MB | 98.59 MB | 109.8% | 152.5% |
<!-- BENCH_RESULTS_END -->
