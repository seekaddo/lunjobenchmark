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
Generated: 2026-05-28T23:24:58.655714+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0356s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1153s | 0.1097s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0795s | 0.0759s | +0.0036s | worse |
| `lteNRRCC` | 0.1234s | 0.1196s | +0.0038s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.86 MB | 53.55 MB | 13.9% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.8% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0360s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0916s | 0.0940s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0645s | 0.0663s | -0.0018s | improved |
| `lteNRRCC` | 0.1243s | 0.1283s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.36 MB | 36.59 MB | 100.0% | 110.7% |
| `f1ap_rel18.6_specs` | 22.25 MB | 103.24 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.16 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.41 MB | 65.92 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0412s | -0.0062s | improved |
| `f1ap_rel18.6_specs` | 0.0923s | 0.1027s | -0.0104s | improved |
| `ngap_rel18.6_specs` | 0.0638s | 0.0723s | -0.0085s | improved |
| `lteNRRCC` | 0.1186s | 0.1371s | -0.0185s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.83 MB | 76.7% | 110.3% |
| `f1ap_rel18.6_specs` | 34.54 MB | 164.77 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.20 MB | 117.26 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.91 MB | 102.51 MB | 106.9% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0172s | 0.0417s | -0.0245s | improved |
| `f1ap_rel18.6_specs` | 0.0687s | 0.0670s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0465s | 0.0477s | -0.0012s | improved |
| `lteNRRCC` | 0.0765s | 0.0823s | -0.0058s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.64 MB | 4.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 5.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.80 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.83 MB | 3.73 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0391s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1064s | 0.1129s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0749s | 0.0837s | -0.0088s | improved |
| `lteNRRCC` | 0.1415s | 0.1486s | -0.0071s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.83 MB | 7.34 MB | 236.6% | 161.2% |
| `f1ap_rel18.6_specs` | 8.17 MB | 106.63 MB | 109.8% | 227.0% |
| `ngap_rel18.6_specs` | 7.47 MB | 8.05 MB | 164.6% | 111.8% |
| `lteNRRCC` | 49.77 MB | 68.97 MB | 108.6% | 110.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0400s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1202s | 0.1150s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0829s | 0.0788s | +0.0041s | worse |
| `lteNRRCC` | 0.1294s | 0.1297s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.33 MB | 11.73 MB | 116.7% | 102.9% |
| `f1ap_rel18.6_specs` | 10.26 MB | 11.00 MB | 116.9% | 117.5% |
| `ngap_rel18.6_specs` | 9.65 MB | 10.57 MB | 116.9% | 119.0% |
| `lteNRRCC` | 8.88 MB | 9.24 MB | 116.5% | 239.8% |
<!-- BENCH_RESULTS_END -->
