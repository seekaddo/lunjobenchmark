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
Generated: 2026-08-05T23:07:15.934048+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0354s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1127s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0768s | -0.0012s | improved |
| `lteNRRCC` | 0.1185s | 0.1207s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 90.0% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.6% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0263s | +0.0079s | worse |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0722s | +0.0211s | worse |
| `ngap_rel18.6_specs` | 0.0646s | 0.0496s | +0.0150s | worse |
| `lteNRRCC` | 0.1323s | 0.0965s | +0.0358s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.28 MB | 35.99 MB | 17.9% | 103.8% |
| `f1ap_rel18.6_specs` | 21.87 MB | 103.17 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.29 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.77 MB | 66.51 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0342s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0997s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0638s | 0.0679s | -0.0041s | improved |
| `lteNRRCC` | 0.1170s | 0.1216s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 55.85 MB | 83.3% | 107.7% |
| `f1ap_rel18.6_specs` | 35.17 MB | 164.19 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.20 MB | 117.80 MB | 108.7% | 104.9% |
| `lteNRRCC` | 74.98 MB | 102.78 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0275s | +0.0139s | worse |
| `f1ap_rel18.6_specs` | 0.1187s | 0.0744s | +0.0443s | worse |
| `ngap_rel18.6_specs` | 0.0568s | 0.0523s | +0.0045s | worse |
| `lteNRRCC` | 0.1181s | 0.0805s | +0.0376s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.28 MB | 7.09 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.62 MB | 7.64 MB | 0.0% | 1.4% |
| `ngap_rel18.6_specs` | 5.09 MB | 6.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.95 MB | 5.09 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0375s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.0938s | 0.1053s | -0.0115s | improved |
| `ngap_rel18.6_specs` | 0.0656s | 0.0726s | -0.0070s | improved |
| `lteNRRCC` | 0.1150s | 0.1438s | -0.0288s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.97 MB | 0.0% | 141.6% |
| `f1ap_rel18.6_specs` | 8.67 MB | 8.73 MB | 136.6% | 136.2% |
| `ngap_rel18.6_specs` | 8.15 MB | 8.30 MB | 139.0% | 139.0% |
| `lteNRRCC` | 49.52 MB | 54.07 MB | 118.1% | 137.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0386s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.1068s | 0.1139s | -0.0071s | improved |
| `ngap_rel18.6_specs` | 0.0717s | 0.0791s | -0.0074s | improved |
| `lteNRRCC` | 0.1137s | 0.1293s | -0.0156s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.91 MB | 0.0% | 100.3% |
| `f1ap_rel18.6_specs` | 10.31 MB | 154.58 MB | 106.5% | 190.9% |
| `ngap_rel18.6_specs` | 9.56 MB | 10.51 MB | 207.4% | 95.4% |
| `lteNRRCC` | 72.97 MB | 79.65 MB | 193.8% | 191.7% |
<!-- BENCH_RESULTS_END -->
