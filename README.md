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
Generated: 2026-06-15T15:51:23.860724+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0352s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1103s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0757s | +0.0001s | worse |
| `lteNRRCC` | 0.1193s | 0.1187s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.92 MB | 53.55 MB | 21.7% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0343s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0972s | 0.0936s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0663s | +0.0029s | worse |
| `lteNRRCC` | 0.1282s | 0.1245s | +0.0037s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.25 MB | 22.1% | 110.0% |
| `f1ap_rel18.6_specs` | 22.36 MB | 103.29 MB | 106.1% | 105.0% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.39 MB | 114.8% | 106.4% |
| `lteNRRCC` | 48.50 MB | 65.98 MB | 106.3% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0364s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0952s | 0.0973s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0642s | 0.0665s | -0.0023s | improved |
| `lteNRRCC` | 0.1162s | 0.1290s | -0.0128s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.40 MB | 55.44 MB | 88.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.42 MB | 163.53 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 24.41 MB | 116.88 MB | 112.5% | 107.1% |
| `lteNRRCC` | 74.69 MB | 102.94 MB | 103.4% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0261s | 0.0176s | +0.0085s | worse |
| `f1ap_rel18.6_specs` | 0.0977s | 0.0713s | +0.0264s | worse |
| `ngap_rel18.6_specs` | 0.0592s | 0.0460s | +0.0132s | worse |
| `lteNRRCC` | 0.1019s | 0.0761s | +0.0258s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.33 MB | 3.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.97 MB | 8.41 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.80 MB | 4.98 MB | 1.0% | 0.1% |
| `lteNRRCC` | 3.94 MB | 11.39 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0476s | 0.0387s | +0.0089s | worse |
| `f1ap_rel18.6_specs` | 0.1186s | 0.1075s | +0.0111s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0783s | +0.0020s | worse |
| `lteNRRCC` | 0.1426s | 0.1367s | +0.0059s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.82 MB | 8.11 MB | 80.3% | 97.2% |
| `f1ap_rel18.6_specs` | 8.61 MB | 106.65 MB | 82.4% | 107.8% |
| `ngap_rel18.6_specs` | 8.25 MB | 8.24 MB | 160.2% | 160.1% |
| `lteNRRCC` | 8.67 MB | 57.71 MB | 85.5% | 162.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0321s | 0.0449s | -0.0128s | improved |
| `f1ap_rel18.6_specs` | 0.0814s | 0.1276s | -0.0462s | improved |
| `ngap_rel18.6_specs` | 0.0561s | 0.0906s | -0.0345s | improved |
| `lteNRRCC` | 0.0873s | 0.1477s | -0.0604s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 13.48 MB | 111.0% | 133.2% |
| `f1ap_rel18.6_specs` | 20.07 MB | 20.63 MB | 94.8% | 145.5% |
| `ngap_rel18.6_specs` | 16.27 MB | 14.74 MB | 169.3% | 87.0% |
| `lteNRRCC` | 73.77 MB | 18.87 MB | 0.0% | 90.1% |
<!-- BENCH_RESULTS_END -->
