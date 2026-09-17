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
Generated: 2026-09-17T14:49:12.196339+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0361s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1095s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0784s | 0.0763s | +0.0021s | worse |
| `lteNRRCC` | 0.1226s | 0.1200s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 76.0% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0202s | 0.0361s | -0.0159s | improved |
| `f1ap_rel18.6_specs` | 0.0550s | 0.0971s | -0.0421s | improved |
| `ngap_rel18.6_specs` | 0.0386s | 0.0680s | -0.0294s | improved |
| `lteNRRCC` | 0.0701s | 0.1306s | -0.0605s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 36.72 MB | 39.4% | 112.5% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.34 MB | 105.6% | 100.0% |
| `ngap_rel18.6_specs` | 18.06 MB | 74.70 MB | 106.7% | 103.8% |
| `lteNRRCC` | 47.99 MB | 66.42 MB | 102.9% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0350s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0886s | 0.0921s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0613s | 0.0639s | -0.0026s | improved |
| `lteNRRCC` | 0.1159s | 0.1270s | -0.0111s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 55.81 MB | 80.0% | 108.0% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.38 MB | 107.1% | 101.9% |
| `ngap_rel18.6_specs` | 23.92 MB | 117.12 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.14 MB | 102.92 MB | 100.0% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0374s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.1171s | 0.0742s | +0.0429s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0502s | +0.0267s | worse |
| `lteNRRCC` | 0.1109s | 0.0943s | +0.0166s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.67 MB | 6.67 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.11 MB | 4.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.17 MB | 5.77 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.47 MB | 5.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0274s | +0.0130s | worse |
| `f1ap_rel18.6_specs` | 0.1083s | 0.0737s | +0.0346s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0530s | +0.0239s | worse |
| `lteNRRCC` | 0.1404s | 0.0883s | +0.0521s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.41 MB | 7.50 MB | 198.8% | 106.5% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.11 MB | 80.5% | 94.9% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.68 MB | 79.8% | 78.8% |
| `lteNRRCC` | 50.81 MB | 52.70 MB | 160.5% | 157.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0410s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1219s | 0.1157s | +0.0062s | worse |
| `ngap_rel18.6_specs` | 0.0845s | 0.0813s | +0.0032s | worse |
| `lteNRRCC` | 0.1393s | 0.1379s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.73 MB | 9.01 MB | 106.1% | 162.3% |
| `f1ap_rel18.6_specs` | 10.58 MB | 164.16 MB | 102.3% | 106.3% |
| `ngap_rel18.6_specs` | 9.35 MB | 9.21 MB | 169.9% | 157.7% |
| `lteNRRCC` | 69.99 MB | 74.14 MB | 111.8% | 106.3% |
<!-- BENCH_RESULTS_END -->
