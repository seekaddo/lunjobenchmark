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
Generated: 2026-05-05T23:00:48.689523+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0384s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1142s | 0.1175s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0816s | -0.0040s | improved |
| `lteNRRCC` | 0.1221s | 0.1269s | -0.0048s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 27.4% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 105.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.3% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0377s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0992s | 0.0999s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0694s | 0.0706s | -0.0012s | improved |
| `lteNRRCC` | 0.1335s | 0.1336s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.50 MB | 86.2% | 110.0% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.46 MB | 108.8% | 105.0% |
| `ngap_rel18.6_specs` | 16.73 MB | 74.37 MB | 110.7% | 106.5% |
| `lteNRRCC` | 48.41 MB | 66.51 MB | 106.0% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0335s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0990s | 0.0887s | +0.0103s | worse |
| `ngap_rel18.6_specs` | 0.0674s | 0.0617s | +0.0057s | worse |
| `lteNRRCC` | 0.1162s | 0.1151s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.36 MB | 55.66 MB | 100.0% | 107.7% |
| `f1ap_rel18.6_specs` | 35.25 MB | 164.19 MB | 107.4% | 103.4% |
| `ngap_rel18.6_specs` | 24.50 MB | 117.27 MB | 109.1% | 104.7% |
| `lteNRRCC` | 74.90 MB | 102.70 MB | 103.6% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0193s | 0.0200s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0600s | 0.0652s | -0.0052s | improved |
| `ngap_rel18.6_specs` | 0.0401s | 0.0413s | -0.0012s | improved |
| `lteNRRCC` | 0.0766s | 0.0725s | +0.0041s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.33 MB | 4.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.12 MB | 4.56 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.84 MB | 6.67 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.20 MB | 7.09 MB | 0.7% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0396s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1068s | 0.1079s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0796s | 0.0745s | +0.0051s | worse |
| `lteNRRCC` | 0.1375s | 0.1387s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.44 MB | 165.2% | 160.4% |
| `f1ap_rel18.6_specs` | 8.38 MB | 106.65 MB | 161.0% | 146.4% |
| `ngap_rel18.6_specs` | 7.68 MB | 7.88 MB | 80.0% | 157.4% |
| `lteNRRCC` | 46.69 MB | 55.51 MB | 160.1% | 104.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0426s | 0.0386s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.1370s | 0.1123s | +0.0247s | worse |
| `ngap_rel18.6_specs` | 0.0898s | 0.0771s | +0.0127s | worse |
| `lteNRRCC` | 0.1369s | 0.1272s | +0.0097s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.71 MB | 9.55 MB | 160.7% | 154.8% |
| `f1ap_rel18.6_specs` | 9.99 MB | 10.05 MB | 161.3% | 171.4% |
| `ngap_rel18.6_specs` | 10.05 MB | 9.38 MB | 233.9% | 165.6% |
| `lteNRRCC` | 8.55 MB | 98.82 MB | 162.6% | 107.6% |
<!-- BENCH_RESULTS_END -->
