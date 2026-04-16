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
Generated: 2026-04-16T22:52:06.817225+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0404s | -0.0050s | improved |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1223s | -0.0098s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0852s | -0.0107s | improved |
| `lteNRRCC` | 0.1168s | 0.1297s | -0.0129s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 53.55 MB | 25.0% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.2% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0340s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.0921s | 0.0928s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0660s | -0.0007s | improved |
| `lteNRRCC` | 0.1288s | 0.1292s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.12 MB | 96.2% | 110.3% |
| `f1ap_rel18.6_specs` | 22.35 MB | 102.61 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.28 MB | 114.8% | 106.5% |
| `lteNRRCC` | 48.69 MB | 65.68 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0330s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0905s | 0.0890s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0653s | 0.0614s | +0.0039s | worse |
| `lteNRRCC` | 0.1168s | 0.1183s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.40 MB | 20.5% | 110.7% |
| `f1ap_rel18.6_specs` | 34.71 MB | 163.80 MB | 110.3% | 105.3% |
| `ngap_rel18.6_specs` | 24.57 MB | 117.08 MB | 112.0% | 106.8% |
| `lteNRRCC` | 74.93 MB | 102.80 MB | 105.1% | 105.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0190s | 0.0260s | -0.0070s | improved |
| `f1ap_rel18.6_specs` | 0.0619s | 0.0712s | -0.0093s | improved |
| `ngap_rel18.6_specs` | 0.0484s | 0.0425s | +0.0059s | worse |
| `lteNRRCC` | 0.0682s | 0.0671s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.61 MB | 3.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.89 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.12 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.98 MB | 3.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0405s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1061s | 0.1075s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0772s | -0.0034s | improved |
| `lteNRRCC` | 0.1374s | 0.1276s | +0.0098s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.56 MB | 159.9% | 158.5% |
| `f1ap_rel18.6_specs` | 8.17 MB | 106.64 MB | 161.6% | 106.6% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.11 MB | 221.4% | 103.7% |
| `lteNRRCC` | 49.07 MB | 69.61 MB | 157.0% | 156.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0384s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1086s | +0.0058s | worse |
| `ngap_rel18.6_specs` | 0.0794s | 0.0771s | +0.0023s | worse |
| `lteNRRCC` | 0.1294s | 0.1253s | +0.0041s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.78 MB | 8.93 MB | 78.2% | 177.5% |
| `f1ap_rel18.6_specs` | 10.05 MB | 10.05 MB | 157.2% | 152.5% |
| `ngap_rel18.6_specs` | 11.16 MB | 9.26 MB | 211.9% | 156.2% |
| `lteNRRCC` | 8.74 MB | 85.80 MB | 149.8% | 156.6% |
<!-- BENCH_RESULTS_END -->
