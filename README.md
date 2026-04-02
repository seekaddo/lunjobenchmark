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
Generated: 2026-04-02T10:59:41.450254+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0356s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1109s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0770s | +0.0005s | worse |
| `lteNRRCC` | 0.1206s | 0.1193s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 27.5% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0367s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0988s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0682s | 0.0697s | -0.0015s | improved |
| `lteNRRCC` | 0.1297s | 0.1338s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.15 MB | 36.36 MB | 88.9% | 110.3% |
| `f1ap_rel18.6_specs` | 22.38 MB | 103.30 MB | 105.9% | 105.2% |
| `ngap_rel18.6_specs` | 16.85 MB | 74.38 MB | 114.8% | 106.8% |
| `lteNRRCC` | 48.64 MB | 66.53 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0326s | 0.0323s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0874s | 0.0883s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0611s | 0.0615s | -0.0004s | improved |
| `lteNRRCC` | 0.1159s | 0.1148s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.32 MB | 55.30 MB | 100.0% | 107.4% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.48 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.82 MB | 116.7% | 107.3% |
| `lteNRRCC` | 74.98 MB | 102.91 MB | 103.4% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0196s | 0.0194s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0634s | 0.0591s | +0.0043s | worse |
| `ngap_rel18.6_specs` | 0.0427s | 0.0404s | +0.0023s | worse |
| `lteNRRCC` | 0.0769s | 0.0677s | +0.0092s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.88 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.70 MB | 4.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.00 MB | 3.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0394s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1061s | 0.1043s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0725s | +0.0064s | worse |
| `lteNRRCC` | 0.1394s | 0.1346s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.34 MB | 109.6% | 165.7% |
| `f1ap_rel18.6_specs` | 8.02 MB | 8.02 MB | 164.8% | 83.1% |
| `ngap_rel18.6_specs` | 7.60 MB | 7.54 MB | 165.6% | 164.5% |
| `lteNRRCC` | 46.18 MB | 50.86 MB | 107.3% | 163.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0378s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1134s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0779s | 0.0776s | +0.0003s | worse |
| `lteNRRCC` | 0.1255s | 0.1249s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.14 MB | 10.45 MB | 116.9% | 116.5% |
| `f1ap_rel18.6_specs` | 11.32 MB | 164.18 MB | 118.1% | 165.1% |
| `ngap_rel18.6_specs` | 10.75 MB | 8.95 MB | 119.9% | 162.7% |
| `lteNRRCC` | 73.14 MB | 98.74 MB | 109.6% | 116.8% |
<!-- BENCH_RESULTS_END -->
