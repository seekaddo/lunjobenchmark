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
Generated: 2026-03-29T22:39:41.838175+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0366s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1146s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0796s | 0.0794s | +0.0002s | worse |
| `lteNRRCC` | 0.1239s | 0.1218s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.91 MB | 53.55 MB | 29.9% | 112.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0312s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0948s | 0.0922s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0648s | 0.0634s | +0.0014s | worse |
| `lteNRRCC` | 0.1164s | 0.1151s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.21 MB | 36.24 MB | 90.9% | 108.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.08 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 16.73 MB | 74.35 MB | 109.1% | 104.9% |
| `lteNRRCC` | 48.64 MB | 66.45 MB | 103.6% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0327s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0896s | 0.0897s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0621s | 0.0615s | +0.0006s | worse |
| `lteNRRCC` | 0.1167s | 0.1157s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.29 MB | 55.71 MB | 26.7% | 110.7% |
| `f1ap_rel18.6_specs` | 35.11 MB | 164.50 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 23.61 MB | 117.45 MB | 112.5% | 107.1% |
| `lteNRRCC` | 74.78 MB | 102.93 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0255s | 0.0204s | +0.0051s | worse |
| `f1ap_rel18.6_specs` | 0.0651s | 0.0601s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0442s | 0.0401s | +0.0041s | worse |
| `lteNRRCC` | 0.0744s | 0.0701s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.61 MB | 3.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.94 MB | 448 KB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.38 MB | 4.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.20 MB | 4.23 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0400s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1054s | 0.1096s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0723s | 0.0795s | -0.0072s | improved |
| `lteNRRCC` | 0.1384s | 0.1283s | +0.0101s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.30 MB | 7.29 MB | 176.7% | 166.3% |
| `f1ap_rel18.6_specs` | 8.03 MB | 106.64 MB | 84.7% | 115.9% |
| `ngap_rel18.6_specs` | 8.17 MB | 7.54 MB | 118.2% | 166.4% |
| `lteNRRCC` | 47.62 MB | 51.07 MB | 106.3% | 165.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0384s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1106s | +0.0041s | worse |
| `ngap_rel18.6_specs` | 0.0774s | 0.0764s | +0.0010s | worse |
| `lteNRRCC` | 0.1267s | 0.1254s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.45 MB | 9.00 MB | 97.1% | 152.2% |
| `f1ap_rel18.6_specs` | 10.94 MB | 10.57 MB | 230.9% | 106.8% |
| `ngap_rel18.6_specs` | 8.77 MB | 13.39 MB | 172.7% | 195.1% |
| `lteNRRCC` | 72.59 MB | 72.71 MB | 162.1% | 157.1% |
<!-- BENCH_RESULTS_END -->
