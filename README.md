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
Generated: 2026-09-14T16:16:35.663082+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0353s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1102s | +0.0055s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0758s | +0.0028s | worse |
| `lteNRRCC` | 0.1230s | 0.1197s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.67 MB | 53.55 MB | 83.3% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0359s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0961s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0659s | 0.0675s | -0.0016s | improved |
| `lteNRRCC` | 0.1293s | 0.1307s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.28 MB | 21.4% | 107.7% |
| `f1ap_rel18.6_specs` | 21.90 MB | 102.71 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.66 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.23 MB | 65.89 MB | 100.0% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0291s | +0.0074s | worse |
| `f1ap_rel18.6_specs` | 0.0915s | 0.0882s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0623s | +0.0044s | worse |
| `lteNRRCC` | 0.1217s | 0.1023s | +0.0194s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.01 MB | 17.5% | 103.6% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.24 MB | 103.4% | 103.6% |
| `ngap_rel18.6_specs` | 24.20 MB | 117.62 MB | 104.0% | 104.8% |
| `lteNRRCC` | 74.54 MB | 102.57 MB | 101.7% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0202s | +0.0143s | worse |
| `f1ap_rel18.6_specs` | 0.0998s | 0.0696s | +0.0302s | worse |
| `ngap_rel18.6_specs` | 0.0681s | 0.0453s | +0.0228s | worse |
| `lteNRRCC` | 0.1101s | 0.0772s | +0.0329s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.92 MB | 2.62 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.59 MB | 5.52 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.50 MB | 5.06 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.52 MB | 4.19 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0327s | +0.0094s | worse |
| `f1ap_rel18.6_specs` | 0.1185s | 0.0934s | +0.0251s | worse |
| `ngap_rel18.6_specs` | 0.0817s | 0.0653s | +0.0164s | worse |
| `lteNRRCC` | 0.1492s | 0.1126s | +0.0366s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.70 MB | 7.89 MB | 104.4% | 162.1% |
| `f1ap_rel18.6_specs` | 8.87 MB | 106.65 MB | 99.6% | 107.8% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.37 MB | 81.5% | 191.7% |
| `lteNRRCC` | 46.76 MB | 57.83 MB | 105.9% | 108.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0374s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1086s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0758s | +0.0011s | worse |
| `lteNRRCC` | 0.1273s | 0.1271s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 9.65 MB | 177.1% | 88.4% |
| `f1ap_rel18.6_specs` | 11.95 MB | 164.19 MB | 103.1% | 153.5% |
| `ngap_rel18.6_specs` | 9.08 MB | 11.13 MB | 151.8% | 223.1% |
| `lteNRRCC` | 8.87 MB | 98.59 MB | 157.0% | 142.7% |
<!-- BENCH_RESULTS_END -->
