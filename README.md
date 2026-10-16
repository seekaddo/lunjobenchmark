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
Generated: 2026-10-16T14:42:10.343075+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0349s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1120s | 0.1085s | +0.0035s | worse |
| `ngap_rel18.6_specs` | 0.0768s | 0.0747s | +0.0021s | worse |
| `lteNRRCC` | 0.1198s | 0.1193s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.00 MB | 53.55 MB | 13.3% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0262s | +0.0089s | worse |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0729s | +0.0202s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0509s | +0.0149s | worse |
| `lteNRRCC` | 0.1286s | 0.0968s | +0.0318s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.42 MB | 35.71 MB | 71.4% | 107.7% |
| `f1ap_rel18.6_specs` | 22.27 MB | 102.95 MB | 103.3% | 103.6% |
| `ngap_rel18.6_specs` | 18.06 MB | 74.43 MB | 104.2% | 102.4% |
| `lteNRRCC` | 48.05 MB | 66.18 MB | 101.6% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0285s | +0.0061s | worse |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0758s | +0.0148s | worse |
| `ngap_rel18.6_specs` | 0.0636s | 0.0528s | +0.0108s | worse |
| `lteNRRCC` | 0.1173s | 0.1016s | +0.0157s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.63 MB | 55.12 MB | 72.0% | 103.8% |
| `f1ap_rel18.6_specs` | 35.14 MB | 164.33 MB | 103.6% | 101.8% |
| `ngap_rel18.6_specs` | 23.96 MB | 117.18 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.78 MB | 102.92 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0266s | 0.0206s | +0.0060s | worse |
| `f1ap_rel18.6_specs` | 0.0775s | 0.0862s | -0.0087s | improved |
| `ngap_rel18.6_specs` | 0.0520s | 0.0905s | -0.0385s | improved |
| `lteNRRCC` | 0.0961s | 0.0884s | +0.0077s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.25 MB | 7.69 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.62 MB | 4.08 MB | 0.9% | 0.0% |
| `ngap_rel18.6_specs` | 4.42 MB | 2.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 9.31 MB | 2.03 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0410s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1144s | -0.0045s | improved |
| `ngap_rel18.6_specs` | 0.0764s | 0.0811s | -0.0047s | improved |
| `lteNRRCC` | 0.1387s | 0.1441s | -0.0054s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.72 MB | 7.54 MB | 218.7% | 79.6% |
| `f1ap_rel18.6_specs` | 8.02 MB | 8.09 MB | 161.1% | 186.4% |
| `ngap_rel18.6_specs` | 7.46 MB | 7.96 MB | 162.9% | 106.8% |
| `lteNRRCC` | 48.42 MB | 70.34 MB | 157.2% | 160.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0421s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.1129s | 0.1177s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0837s | -0.0047s | improved |
| `lteNRRCC` | 0.1283s | 0.1368s | -0.0085s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.44 MB | 0.0% | 114.9% |
| `f1ap_rel18.6_specs` | 9.78 MB | 9.54 MB | 159.6% | 160.7% |
| `ngap_rel18.6_specs` | 8.96 MB | 8.87 MB | 77.7% | 160.6% |
| `lteNRRCC` | 9.46 MB | 79.55 MB | 113.6% | 159.6% |
<!-- BENCH_RESULTS_END -->
