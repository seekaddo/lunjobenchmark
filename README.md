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
Generated: 2026-04-08T22:51:35.312837+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0389s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1217s | -0.0105s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0826s | -0.0068s | improved |
| `lteNRRCC` | 0.1194s | 0.1264s | -0.0070s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 53.55 MB | 25.9% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 106.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0370s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0955s | 0.0979s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0689s | -0.0028s | improved |
| `lteNRRCC` | 0.1292s | 0.1335s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 36.69 MB | 92.3% | 110.7% |
| `f1ap_rel18.6_specs` | 22.10 MB | 103.42 MB | 108.8% | 105.2% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.37 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.80 MB | 66.39 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0320s | 0.0352s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.0884s | 0.0946s | -0.0062s | improved |
| `ngap_rel18.6_specs` | 0.0596s | 0.0663s | -0.0067s | improved |
| `lteNRRCC` | 0.1102s | 0.1301s | -0.0199s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.77 MB | 92.0% | 111.1% |
| `f1ap_rel18.6_specs` | 35.26 MB | 163.75 MB | 110.7% | 105.5% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.08 MB | 107.1% | 104.9% |
| `lteNRRCC` | 74.81 MB | 102.43 MB | 105.3% | 104.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0206s | 0.0257s | -0.0051s | improved |
| `f1ap_rel18.6_specs` | 0.0636s | 0.0746s | -0.0110s | improved |
| `ngap_rel18.6_specs` | 0.0442s | 0.0520s | -0.0078s | improved |
| `lteNRRCC` | 0.0776s | 0.0851s | -0.0075s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.62 MB | 4.00 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 3.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.41 MB | 4.23 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.30 MB | 5.08 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0395s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1061s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0753s | +0.0016s | worse |
| `lteNRRCC` | 0.1395s | 0.1366s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.62 MB | 7.74 MB | 83.4% | 165.9% |
| `f1ap_rel18.6_specs` | 8.60 MB | 8.54 MB | 164.9% | 163.0% |
| `ngap_rel18.6_specs` | 7.95 MB | 8.11 MB | 160.4% | 165.9% |
| `lteNRRCC` | 51.01 MB | 70.55 MB | 165.3% | 166.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0432s | 0.0395s | +0.0037s | worse |
| `f1ap_rel18.6_specs` | 0.1170s | 0.1107s | +0.0063s | worse |
| `ngap_rel18.6_specs` | 0.0822s | 0.0795s | +0.0027s | worse |
| `lteNRRCC` | 0.1299s | 0.1272s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.71 MB | 10.02 MB | 182.4% | 119.9% |
| `f1ap_rel18.6_specs` | 9.86 MB | 11.02 MB | 161.2% | 233.0% |
| `ngap_rel18.6_specs` | 9.14 MB | 9.80 MB | 165.4% | 118.9% |
| `lteNRRCC` | 7.11 MB | 94.72 MB | 105.9% | 117.5% |
<!-- BENCH_RESULTS_END -->
