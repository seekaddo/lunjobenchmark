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
Generated: 2026-07-05T11:39:39.626527+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0331s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1068s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0740s | +0.0027s | worse |
| `lteNRRCC` | 0.1206s | 0.1179s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 13.0% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0361s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0992s | -0.0057s | improved |
| `ngap_rel18.6_specs` | 0.0676s | 0.0692s | -0.0016s | improved |
| `lteNRRCC` | 0.1285s | 0.1319s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 36.66 MB | 82.1% | 110.3% |
| `f1ap_rel18.6_specs` | 22.42 MB | 103.23 MB | 109.4% | 103.5% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.64 MB | 107.7% | 107.0% |
| `lteNRRCC` | 48.27 MB | 65.85 MB | 104.7% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0358s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0894s | 0.0900s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0617s | 0.0614s | +0.0003s | worse |
| `lteNRRCC` | 0.1151s | 0.1143s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.30 MB | 55.35 MB | 81.5% | 107.4% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.72 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 23.71 MB | 117.59 MB | 108.3% | 107.3% |
| `lteNRRCC` | 74.75 MB | 102.94 MB | 105.3% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0196s | 0.0221s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.0734s | 0.0674s | +0.0060s | worse |
| `ngap_rel18.6_specs` | 0.0494s | 0.0457s | +0.0037s | worse |
| `lteNRRCC` | 0.0788s | 0.0787s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.89 MB | 4.30 MB | 0.3% | 0.0% |
| `f1ap_rel18.6_specs` | 5.02 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.47 MB | 4.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.06 MB | 4.58 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0492s | 0.0420s | +0.0072s | worse |
| `f1ap_rel18.6_specs` | 0.1184s | 0.1188s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0816s | 0.0827s | -0.0011s | improved |
| `lteNRRCC` | 0.1426s | 0.1443s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.80 MB | 7.81 MB | 82.9% | 96.0% |
| `f1ap_rel18.6_specs` | 8.55 MB | 105.37 MB | 161.5% | 110.8% |
| `ngap_rel18.6_specs` | 7.96 MB | 8.18 MB | 90.9% | 82.0% |
| `lteNRRCC` | 47.51 MB | 70.55 MB | 101.3% | 105.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0441s | 0.0448s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1303s | 0.1317s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0881s | 0.0922s | -0.0041s | improved |
| `lteNRRCC` | 0.1439s | 0.1425s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.97 MB | 9.20 MB | 89.9% | 162.5% |
| `f1ap_rel18.6_specs` | 10.16 MB | 164.18 MB | 164.0% | 158.8% |
| `ngap_rel18.6_specs` | 9.41 MB | 9.27 MB | 160.0% | 162.1% |
| `lteNRRCC` | 8.88 MB | 100.15 MB | 158.7% | 106.8% |
<!-- BENCH_RESULTS_END -->
