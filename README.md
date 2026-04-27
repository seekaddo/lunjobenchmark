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
Generated: 2026-04-27T22:58:48.717405+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0355s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1122s | 0.1121s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0766s | +0.0010s | worse |
| `lteNRRCC` | 0.1211s | 0.1209s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.82 MB | 53.55 MB | 8.0% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0265s | 0.0363s | -0.0098s | improved |
| `f1ap_rel18.6_specs` | 0.0727s | 0.0969s | -0.0242s | improved |
| `ngap_rel18.6_specs` | 0.0510s | 0.0677s | -0.0167s | improved |
| `lteNRRCC` | 0.0962s | 0.1316s | -0.0354s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.74 MB | 36.46 MB | 86.4% | 109.1% |
| `f1ap_rel18.6_specs` | 22.17 MB | 103.45 MB | 108.0% | 106.7% |
| `ngap_rel18.6_specs` | 16.82 MB | 74.11 MB | 109.5% | 105.7% |
| `lteNRRCC` | 48.58 MB | 65.93 MB | 104.1% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0338s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0929s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0632s | 0.0634s | -0.0002s | improved |
| `lteNRRCC` | 0.1157s | 0.1188s | -0.0031s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.41 MB | 92.0% | 114.8% |
| `f1ap_rel18.6_specs` | 34.61 MB | 163.86 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 24.27 MB | 117.34 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.96 MB | 102.62 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0286s | +0.0062s | worse |
| `f1ap_rel18.6_specs` | 0.0820s | 0.1032s | -0.0212s | improved |
| `ngap_rel18.6_specs` | 0.0543s | 0.0723s | -0.0180s | improved |
| `lteNRRCC` | 0.0971s | 0.1038s | -0.0067s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.09 MB | 9.38 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.16 MB | 7.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.56 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.78 MB | 4.17 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0386s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1084s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0765s | 0.0733s | +0.0032s | worse |
| `lteNRRCC` | 0.1438s | 0.1361s | +0.0077s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.43 MB | 80.8% | 157.2% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.10 MB | 164.4% | 81.7% |
| `ngap_rel18.6_specs` | 8.17 MB | 7.98 MB | 228.3% | 93.4% |
| `lteNRRCC` | 50.80 MB | 69.21 MB | 159.0% | 160.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0357s | +0.0037s | worse |
| `f1ap_rel18.6_specs` | 0.1048s | 0.0995s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0753s | 0.0726s | +0.0027s | worse |
| `lteNRRCC` | 0.1242s | 0.1128s | +0.0114s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.52 MB | 10.40 MB | 164.3% | 118.8% |
| `f1ap_rel18.6_specs` | 10.64 MB | 164.20 MB | 110.6% | 107.9% |
| `ngap_rel18.6_specs` | 8.77 MB | 10.65 MB | 81.3% | 119.0% |
| `lteNRRCC` | 9.30 MB | 73.88 MB | 235.4% | 108.2% |
<!-- BENCH_RESULTS_END -->
