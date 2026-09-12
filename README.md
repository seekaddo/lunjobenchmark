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
Generated: 2026-09-12T13:30:03.327103+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0339s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1156s | 0.1078s | +0.0078s | worse |
| `ngap_rel18.6_specs` | 0.0804s | 0.0744s | +0.0060s | worse |
| `lteNRRCC` | 0.1233s | 0.1184s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.66 MB | 53.55 MB | 13.2% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0261s | +0.0083s | worse |
| `f1ap_rel18.6_specs` | 0.0926s | 0.0723s | +0.0203s | worse |
| `ngap_rel18.6_specs` | 0.0646s | 0.0507s | +0.0139s | worse |
| `lteNRRCC` | 0.1274s | 0.0963s | +0.0311s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.60 MB | 35.34 MB | 18.9% | 103.7% |
| `f1ap_rel18.6_specs` | 22.43 MB | 103.17 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.20 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.47 MB | 66.52 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0277s | 0.0335s | -0.0058s | improved |
| `f1ap_rel18.6_specs` | 0.0876s | 0.0910s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0589s | 0.0631s | -0.0042s | improved |
| `lteNRRCC` | 0.0987s | 0.1176s | -0.0189s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 55.73 MB | 62.5% | 110.0% |
| `f1ap_rel18.6_specs` | 34.37 MB | 163.86 MB | 100.0% | 103.9% |
| `ngap_rel18.6_specs` | 24.20 MB | 117.83 MB | 105.6% | 102.8% |
| `lteNRRCC` | 74.34 MB | 102.41 MB | 100.0% | 101.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0316s | 0.0401s | -0.0085s | improved |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0718s | +0.0184s | worse |
| `ngap_rel18.6_specs` | 0.0595s | 0.0690s | -0.0095s | improved |
| `lteNRRCC` | 0.1019s | 0.1065s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.22 MB | 3.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.59 MB | 8.11 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 1.94 MB | 7.94 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.45 MB | 5.70 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0324s | 0.0257s | +0.0067s | worse |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0738s | +0.0200s | worse |
| `ngap_rel18.6_specs` | 0.0655s | 0.0538s | +0.0117s | worse |
| `lteNRRCC` | 0.1123s | 0.0839s | +0.0284s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.83 MB | 0.0% | 121.6% |
| `f1ap_rel18.6_specs` | 8.81 MB | 8.74 MB | 130.7% | 132.6% |
| `ngap_rel18.6_specs` | 8.25 MB | 8.37 MB | 131.7% | 138.0% |
| `lteNRRCC` | 8.55 MB | 67.55 MB | 134.5% | 115.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0397s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1176s | 0.1113s | +0.0063s | worse |
| `ngap_rel18.6_specs` | 0.0804s | 0.0752s | +0.0052s | worse |
| `lteNRRCC` | 0.1300s | 0.1270s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.22 MB | 8.59 MB | 103.9% | 157.7% |
| `f1ap_rel18.6_specs` | 9.68 MB | 158.73 MB | 159.5% | 156.4% |
| `ngap_rel18.6_specs` | 9.24 MB | 9.14 MB | 149.7% | 152.0% |
| `lteNRRCC` | 9.23 MB | 78.31 MB | 106.3% | 104.9% |
<!-- BENCH_RESULTS_END -->
