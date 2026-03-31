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
Generated: 2026-03-31T22:41:45.767707+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0380s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1167s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0814s | 0.0807s | +0.0007s | worse |
| `lteNRRCC` | 0.1225s | 0.1241s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 20.2% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 105.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0353s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0919s | 0.0933s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0653s | +0.0000s | flat |
| `lteNRRCC` | 0.1271s | 0.1286s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.21 MB | 36.29 MB | 92.3% | 107.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.02 MB | 112.5% | 105.3% |
| `ngap_rel18.6_specs` | 16.75 MB | 74.32 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.79 MB | 66.39 MB | 104.7% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0346s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0914s | 0.0902s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0627s | 0.0636s | -0.0009s | improved |
| `lteNRRCC` | 0.1177s | 0.1172s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.31 MB | 55.82 MB | 95.8% | 107.1% |
| `f1ap_rel18.6_specs` | 34.62 MB | 163.49 MB | 110.3% | 105.4% |
| `ngap_rel18.6_specs` | 23.98 MB | 117.36 MB | 112.0% | 104.8% |
| `lteNRRCC` | 74.80 MB | 102.66 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0191s | 0.0226s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.0589s | 0.0682s | -0.0093s | improved |
| `ngap_rel18.6_specs` | 0.0401s | 0.0383s | +0.0018s | worse |
| `lteNRRCC` | 0.0687s | 0.0703s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.80 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.12 MB | 4.31 MB | 0.0% | 1.3% |
| `ngap_rel18.6_specs` | 3.97 MB | 4.73 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.66 MB | 4.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0400s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1090s | 0.1110s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0760s | -0.0008s | improved |
| `lteNRRCC` | 0.1374s | 0.1387s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.61 MB | 7.35 MB | 107.5% | 164.6% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.02 MB | 166.6% | 166.3% |
| `ngap_rel18.6_specs` | 7.60 MB | 7.54 MB | 166.7% | 164.7% |
| `lteNRRCC` | 47.12 MB | 70.54 MB | 115.2% | 163.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0445s | -0.0066s | improved |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1290s | -0.0158s | improved |
| `ngap_rel18.6_specs` | 0.0782s | 0.0899s | -0.0117s | improved |
| `lteNRRCC` | 0.1279s | 0.1322s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.52 MB | 8.46 MB | 160.6% | 162.5% |
| `f1ap_rel18.6_specs` | 9.56 MB | 164.20 MB | 80.4% | 161.6% |
| `ngap_rel18.6_specs` | 10.25 MB | 10.44 MB | 118.1% | 231.9% |
| `lteNRRCC` | 8.56 MB | 76.95 MB | 162.2% | 105.0% |
<!-- BENCH_RESULTS_END -->
