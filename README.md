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
Generated: 2026-04-29T11:45:17.666821+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0355s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1153s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0782s | 0.0787s | -0.0005s | improved |
| `lteNRRCC` | 0.1215s | 0.1232s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.90 MB | 53.55 MB | 9.5% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0347s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0933s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0663s | 0.0724s | -0.0061s | improved |
| `lteNRRCC` | 0.1278s | 0.1252s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.40 MB | 92.3% | 110.7% |
| `f1ap_rel18.6_specs` | 21.93 MB | 103.38 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.44 MB | 107.4% | 109.3% |
| `lteNRRCC` | 48.50 MB | 65.97 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0363s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0900s | 0.0959s | -0.0059s | improved |
| `ngap_rel18.6_specs` | 0.0643s | 0.0682s | -0.0039s | improved |
| `lteNRRCC` | 0.1158s | 0.1235s | -0.0077s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.26 MB | 55.89 MB | 92.0% | 110.7% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.77 MB | 106.7% | 105.4% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.69 MB | 112.0% | 104.8% |
| `lteNRRCC` | 74.70 MB | 102.71 MB | 103.4% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0203s | 0.0211s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0586s | 0.0789s | -0.0203s | improved |
| `ngap_rel18.6_specs` | 0.0405s | 0.0519s | -0.0114s | improved |
| `lteNRRCC` | 0.0744s | 0.1047s | -0.0303s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.06 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.58 MB | 4.31 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.84 MB | 4.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.84 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0377s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1056s | 0.1036s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0764s | 0.0733s | +0.0031s | worse |
| `lteNRRCC` | 0.1417s | 0.1355s | +0.0062s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.35 MB | 7.98 MB | 161.4% | 221.5% |
| `f1ap_rel18.6_specs` | 8.04 MB | 7.97 MB | 163.7% | 163.4% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.55 MB | 80.0% | 160.7% |
| `lteNRRCC` | 51.56 MB | 70.55 MB | 107.6% | 230.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0373s | +0.0043s | worse |
| `f1ap_rel18.6_specs` | 0.1180s | 0.1048s | +0.0132s | worse |
| `ngap_rel18.6_specs` | 0.0819s | 0.0751s | +0.0068s | worse |
| `lteNRRCC` | 0.1367s | 0.1237s | +0.0130s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.07 MB | 8.93 MB | 82.8% | 83.4% |
| `f1ap_rel18.6_specs` | 11.20 MB | 149.95 MB | 109.7% | 164.0% |
| `ngap_rel18.6_specs` | 9.21 MB | 9.30 MB | 82.0% | 83.0% |
| `lteNRRCC` | 68.67 MB | 101.71 MB | 103.6% | 112.5% |
<!-- BENCH_RESULTS_END -->
