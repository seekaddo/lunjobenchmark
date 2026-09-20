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
Generated: 2026-09-20T14:04:04.970427+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0352s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1103s | 0.1089s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0750s | 0.0734s | +0.0016s | worse |
| `lteNRRCC` | 0.1202s | 0.1171s | +0.0031s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 56.2% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 100.0% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0353s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1017s | 0.0963s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0710s | 0.0674s | +0.0036s | worse |
| `lteNRRCC` | 0.1367s | 0.1286s | +0.0081s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.25 MB | 84.6% | 103.4% |
| `f1ap_rel18.6_specs` | 22.00 MB | 103.02 MB | 106.1% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.40 MB | 103.7% | 102.1% |
| `lteNRRCC` | 48.53 MB | 66.11 MB | 101.5% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0307s | 0.0301s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0880s | 0.0912s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0583s | 0.0626s | -0.0043s | improved |
| `lteNRRCC` | 0.0978s | 0.0944s | +0.0034s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 55.76 MB | 21.1% | 104.8% |
| `f1ap_rel18.6_specs` | 34.49 MB | 164.54 MB | 104.5% | 100.0% |
| `ngap_rel18.6_specs` | 24.57 MB | 117.76 MB | 105.6% | 100.0% |
| `lteNRRCC` | 74.90 MB | 102.76 MB | 102.1% | 103.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0216s | 0.0550s | -0.0334s | improved |
| `f1ap_rel18.6_specs` | 0.0847s | 0.0837s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0486s | 0.0895s | -0.0409s | improved |
| `lteNRRCC` | 0.0770s | 0.1049s | -0.0279s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.88 MB | 4.19 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.66 MB | 9.09 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.17 MB | 3.86 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.39 MB | 7.19 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0443s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1310s | -0.0209s | improved |
| `ngap_rel18.6_specs` | 0.0774s | 0.0841s | -0.0067s | improved |
| `lteNRRCC` | 0.1379s | 0.1609s | -0.0230s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.77 MB | 7.59 MB | 0.0% | 76.3% |
| `f1ap_rel18.6_specs` | 8.07 MB | 8.37 MB | 159.0% | 156.4% |
| `ngap_rel18.6_specs` | 8.52 MB | 8.33 MB | 222.7% | 212.7% |
| `lteNRRCC` | 8.19 MB | 63.25 MB | 157.4% | 109.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0382s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1164s | 0.1108s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0807s | 0.0797s | +0.0010s | worse |
| `lteNRRCC` | 0.1328s | 0.1244s | +0.0084s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.94 MB | 10.69 MB | 165.6% | 88.9% |
| `f1ap_rel18.6_specs` | 9.91 MB | 12.78 MB | 153.6% | 197.5% |
| `ngap_rel18.6_specs` | 9.78 MB | 9.31 MB | 93.7% | 153.2% |
| `lteNRRCC` | 8.85 MB | 89.30 MB | 150.0% | 204.9% |
<!-- BENCH_RESULTS_END -->
