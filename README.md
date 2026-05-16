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
Generated: 2026-05-16T11:08:18.691339+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0375s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1103s | 0.1173s | -0.0070s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0803s | -0.0051s | improved |
| `lteNRRCC` | 0.1166s | 0.1241s | -0.0075s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 8.2% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0342s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0949s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0687s | 0.0675s | +0.0012s | worse |
| `lteNRRCC` | 0.1271s | 0.1258s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 36.25 MB | 27.3% | 110.7% |
| `f1ap_rel18.6_specs` | 22.12 MB | 103.18 MB | 109.4% | 107.0% |
| `ngap_rel18.6_specs` | 16.45 MB | 74.30 MB | 115.4% | 106.8% |
| `lteNRRCC` | 48.47 MB | 66.30 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0341s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0879s | 0.0914s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0610s | 0.0650s | -0.0040s | improved |
| `lteNRRCC` | 0.1151s | 0.1181s | -0.0030s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 55.62 MB | 23.2% | 111.1% |
| `f1ap_rel18.6_specs` | 34.65 MB | 164.27 MB | 110.3% | 105.6% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.82 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.65 MB | 102.80 MB | 105.2% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0199s | +0.0175s | worse |
| `f1ap_rel18.6_specs` | 0.0694s | 0.0666s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0418s | 0.0501s | -0.0083s | improved |
| `lteNRRCC` | 0.0702s | 0.0708s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.81 MB | 5.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.09 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.17 MB | 4.00 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0414s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1067s | 0.1106s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0762s | -0.0011s | improved |
| `lteNRRCC` | 0.1370s | 0.1291s | +0.0079s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.44 MB | 158.6% | 240.6% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.17 MB | 161.4% | 147.9% |
| `ngap_rel18.6_specs` | 8.14 MB | 8.17 MB | 228.6% | 217.4% |
| `lteNRRCC` | 46.57 MB | 51.08 MB | 158.9% | 216.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0424s | 0.0409s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1251s | 0.1136s | +0.0115s | worse |
| `ngap_rel18.6_specs` | 0.0867s | 0.0794s | +0.0073s | worse |
| `lteNRRCC` | 0.1335s | 0.1280s | +0.0055s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.96 MB | 9.65 MB | 115.7% | 159.8% |
| `f1ap_rel18.6_specs` | 10.24 MB | 10.05 MB | 164.7% | 80.6% |
| `ngap_rel18.6_specs` | 9.38 MB | 9.27 MB | 161.8% | 162.4% |
| `lteNRRCC` | 9.23 MB | 101.70 MB | 103.5% | 112.5% |
<!-- BENCH_RESULTS_END -->
