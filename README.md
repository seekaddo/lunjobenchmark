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
Generated: 2026-07-06T13:52:41.895548+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0366s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.1073s | 0.1151s | -0.0078s | improved |
| `ngap_rel18.6_specs` | 0.0724s | 0.0769s | -0.0045s | improved |
| `lteNRRCC` | 0.1171s | 0.1220s | -0.0049s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 23.8% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 104.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 106.5% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.6% | 104.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0351s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0954s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0708s | 0.0678s | +0.0030s | worse |
| `lteNRRCC` | 0.1286s | 0.1289s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 36.14 MB | 88.5% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.36 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.64 MB | 111.5% | 106.8% |
| `lteNRRCC` | 48.39 MB | 66.24 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0334s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0884s | +0.0079s | worse |
| `ngap_rel18.6_specs` | 0.0675s | 0.0609s | +0.0066s | worse |
| `lteNRRCC` | 0.1157s | 0.1149s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 55.28 MB | 19.6% | 108.0% |
| `f1ap_rel18.6_specs` | 34.61 MB | 164.68 MB | 107.7% | 103.5% |
| `ngap_rel18.6_specs` | 24.43 MB | 117.84 MB | 104.8% | 104.8% |
| `lteNRRCC` | 74.45 MB | 102.10 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0291s | 0.0349s | -0.0058s | improved |
| `f1ap_rel18.6_specs` | 0.0816s | 0.1057s | -0.0241s | improved |
| `ngap_rel18.6_specs` | 0.0479s | 0.0642s | -0.0163s | improved |
| `lteNRRCC` | 0.0772s | 0.1122s | -0.0350s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.22 MB | 3.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.92 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 3.97 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0391s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1155s | 0.1049s | +0.0106s | worse |
| `ngap_rel18.6_specs` | 0.0817s | 0.0752s | +0.0065s | worse |
| `lteNRRCC` | 0.1411s | 0.1370s | +0.0041s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.75 MB | 167.3% | 83.5% |
| `f1ap_rel18.6_specs` | 8.39 MB | 106.55 MB | 165.3% | 165.6% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.09 MB | 81.8% | 165.7% |
| `lteNRRCC` | 51.83 MB | 51.33 MB | 104.9% | 109.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0400s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1180s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0788s | 0.0812s | -0.0024s | improved |
| `lteNRRCC` | 0.1269s | 0.1305s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.55 MB | 9.65 MB | 150.3% | 73.7% |
| `f1ap_rel18.6_specs` | 9.75 MB | 10.91 MB | 156.3% | 92.3% |
| `ngap_rel18.6_specs` | 10.88 MB | 11.26 MB | 199.3% | 183.6% |
| `lteNRRCC` | 8.96 MB | 91.07 MB | 151.2% | 151.9% |
<!-- BENCH_RESULTS_END -->
