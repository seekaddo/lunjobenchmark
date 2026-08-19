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
Generated: 2026-08-19T22:30:45.890150+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0352s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1135s | 0.1119s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0769s | +0.0002s | worse |
| `lteNRRCC` | 0.1219s | 0.1210s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 82.6% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0345s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0964s | 0.0932s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0693s | 0.0654s | +0.0039s | worse |
| `lteNRRCC` | 0.1318s | 0.1276s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.57 MB | 73.3% | 103.7% |
| `f1ap_rel18.6_specs` | 22.26 MB | 102.70 MB | 106.2% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.68 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.04 MB | 65.93 MB | 103.1% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0336s | +0.0038s | worse |
| `f1ap_rel18.6_specs` | 0.1036s | 0.0902s | +0.0134s | worse |
| `ngap_rel18.6_specs` | 0.0712s | 0.0626s | +0.0086s | worse |
| `lteNRRCC` | 0.1187s | 0.1162s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.56 MB | 55.71 MB | 20.2% | 104.0% |
| `f1ap_rel18.6_specs` | 34.70 MB | 163.50 MB | 103.8% | 101.7% |
| `ngap_rel18.6_specs` | 23.79 MB | 117.82 MB | 104.8% | 102.3% |
| `lteNRRCC` | 74.39 MB | 102.36 MB | 101.8% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0188s | 0.0442s | -0.0254s | improved |
| `f1ap_rel18.6_specs` | 0.0693s | 0.0833s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0471s | 0.0644s | -0.0173s | improved |
| `lteNRRCC` | 0.0832s | 0.1117s | -0.0285s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.34 MB | 4.44 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.06 MB | 9.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.50 MB | 8.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.44 MB | 4.44 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0395s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1094s | 0.1077s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0761s | +0.0010s | worse |
| `lteNRRCC` | 0.1415s | 0.1380s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.82 MB | 0.0% | 111.0% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.41 MB | 91.1% | 93.2% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.00 MB | 107.4% | 101.4% |
| `lteNRRCC` | 51.84 MB | 51.88 MB | 108.5% | 156.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0425s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.1191s | 0.1256s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0831s | 0.0821s | +0.0010s | worse |
| `lteNRRCC` | 0.1170s | 0.1304s | -0.0134s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.21 MB | 0.0% | 129.3% |
| `f1ap_rel18.6_specs` | 10.43 MB | 151.29 MB | 195.6% | 131.9% |
| `ngap_rel18.6_specs` | 10.38 MB | 10.05 MB | 128.5% | 106.6% |
| `lteNRRCC` | 9.16 MB | 74.15 MB | 129.4% | 129.2% |
<!-- BENCH_RESULTS_END -->
