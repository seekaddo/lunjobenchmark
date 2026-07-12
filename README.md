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
Generated: 2026-07-12T11:16:30.099084+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0356s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1123s | 0.1099s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0758s | 0.0751s | +0.0007s | worse |
| `lteNRRCC` | 0.1191s | 0.1189s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 18.3% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0322s | +0.0051s | worse |
| `f1ap_rel18.6_specs` | 0.0957s | 0.0940s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0671s | 0.0642s | +0.0029s | worse |
| `lteNRRCC` | 0.1291s | 0.1170s | +0.0121s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 36.70 MB | 79.3% | 110.7% |
| `f1ap_rel18.6_specs` | 22.28 MB | 103.11 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.49 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.50 MB | 66.45 MB | 103.1% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0359s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.0883s | 0.0943s | -0.0060s | improved |
| `ngap_rel18.6_specs` | 0.0613s | 0.0672s | -0.0059s | improved |
| `lteNRRCC` | 0.1139s | 0.1220s | -0.0081s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.36 MB | 70.0% | 111.5% |
| `f1ap_rel18.6_specs` | 34.33 MB | 164.25 MB | 106.7% | 105.6% |
| `ngap_rel18.6_specs` | 24.37 MB | 117.52 MB | 112.5% | 104.9% |
| `lteNRRCC` | 74.78 MB | 102.78 MB | 105.3% | 104.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0220s | 0.0229s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0684s | 0.0671s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0458s | 0.0481s | -0.0023s | improved |
| `lteNRRCC` | 0.0798s | 0.0902s | -0.0104s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.08 MB | 3.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.62 MB | 4.02 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.84 MB | 5.50 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.28 MB | 4.95 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0519s | -0.0123s | improved |
| `f1ap_rel18.6_specs` | 0.1168s | 0.1156s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0764s | 0.0808s | -0.0044s | improved |
| `lteNRRCC` | 0.1384s | 0.1445s | -0.0061s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.12 MB | 7.82 MB | 218.1% | 179.1% |
| `f1ap_rel18.6_specs` | 8.74 MB | 8.04 MB | 111.6% | 81.5% |
| `ngap_rel18.6_specs` | 8.37 MB | 7.68 MB | 217.1% | 160.3% |
| `lteNRRCC` | 8.23 MB | 51.33 MB | 80.8% | 160.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0435s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.1163s | 0.1285s | -0.0122s | improved |
| `ngap_rel18.6_specs` | 0.0815s | 0.0899s | -0.0084s | improved |
| `lteNRRCC` | 0.1387s | 0.1279s | +0.0108s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.79 MB | 10.15 MB | 77.2% | 107.2% |
| `f1ap_rel18.6_specs` | 9.55 MB | 164.19 MB | 155.5% | 159.2% |
| `ngap_rel18.6_specs` | 8.98 MB | 9.14 MB | 153.5% | 149.0% |
| `lteNRRCC` | 9.23 MB | 83.14 MB | 96.5% | 106.3% |
<!-- BENCH_RESULTS_END -->
