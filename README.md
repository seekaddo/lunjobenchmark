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
Generated: 2026-03-14T05:13:01.108958+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0394s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.1168s | 0.1223s | -0.0055s | improved |
| `ngap_rel18.6_specs` | 0.0819s | 0.0837s | -0.0018s | improved |
| `lteNRRCC` | 0.1234s | n/a | n/a | new |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.26 MB | 55.64 MB | 72.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.14 MB | 176.76 MB | 103.4% | 102.9% |
| `ngap_rel18.6_specs` | 22.14 MB | 125.64 MB | 109.1% | 103.9% |
| `lteNRRCC` | 72.14 MB | 99.89 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0370s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0984s | 0.0990s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0697s | 0.0711s | -0.0014s | improved |
| `lteNRRCC` | 0.1330s | n/a | n/a | new |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 37.52 MB | 24.0% | 110.0% |
| `f1ap_rel18.6_specs` | 22.33 MB | 111.79 MB | 105.7% | 104.9% |
| `ngap_rel18.6_specs` | 16.25 MB | 79.80 MB | 110.3% | 106.4% |
| `lteNRRCC` | 47.99 MB | 65.65 MB | 104.3% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0352s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0924s | 0.0942s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0655s | 0.0679s | -0.0024s | improved |
| `lteNRRCC` | 0.1174s | n/a | n/a | new |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 57.87 MB | 100.0% | 109.7% |
| `f1ap_rel18.6_specs` | 34.29 MB | 179.09 MB | 109.7% | 106.9% |
| `ngap_rel18.6_specs` | 24.11 MB | 127.44 MB | 111.5% | 104.4% |
| `lteNRRCC` | 74.80 MB | 102.30 MB | 105.0% | 105.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0235s | 0.0241s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0692s | 0.0648s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0492s | 0.0418s | +0.0074s | worse |
| `lteNRRCC` | 0.0774s | n/a | n/a | new |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 4.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.88 MB | 3.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.75 MB | 4.09 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.48 MB | 4.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0431s | 0.0404s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1177s | 0.1147s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0848s | 0.0817s | +0.0031s | worse |
| `lteNRRCC` | 0.1301s | n/a | n/a | new |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.92 MB | 7.88 MB | 112.4% | 102.0% |
| `f1ap_rel18.6_specs` | 8.70 MB | 8.20 MB | 109.2% | 163.9% |
| `ngap_rel18.6_specs` | 8.07 MB | 8.07 MB | 78.7% | 162.2% |
| `lteNRRCC` | 8.10 MB | 70.53 MB | 89.8% | 108.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0380s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1191s | -0.0086s | improved |
| `ngap_rel18.6_specs` | 0.0779s | 0.0778s | +0.0001s | worse |
| `lteNRRCC` | 0.1295s | n/a | n/a | new |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.52 MB | 10.20 MB | 161.0% | 97.7% |
| `f1ap_rel18.6_specs` | 11.27 MB | 179.13 MB | 230.3% | 115.2% |
| `ngap_rel18.6_specs` | 8.91 MB | 8.85 MB | 92.0% | 95.4% |
| `lteNRRCC` | 9.67 MB | 98.90 MB | 232.6% | 114.0% |
<!-- BENCH_RESULTS_END -->
