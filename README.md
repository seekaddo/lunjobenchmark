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
Generated: 2026-10-06T02:09:26.454335+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0347s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1070s | 0.1091s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0751s | +0.0001s | worse |
| `lteNRRCC` | 0.1184s | 0.1185s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 81.0% | 100.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.7% | 103.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0251s | +0.0118s | worse |
| `f1ap_rel18.6_specs` | 0.1006s | 0.0708s | +0.0298s | worse |
| `ngap_rel18.6_specs` | 0.0693s | 0.0491s | +0.0202s | worse |
| `lteNRRCC` | 0.1349s | 0.0900s | +0.0449s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.40 MB | 36.39 MB | 75.9% | 103.7% |
| `f1ap_rel18.6_specs` | 22.04 MB | 103.31 MB | 103.1% | 103.4% |
| `ngap_rel18.6_specs` | 18.04 MB | 74.63 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.35 MB | 66.54 MB | 103.1% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0356s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0998s | 0.0950s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0666s | +0.0026s | worse |
| `lteNRRCC` | 0.1167s | 0.1215s | -0.0048s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 55.37 MB | 77.3% | 104.0% |
| `f1ap_rel18.6_specs` | 34.65 MB | 164.60 MB | 103.8% | 101.8% |
| `ngap_rel18.6_specs` | 24.00 MB | 117.81 MB | 110.0% | 102.4% |
| `lteNRRCC` | 74.15 MB | 102.09 MB | 101.9% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0315s | +0.0053s | worse |
| `f1ap_rel18.6_specs` | 0.0985s | 0.1053s | -0.0068s | improved |
| `ngap_rel18.6_specs` | 0.0915s | 0.0689s | +0.0226s | worse |
| `lteNRRCC` | 0.0914s | 0.1218s | -0.0304s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.80 MB | 5.30 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.56 MB | 8.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.36 MB | 7.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.39 MB | 3.83 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0286s | 0.0398s | -0.0112s | improved |
| `f1ap_rel18.6_specs` | 0.0774s | 0.1092s | -0.0318s | improved |
| `ngap_rel18.6_specs` | 0.0554s | 0.0766s | -0.0212s | improved |
| `lteNRRCC` | 0.0919s | 0.1295s | -0.0376s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.30 MB | 22.06 MB | 0.0% | 156.0% |
| `f1ap_rel18.6_specs` | 21.05 MB | 14.42 MB | 115.2% | 89.0% |
| `ngap_rel18.6_specs` | 11.35 MB | 42.34 MB | 111.7% | 122.4% |
| `lteNRRCC` | 13.19 MB | 18.96 MB | 85.5% | 128.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0400s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1170s | 0.1129s | +0.0041s | worse |
| `ngap_rel18.6_specs` | 0.0855s | 0.0825s | +0.0030s | worse |
| `lteNRRCC` | 0.1304s | 0.1275s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.15 MB | 11.52 MB | 0.0% | 195.7% |
| `f1ap_rel18.6_specs` | 10.05 MB | 164.18 MB | 158.4% | 108.0% |
| `ngap_rel18.6_specs` | 9.54 MB | 9.40 MB | 144.5% | 146.0% |
| `lteNRRCC` | 9.23 MB | 98.73 MB | 97.3% | 149.8% |
<!-- BENCH_RESULTS_END -->
