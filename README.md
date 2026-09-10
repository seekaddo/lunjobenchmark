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
Generated: 2026-09-10T00:00:02.711753+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0349s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1110s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0767s | +0.0009s | worse |
| `lteNRRCC` | 0.1213s | 0.1207s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.49 MB | 53.55 MB | 12.8% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0367s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0984s | -0.0052s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0683s | -0.0022s | improved |
| `lteNRRCC` | 0.1281s | 0.1297s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.49 MB | 36.59 MB | 76.9% | 103.7% |
| `f1ap_rel18.6_specs` | 22.39 MB | 103.38 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.88 MB | 73.79 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.75 MB | 66.21 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0299s | +0.0055s | worse |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0782s | +0.0168s | worse |
| `ngap_rel18.6_specs` | 0.0654s | 0.0530s | +0.0124s | worse |
| `lteNRRCC` | 0.1199s | 0.1015s | +0.0184s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 55.65 MB | 80.8% | 107.4% |
| `f1ap_rel18.6_specs` | 34.78 MB | 164.30 MB | 103.4% | 103.6% |
| `ngap_rel18.6_specs` | 23.75 MB | 117.79 MB | 104.2% | 104.8% |
| `lteNRRCC` | 74.78 MB | 102.90 MB | 101.7% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0469s | 0.0331s | +0.0138s | worse |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0934s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0614s | 0.0509s | +0.0105s | worse |
| `lteNRRCC` | 0.1009s | 0.0998s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.98 MB | 6.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 8.28 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 1.80 MB | 9.03 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.70 MB | 48 KB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0399s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1045s | 0.1125s | -0.0080s | improved |
| `ngap_rel18.6_specs` | 0.0731s | 0.0772s | -0.0041s | improved |
| `lteNRRCC` | 0.1362s | 0.1444s | -0.0082s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.57 MB | 7.34 MB | 190.5% | 169.0% |
| `f1ap_rel18.6_specs` | 7.97 MB | 8.67 MB | 82.6% | 222.4% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.68 MB | 81.2% | 117.8% |
| `lteNRRCC` | 51.83 MB | 70.55 MB | 108.0% | 165.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0421s | -0.0037s | improved |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1261s | -0.0160s | improved |
| `ngap_rel18.6_specs` | 0.0773s | 0.0860s | -0.0087s | improved |
| `lteNRRCC` | 0.1271s | 0.1376s | -0.0105s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.54 MB | 8.59 MB | 223.5% | 80.2% |
| `f1ap_rel18.6_specs` | 9.56 MB | 164.20 MB | 160.5% | 161.8% |
| `ngap_rel18.6_specs` | 8.95 MB | 8.90 MB | 159.7% | 79.4% |
| `lteNRRCC` | 8.69 MB | 101.72 MB | 93.5% | 159.7% |
<!-- BENCH_RESULTS_END -->
