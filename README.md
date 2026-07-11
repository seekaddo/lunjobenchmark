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
Generated: 2026-07-11T11:11:41.415803+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0374s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1121s | 0.1143s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0790s | -0.0014s | improved |
| `lteNRRCC` | 0.1215s | 0.1216s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 19.8% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 103.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0313s | 0.0346s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.0922s | 0.0944s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0641s | 0.0667s | -0.0026s | improved |
| `lteNRRCC` | 0.1147s | 0.1289s | -0.0142s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 36.57 MB | 85.7% | 108.3% |
| `f1ap_rel18.6_specs` | 22.43 MB | 102.61 MB | 103.7% | 105.6% |
| `ngap_rel18.6_specs` | 17.68 MB | 74.57 MB | 109.5% | 105.0% |
| `lteNRRCC` | 47.83 MB | 65.96 MB | 103.6% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0296s | 0.0362s | -0.0066s | improved |
| `f1ap_rel18.6_specs` | 0.0765s | 0.0927s | -0.0162s | improved |
| `ngap_rel18.6_specs` | 0.0537s | 0.0653s | -0.0116s | improved |
| `lteNRRCC` | 0.1010s | 0.1210s | -0.0200s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.21 MB | 55.79 MB | 14.5% | 104.3% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.60 MB | 108.0% | 102.1% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.72 MB | 109.5% | 105.7% |
| `lteNRRCC` | 74.42 MB | 102.77 MB | 104.0% | 105.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0255s | 0.0230s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.0896s | 0.0654s | +0.0242s | worse |
| `ngap_rel18.6_specs` | 0.0651s | 0.0485s | +0.0166s | worse |
| `lteNRRCC` | 0.0757s | 0.0761s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.00 MB | 7.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.39 MB | 5.08 MB | 2.1% | 0.0% |
| `ngap_rel18.6_specs` | 6.09 MB | 7.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.66 MB | 7.69 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0394s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1077s | 0.1083s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0737s | +0.0021s | worse |
| `lteNRRCC` | 0.1388s | 0.1373s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.35 MB | 164.5% | 80.8% |
| `f1ap_rel18.6_specs` | 7.98 MB | 8.18 MB | 81.0% | 180.3% |
| `ngap_rel18.6_specs` | 8.00 MB | 7.62 MB | 110.2% | 98.4% |
| `lteNRRCC` | 46.68 MB | 57.21 MB | 106.2% | 109.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0385s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1176s | 0.1090s | +0.0086s | worse |
| `ngap_rel18.6_specs` | 0.0812s | 0.0785s | +0.0027s | worse |
| `lteNRRCC` | 0.1367s | 0.1247s | +0.0120s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.94 MB | 9.72 MB | 170.1% | 97.1% |
| `f1ap_rel18.6_specs` | 10.07 MB | 164.20 MB | 81.8% | 111.7% |
| `ngap_rel18.6_specs` | 10.76 MB | 9.42 MB | 222.1% | 168.4% |
| `lteNRRCC` | 69.80 MB | 99.59 MB | 163.8% | 162.5% |
<!-- BENCH_RESULTS_END -->
