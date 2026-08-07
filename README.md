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
Generated: 2026-08-07T22:44:02.035601+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0362s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1077s | 0.1140s | -0.0063s | improved |
| `ngap_rel18.6_specs` | 0.0741s | 0.0775s | -0.0034s | improved |
| `lteNRRCC` | 0.1179s | 0.1208s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 14.4% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.6% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0346s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0928s | 0.0921s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0647s | 0.0650s | -0.0003s | improved |
| `lteNRRCC` | 0.1251s | 0.1267s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.29 MB | 36.48 MB | 80.8% | 107.4% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.31 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.46 MB | 108.0% | 104.7% |
| `lteNRRCC` | 48.60 MB | 65.98 MB | 103.3% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0345s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1002s | 0.0918s | +0.0084s | worse |
| `ngap_rel18.6_specs` | 0.0682s | 0.0641s | +0.0041s | worse |
| `lteNRRCC` | 0.1138s | 0.1187s | -0.0049s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.50 MB | 55.45 MB | 69.2% | 104.0% |
| `f1ap_rel18.6_specs` | 34.49 MB | 164.45 MB | 107.7% | 101.7% |
| `ngap_rel18.6_specs` | 24.22 MB | 117.56 MB | 104.8% | 102.4% |
| `lteNRRCC` | 74.93 MB | 102.68 MB | 101.9% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0336s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1026s | 0.0613s | +0.0413s | worse |
| `ngap_rel18.6_specs` | 0.0640s | 0.0429s | +0.0211s | worse |
| `lteNRRCC` | 0.1170s | 0.0752s | +0.0418s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.53 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 10.17 MB | 5.56 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 9.72 MB | 7.48 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.56 MB | 5.75 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0402s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1050s | 0.1102s | -0.0052s | improved |
| `ngap_rel18.6_specs` | 0.0735s | 0.0770s | -0.0035s | improved |
| `lteNRRCC` | 0.1366s | 0.1398s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.36 MB | 0.0% | 161.8% |
| `f1ap_rel18.6_specs` | 8.18 MB | 8.11 MB | 104.1% | 160.7% |
| `ngap_rel18.6_specs` | 7.92 MB | 7.55 MB | 113.1% | 162.9% |
| `lteNRRCC` | 49.71 MB | 57.77 MB | 170.2% | 159.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0476s | 0.0405s | +0.0071s | worse |
| `f1ap_rel18.6_specs` | 0.1416s | 0.1213s | +0.0203s | worse |
| `ngap_rel18.6_specs` | 0.0963s | 0.0839s | +0.0124s | worse |
| `lteNRRCC` | 0.1384s | 0.1396s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 10.52 MB | 0.0% | 155.3% |
| `f1ap_rel18.6_specs` | 10.57 MB | 149.98 MB | 150.9% | 109.1% |
| `ngap_rel18.6_specs` | 10.38 MB | 10.31 MB | 150.3% | 166.7% |
| `lteNRRCC` | 9.48 MB | 99.77 MB | 203.2% | 151.8% |
<!-- BENCH_RESULTS_END -->
