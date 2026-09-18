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
Generated: 2026-09-18T14:18:44.481473+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0357s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1101s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0746s | +0.0047s | worse |
| `lteNRRCC` | 0.1206s | 0.1205s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 15.6% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0355s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0965s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0671s | -0.0010s | improved |
| `lteNRRCC` | 0.1285s | 0.1299s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.41 MB | 80.0% | 103.7% |
| `f1ap_rel18.6_specs` | 22.52 MB | 103.15 MB | 103.2% | 103.5% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.70 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.47 MB | 66.02 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0328s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0980s | 0.0903s | +0.0077s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0632s | +0.0060s | worse |
| `lteNRRCC` | 0.1140s | 0.1158s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 55.47 MB | 43.6% | 104.2% |
| `f1ap_rel18.6_specs` | 35.23 MB | 164.68 MB | 107.7% | 101.8% |
| `ngap_rel18.6_specs` | 24.42 MB | 117.45 MB | 100.0% | 100.0% |
| `lteNRRCC` | 74.70 MB | 102.51 MB | 100.0% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0242s | 0.0339s | -0.0097s | improved |
| `f1ap_rel18.6_specs` | 0.1627s | 0.0751s | +0.0876s | worse |
| `ngap_rel18.6_specs` | 0.0518s | 0.0554s | -0.0036s | improved |
| `lteNRRCC` | 0.0969s | 0.0966s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.56 MB | 7.61 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.91 MB | 8.41 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.19 MB | 8.98 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.78 MB | 5.03 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0389s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1103s | 0.1071s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0778s | 0.0755s | +0.0023s | worse |
| `lteNRRCC` | 0.1408s | 0.1373s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.31 MB | 7.65 MB | 0.0% | 88.7% |
| `f1ap_rel18.6_specs` | 8.51 MB | 8.41 MB | 147.4% | 74.0% |
| `ngap_rel18.6_specs` | 7.84 MB | 7.95 MB | 151.8% | 77.8% |
| `lteNRRCC` | 8.00 MB | 70.51 MB | 153.8% | 144.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0379s | +0.0038s | worse |
| `f1ap_rel18.6_specs` | 0.1179s | 0.1105s | +0.0074s | worse |
| `ngap_rel18.6_specs` | 0.0818s | 0.0754s | +0.0064s | worse |
| `lteNRRCC` | 0.1328s | 0.1274s | +0.0054s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.84 MB | 0.0% | 163.7% |
| `f1ap_rel18.6_specs` | 10.01 MB | 11.30 MB | 91.4% | 221.8% |
| `ngap_rel18.6_specs` | 9.15 MB | 8.74 MB | 171.3% | 94.8% |
| `lteNRRCC` | 69.90 MB | 98.93 MB | 153.0% | 205.1% |
<!-- BENCH_RESULTS_END -->
