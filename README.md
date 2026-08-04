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
Generated: 2026-08-04T12:05:38.821472+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0349s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1095s | 0.1098s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0746s | 0.0752s | -0.0006s | improved |
| `lteNRRCC` | 0.1191s | 0.1194s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 15.3% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.6% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0348s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0965s | 0.0927s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0671s | 0.0653s | +0.0018s | worse |
| `lteNRRCC` | 0.1305s | 0.1256s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.50 MB | 36.61 MB | 21.6% | 107.1% |
| `f1ap_rel18.6_specs` | 22.06 MB | 103.34 MB | 103.0% | 103.4% |
| `ngap_rel18.6_specs` | 17.59 MB | 73.89 MB | 107.7% | 102.2% |
| `lteNRRCC` | 48.53 MB | 66.19 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0360s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0944s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0668s | 0.0660s | +0.0008s | worse |
| `lteNRRCC` | 0.1184s | 0.1283s | -0.0099s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.38 MB | 55.54 MB | 80.8% | 107.4% |
| `f1ap_rel18.6_specs` | 34.57 MB | 164.74 MB | 106.9% | 101.7% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.19 MB | 108.3% | 104.8% |
| `lteNRRCC` | 74.87 MB | 102.71 MB | 101.7% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0252s | 0.0239s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0768s | 0.0716s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0499s | 0.0495s | +0.0004s | worse |
| `lteNRRCC` | 0.0772s | 0.0805s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.30 MB | 4.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.89 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.38 MB | 4.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.23 MB | 4.22 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0407s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1130s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0767s | +0.0021s | worse |
| `lteNRRCC` | 0.1432s | 0.1409s | +0.0023s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.32 MB | 0.0% | 165.8% |
| `f1ap_rel18.6_specs` | 7.87 MB | 7.96 MB | 82.5% | 83.4% |
| `ngap_rel18.6_specs` | 7.97 MB | 7.48 MB | 233.6% | 164.4% |
| `lteNRRCC` | 46.94 MB | 51.26 MB | 158.2% | 107.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0576s | 0.0397s | +0.0179s | worse |
| `f1ap_rel18.6_specs` | 0.1390s | 0.1117s | +0.0273s | worse |
| `ngap_rel18.6_specs` | 0.0982s | 0.0790s | +0.0192s | worse |
| `lteNRRCC` | 0.1365s | 0.1281s | +0.0084s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.57 MB | 0.0% | 105.6% |
| `f1ap_rel18.6_specs` | 11.14 MB | 118.02 MB | 166.9% | 109.7% |
| `ngap_rel18.6_specs` | 10.31 MB | 10.56 MB | 77.6% | 156.3% |
| `lteNRRCC` | 73.77 MB | 81.12 MB | 109.4% | 110.1% |
<!-- BENCH_RESULTS_END -->
