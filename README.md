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
Generated: 2026-07-05T23:07:08.916107+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0361s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1151s | 0.1112s | +0.0039s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0767s | +0.0002s | worse |
| `lteNRRCC` | 0.1220s | 0.1206s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.66 MB | 53.55 MB | 22.8% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0340s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0954s | 0.0935s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0678s | 0.0676s | +0.0002s | worse |
| `lteNRRCC` | 0.1289s | 0.1285s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 36.62 MB | 19.7% | 107.1% |
| `f1ap_rel18.6_specs` | 22.18 MB | 103.25 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.60 MB | 107.7% | 104.5% |
| `lteNRRCC` | 47.83 MB | 66.13 MB | 103.1% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0336s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0884s | 0.0894s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0609s | 0.0617s | -0.0008s | improved |
| `lteNRRCC` | 0.1149s | 0.1151s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.53 MB | 55.68 MB | 84.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.28 MB | 164.40 MB | 110.7% | 105.5% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.52 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.71 MB | 102.59 MB | 105.3% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0196s | +0.0153s | worse |
| `f1ap_rel18.6_specs` | 0.1057s | 0.0734s | +0.0323s | worse |
| `ngap_rel18.6_specs` | 0.0642s | 0.0494s | +0.0148s | worse |
| `lteNRRCC` | 0.1122s | 0.0788s | +0.0334s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.70 MB | 416 KB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.55 MB | 8.27 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.28 MB | 992 KB | 0.0% | 0.0% |
| `lteNRRCC` | 8.05 MB | 4.75 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0492s | -0.0101s | improved |
| `f1ap_rel18.6_specs` | 0.1049s | 0.1184s | -0.0135s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0816s | -0.0064s | improved |
| `lteNRRCC` | 0.1370s | 0.1426s | -0.0056s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.29 MB | 7.30 MB | 82.7% | 175.3% |
| `f1ap_rel18.6_specs` | 8.03 MB | 106.64 MB | 78.3% | 115.5% |
| `ngap_rel18.6_specs` | 8.23 MB | 7.47 MB | 167.7% | 94.3% |
| `lteNRRCC` | 51.13 MB | 51.98 MB | 161.1% | 223.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0441s | -0.0041s | improved |
| `f1ap_rel18.6_specs` | 0.1180s | 0.1303s | -0.0123s | improved |
| `ngap_rel18.6_specs` | 0.0812s | 0.0881s | -0.0069s | improved |
| `lteNRRCC` | 0.1305s | 0.1439s | -0.0134s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 8.72 MB | 155.4% | 156.7% |
| `f1ap_rel18.6_specs` | 10.61 MB | 9.87 MB | 103.4% | 152.2% |
| `ngap_rel18.6_specs` | 9.08 MB | 9.33 MB | 92.1% | 152.2% |
| `lteNRRCC` | 73.78 MB | 74.15 MB | 152.6% | 151.4% |
<!-- BENCH_RESULTS_END -->
