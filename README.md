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
Generated: 2026-07-17T11:25:21.221707+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0360s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1102s | 0.1109s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0752s | +0.0007s | worse |
| `lteNRRCC` | 0.1194s | 0.1198s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 19.6% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.2% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0264s | 0.0352s | -0.0088s | improved |
| `f1ap_rel18.6_specs` | 0.0725s | 0.0942s | -0.0217s | improved |
| `ngap_rel18.6_specs` | 0.0515s | 0.0665s | -0.0150s | improved |
| `lteNRRCC` | 0.0971s | 0.1296s | -0.0325s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.11 MB | 36.31 MB | 83.3% | 109.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.25 MB | 108.0% | 102.2% |
| `ngap_rel18.6_specs` | 19.20 MB | 74.45 MB | 109.5% | 105.9% |
| `lteNRRCC` | 48.63 MB | 66.40 MB | 104.2% | 103.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0348s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0885s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0635s | 0.0621s | +0.0014s | worse |
| `lteNRRCC` | 0.1182s | 0.1150s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.42 MB | 55.67 MB | 75.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.65 MB | 163.83 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.18 MB | 116.61 MB | 112.5% | 104.8% |
| `lteNRRCC` | 74.96 MB | 102.49 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0191s | +0.0224s | worse |
| `f1ap_rel18.6_specs` | 0.1121s | 0.0581s | +0.0540s | worse |
| `ngap_rel18.6_specs` | 0.0812s | 0.0397s | +0.0415s | worse |
| `lteNRRCC` | 0.1230s | 0.0672s | +0.0558s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.81 MB | 6.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.30 MB | 4.80 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.03 MB | 4.92 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.03 MB | 3.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0387s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1041s | +0.0057s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0733s | +0.0042s | worse |
| `lteNRRCC` | 0.1405s | 0.1362s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.60 MB | 7.81 MB | 94.7% | 100.2% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.11 MB | 160.2% | 78.9% |
| `ngap_rel18.6_specs` | 8.30 MB | 7.68 MB | 111.7% | 166.8% |
| `lteNRRCC` | 51.84 MB | 51.75 MB | 198.2% | 224.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0446s | 0.0377s | +0.0069s | worse |
| `f1ap_rel18.6_specs` | 0.1290s | 0.1051s | +0.0239s | worse |
| `ngap_rel18.6_specs` | 0.0873s | 0.0725s | +0.0148s | worse |
| `lteNRRCC` | 0.1439s | 0.1240s | +0.0199s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.84 MB | 10.52 MB | 102.9% | 211.5% |
| `f1ap_rel18.6_specs` | 11.26 MB | 148.97 MB | 108.9% | 106.8% |
| `ngap_rel18.6_specs` | 10.81 MB | 10.93 MB | 107.6% | 104.5% |
| `lteNRRCC` | 73.77 MB | 98.57 MB | 104.6% | 182.8% |
<!-- BENCH_RESULTS_END -->
