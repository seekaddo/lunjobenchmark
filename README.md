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
Generated: 2026-10-14T14:58:21.400979+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0378s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1183s | 0.1165s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0801s | +0.0002s | worse |
| `lteNRRCC` | 0.1241s | 0.1241s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 78.3% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0343s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0997s | 0.0948s | +0.0049s | worse |
| `ngap_rel18.6_specs` | 0.0704s | 0.0657s | +0.0047s | worse |
| `lteNRRCC` | 0.1211s | 0.1292s | -0.0081s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.64 MB | 81.8% | 103.8% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.20 MB | 103.6% | 101.7% |
| `ngap_rel18.6_specs` | 18.11 MB | 74.54 MB | 104.5% | 102.3% |
| `lteNRRCC` | 48.61 MB | 65.96 MB | 101.8% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0235s | +0.0106s | worse |
| `f1ap_rel18.6_specs` | 0.0908s | 0.0642s | +0.0266s | worse |
| `ngap_rel18.6_specs` | 0.0631s | 0.0441s | +0.0190s | worse |
| `lteNRRCC` | 0.1188s | 0.0790s | +0.0398s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 54.91 MB | 8.8% | 107.7% |
| `f1ap_rel18.6_specs` | 34.62 MB | 164.67 MB | 103.6% | 101.8% |
| `ngap_rel18.6_specs` | 22.60 MB | 117.78 MB | 104.3% | 102.4% |
| `lteNRRCC` | 74.43 MB | 102.85 MB | 101.7% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0321s | 0.0300s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1367s | -0.0221s | improved |
| `ngap_rel18.6_specs` | 0.0725s | 0.0741s | -0.0016s | improved |
| `lteNRRCC` | 0.0857s | 0.1015s | -0.0158s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.48 MB | 2.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.88 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.89 MB | 2.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.61 MB | 5.19 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0386s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1055s | 0.1069s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0732s | 0.0752s | -0.0020s | improved |
| `lteNRRCC` | 0.1372s | 0.1378s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.16 MB | 7.48 MB | 110.5% | 161.3% |
| `f1ap_rel18.6_specs` | 8.02 MB | 8.35 MB | 160.0% | 158.6% |
| `ngap_rel18.6_specs` | 7.53 MB | 7.53 MB | 80.3% | 79.8% |
| `lteNRRCC` | 51.82 MB | 52.87 MB | 159.2% | 160.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0402s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1152s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0794s | 0.0793s | +0.0001s | worse |
| `lteNRRCC` | 0.1353s | 0.1361s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 8.84 MB | 0.0% | 99.2% |
| `f1ap_rel18.6_specs` | 11.55 MB | 164.17 MB | 228.3% | 216.7% |
| `ngap_rel18.6_specs` | 10.98 MB | 10.67 MB | 224.2% | 216.6% |
| `lteNRRCC` | 73.75 MB | 85.61 MB | 94.3% | 105.0% |
<!-- BENCH_RESULTS_END -->
