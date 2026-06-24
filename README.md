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
Generated: 2026-06-24T23:12:38.476058+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0371s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.1089s | 0.1155s | -0.0066s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0792s | -0.0049s | improved |
| `lteNRRCC` | 0.1183s | 0.1220s | -0.0037s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 21.5% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0352s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0948s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0661s | -0.0008s | improved |
| `lteNRRCC` | 0.1281s | 0.1257s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.36 MB | 36.05 MB | 75.9% | 111.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.19 MB | 106.2% | 105.4% |
| `ngap_rel18.6_specs` | 17.65 MB | 74.61 MB | 107.7% | 107.0% |
| `lteNRRCC` | 48.64 MB | 66.15 MB | 104.7% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0369s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0922s | 0.1095s | -0.0173s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0734s | -0.0080s | improved |
| `lteNRRCC` | 0.1171s | 0.1251s | -0.0080s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 55.74 MB | 81.5% | 110.7% |
| `f1ap_rel18.6_specs` | 35.26 MB | 164.32 MB | 110.3% | 105.3% |
| `ngap_rel18.6_specs` | 24.56 MB | 117.84 MB | 108.0% | 107.0% |
| `lteNRRCC` | 74.26 MB | 102.96 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0211s | 0.0246s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.1134s | 0.0622s | +0.0512s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0441s | +0.0349s | worse |
| `lteNRRCC` | 0.0762s | 0.0773s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.30 MB | 4.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.05 MB | 8.31 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.83 MB | 5.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.47 MB | 5.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0446s | -0.0058s | improved |
| `f1ap_rel18.6_specs` | 0.1088s | 0.1227s | -0.0139s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0954s | -0.0203s | improved |
| `lteNRRCC` | 0.1372s | 0.1457s | -0.0085s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.44 MB | 7.83 MB | 100.3% | 215.5% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.04 MB | 165.6% | 162.0% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.52 MB | 163.4% | 163.7% |
| `lteNRRCC` | 47.51 MB | 70.55 MB | 110.1% | 105.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0429s | -0.0078s | improved |
| `f1ap_rel18.6_specs` | 0.1037s | 0.1241s | -0.0204s | improved |
| `ngap_rel18.6_specs` | 0.0729s | 0.0867s | -0.0138s | improved |
| `lteNRRCC` | 0.1126s | 0.1394s | -0.0268s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.09 MB | 10.30 MB | 137.0% | 136.8% |
| `f1ap_rel18.6_specs` | 10.51 MB | 11.20 MB | 139.6% | 136.8% |
| `ngap_rel18.6_specs` | 10.19 MB | 10.50 MB | 139.8% | 143.1% |
| `lteNRRCC` | 8.74 MB | 74.70 MB | 102.0% | 140.1% |
<!-- BENCH_RESULTS_END -->
