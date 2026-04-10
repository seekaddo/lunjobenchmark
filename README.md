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
Generated: 2026-04-10T11:03:08.295406+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0366s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1184s | 0.1142s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0812s | 0.0778s | +0.0034s | worse |
| `lteNRRCC` | 0.1248s | 0.1219s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.86 MB | 53.55 MB | 24.7% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 105.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.8% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0344s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0938s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0668s | 0.0659s | +0.0009s | worse |
| `lteNRRCC` | 0.1274s | 0.1284s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.41 MB | 88.9% | 106.9% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.86 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 16.72 MB | 74.60 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.66 MB | 66.41 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0331s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0910s | 0.0930s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0625s | 0.0625s | +0.0000s | flat |
| `lteNRRCC` | 0.1161s | 0.1155s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.17 MB | 55.37 MB | 23.5% | 107.1% |
| `f1ap_rel18.6_specs` | 35.12 MB | 164.35 MB | 106.7% | 105.3% |
| `ngap_rel18.6_specs` | 24.13 MB | 117.81 MB | 108.0% | 107.1% |
| `lteNRRCC` | 74.77 MB | 102.62 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0249s | 0.0187s | +0.0062s | worse |
| `f1ap_rel18.6_specs` | 0.0814s | 0.0626s | +0.0188s | worse |
| `ngap_rel18.6_specs` | 0.0694s | 0.0405s | +0.0289s | worse |
| `lteNRRCC` | 0.0910s | 0.0755s | +0.0155s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.58 MB | 7.73 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.52 MB | 8.19 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.39 MB | 7.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.75 MB | 3.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0419s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1145s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0783s | 0.0815s | -0.0032s | improved |
| `lteNRRCC` | 0.1394s | 0.1418s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.81 MB | 164.7% | 92.7% |
| `f1ap_rel18.6_specs` | 8.41 MB | 8.61 MB | 165.1% | 164.7% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.18 MB | 170.4% | 82.5% |
| `lteNRRCC` | 48.39 MB | 69.99 MB | 165.0% | 165.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0428s | 0.0374s | +0.0054s | worse |
| `f1ap_rel18.6_specs` | 0.1187s | 0.1059s | +0.0128s | worse |
| `ngap_rel18.6_specs` | 0.0829s | 0.0745s | +0.0084s | worse |
| `lteNRRCC` | 0.1295s | 0.1234s | +0.0061s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.89 MB | 10.26 MB | 108.2% | 0.0% |
| `f1ap_rel18.6_specs` | 10.56 MB | 10.56 MB | 121.5% | 120.5% |
| `ngap_rel18.6_specs` | 9.47 MB | 9.32 MB | 82.1% | 83.2% |
| `lteNRRCC` | 8.67 MB | 76.62 MB | 81.7% | 163.0% |
<!-- BENCH_RESULTS_END -->
