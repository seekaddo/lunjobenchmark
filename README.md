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
Generated: 2026-10-09T01:55:11.192714+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0359s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1066s | 0.1135s | -0.0069s | improved |
| `ngap_rel18.6_specs` | 0.0734s | 0.0767s | -0.0033s | improved |
| `lteNRRCC` | 0.1171s | 0.1201s | -0.0030s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 72.0% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0290s | 0.0333s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.0851s | 0.0934s | -0.0083s | improved |
| `ngap_rel18.6_specs` | 0.0592s | 0.0635s | -0.0043s | improved |
| `lteNRRCC` | 0.1051s | 0.1132s | -0.0081s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 36.43 MB | 69.6% | 104.5% |
| `f1ap_rel18.6_specs` | 22.07 MB | 103.38 MB | 108.3% | 102.0% |
| `ngap_rel18.6_specs` | 18.17 MB | 73.39 MB | 105.0% | 100.0% |
| `lteNRRCC` | 47.95 MB | 66.20 MB | 100.0% | 101.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0219s | 0.0350s | -0.0131s | improved |
| `f1ap_rel18.6_specs` | 0.0820s | 0.0956s | -0.0136s | improved |
| `ngap_rel18.6_specs` | 0.0522s | 0.0709s | -0.0187s | improved |
| `lteNRRCC` | 0.0813s | 0.1193s | -0.0380s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 55.86 MB | 72.2% | 105.6% |
| `f1ap_rel18.6_specs` | 34.29 MB | 164.22 MB | 105.3% | 102.1% |
| `ngap_rel18.6_specs` | 24.32 MB | 117.34 MB | 106.7% | 100.0% |
| `lteNRRCC` | 74.40 MB | 102.59 MB | 100.0% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0458s | -0.0101s | improved |
| `f1ap_rel18.6_specs` | 0.0879s | 0.0736s | +0.0143s | worse |
| `ngap_rel18.6_specs` | 0.0701s | 0.0440s | +0.0261s | worse |
| `lteNRRCC` | 0.1043s | 0.0755s | +0.0288s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.67 MB | 8.55 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.73 MB | 7.25 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.20 MB | 7.36 MB | 0.0% | 0.0% |
| `lteNRRCC` | 18.64 MB | 6.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0443s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1124s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0783s | 0.0759s | +0.0024s | worse |
| `lteNRRCC` | 0.1412s | 0.1401s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.82 MB | 7.46 MB | 0.0% | 155.5% |
| `f1ap_rel18.6_specs` | 8.43 MB | 8.36 MB | 76.3% | 157.1% |
| `ngap_rel18.6_specs` | 8.07 MB | 7.82 MB | 112.6% | 157.0% |
| `lteNRRCC` | 8.43 MB | 53.71 MB | 220.6% | 110.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0402s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1144s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0780s | 0.0802s | -0.0022s | improved |
| `lteNRRCC` | 0.1284s | 0.1288s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.15 MB | 10.64 MB | 0.0% | 205.5% |
| `f1ap_rel18.6_specs` | 9.46 MB | 10.63 MB | 81.4% | 108.0% |
| `ngap_rel18.6_specs` | 10.62 MB | 10.55 MB | 103.0% | 235.2% |
| `lteNRRCC` | 8.86 MB | 72.45 MB | 154.3% | 157.6% |
<!-- BENCH_RESULTS_END -->
