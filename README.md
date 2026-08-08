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
Generated: 2026-08-08T22:35:54.433935+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0340s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1156s | 0.1087s | +0.0069s | worse |
| `ngap_rel18.6_specs` | 0.0795s | 0.0743s | +0.0052s | worse |
| `lteNRRCC` | 0.1228s | 0.1174s | +0.0054s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 59.4% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0373s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0951s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0644s | 0.0664s | -0.0020s | improved |
| `lteNRRCC` | 0.1277s | 0.1269s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.50 MB | 35.97 MB | 76.9% | 103.8% |
| `f1ap_rel18.6_specs` | 22.15 MB | 103.09 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.18 MB | 108.0% | 104.9% |
| `lteNRRCC` | 48.69 MB | 66.48 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0342s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0960s | 0.0903s | +0.0057s | worse |
| `ngap_rel18.6_specs` | 0.0669s | 0.0614s | +0.0055s | worse |
| `lteNRRCC` | 0.1292s | 0.1248s | +0.0044s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.34 MB | 68.8% | 107.1% |
| `f1ap_rel18.6_specs` | 35.19 MB | 164.16 MB | 103.2% | 101.7% |
| `ngap_rel18.6_specs` | 24.24 MB | 117.60 MB | 108.0% | 104.7% |
| `lteNRRCC` | 74.69 MB | 102.81 MB | 103.2% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0241s | 0.0218s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0710s | 0.0718s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0489s | 0.0498s | -0.0009s | improved |
| `lteNRRCC` | 0.0775s | 0.0793s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.36 MB | 4.30 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.36 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.52 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.61 MB | 4.45 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0394s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1089s | 0.1085s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0765s | 0.0761s | +0.0004s | worse |
| `lteNRRCC` | 0.1387s | 0.1409s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.77 MB | 7.34 MB | 0.0% | 82.2% |
| `f1ap_rel18.6_specs` | 7.88 MB | 8.48 MB | 166.3% | 239.2% |
| `ngap_rel18.6_specs` | 7.39 MB | 7.50 MB | 82.9% | 98.1% |
| `lteNRRCC` | 48.40 MB | 49.66 MB | 116.0% | 102.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0386s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1129s | 0.1162s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0767s | 0.0796s | -0.0029s | improved |
| `lteNRRCC` | 0.1275s | 0.1320s | -0.0045s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.72 MB | 0.0% | 100.1% |
| `f1ap_rel18.6_specs` | 10.06 MB | 9.55 MB | 95.6% | 163.8% |
| `ngap_rel18.6_specs` | 10.63 MB | 7.82 MB | 117.1% | 112.5% |
| `lteNRRCC` | 9.24 MB | 93.70 MB | 116.2% | 105.0% |
<!-- BENCH_RESULTS_END -->
