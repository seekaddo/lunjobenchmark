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
Generated: 2026-04-19T10:50:15.985173+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0372s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1130s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0775s | 0.0790s | -0.0015s | improved |
| `lteNRRCC` | 0.1220s | 0.1216s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 6.9% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0312s | 0.0343s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0930s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0641s | 0.0669s | -0.0028s | improved |
| `lteNRRCC` | 0.1151s | 0.1298s | -0.0147s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.36 MB | 36.25 MB | 90.5% | 108.3% |
| `f1ap_rel18.6_specs` | 22.09 MB | 103.06 MB | 111.1% | 103.7% |
| `ngap_rel18.6_specs` | 16.57 MB | 73.84 MB | 113.6% | 107.5% |
| `lteNRRCC` | 48.77 MB | 66.51 MB | 103.6% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0274s | +0.0078s | worse |
| `f1ap_rel18.6_specs` | 0.0941s | 0.0765s | +0.0176s | worse |
| `ngap_rel18.6_specs` | 0.0651s | 0.0526s | +0.0125s | worse |
| `lteNRRCC` | 0.1287s | 0.1075s | +0.0212s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.56 MB | 30.9% | 110.3% |
| `f1ap_rel18.6_specs` | 34.29 MB | 164.71 MB | 112.5% | 105.2% |
| `ngap_rel18.6_specs` | 24.35 MB | 117.69 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.10 MB | 102.82 MB | 104.7% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0240s | 0.0228s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0626s | 0.0610s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0444s | 0.0423s | +0.0021s | worse |
| `lteNRRCC` | 0.0685s | 0.0708s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.12 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.11 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.75 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0415s | -0.0081s | improved |
| `f1ap_rel18.6_specs` | 0.0937s | 0.1112s | -0.0175s | improved |
| `ngap_rel18.6_specs` | 0.0671s | 0.0787s | -0.0116s | improved |
| `lteNRRCC` | 0.1111s | 0.1415s | -0.0304s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.72 MB | 7.86 MB | 209.5% | 128.7% |
| `f1ap_rel18.6_specs` | 8.39 MB | 106.64 MB | 209.2% | 105.3% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.42 MB | 101.0% | 98.4% |
| `lteNRRCC` | 49.51 MB | 56.21 MB | 141.2% | 103.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0383s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1077s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0763s | 0.0799s | -0.0036s | improved |
| `lteNRRCC` | 0.1243s | 0.1266s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.65 MB | 8.45 MB | 168.2% | 164.7% |
| `f1ap_rel18.6_specs` | 9.55 MB | 154.97 MB | 82.0% | 108.8% |
| `ngap_rel18.6_specs` | 10.44 MB | 8.89 MB | 237.3% | 165.8% |
| `lteNRRCC` | 9.36 MB | 98.59 MB | 235.2% | 159.2% |
<!-- BENCH_RESULTS_END -->
