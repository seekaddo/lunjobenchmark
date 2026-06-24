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
Generated: 2026-06-24T12:23:12.707796+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0364s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1155s | 0.1128s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0792s | 0.0764s | +0.0028s | worse |
| `lteNRRCC` | 0.1220s | 0.1210s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 22.9% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.1% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0355s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0948s | 0.0946s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0661s | 0.0673s | -0.0012s | improved |
| `lteNRRCC` | 0.1257s | 0.1302s | -0.0045s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.29 MB | 36.66 MB | 18.0% | 106.9% |
| `f1ap_rel18.6_specs` | 21.67 MB | 103.41 MB | 106.2% | 105.1% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.62 MB | 107.4% | 104.4% |
| `lteNRRCC` | 48.50 MB | 66.03 MB | 106.5% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0283s | +0.0086s | worse |
| `f1ap_rel18.6_specs` | 0.1095s | 0.0755s | +0.0340s | worse |
| `ngap_rel18.6_specs` | 0.0734s | 0.0523s | +0.0211s | worse |
| `lteNRRCC` | 0.1251s | 0.1005s | +0.0246s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 55.88 MB | 20.2% | 103.7% |
| `f1ap_rel18.6_specs` | 34.78 MB | 164.71 MB | 103.4% | 103.1% |
| `ngap_rel18.6_specs` | 24.47 MB | 117.82 MB | 113.0% | 106.2% |
| `lteNRRCC` | 74.75 MB | 102.83 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0246s | 0.0291s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.0622s | 0.0865s | -0.0243s | improved |
| `ngap_rel18.6_specs` | 0.0441s | 0.0610s | -0.0169s | improved |
| `lteNRRCC` | 0.0773s | 0.0961s | -0.0188s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.16 MB | 7.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.95 MB | 4.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 4.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0446s | 0.0416s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.1227s | 0.1127s | +0.0100s | worse |
| `ngap_rel18.6_specs` | 0.0954s | 0.0787s | +0.0167s | worse |
| `lteNRRCC` | 0.1457s | 0.1321s | +0.0136s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.11 MB | 8.07 MB | 76.9% | 78.4% |
| `f1ap_rel18.6_specs` | 9.04 MB | 106.65 MB | 152.2% | 109.8% |
| `ngap_rel18.6_specs` | 8.80 MB | 8.49 MB | 148.1% | 77.0% |
| `lteNRRCC` | 8.66 MB | 57.70 MB | 149.8% | 111.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0429s | 0.0354s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.1241s | 0.1071s | +0.0170s | worse |
| `ngap_rel18.6_specs` | 0.0867s | 0.0738s | +0.0129s | worse |
| `lteNRRCC` | 0.1394s | 0.1140s | +0.0254s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.65 MB | 8.86 MB | 92.8% | 151.5% |
| `f1ap_rel18.6_specs` | 9.87 MB | 164.14 MB | 154.0% | 107.1% |
| `ngap_rel18.6_specs` | 9.08 MB | 9.27 MB | 147.2% | 76.0% |
| `lteNRRCC` | 8.68 MB | 79.88 MB | 145.9% | 145.9% |
<!-- BENCH_RESULTS_END -->
