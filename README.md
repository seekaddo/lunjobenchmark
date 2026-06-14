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
Generated: 2026-06-14T12:03:42.973472+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0361s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1118s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0780s | -0.0022s | improved |
| `lteNRRCC` | 0.1208s | 0.1203s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 21.7% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.1% |
| `lteNRRCC` | 72.32 MB | 100.11 MB | 105.2% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0346s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0904s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0657s | 0.0633s | +0.0024s | worse |
| `lteNRRCC` | 0.1269s | 0.1223s | +0.0046s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.36 MB | 36.61 MB | 30.3% | 111.1% |
| `f1ap_rel18.6_specs` | 22.07 MB | 103.46 MB | 106.2% | 103.5% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.16 MB | 107.7% | 107.0% |
| `lteNRRCC` | 48.15 MB | 66.34 MB | 104.7% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0330s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.0962s | 0.0884s | +0.0078s | worse |
| `ngap_rel18.6_specs` | 0.0726s | 0.0656s | +0.0070s | worse |
| `lteNRRCC` | 0.1282s | 0.1176s | +0.0106s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.82 MB | 88.9% | 110.3% |
| `f1ap_rel18.6_specs` | 34.49 MB | 164.60 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.58 MB | 117.58 MB | 111.5% | 106.8% |
| `lteNRRCC` | 74.79 MB | 102.91 MB | 103.1% | 102.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0244s | 0.0216s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.0823s | 0.0805s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0470s | 0.0465s | +0.0005s | worse |
| `lteNRRCC` | 0.0801s | 0.0784s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.75 MB | 4.80 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.62 MB | 5.31 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 4.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.59 MB | 4.05 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0409s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1077s | 0.1081s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0747s | 0.0767s | -0.0020s | improved |
| `lteNRRCC` | 0.1274s | 0.1400s | -0.0126s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.98 MB | 119.6% | 237.5% |
| `f1ap_rel18.6_specs` | 8.23 MB | 8.11 MB | 119.6% | 89.9% |
| `ngap_rel18.6_specs` | 7.47 MB | 8.17 MB | 116.7% | 118.5% |
| `lteNRRCC` | 8.41 MB | 69.16 MB | 119.4% | 161.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0404s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1148s | 0.1169s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0802s | -0.0032s | improved |
| `lteNRRCC` | 0.1262s | 0.1347s | -0.0085s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.58 MB | 8.58 MB | 162.6% | 165.7% |
| `f1ap_rel18.6_specs` | 9.55 MB | 164.18 MB | 161.1% | 235.2% |
| `ngap_rel18.6_specs` | 9.27 MB | 8.94 MB | 105.3% | 165.7% |
| `lteNRRCC` | 72.16 MB | 72.30 MB | 160.1% | 161.7% |
<!-- BENCH_RESULTS_END -->
