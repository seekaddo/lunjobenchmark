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
Generated: 2026-09-26T00:28:29.408286+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0383s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1229s | 0.1169s | +0.0060s | worse |
| `ngap_rel18.6_specs` | 0.0861s | 0.0791s | +0.0070s | worse |
| `lteNRRCC` | 0.1288s | 0.1231s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.55 MB | 53.55 MB | 66.7% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 101.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.6% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0356s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0912s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0665s | 0.0651s | +0.0014s | worse |
| `lteNRRCC` | 0.1278s | 0.1234s | +0.0044s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.17 MB | 76.9% | 103.8% |
| `f1ap_rel18.6_specs` | 22.43 MB | 103.30 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.39 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.47 MB | 66.13 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0233s | +0.0104s | worse |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0617s | +0.0289s | worse |
| `ngap_rel18.6_specs` | 0.0639s | 0.0424s | +0.0215s | worse |
| `lteNRRCC` | 0.1166s | 0.0773s | +0.0393s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.87 MB | 71.4% | 107.7% |
| `f1ap_rel18.6_specs` | 34.34 MB | 164.74 MB | 103.6% | 101.8% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.67 MB | 104.2% | 102.5% |
| `lteNRRCC` | 74.75 MB | 102.83 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0252s | +0.0097s | worse |
| `f1ap_rel18.6_specs` | 0.1089s | 0.0960s | +0.0129s | worse |
| `ngap_rel18.6_specs` | 0.0748s | 0.0709s | +0.0039s | worse |
| `lteNRRCC` | 0.1009s | 0.1018s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 896 KB | 2.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.30 MB | 6.25 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 17.53 MB | 8.97 MB | 4.1% | 0.0% |
| `lteNRRCC` | 1.33 MB | 6.77 MB | 0.0% | 0.5% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0419s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1183s | -0.0091s | improved |
| `ngap_rel18.6_specs` | 0.0791s | 0.0786s | +0.0005s | worse |
| `lteNRRCC` | 0.1400s | 0.1435s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 7.34 MB | 108.0% | 81.1% |
| `f1ap_rel18.6_specs` | 8.21 MB | 106.62 MB | 160.5% | 102.9% |
| `ngap_rel18.6_specs` | 8.15 MB | 7.65 MB | 222.6% | 172.9% |
| `lteNRRCC` | 51.81 MB | 51.49 MB | 158.0% | 158.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0296s | +0.0096s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.0810s | +0.0296s | worse |
| `ngap_rel18.6_specs` | 0.0783s | 0.0563s | +0.0220s | worse |
| `lteNRRCC` | 0.1276s | 0.0879s | +0.0397s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.45 MB | 10.39 MB | 110.9% | 230.8% |
| `f1ap_rel18.6_specs` | 9.46 MB | 11.38 MB | 161.7% | 116.0% |
| `ngap_rel18.6_specs` | 8.88 MB | 10.68 MB | 77.8% | 112.0% |
| `lteNRRCC` | 8.42 MB | 98.57 MB | 157.0% | 156.9% |
<!-- BENCH_RESULTS_END -->
