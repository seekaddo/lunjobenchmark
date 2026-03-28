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
Generated: 2026-03-28T22:37:31.795395+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0351s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1204s | 0.1091s | +0.0113s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0750s | +0.0027s | worse |
| `lteNRRCC` | 0.1200s | 0.1174s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.83 MB | 53.55 MB | 10.1% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0363s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0927s | 0.0935s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0650s | 0.0669s | -0.0019s | improved |
| `lteNRRCC` | 0.1266s | 0.1290s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.15 MB | 36.55 MB | 27.9% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.68 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.57 MB | 74.65 MB | 111.5% | 104.3% |
| `lteNRRCC` | 48.66 MB | 65.89 MB | 103.0% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0359s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1014s | 0.0901s | +0.0113s | worse |
| `ngap_rel18.6_specs` | 0.0695s | 0.0621s | +0.0074s | worse |
| `lteNRRCC` | 0.1168s | 0.1166s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.35 MB | 55.62 MB | 26.0% | 107.7% |
| `f1ap_rel18.6_specs` | 34.20 MB | 164.52 MB | 107.1% | 105.1% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.82 MB | 109.1% | 107.0% |
| `lteNRRCC` | 74.00 MB | 102.81 MB | 105.5% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0194s | 0.0221s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.0626s | 0.0648s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0400s | 0.0442s | -0.0042s | improved |
| `lteNRRCC` | 0.0675s | 0.0710s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 4.12 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.78 MB | 4.17 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0413s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1093s | 0.1127s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0785s | -0.0023s | improved |
| `lteNRRCC` | 0.1394s | 0.1420s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.50 MB | 232.1% | 81.2% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.11 MB | 167.4% | 161.8% |
| `ngap_rel18.6_specs` | 7.68 MB | 7.61 MB | 163.6% | 161.7% |
| `lteNRRCC` | 49.25 MB | 49.64 MB | 177.5% | 108.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0388s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1131s | 0.1090s | +0.0041s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0762s | +0.0011s | worse |
| `lteNRRCC` | 0.1262s | 0.1348s | -0.0086s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.71 MB | 10.14 MB | 103.9% | 99.1% |
| `f1ap_rel18.6_specs` | 11.32 MB | 161.47 MB | 103.9% | 161.0% |
| `ngap_rel18.6_specs` | 9.07 MB | 9.01 MB | 156.0% | 178.5% |
| `lteNRRCC` | 73.75 MB | 71.55 MB | 151.8% | 154.5% |
<!-- BENCH_RESULTS_END -->
