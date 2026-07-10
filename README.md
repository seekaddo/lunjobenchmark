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
Generated: 2026-07-10T23:03:47.317404+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0366s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1147s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0790s | +0.0000s | flat |
| `lteNRRCC` | 0.1216s | 0.1230s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 21.4% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0293s | +0.0053s | worse |
| `f1ap_rel18.6_specs` | 0.0944s | 0.0765s | +0.0179s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0539s | +0.0128s | worse |
| `lteNRRCC` | 0.1289s | 0.0984s | +0.0305s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 36.31 MB | 82.1% | 107.4% |
| `f1ap_rel18.6_specs` | 22.34 MB | 103.25 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.57 MB | 74.70 MB | 111.5% | 109.5% |
| `lteNRRCC` | 48.18 MB | 66.52 MB | 104.7% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0353s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0927s | 0.0925s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0653s | 0.0654s | -0.0001s | improved |
| `lteNRRCC` | 0.1210s | 0.1213s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.29 MB | 55.74 MB | 75.8% | 110.3% |
| `f1ap_rel18.6_specs` | 34.62 MB | 164.37 MB | 106.7% | 105.2% |
| `ngap_rel18.6_specs` | 24.16 MB | 117.70 MB | 111.5% | 106.5% |
| `lteNRRCC` | 74.86 MB | 102.75 MB | 106.9% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0230s | 0.0226s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0654s | 0.0635s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0485s | 0.0424s | +0.0061s | worse |
| `lteNRRCC` | 0.0761s | 0.0737s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.17 MB | 4.52 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.73 MB | 3.89 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.94 MB | 5.06 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.17 MB | 3.61 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0432s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1126s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0737s | 0.0789s | -0.0052s | improved |
| `lteNRRCC` | 0.1373s | 0.1425s | -0.0052s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.93 MB | 7.29 MB | 113.2% | 80.7% |
| `f1ap_rel18.6_specs` | 7.97 MB | 8.04 MB | 164.7% | 162.5% |
| `ngap_rel18.6_specs` | 7.54 MB | 8.11 MB | 160.9% | 113.3% |
| `lteNRRCC` | 47.82 MB | 49.64 MB | 162.0% | 165.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0421s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.1090s | 0.1206s | -0.0116s | improved |
| `ngap_rel18.6_specs` | 0.0785s | 0.0833s | -0.0048s | improved |
| `lteNRRCC` | 0.1247s | 0.1304s | -0.0057s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 8.54 MB | 161.6% | 163.0% |
| `f1ap_rel18.6_specs` | 9.58 MB | 164.18 MB | 159.5% | 116.8% |
| `ngap_rel18.6_specs` | 8.89 MB | 9.02 MB | 158.4% | 159.7% |
| `lteNRRCC` | 73.77 MB | 87.14 MB | 159.1% | 105.7% |
<!-- BENCH_RESULTS_END -->
