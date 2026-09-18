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
Generated: 2026-09-18T00:01:50.255354+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0373s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1143s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0746s | 0.0784s | -0.0038s | improved |
| `lteNRRCC` | 0.1205s | 0.1226s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 77.3% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 100.0% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0202s | +0.0153s | worse |
| `f1ap_rel18.6_specs` | 0.0965s | 0.0550s | +0.0415s | worse |
| `ngap_rel18.6_specs` | 0.0671s | 0.0386s | +0.0285s | worse |
| `lteNRRCC` | 0.1299s | 0.0701s | +0.0598s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.57 MB | 74.1% | 103.6% |
| `f1ap_rel18.6_specs` | 22.16 MB | 103.07 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.54 MB | 107.7% | 102.3% |
| `lteNRRCC` | 48.46 MB | 66.34 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0331s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0903s | 0.0886s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0632s | 0.0613s | +0.0019s | worse |
| `lteNRRCC` | 0.1158s | 0.1159s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.58 MB | 55.52 MB | 80.0% | 103.7% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.78 MB | 106.9% | 103.7% |
| `ngap_rel18.6_specs` | 24.37 MB | 117.46 MB | 104.2% | 105.0% |
| `lteNRRCC` | 74.15 MB | 102.82 MB | 103.6% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0344s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0751s | 0.1171s | -0.0420s | improved |
| `ngap_rel18.6_specs` | 0.0554s | 0.0769s | -0.0215s | improved |
| `lteNRRCC` | 0.0966s | 0.1109s | -0.0143s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.05 MB | 2.66 MB | 0.0% | 0.5% |
| `f1ap_rel18.6_specs` | 5.02 MB | 6.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.30 MB | 3.64 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.94 MB | 3.03 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0404s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1071s | 0.1083s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0769s | -0.0014s | improved |
| `lteNRRCC` | 0.1373s | 0.1404s | -0.0031s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.48 MB | 0.0% | 162.5% |
| `f1ap_rel18.6_specs` | 8.09 MB | 9.02 MB | 160.5% | 217.6% |
| `ngap_rel18.6_specs` | 7.96 MB | 8.31 MB | 160.4% | 217.8% |
| `lteNRRCC` | 51.81 MB | 60.33 MB | 228.6% | 158.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0417s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1219s | -0.0114s | improved |
| `ngap_rel18.6_specs` | 0.0754s | 0.0845s | -0.0091s | improved |
| `lteNRRCC` | 0.1274s | 0.1393s | -0.0119s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.30 MB | 9.34 MB | 0.0% | 101.7% |
| `f1ap_rel18.6_specs` | 9.82 MB | 9.76 MB | 163.7% | 179.8% |
| `ngap_rel18.6_specs` | 10.45 MB | 9.03 MB | 105.4% | 161.1% |
| `lteNRRCC` | 9.56 MB | 74.91 MB | 233.4% | 116.1% |
<!-- BENCH_RESULTS_END -->
