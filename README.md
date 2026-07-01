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
Generated: 2026-07-01T23:22:24.667275+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0353s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1113s | 0.1121s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0765s | 0.0769s | -0.0004s | improved |
| `lteNRRCC` | 0.1204s | 0.1204s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 23.5% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0362s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0963s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0662s | 0.0671s | -0.0009s | improved |
| `lteNRRCC` | 0.1297s | 0.1293s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.12 MB | 36.68 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 22.01 MB | 102.89 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.48 MB | 74.28 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.52 MB | 65.95 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0324s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0915s | 0.0882s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0639s | 0.0615s | +0.0024s | worse |
| `lteNRRCC` | 0.1166s | 0.1144s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.15 MB | 55.52 MB | 84.6% | 107.4% |
| `f1ap_rel18.6_specs` | 35.17 MB | 164.66 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 24.41 MB | 117.58 MB | 108.3% | 107.3% |
| `lteNRRCC` | 74.20 MB | 102.74 MB | 105.3% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0234s | 0.0238s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0682s | 0.0712s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0472s | 0.0475s | -0.0003s | improved |
| `lteNRRCC` | 0.0782s | 0.0785s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.45 MB | 3.81 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.61 MB | 3.08 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.27 MB | 5.50 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.27 MB | 4.25 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0397s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1069s | 0.1092s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0741s | 0.0762s | -0.0021s | improved |
| `lteNRRCC` | 0.1378s | 0.1390s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.50 MB | 79.8% | 161.4% |
| `f1ap_rel18.6_specs` | 8.17 MB | 106.64 MB | 81.7% | 105.5% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.48 MB | 163.0% | 163.1% |
| `lteNRRCC` | 49.18 MB | 69.42 MB | 162.5% | 107.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0380s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1071s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0732s | 0.0771s | -0.0039s | improved |
| `lteNRRCC` | 0.1267s | 0.1272s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.58 MB | 8.63 MB | 159.6% | 157.4% |
| `f1ap_rel18.6_specs` | 10.57 MB | 11.64 MB | 108.1% | 108.3% |
| `ngap_rel18.6_specs` | 9.08 MB | 9.08 MB | 161.7% | 158.7% |
| `lteNRRCC` | 8.68 MB | 81.27 MB | 157.6% | 106.1% |
<!-- BENCH_RESULTS_END -->
