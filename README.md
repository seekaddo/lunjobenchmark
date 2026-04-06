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
Generated: 2026-04-06T11:04:43.522032+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0372s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1121s | 0.1159s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0790s | -0.0019s | improved |
| `lteNRRCC` | 0.1220s | 0.1231s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 11.3% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 106.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0345s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0943s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0662s | -0.0008s | improved |
| `lteNRRCC` | 0.1167s | 0.1281s | -0.0114s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.32 MB | 36.41 MB | 95.2% | 108.0% |
| `f1ap_rel18.6_specs` | 21.98 MB | 103.32 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 16.68 MB | 74.63 MB | 113.6% | 107.3% |
| `lteNRRCC` | 48.42 MB | 66.34 MB | 103.5% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0327s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0980s | 0.0868s | +0.0112s | worse |
| `ngap_rel18.6_specs` | 0.0683s | 0.0603s | +0.0080s | worse |
| `lteNRRCC` | 0.1150s | 0.1141s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.33 MB | 55.45 MB | 95.0% | 107.7% |
| `f1ap_rel18.6_specs` | 35.16 MB | 164.77 MB | 107.4% | 105.3% |
| `ngap_rel18.6_specs` | 24.12 MB | 117.42 MB | 104.5% | 104.5% |
| `lteNRRCC` | 74.71 MB | 102.16 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0261s | 0.0194s | +0.0067s | worse |
| `f1ap_rel18.6_specs` | 0.0657s | 0.0588s | +0.0069s | worse |
| `ngap_rel18.6_specs` | 0.0564s | 0.0400s | +0.0164s | worse |
| `lteNRRCC` | 0.0760s | 0.0679s | +0.0081s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.30 MB | 3.92 MB | 0.7% | 0.0% |
| `f1ap_rel18.6_specs` | 2.97 MB | 3.17 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 1.94 MB | 224 KB | 0.0% | 0.0% |
| `lteNRRCC` | 3.39 MB | 1.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0382s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1045s | +0.0072s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0731s | +0.0046s | worse |
| `lteNRRCC` | 0.1303s | 0.1357s | -0.0054s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.97 MB | 7.83 MB | 234.7% | 163.2% |
| `f1ap_rel18.6_specs` | 8.54 MB | 8.54 MB | 81.3% | 163.2% |
| `ngap_rel18.6_specs` | 8.35 MB | 8.29 MB | 118.9% | 236.8% |
| `lteNRRCC` | 8.59 MB | 8.59 MB | 113.5% | 225.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0438s | 0.0403s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.1252s | 0.1222s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0876s | 0.0829s | +0.0047s | worse |
| `lteNRRCC` | 0.1315s | 0.1274s | +0.0041s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.52 MB | 10.14 MB | 116.0% | 119.3% |
| `f1ap_rel18.6_specs` | 11.00 MB | 10.90 MB | 120.0% | 240.7% |
| `ngap_rel18.6_specs` | 9.47 MB | 10.37 MB | 165.2% | 117.8% |
| `lteNRRCC` | 9.29 MB | 9.23 MB | 117.0% | 118.5% |
<!-- BENCH_RESULTS_END -->
