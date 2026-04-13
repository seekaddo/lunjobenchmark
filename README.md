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
Generated: 2026-04-13T11:22:35.563582+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0367s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1177s | 0.1143s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0813s | 0.0780s | +0.0033s | worse |
| `lteNRRCC` | 0.1246s | 0.1219s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 6.2% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 115.4% | 105.6% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0336s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0963s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0675s | -0.0018s | improved |
| `lteNRRCC` | 0.1287s | 0.1280s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.41 MB | 92.3% | 110.7% |
| `f1ap_rel18.6_specs` | 22.41 MB | 103.11 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.19 MB | 111.1% | 107.0% |
| `lteNRRCC` | 48.34 MB | 66.32 MB | 104.6% | 105.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0351s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0928s | 0.0936s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0646s | 0.0642s | +0.0004s | worse |
| `lteNRRCC` | 0.1262s | 0.1265s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.42 MB | 96.2% | 110.3% |
| `f1ap_rel18.6_specs` | 35.19 MB | 164.35 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.40 MB | 107.4% | 106.8% |
| `lteNRRCC` | 74.39 MB | 102.80 MB | 103.1% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0323s | 0.0218s | +0.0105s | worse |
| `f1ap_rel18.6_specs` | 0.0565s | 0.0643s | -0.0078s | improved |
| `ngap_rel18.6_specs` | 0.0411s | 0.0407s | +0.0004s | worse |
| `lteNRRCC` | 0.0684s | 0.0685s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.77 MB | 3.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.94 MB | 4.77 MB | 1.3% | 0.0% |
| `ngap_rel18.6_specs` | 4.84 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.00 MB | 4.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0448s | 0.0379s | +0.0069s | worse |
| `f1ap_rel18.6_specs` | 0.1141s | 0.1044s | +0.0097s | worse |
| `ngap_rel18.6_specs` | 0.0824s | 0.0743s | +0.0081s | worse |
| `lteNRRCC` | 0.1289s | 0.1357s | -0.0068s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.82 MB | 7.84 MB | 163.6% | 159.6% |
| `f1ap_rel18.6_specs` | 8.85 MB | 8.84 MB | 114.7% | 115.6% |
| `ngap_rel18.6_specs` | 8.10 MB | 8.29 MB | 163.0% | 160.4% |
| `lteNRRCC` | 8.34 MB | 8.59 MB | 161.1% | 235.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0374s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1137s | 0.1080s | +0.0057s | worse |
| `ngap_rel18.6_specs` | 0.0787s | 0.0753s | +0.0034s | worse |
| `lteNRRCC` | 0.1287s | 0.1234s | +0.0053s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.93 MB | 10.96 MB | 153.0% | 226.6% |
| `f1ap_rel18.6_specs` | 11.63 MB | 9.74 MB | 109.9% | 161.9% |
| `ngap_rel18.6_specs` | 8.76 MB | 8.95 MB | 86.9% | 161.9% |
| `lteNRRCC` | 8.24 MB | 94.57 MB | 113.9% | 106.3% |
<!-- BENCH_RESULTS_END -->
