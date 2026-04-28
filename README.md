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
Generated: 2026-04-28T11:51:58.460682+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0357s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.1154s | 0.1122s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0781s | 0.0776s | +0.0005s | worse |
| `lteNRRCC` | 0.1247s | 0.1211s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.93 MB | 53.55 MB | 28.4% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0265s | +0.0088s | worse |
| `f1ap_rel18.6_specs` | 0.0995s | 0.0727s | +0.0268s | worse |
| `ngap_rel18.6_specs` | 0.0689s | 0.0510s | +0.0179s | worse |
| `lteNRRCC` | 0.1203s | 0.0962s | +0.0241s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.33 MB | 36.37 MB | 92.0% | 107.1% |
| `f1ap_rel18.6_specs` | 22.20 MB | 103.18 MB | 110.3% | 103.3% |
| `ngap_rel18.6_specs` | 16.82 MB | 74.66 MB | 108.3% | 104.4% |
| `lteNRRCC` | 48.54 MB | 66.23 MB | 103.4% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0334s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0921s | 0.0942s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0636s | 0.0632s | +0.0004s | worse |
| `lteNRRCC` | 0.1164s | 0.1157s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.66 MB | 55.89 MB | 92.0% | 107.1% |
| `f1ap_rel18.6_specs` | 34.73 MB | 164.64 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.04 MB | 116.98 MB | 116.7% | 107.0% |
| `lteNRRCC` | 74.67 MB | 102.79 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0281s | 0.0348s | -0.0067s | improved |
| `f1ap_rel18.6_specs` | 0.0692s | 0.0820s | -0.0128s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0543s | +0.0075s | worse |
| `lteNRRCC` | 0.0723s | 0.0971s | -0.0248s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.44 MB | 1.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.17 MB | 5.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.55 MB | 8.33 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.28 MB | 1.33 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0400s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1176s | 0.1091s | +0.0085s | worse |
| `ngap_rel18.6_specs` | 0.0808s | 0.0765s | +0.0043s | worse |
| `lteNRRCC` | 0.1409s | 0.1438s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.89 MB | 164.0% | 81.1% |
| `f1ap_rel18.6_specs` | 8.46 MB | 102.27 MB | 163.2% | 111.7% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.29 MB | 156.3% | 79.9% |
| `lteNRRCC` | 48.88 MB | 51.39 MB | 211.6% | 160.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0394s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1074s | 0.1048s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0754s | 0.0753s | +0.0001s | worse |
| `lteNRRCC` | 0.1248s | 0.1242s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.02 MB | 8.59 MB | 111.2% | 80.2% |
| `f1ap_rel18.6_specs` | 9.75 MB | 164.20 MB | 160.2% | 160.7% |
| `ngap_rel18.6_specs` | 8.77 MB | 9.15 MB | 177.1% | 161.0% |
| `lteNRRCC` | 73.78 MB | 74.88 MB | 108.0% | 110.2% |
<!-- BENCH_RESULTS_END -->
