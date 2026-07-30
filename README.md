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
Generated: 2026-07-30T11:56:02.518745+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0355s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1082s | 0.1108s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0741s | 0.0755s | -0.0014s | improved |
| `lteNRRCC` | 0.1191s | 0.1198s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 78.3% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0280s | 0.0377s | -0.0097s | improved |
| `f1ap_rel18.6_specs` | 0.0756s | 0.0972s | -0.0216s | improved |
| `ngap_rel18.6_specs` | 0.0529s | 0.0686s | -0.0157s | improved |
| `lteNRRCC` | 0.0993s | 0.1325s | -0.0332s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.11 MB | 36.15 MB | 61.3% | 104.5% |
| `f1ap_rel18.6_specs` | 22.42 MB | 103.17 MB | 108.3% | 100.0% |
| `ngap_rel18.6_specs` | 19.11 MB | 74.48 MB | 105.0% | 102.9% |
| `lteNRRCC` | 47.95 MB | 66.32 MB | 102.1% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0366s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.0927s | 0.1013s | -0.0086s | improved |
| `ngap_rel18.6_specs` | 0.0666s | 0.0696s | -0.0030s | improved |
| `lteNRRCC` | 0.1192s | 0.1173s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.12 MB | 55.78 MB | 18.3% | 103.7% |
| `f1ap_rel18.6_specs` | 34.76 MB | 164.66 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.47 MB | 117.68 MB | 104.2% | 104.9% |
| `lteNRRCC` | 74.95 MB | 102.91 MB | 103.5% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0239s | 0.0236s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0653s | 0.0957s | -0.0304s | improved |
| `ngap_rel18.6_specs` | 0.0447s | 0.0613s | -0.0166s | improved |
| `lteNRRCC` | 0.0824s | 0.0868s | -0.0044s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.81 MB | 7.80 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.61 MB | 3.91 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.94 MB | 4.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.58 MB | 8.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0396s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1067s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0756s | +0.0010s | worse |
| `lteNRRCC` | 0.1394s | 0.1385s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.46 MB | 7.62 MB | 87.5% | 156.7% |
| `f1ap_rel18.6_specs` | 8.36 MB | 8.73 MB | 96.4% | 100.6% |
| `ngap_rel18.6_specs` | 7.98 MB | 8.11 MB | 155.0% | 149.8% |
| `lteNRRCC` | 8.66 MB | 50.08 MB | 216.0% | 110.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0455s | 0.0425s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.1232s | 0.1216s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0863s | 0.0870s | -0.0007s | improved |
| `lteNRRCC` | 0.1384s | 0.1391s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.04 MB | 9.78 MB | 0.0% | 156.7% |
| `f1ap_rel18.6_specs` | 11.39 MB | 164.19 MB | 108.4% | 209.7% |
| `ngap_rel18.6_specs` | 10.50 MB | 11.26 MB | 90.6% | 106.9% |
| `lteNRRCC` | 72.18 MB | 101.70 MB | 152.5% | 145.3% |
<!-- BENCH_RESULTS_END -->
