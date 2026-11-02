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
Generated: 2026-11-02T20:09:57.285059+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0399s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1211s | 0.1211s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0828s | 0.0853s | -0.0025s | improved |
| `lteNRRCC` | 0.1261s | 0.1274s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 19.8% | 103.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.2% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 101.9% |
| `lteNRRCC` | 72.35 MB | 100.18 MB | 101.6% | 101.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0481s | 0.0373s | +0.0108s | worse |
| `f1ap_rel18.6_specs` | 0.1473s | 0.1151s | +0.0322s | worse |
| `ngap_rel18.6_specs` | 0.0982s | 0.0786s | +0.0196s | worse |
| `lteNRRCC` | 0.1581s | 0.1285s | +0.0296s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 34.65 MB | 79.3% | 105.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.6% | 102.4% |
| `ngap_rel18.6_specs` | 17.97 MB | 72.65 MB | 107.1% | 103.2% |
| `lteNRRCC` | 46.71 MB | 64.21 MB | 102.7% | 102.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0555s | -0.0177s | improved |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1687s | -0.0530s | improved |
| `ngap_rel18.6_specs` | 0.0781s | 0.1171s | -0.0390s | improved |
| `lteNRRCC` | 0.1107s | 0.1630s | -0.0523s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.85 MB | 53.73 MB | 80.0% | 103.7% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 104.0% | 101.5% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 110.5% | 102.1% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 102.0% | 101.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0319s | 0.0304s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0918s | 0.1174s | -0.0256s | improved |
| `ngap_rel18.6_specs` | 0.0581s | 0.0797s | -0.0216s | improved |
| `lteNRRCC` | 0.0833s | 0.1012s | -0.0179s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.41 MB | 4.81 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.66 MB | 8.47 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.19 MB | 7.92 MB | 0.0% | 1.1% |
| `lteNRRCC` | 3.75 MB | 7.58 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0420s | 0.0391s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1078s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0820s | 0.0760s | +0.0060s | worse |
| `lteNRRCC` | 0.1286s | 0.1391s | -0.0105s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.24 MB | 8.12 MB | 0.0% | 84.7% |
| `f1ap_rel18.6_specs` | 8.67 MB | 106.64 MB | 156.5% | 154.8% |
| `ngap_rel18.6_specs` | 8.43 MB | 8.55 MB | 82.3% | 214.5% |
| `lteNRRCC` | 51.84 MB | 61.98 MB | 153.6% | 153.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0429s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1215s | -0.0089s | improved |
| `ngap_rel18.6_specs` | 0.0806s | 0.0855s | -0.0049s | improved |
| `lteNRRCC` | 0.1334s | 0.1319s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.18 MB | 8.68 MB | 0.0% | 78.4% |
| `f1ap_rel18.6_specs` | 10.38 MB | 164.18 MB | 99.6% | 107.1% |
| `ngap_rel18.6_specs` | 10.89 MB | 10.52 MB | 112.8% | 107.8% |
| `lteNRRCC` | 8.76 MB | 98.15 MB | 94.4% | 106.9% |
<!-- BENCH_RESULTS_END -->
