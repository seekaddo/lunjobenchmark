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
Generated: 2026-07-29T23:03:35.988591+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0367s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1127s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0775s | -0.0020s | improved |
| `lteNRRCC` | 0.1198s | 0.1214s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 16.8% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0348s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.0972s | 0.0933s | +0.0039s | worse |
| `ngap_rel18.6_specs` | 0.0686s | 0.0651s | +0.0035s | worse |
| `lteNRRCC` | 0.1325s | 0.1250s | +0.0075s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 36.36 MB | 78.6% | 107.4% |
| `f1ap_rel18.6_specs` | 22.04 MB | 103.10 MB | 106.2% | 103.4% |
| `ngap_rel18.6_specs` | 17.57 MB | 73.82 MB | 107.7% | 104.5% |
| `lteNRRCC` | 47.65 MB | 66.38 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0333s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.1013s | 0.0898s | +0.0115s | worse |
| `ngap_rel18.6_specs` | 0.0696s | 0.0629s | +0.0067s | worse |
| `lteNRRCC` | 0.1173s | 0.1174s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.31 MB | 55.85 MB | 45.2% | 103.8% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.62 MB | 103.7% | 101.7% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.86 MB | 104.8% | 104.8% |
| `lteNRRCC` | 74.64 MB | 102.95 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0236s | 0.0679s | -0.0443s | improved |
| `f1ap_rel18.6_specs` | 0.0957s | 0.0954s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0613s | 0.0697s | -0.0084s | improved |
| `lteNRRCC` | 0.0868s | 0.1073s | -0.0205s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.11 MB | 8.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.23 MB | 9.92 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.84 MB | 8.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 1.06 MB | 7.45 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0383s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1067s | 0.1049s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0756s | 0.0730s | +0.0026s | worse |
| `lteNRRCC` | 0.1385s | 0.1370s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.76 MB | 7.50 MB | 221.7% | 161.3% |
| `f1ap_rel18.6_specs` | 7.91 MB | 8.11 MB | 185.7% | 163.8% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.61 MB | 162.4% | 160.7% |
| `lteNRRCC` | 45.26 MB | 57.69 MB | 198.4% | 110.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0425s | 0.0397s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1216s | 0.1136s | +0.0080s | worse |
| `ngap_rel18.6_specs` | 0.0870s | 0.0804s | +0.0066s | worse |
| `lteNRRCC` | 0.1391s | 0.1283s | +0.0108s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.29 MB | 9.02 MB | 0.0% | 163.2% |
| `f1ap_rel18.6_specs` | 10.91 MB | 164.20 MB | 216.0% | 163.7% |
| `ngap_rel18.6_specs` | 10.38 MB | 9.49 MB | 216.8% | 159.6% |
| `lteNRRCC` | 73.35 MB | 98.70 MB | 104.1% | 105.3% |
<!-- BENCH_RESULTS_END -->
