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
Generated: 2026-08-06T12:06:26.341888+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0356s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1106s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0760s | 0.0756s | +0.0004s | worse |
| `lteNRRCC` | 0.1202s | 0.1185s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 66.7% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0279s | 0.0342s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0733s | 0.0933s | -0.0200s | improved |
| `ngap_rel18.6_specs` | 0.0510s | 0.0646s | -0.0136s | improved |
| `lteNRRCC` | 0.0974s | 0.1323s | -0.0349s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.11 MB | 36.09 MB | 69.2% | 104.8% |
| `f1ap_rel18.6_specs` | 22.20 MB | 103.14 MB | 104.2% | 102.3% |
| `ngap_rel18.6_specs` | 19.21 MB | 74.43 MB | 100.0% | 100.0% |
| `lteNRRCC` | 48.12 MB | 66.51 MB | 100.0% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0339s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0964s | 0.0930s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0677s | 0.0638s | +0.0039s | worse |
| `lteNRRCC` | 0.1314s | 0.1170s | +0.0144s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.50 MB | 55.29 MB | 95.7% | 106.9% |
| `f1ap_rel18.6_specs` | 33.99 MB | 164.68 MB | 103.2% | 101.7% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.39 MB | 103.8% | 102.3% |
| `lteNRRCC` | 74.92 MB | 102.73 MB | 101.6% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0306s | 0.0414s | -0.0108s | improved |
| `f1ap_rel18.6_specs` | 0.0939s | 0.1187s | -0.0248s | improved |
| `ngap_rel18.6_specs` | 0.0587s | 0.0568s | +0.0019s | worse |
| `lteNRRCC` | 0.1193s | 0.1181s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.23 MB | 7.62 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.84 MB | 5.72 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.05 MB | 7.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.98 MB | 2.59 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0330s | +0.0063s | worse |
| `f1ap_rel18.6_specs` | 0.1086s | 0.0938s | +0.0148s | worse |
| `ngap_rel18.6_specs` | 0.0764s | 0.0656s | +0.0108s | worse |
| `lteNRRCC` | 0.1379s | 0.1150s | +0.0229s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.76 MB | 0.0% | 85.1% |
| `f1ap_rel18.6_specs` | 8.55 MB | 106.65 MB | 0.0% | 110.4% |
| `ngap_rel18.6_specs` | 7.99 MB | 8.05 MB | 83.0% | 84.9% |
| `lteNRRCC` | 51.65 MB | 51.97 MB | 155.8% | 109.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0351s | +0.0063s | worse |
| `f1ap_rel18.6_specs` | 0.1212s | 0.1068s | +0.0144s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0717s | +0.0099s | worse |
| `lteNRRCC` | 0.1372s | 0.1137s | +0.0235s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.65 MB | 0.0% | 78.9% |
| `f1ap_rel18.6_specs` | 10.30 MB | 164.19 MB | 160.7% | 110.5% |
| `ngap_rel18.6_specs` | 9.34 MB | 9.48 MB | 161.0% | 81.5% |
| `lteNRRCC` | 73.09 MB | 74.13 MB | 107.6% | 105.4% |
<!-- BENCH_RESULTS_END -->
