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
Generated: 2026-03-19T10:53:23.591883+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0392s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.1159s | 0.1255s | -0.0096s | improved |
| `ngap_rel18.6_specs` | 0.0794s | 0.0856s | -0.0062s | improved |
| `lteNRRCC` | 0.1175s | 0.1237s | -0.0062s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.53 MB | 55.78 MB | 94.7% | 107.4% |
| `f1ap_rel18.6_specs` | 32.53 MB | 176.91 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.41 MB | 125.78 MB | 109.1% | 102.0% |
| `lteNRRCC` | 72.32 MB | 100.09 MB | 105.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0370s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0976s | 0.0977s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0688s | 0.0692s | -0.0004s | improved |
| `lteNRRCC` | 0.1309s | 0.1316s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.31 MB | 37.83 MB | 30.5% | 110.0% |
| `f1ap_rel18.6_specs` | 22.08 MB | 111.95 MB | 108.8% | 105.0% |
| `ngap_rel18.6_specs` | 16.84 MB | 80.16 MB | 114.3% | 106.5% |
| `lteNRRCC` | 48.52 MB | 66.46 MB | 104.5% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0343s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1002s | 0.0924s | +0.0078s | worse |
| `ngap_rel18.6_specs` | 0.0697s | 0.0666s | +0.0031s | worse |
| `lteNRRCC` | 0.1134s | 0.1148s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.56 MB | 57.71 MB | 90.0% | 111.5% |
| `f1ap_rel18.6_specs` | 34.69 MB | 178.96 MB | 111.5% | 103.4% |
| `ngap_rel18.6_specs` | 24.33 MB | 127.60 MB | 109.5% | 104.5% |
| `lteNRRCC` | 75.01 MB | 102.52 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0200s | 0.0259s | -0.0059s | improved |
| `f1ap_rel18.6_specs` | 0.0629s | 0.0826s | -0.0197s | improved |
| `ngap_rel18.6_specs` | 0.0423s | 0.0545s | -0.0122s | improved |
| `lteNRRCC` | 0.0729s | 0.0900s | -0.0171s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.48 MB | 3.89 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.92 MB | 4.14 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.11 MB | 3.95 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 4.06 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0426s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1130s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0793s | 0.0784s | +0.0009s | worse |
| `lteNRRCC` | 0.1387s | 0.1382s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.43 MB | 155.7% | 162.0% |
| `f1ap_rel18.6_specs` | 8.17 MB | 8.11 MB | 97.4% | 171.5% |
| `ngap_rel18.6_specs` | 7.66 MB | 7.87 MB | 163.4% | 157.8% |
| `lteNRRCC` | 8.31 MB | 50.96 MB | 80.4% | 109.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0405s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1170s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0826s | -0.0036s | improved |
| `lteNRRCC` | 0.1278s | 0.1293s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.40 MB | 8.56 MB | 103.8% | 164.5% |
| `f1ap_rel18.6_specs` | 9.46 MB | 179.18 MB | 81.8% | 117.3% |
| `ngap_rel18.6_specs` | 9.14 MB | 10.63 MB | 161.8% | 118.1% |
| `lteNRRCC` | 9.66 MB | 89.99 MB | 118.3% | 117.9% |
<!-- BENCH_RESULTS_END -->
