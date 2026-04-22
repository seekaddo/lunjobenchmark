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
Generated: 2026-04-22T11:14:22.461435+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0379s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1216s | 0.1168s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0843s | 0.0820s | +0.0023s | worse |
| `lteNRRCC` | 0.1275s | 0.1251s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 9.5% | 108.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 108.8% | 104.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 114.8% | 105.4% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 106.3% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0355s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0950s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0661s | -0.0007s | improved |
| `lteNRRCC` | 0.1278s | 0.1291s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 36.49 MB | 88.9% | 110.7% |
| `f1ap_rel18.6_specs` | 22.23 MB | 102.99 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.51 MB | 74.27 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.44 MB | 66.36 MB | 104.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0325s | 0.0355s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.0895s | 0.0948s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0616s | 0.0658s | -0.0042s | improved |
| `lteNRRCC` | 0.1166s | 0.1287s | -0.0121s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.14 MB | 55.80 MB | 96.0% | 107.1% |
| `f1ap_rel18.6_specs` | 34.73 MB | 163.75 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 23.95 MB | 117.12 MB | 112.5% | 104.8% |
| `lteNRRCC` | 74.86 MB | 102.73 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0322s | 0.0245s | +0.0077s | worse |
| `f1ap_rel18.6_specs` | 0.1115s | 0.0646s | +0.0469s | worse |
| `ngap_rel18.6_specs` | 0.0847s | 0.0493s | +0.0354s | worse |
| `lteNRRCC` | 0.1027s | 0.0758s | +0.0269s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.28 MB | 6.67 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.09 MB | 2.95 MB | 1.0% | 0.0% |
| `ngap_rel18.6_specs` | 9.98 MB | 6.05 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.86 MB | 3.70 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0399s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1100s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0767s | -0.0012s | improved |
| `lteNRRCC` | 0.1378s | 0.1402s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.57 MB | 7.57 MB | 156.7% | 161.5% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.11 MB | 82.3% | 165.7% |
| `ngap_rel18.6_specs` | 8.30 MB | 7.88 MB | 116.4% | 180.7% |
| `lteNRRCC` | 48.07 MB | 49.71 MB | 105.3% | 160.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0387s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1146s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0799s | 0.0781s | +0.0018s | worse |
| `lteNRRCC` | 0.1261s | 0.1276s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.46 MB | 8.59 MB | 161.7% | 161.5% |
| `f1ap_rel18.6_specs` | 9.81 MB | 9.56 MB | 93.7% | 81.5% |
| `ngap_rel18.6_specs` | 9.15 MB | 9.02 MB | 97.2% | 161.4% |
| `lteNRRCC` | 73.03 MB | 97.88 MB | 160.7% | 107.1% |
<!-- BENCH_RESULTS_END -->
