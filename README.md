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
Generated: 2026-06-15T23:51:49.058882+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0353s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1099s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0740s | 0.0758s | -0.0018s | improved |
| `lteNRRCC` | 0.1164s | 0.1193s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 20.4% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0262s | 0.0364s | -0.0102s | improved |
| `f1ap_rel18.6_specs` | 0.0723s | 0.0972s | -0.0249s | improved |
| `ngap_rel18.6_specs` | 0.0505s | 0.0692s | -0.0187s | improved |
| `lteNRRCC` | 0.0970s | 0.1282s | -0.0312s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.31 MB | 36.64 MB | 90.9% | 113.6% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.39 MB | 104.0% | 104.4% |
| `ngap_rel18.6_specs` | 19.28 MB | 74.63 MB | 115.0% | 105.9% |
| `lteNRRCC` | 48.68 MB | 65.86 MB | 104.2% | 103.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0344s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0952s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0668s | 0.0642s | +0.0026s | worse |
| `lteNRRCC` | 0.1279s | 0.1162s | +0.0117s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.56 MB | 88.9% | 106.9% |
| `f1ap_rel18.6_specs` | 34.25 MB | 163.73 MB | 109.7% | 103.4% |
| `ngap_rel18.6_specs` | 24.13 MB | 116.66 MB | 111.5% | 107.0% |
| `lteNRRCC` | 74.82 MB | 102.96 MB | 104.7% | 104.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0276s | 0.0261s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0875s | 0.0977s | -0.0102s | improved |
| `ngap_rel18.6_specs` | 0.0642s | 0.0592s | +0.0050s | worse |
| `lteNRRCC` | 0.1038s | 0.1019s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.53 MB | 8.66 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 10.09 MB | 3.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.70 MB | 8.34 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.56 MB | 3.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0476s | -0.0076s | improved |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1186s | -0.0101s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0803s | -0.0053s | improved |
| `lteNRRCC` | 0.1277s | 0.1426s | -0.0149s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.74 MB | 7.68 MB | 82.2% | 83.5% |
| `f1ap_rel18.6_specs` | 8.36 MB | 8.64 MB | 165.7% | 117.5% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.30 MB | 163.0% | 118.7% |
| `lteNRRCC` | 8.47 MB | 69.16 MB | 120.8% | 236.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0321s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.1021s | 0.0814s | +0.0207s | worse |
| `ngap_rel18.6_specs` | 0.0706s | 0.0561s | +0.0145s | worse |
| `lteNRRCC` | 0.1117s | 0.0873s | +0.0244s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.25 MB | 9.00 MB | 140.9% | 94.2% |
| `f1ap_rel18.6_specs` | 10.08 MB | 164.18 MB | 103.9% | 103.7% |
| `ngap_rel18.6_specs` | 10.37 MB | 10.37 MB | 142.5% | 141.1% |
| `lteNRRCC` | 9.42 MB | 80.01 MB | 135.3% | 141.4% |
<!-- BENCH_RESULTS_END -->
