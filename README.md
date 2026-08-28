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
Generated: 2026-08-28T21:09:29.055973+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0364s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1128s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0772s | +0.0005s | worse |
| `lteNRRCC` | 0.1219s | 0.1212s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 82.6% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0339s | +0.0034s | worse |
| `f1ap_rel18.6_specs` | 0.0978s | 0.0940s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0696s | 0.0661s | +0.0035s | worse |
| `lteNRRCC` | 0.1319s | 0.1315s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.70 MB | 36.18 MB | 14.7% | 103.6% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.31 MB | 106.2% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.25 MB | 103.6% | 104.5% |
| `lteNRRCC` | 48.70 MB | 66.12 MB | 101.5% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0340s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0889s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0643s | 0.0607s | +0.0036s | worse |
| `lteNRRCC` | 0.1179s | 0.1147s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.61 MB | 83.3% | 107.7% |
| `f1ap_rel18.6_specs` | 33.74 MB | 164.71 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 24.41 MB | 117.68 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.75 MB | 102.41 MB | 103.6% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0236s | 0.0238s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0998s | 0.0696s | +0.0302s | worse |
| `ngap_rel18.6_specs` | 0.0471s | 0.0494s | -0.0023s | improved |
| `lteNRRCC` | 0.0780s | 0.0788s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.03 MB | 6.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.83 MB | 6.27 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.20 MB | 6.36 MB | 1.2% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0386s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1063s | 0.1050s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0737s | 0.0735s | +0.0002s | worse |
| `lteNRRCC` | 0.1371s | 0.1367s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.93 MB | 7.44 MB | 0.0% | 161.9% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.03 MB | 163.4% | 161.7% |
| `ngap_rel18.6_specs` | 7.54 MB | 8.24 MB | 164.3% | 230.0% |
| `lteNRRCC` | 47.63 MB | 50.93 MB | 158.0% | 155.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0372s | +0.0044s | worse |
| `f1ap_rel18.6_specs` | 0.1174s | 0.1104s | +0.0070s | worse |
| `ngap_rel18.6_specs` | 0.0844s | 0.0769s | +0.0075s | worse |
| `lteNRRCC` | 0.1306s | 0.1262s | +0.0044s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 10.32 MB | 0.0% | 105.5% |
| `f1ap_rel18.6_specs` | 9.62 MB | 10.93 MB | 117.2% | 120.5% |
| `ngap_rel18.6_specs` | 9.14 MB | 10.44 MB | 111.5% | 119.8% |
| `lteNRRCC` | 8.62 MB | 101.21 MB | 93.6% | 117.4% |
<!-- BENCH_RESULTS_END -->
