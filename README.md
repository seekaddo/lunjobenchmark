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
Generated: 2026-03-18T22:40:12.325700+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0382s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1255s | 0.1223s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0856s | 0.0836s | +0.0020s | worse |
| `lteNRRCC` | 0.1237s | 0.1224s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.53 MB | 55.78 MB | 105.3% | 106.7% |
| `f1ap_rel18.6_specs` | 32.53 MB | 176.91 MB | 106.7% | 102.8% |
| `ngap_rel18.6_specs` | 22.41 MB | 125.78 MB | 108.3% | 105.7% |
| `lteNRRCC` | 72.33 MB | 100.09 MB | 103.4% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0361s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0977s | 0.0967s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0694s | -0.0002s | improved |
| `lteNRRCC` | 0.1316s | 0.1297s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.37 MB | 37.89 MB | 71.4% | 110.0% |
| `f1ap_rel18.6_specs` | 22.14 MB | 111.86 MB | 111.8% | 104.9% |
| `ngap_rel18.6_specs` | 16.81 MB | 80.45 MB | 110.3% | 106.2% |
| `lteNRRCC` | 48.67 MB | 65.50 MB | 104.4% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0361s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0924s | 0.0950s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0666s | 0.0677s | -0.0011s | improved |
| `lteNRRCC` | 0.1148s | 0.1204s | -0.0056s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.44 MB | 57.79 MB | 69.7% | 110.3% |
| `f1ap_rel18.6_specs` | 34.81 MB | 179.10 MB | 110.0% | 107.0% |
| `ngap_rel18.6_specs` | 24.39 MB | 127.33 MB | 111.5% | 106.8% |
| `lteNRRCC` | 74.19 MB | 102.77 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0259s | 0.0262s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0826s | 0.0890s | -0.0064s | improved |
| `ngap_rel18.6_specs` | 0.0545s | 0.0570s | -0.0025s | improved |
| `lteNRRCC` | 0.0900s | 0.0880s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.52 MB | 4.09 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.11 MB | 3.88 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.11 MB | 2.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.30 MB | 3.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0426s | 0.0403s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1124s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0784s | 0.0793s | -0.0009s | improved |
| `lteNRRCC` | 0.1382s | 0.1352s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.68 MB | 7.55 MB | 78.2% | 154.2% |
| `f1ap_rel18.6_specs` | 8.36 MB | 7.98 MB | 79.9% | 81.5% |
| `ngap_rel18.6_specs` | 7.54 MB | 8.17 MB | 167.2% | 228.7% |
| `lteNRRCC` | 46.86 MB | 56.86 MB | 178.3% | 106.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0398s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1170s | 0.1162s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0826s | 0.0831s | -0.0005s | improved |
| `lteNRRCC` | 0.1293s | 0.1250s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.84 MB | 8.77 MB | 159.0% | 161.6% |
| `f1ap_rel18.6_specs` | 9.96 MB | 177.33 MB | 76.7% | 155.2% |
| `ngap_rel18.6_specs` | 7.89 MB | 10.76 MB | 229.4% | 231.3% |
| `lteNRRCC` | 9.48 MB | 73.45 MB | 103.0% | 155.2% |
<!-- BENCH_RESULTS_END -->
