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
Generated: 2026-04-15T22:50:47.612727+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0421s | -0.0064s | improved |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1273s | -0.0143s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0873s | -0.0114s | improved |
| `lteNRRCC` | 0.1208s | 0.1288s | -0.0080s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 5.9% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.3% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0355s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0971s | 0.0963s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0675s | 0.0682s | -0.0007s | improved |
| `lteNRRCC` | 0.1305s | 0.1306s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.06 MB | 36.59 MB | 92.6% | 110.3% |
| `f1ap_rel18.6_specs` | 22.19 MB | 102.93 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.86 MB | 74.23 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.48 MB | 66.51 MB | 106.2% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0349s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1021s | 0.0907s | +0.0114s | worse |
| `ngap_rel18.6_specs` | 0.0716s | 0.0635s | +0.0081s | worse |
| `lteNRRCC` | 0.1189s | 0.1170s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.36 MB | 55.58 MB | 21.0% | 111.1% |
| `f1ap_rel18.6_specs` | 35.15 MB | 164.61 MB | 111.1% | 105.1% |
| `ngap_rel18.6_specs` | 24.45 MB | 117.88 MB | 113.6% | 104.4% |
| `lteNRRCC` | 74.98 MB | 102.46 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0135s | 0.0362s | -0.0227s | improved |
| `f1ap_rel18.6_specs` | 0.0861s | 0.0843s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0588s | 0.0552s | +0.0036s | worse |
| `lteNRRCC` | 0.0790s | 0.0727s | +0.0063s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.61 MB | 4.48 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 5.56 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.62 MB | 8.48 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.70 MB | 7.55 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0397s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1051s | 0.1074s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0739s | 0.0788s | -0.0049s | improved |
| `lteNRRCC` | 0.1368s | 0.1370s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.43 MB | 177.8% | 162.4% |
| `f1ap_rel18.6_specs` | 7.96 MB | 8.09 MB | 166.0% | 81.8% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.36 MB | 165.0% | 78.8% |
| `lteNRRCC` | 46.78 MB | 69.10 MB | 111.4% | 227.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0419s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1207s | -0.0116s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0820s | -0.0049s | improved |
| `lteNRRCC` | 0.1275s | 0.1301s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.72 MB | 8.46 MB | 78.8% | 82.5% |
| `f1ap_rel18.6_specs` | 9.45 MB | 164.20 MB | 81.7% | 160.0% |
| `ngap_rel18.6_specs` | 8.91 MB | 9.02 MB | 162.1% | 98.0% |
| `lteNRRCC` | 73.68 MB | 73.01 MB | 160.4% | 159.9% |
<!-- BENCH_RESULTS_END -->
