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
Generated: 2026-07-29T12:05:54.336512+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0351s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1119s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0769s | +0.0006s | worse |
| `lteNRRCC` | 0.1214s | 0.1201s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.61 MB | 53.55 MB | 18.0% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0350s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0939s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0651s | 0.0667s | -0.0016s | improved |
| `lteNRRCC` | 0.1250s | 0.1301s | -0.0051s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 36.65 MB | 77.8% | 107.1% |
| `f1ap_rel18.6_specs` | 22.43 MB | 102.95 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.65 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.44 MB | 65.80 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0293s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.0898s | 0.0774s | +0.0124s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0547s | +0.0082s | worse |
| `lteNRRCC` | 0.1174s | 0.1025s | +0.0149s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 54.98 MB | 82.6% | 103.8% |
| `f1ap_rel18.6_specs` | 34.21 MB | 163.79 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 23.84 MB | 117.73 MB | 104.3% | 104.9% |
| `lteNRRCC` | 74.23 MB | 102.77 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0679s | 0.0562s | +0.0117s | worse |
| `f1ap_rel18.6_specs` | 0.0954s | 0.0933s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0697s | 0.0560s | +0.0137s | worse |
| `lteNRRCC` | 0.1073s | 0.1002s | +0.0071s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.44 MB | 8.11 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.94 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.20 MB | 6.86 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.23 MB | 6.00 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0417s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.1049s | 0.1189s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0730s | 0.0811s | -0.0081s | improved |
| `lteNRRCC` | 0.1370s | 0.1452s | -0.0082s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.82 MB | 7.37 MB | 112.7% | 169.2% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.05 MB | 166.5% | 80.2% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.55 MB | 105.2% | 171.3% |
| `lteNRRCC` | 50.75 MB | 70.55 MB | 167.9% | 162.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0466s | -0.0069s | improved |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1192s | -0.0056s | improved |
| `ngap_rel18.6_specs` | 0.0804s | 0.0853s | -0.0049s | improved |
| `lteNRRCC` | 0.1283s | 0.1178s | +0.0105s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.54 MB | 10.66 MB | 0.0% | 221.2% |
| `f1ap_rel18.6_specs` | 11.21 MB | 11.33 MB | 114.7% | 235.2% |
| `ngap_rel18.6_specs` | 10.46 MB | 8.90 MB | 115.3% | 81.5% |
| `lteNRRCC` | 8.50 MB | 82.83 MB | 172.3% | 107.0% |
<!-- BENCH_RESULTS_END -->
