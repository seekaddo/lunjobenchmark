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
Generated: 2026-05-29T12:50:04.900330+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0366s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1171s | 0.1153s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0795s | -0.0007s | improved |
| `lteNRRCC` | 0.1253s | 0.1234s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 26.1% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 105.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 107.4% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 103.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0341s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0916s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0654s | 0.0645s | +0.0009s | worse |
| `lteNRRCC` | 0.1253s | 0.1243s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.00 MB | 85.7% | 110.3% |
| `f1ap_rel18.6_specs` | 22.00 MB | 103.12 MB | 109.1% | 106.9% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.52 MB | 111.1% | 109.1% |
| `lteNRRCC` | 48.42 MB | 65.75 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0350s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0923s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0674s | 0.0638s | +0.0036s | worse |
| `lteNRRCC` | 0.1292s | 0.1186s | +0.0106s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.60 MB | 24.8% | 113.3% |
| `f1ap_rel18.6_specs` | 35.12 MB | 164.61 MB | 109.1% | 106.8% |
| `ngap_rel18.6_specs` | 24.30 MB | 117.64 MB | 110.7% | 108.9% |
| `lteNRRCC` | 74.58 MB | 102.70 MB | 104.6% | 105.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0172s | +0.0236s | worse |
| `f1ap_rel18.6_specs` | 0.0673s | 0.0687s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0380s | 0.0465s | -0.0085s | improved |
| `lteNRRCC` | 0.0698s | 0.0765s | -0.0067s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.91 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.92 MB | 4.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.84 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.86 MB | 4.30 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0393s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1064s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0749s | +0.0027s | worse |
| `lteNRRCC` | 0.1394s | 0.1415s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.51 MB | 7.51 MB | 161.6% | 79.5% |
| `f1ap_rel18.6_specs` | 8.39 MB | 106.64 MB | 101.4% | 173.7% |
| `ngap_rel18.6_specs` | 7.62 MB | 8.00 MB | 159.9% | 156.3% |
| `lteNRRCC` | 51.09 MB | 51.65 MB | 156.6% | 159.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0447s | 0.0410s | +0.0037s | worse |
| `f1ap_rel18.6_specs` | 0.1319s | 0.1202s | +0.0117s | worse |
| `ngap_rel18.6_specs` | 0.0904s | 0.0829s | +0.0075s | worse |
| `lteNRRCC` | 0.1462s | 0.1294s | +0.0168s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.96 MB | 9.84 MB | 94.2% | 86.4% |
| `f1ap_rel18.6_specs` | 10.57 MB | 164.18 MB | 77.1% | 105.3% |
| `ngap_rel18.6_specs` | 10.12 MB | 11.06 MB | 77.0% | 105.8% |
| `lteNRRCC` | 72.37 MB | 101.71 MB | 110.1% | 158.6% |
<!-- BENCH_RESULTS_END -->
