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
Generated: 2026-03-28T10:39:41.855010+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0369s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1147s | -0.0056s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0785s | -0.0035s | improved |
| `lteNRRCC` | 0.1174s | 0.1218s | -0.0044s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.80 MB | 53.55 MB | 7.4% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0364s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0969s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0669s | 0.0681s | -0.0012s | improved |
| `lteNRRCC` | 0.1290s | 0.1309s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.72 MB | 92.3% | 107.1% |
| `f1ap_rel18.6_specs` | 22.34 MB | 102.91 MB | 109.1% | 103.4% |
| `ngap_rel18.6_specs` | 16.75 MB | 74.71 MB | 107.4% | 104.5% |
| `lteNRRCC` | 48.60 MB | 66.37 MB | 104.7% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0357s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0901s | 0.0893s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0621s | 0.0607s | +0.0014s | worse |
| `lteNRRCC` | 0.1166s | 0.1134s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.02 MB | 55.74 MB | 31.5% | 111.1% |
| `f1ap_rel18.6_specs` | 34.80 MB | 164.18 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.36 MB | 117.32 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.27 MB | 102.70 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0221s | 0.0234s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0648s | 0.0608s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0442s | 0.0400s | +0.0042s | worse |
| `lteNRRCC` | 0.0710s | 0.0682s | +0.0028s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.66 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.58 MB | 5.72 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.80 MB | 3.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.61 MB | 3.77 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0413s | 0.0411s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1118s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0785s | 0.0845s | -0.0060s | improved |
| `lteNRRCC` | 0.1420s | 0.1286s | +0.0134s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.56 MB | 142.8% | 77.3% |
| `f1ap_rel18.6_specs` | 8.61 MB | 8.61 MB | 153.0% | 101.1% |
| `ngap_rel18.6_specs` | 7.98 MB | 7.91 MB | 76.5% | 91.5% |
| `lteNRRCC` | 51.33 MB | 53.70 MB | 209.9% | 150.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0383s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1090s | 0.1122s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0776s | -0.0014s | improved |
| `lteNRRCC` | 0.1348s | 0.1315s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.72 MB | 9.01 MB | 0.0% | 146.3% |
| `f1ap_rel18.6_specs` | 10.24 MB | 164.20 MB | 110.0% | 171.9% |
| `ngap_rel18.6_specs` | 9.02 MB | 7.30 MB | 157.3% | 213.1% |
| `lteNRRCC` | 9.87 MB | 85.70 MB | 230.3% | 188.4% |
<!-- BENCH_RESULTS_END -->
