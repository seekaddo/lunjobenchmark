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
Generated: 2026-07-20T12:21:31.419108+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0352s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1167s | 0.1085s | +0.0082s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0738s | +0.0078s | worse |
| `lteNRRCC` | 0.1251s | 0.1178s | +0.0073s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 21.0% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 105.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0351s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0990s | 0.1027s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0734s | 0.0732s | +0.0002s | worse |
| `lteNRRCC` | 0.1291s | 0.1228s | +0.0063s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.54 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 22.40 MB | 103.34 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.62 MB | 73.93 MB | 107.4% | 104.4% |
| `lteNRRCC` | 48.82 MB | 65.88 MB | 106.2% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0272s | 0.0344s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.0867s | 0.0915s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0514s | 0.0631s | -0.0117s | improved |
| `lteNRRCC` | 0.0970s | 0.1218s | -0.0248s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.20 MB | 55.64 MB | 70.4% | 104.5% |
| `f1ap_rel18.6_specs` | 34.55 MB | 164.25 MB | 104.3% | 106.0% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.68 MB | 110.0% | 105.7% |
| `lteNRRCC` | 74.85 MB | 102.77 MB | 104.2% | 101.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0227s | 0.0266s | -0.0039s | improved |
| `f1ap_rel18.6_specs` | 0.0733s | 0.0684s | +0.0049s | worse |
| `ngap_rel18.6_specs` | 0.0484s | 0.0463s | +0.0021s | worse |
| `lteNRRCC` | 0.0855s | 0.0805s | +0.0050s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.25 MB | 3.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.69 MB | 3.25 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.89 MB | 3.53 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.27 MB | 3.53 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0392s | -0.0062s | improved |
| `f1ap_rel18.6_specs` | 0.0907s | 0.1070s | -0.0163s | improved |
| `ngap_rel18.6_specs` | 0.0628s | 0.0745s | -0.0117s | improved |
| `lteNRRCC` | 0.1106s | 0.1375s | -0.0269s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.83 MB | 7.82 MB | 211.5% | 115.3% |
| `f1ap_rel18.6_specs` | 7.98 MB | 8.24 MB | 134.6% | 126.9% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.25 MB | 140.2% | 139.8% |
| `lteNRRCC` | 51.72 MB | 53.08 MB | 103.2% | 203.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0425s | -0.0047s | improved |
| `f1ap_rel18.6_specs` | 0.1114s | 0.1162s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0747s | 0.0813s | -0.0066s | improved |
| `lteNRRCC` | 0.1165s | 0.1337s | -0.0172s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.66 MB | 10.54 MB | 113.4% | 89.1% |
| `f1ap_rel18.6_specs` | 10.44 MB | 157.42 MB | 93.9% | 106.5% |
| `ngap_rel18.6_specs` | 10.20 MB | 9.93 MB | 186.9% | 99.0% |
| `lteNRRCC` | 73.78 MB | 87.61 MB | 196.8% | 185.3% |
<!-- BENCH_RESULTS_END -->
