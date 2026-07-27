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
Generated: 2026-07-27T13:15:15.096755+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0384s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.1089s | 0.1142s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0740s | 0.0801s | -0.0061s | improved |
| `lteNRRCC` | 0.1188s | 0.1241s | -0.0053s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 75.0% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.6% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0368s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0961s | 0.1001s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0671s | 0.0700s | -0.0029s | improved |
| `lteNRRCC` | 0.1300s | 0.1335s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.11 MB | 72.4% | 103.7% |
| `f1ap_rel18.6_specs` | 22.37 MB | 103.06 MB | 103.1% | 103.5% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.54 MB | 104.0% | 104.7% |
| `lteNRRCC` | 48.20 MB | 66.07 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0296s | 0.0372s | -0.0076s | improved |
| `f1ap_rel18.6_specs` | 0.0764s | 0.1050s | -0.0286s | improved |
| `ngap_rel18.6_specs` | 0.0528s | 0.0696s | -0.0168s | improved |
| `lteNRRCC` | 0.1008s | 0.1232s | -0.0224s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.11 MB | 55.34 MB | 20.4% | 104.5% |
| `f1ap_rel18.6_specs` | 34.25 MB | 164.62 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 24.03 MB | 117.54 MB | 105.0% | 100.0% |
| `lteNRRCC` | 74.58 MB | 102.53 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0228s | 0.0229s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0680s | 0.0687s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0466s | 0.0483s | -0.0017s | improved |
| `lteNRRCC` | 0.0764s | 0.0770s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.73 MB | 4.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.03 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.12 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 3.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0429s | 0.0423s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1200s | 0.1183s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0838s | 0.0834s | +0.0004s | worse |
| `lteNRRCC` | 0.1610s | 0.1472s | +0.0138s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.62 MB | 8.04 MB | 170.8% | 154.6% |
| `f1ap_rel18.6_specs` | 8.91 MB | 106.62 MB | 151.6% | 166.3% |
| `ngap_rel18.6_specs` | 9.06 MB | 8.36 MB | 196.0% | 152.1% |
| `lteNRRCC` | 49.00 MB | 69.09 MB | 153.9% | 107.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0431s | -0.0055s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1249s | -0.0152s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0867s | -0.0098s | improved |
| `lteNRRCC` | 0.1274s | 0.1414s | -0.0140s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 10.08 MB | 0.0% | 108.3% |
| `f1ap_rel18.6_specs` | 9.57 MB | 164.20 MB | 79.4% | 160.8% |
| `ngap_rel18.6_specs` | 8.84 MB | 8.90 MB | 78.5% | 157.2% |
| `lteNRRCC` | 8.50 MB | 90.21 MB | 160.0% | 158.5% |
<!-- BENCH_RESULTS_END -->
