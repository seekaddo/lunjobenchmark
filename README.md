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
Generated: 2026-04-28T23:02:07.285997+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0382s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.1153s | 0.1154s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0787s | 0.0781s | +0.0006s | worse |
| `lteNRRCC` | 0.1232s | 0.1247s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 24.0% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 106.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.3% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0353s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0995s | -0.0062s | improved |
| `ngap_rel18.6_specs` | 0.0724s | 0.0689s | +0.0035s | worse |
| `lteNRRCC` | 0.1252s | 0.1203s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.26 MB | 36.12 MB | 96.2% | 110.3% |
| `f1ap_rel18.6_specs` | 21.89 MB | 103.11 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.64 MB | 74.71 MB | 111.1% | 106.8% |
| `lteNRRCC` | 47.82 MB | 65.93 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0336s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.0959s | 0.0921s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0682s | 0.0636s | +0.0046s | worse |
| `lteNRRCC` | 0.1235s | 0.1164s | +0.0071s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.37 MB | 89.3% | 109.7% |
| `f1ap_rel18.6_specs` | 34.64 MB | 164.57 MB | 109.7% | 104.9% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.77 MB | 115.4% | 106.5% |
| `lteNRRCC` | 74.97 MB | 102.91 MB | 106.7% | 104.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0211s | 0.0281s | -0.0070s | improved |
| `f1ap_rel18.6_specs` | 0.0789s | 0.0692s | +0.0097s | worse |
| `ngap_rel18.6_specs` | 0.0519s | 0.0618s | -0.0099s | improved |
| `lteNRRCC` | 0.1047s | 0.0723s | +0.0324s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.22 MB | 4.55 MB | 1.5% | 0.0% |
| `f1ap_rel18.6_specs` | 1.00 MB | 9.78 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.59 MB | 5.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.09 MB | 3.95 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0415s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1036s | 0.1176s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0733s | 0.0808s | -0.0075s | improved |
| `lteNRRCC` | 0.1355s | 0.1409s | -0.0054s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.81 MB | 94.1% | 119.9% |
| `f1ap_rel18.6_specs` | 7.97 MB | 8.46 MB | 82.3% | 109.3% |
| `ngap_rel18.6_specs` | 8.11 MB | 7.55 MB | 117.4% | 168.2% |
| `lteNRRCC` | 48.75 MB | 49.25 MB | 116.6% | 107.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0387s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1048s | 0.1074s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0754s | -0.0003s | improved |
| `lteNRRCC` | 0.1237s | 0.1248s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.03 MB | 9.71 MB | 0.0% | 112.5% |
| `f1ap_rel18.6_specs` | 11.14 MB | 9.68 MB | 114.9% | 165.9% |
| `ngap_rel18.6_specs` | 8.77 MB | 10.75 MB | 162.7% | 117.7% |
| `lteNRRCC` | 8.30 MB | 76.02 MB | 161.6% | 118.4% |
<!-- BENCH_RESULTS_END -->
