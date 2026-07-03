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
Generated: 2026-07-03T23:12:12.471714+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0363s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1094s | 0.1130s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0765s | -0.0010s | improved |
| `lteNRRCC` | 0.1188s | 0.1230s | -0.0042s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 18.9% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.2% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 105.3% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0353s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0927s | 0.0946s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0648s | 0.0676s | -0.0028s | improved |
| `lteNRRCC` | 0.1314s | 0.1298s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.26 MB | 36.55 MB | 84.6% | 114.8% |
| `f1ap_rel18.6_specs` | 22.43 MB | 103.06 MB | 106.2% | 107.1% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.67 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.61 MB | 66.49 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0359s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.0888s | 0.0963s | -0.0075s | improved |
| `ngap_rel18.6_specs` | 0.0620s | 0.0682s | -0.0062s | improved |
| `lteNRRCC` | 0.1157s | 0.1276s | -0.0119s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.57 MB | 75.0% | 111.1% |
| `f1ap_rel18.6_specs` | 35.22 MB | 164.56 MB | 106.9% | 105.6% |
| `ngap_rel18.6_specs` | 24.49 MB | 117.70 MB | 112.5% | 104.9% |
| `lteNRRCC` | 74.95 MB | 101.97 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0208s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.0674s | 0.0679s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0466s | 0.0459s | +0.0007s | worse |
| `lteNRRCC` | 0.0764s | 0.0793s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.55 MB | 4.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.25 MB | 2.98 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.94 MB | 6.03 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.34 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0389s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1100s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0748s | 0.0746s | +0.0002s | worse |
| `lteNRRCC` | 0.1396s | 0.1374s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.69 MB | 7.33 MB | 117.3% | 81.3% |
| `f1ap_rel18.6_specs` | 7.98 MB | 106.65 MB | 83.2% | 105.5% |
| `ngap_rel18.6_specs` | 7.37 MB | 7.48 MB | 164.8% | 166.8% |
| `lteNRRCC` | 51.84 MB | 70.56 MB | 108.9% | 103.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0401s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1293s | 0.1157s | +0.0136s | worse |
| `ngap_rel18.6_specs` | 0.0876s | 0.0806s | +0.0070s | worse |
| `lteNRRCC` | 0.1328s | 0.1302s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.65 MB | 10.74 MB | 165.4% | 194.2% |
| `f1ap_rel18.6_specs` | 10.17 MB | 164.14 MB | 151.1% | 149.3% |
| `ngap_rel18.6_specs` | 9.35 MB | 11.20 MB | 144.5% | 212.3% |
| `lteNRRCC` | 8.63 MB | 83.65 MB | 150.1% | 150.8% |
<!-- BENCH_RESULTS_END -->
