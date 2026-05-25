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
Generated: 2026-05-25T13:34:45.894154+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0368s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1204s | 0.1127s | +0.0077s | worse |
| `ngap_rel18.6_specs` | 0.0819s | 0.0773s | +0.0046s | worse |
| `lteNRRCC` | 0.1250s | 0.1208s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 27.6% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.5% | 104.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.6% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 106.6% | 105.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0368s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0951s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0647s | 0.0670s | -0.0023s | improved |
| `lteNRRCC` | 0.1237s | 0.1299s | -0.0062s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 36.48 MB | 96.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.25 MB | 103.36 MB | 112.1% | 105.3% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.61 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.71 MB | 66.14 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0382s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.0998s | 0.0945s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0687s | 0.0659s | +0.0028s | worse |
| `lteNRRCC` | 0.1156s | 0.1290s | -0.0134s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.30 MB | 55.69 MB | 86.4% | 107.7% |
| `f1ap_rel18.6_specs` | 34.74 MB | 164.40 MB | 107.4% | 103.4% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.75 MB | 109.1% | 104.7% |
| `lteNRRCC` | 74.64 MB | 102.73 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0504s | 0.0348s | +0.0156s | worse |
| `f1ap_rel18.6_specs` | 0.0865s | 0.0733s | +0.0132s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0591s | +0.0202s | worse |
| `lteNRRCC` | 0.1143s | 0.0932s | +0.0211s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.23 MB | 6.11 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 7.73 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.78 MB | 7.61 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.67 MB | 8.66 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0300s | 0.0413s | -0.0113s | improved |
| `f1ap_rel18.6_specs` | 0.0847s | 0.1118s | -0.0271s | improved |
| `ngap_rel18.6_specs` | 0.0581s | 0.0802s | -0.0221s | improved |
| `lteNRRCC` | 0.0916s | 0.1297s | -0.0381s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 26.82 MB | 0.0% | 116.6% |
| `f1ap_rel18.6_specs` | 22.88 MB | 18.09 MB | 93.8% | 124.9% |
| `ngap_rel18.6_specs` | 11.14 MB | 42.37 MB | 116.8% | 107.5% |
| `lteNRRCC` | 17.93 MB | 28.10 MB | 114.7% | 130.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0454s | -0.0081s | improved |
| `f1ap_rel18.6_specs` | 0.1059s | 0.1309s | -0.0250s | improved |
| `ngap_rel18.6_specs` | 0.0727s | 0.0793s | -0.0066s | improved |
| `lteNRRCC` | 0.1245s | 0.1326s | -0.0081s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.45 MB | 8.39 MB | 158.8% | 161.3% |
| `f1ap_rel18.6_specs` | 11.02 MB | 11.20 MB | 115.9% | 116.5% |
| `ngap_rel18.6_specs` | 8.95 MB | 10.81 MB | 161.9% | 114.0% |
| `lteNRRCC` | 73.44 MB | 77.31 MB | 157.6% | 114.8% |
<!-- BENCH_RESULTS_END -->
