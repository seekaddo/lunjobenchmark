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
Generated: 2026-05-14T23:03:37.195099+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0374s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1120s | 0.1171s | -0.0051s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0796s | -0.0027s | improved |
| `lteNRRCC` | 0.1204s | 0.1245s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 11.3% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0363s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0991s | -0.0054s | improved |
| `ngap_rel18.6_specs` | 0.0662s | 0.0706s | -0.0044s | improved |
| `lteNRRCC` | 0.1290s | 0.1322s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 36.40 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 22.18 MB | 103.27 MB | 112.5% | 103.4% |
| `ngap_rel18.6_specs` | 16.77 MB | 74.62 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.49 MB | 65.87 MB | 104.6% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0357s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0988s | 0.0933s | +0.0055s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0657s | +0.0035s | worse |
| `lteNRRCC` | 0.1150s | 0.1192s | -0.0042s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.00 MB | 55.77 MB | 76.0% | 111.5% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.77 MB | 107.4% | 103.3% |
| `ngap_rel18.6_specs` | 23.91 MB | 117.36 MB | 109.1% | 102.3% |
| `lteNRRCC` | 74.99 MB | 102.66 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0258s | +0.0095s | worse |
| `f1ap_rel18.6_specs` | 0.0657s | 0.0801s | -0.0144s | improved |
| `ngap_rel18.6_specs` | 0.0438s | 0.0510s | -0.0072s | improved |
| `lteNRRCC` | 0.0780s | 0.0794s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.69 MB | 3.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.06 MB | 4.30 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.78 MB | 4.30 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.22 MB | 3.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0392s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1138s | 0.1111s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0762s | 0.0748s | +0.0014s | worse |
| `lteNRRCC` | 0.1398s | 0.1388s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.68 MB | 7.62 MB | 150.8% | 79.5% |
| `f1ap_rel18.6_specs` | 8.36 MB | 8.67 MB | 146.8% | 147.8% |
| `ngap_rel18.6_specs` | 8.29 MB | 7.91 MB | 149.1% | 153.8% |
| `lteNRRCC` | 51.82 MB | 55.20 MB | 219.7% | 105.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0417s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.1082s | 0.1240s | -0.0158s | improved |
| `ngap_rel18.6_specs` | 0.0825s | 0.0857s | -0.0032s | improved |
| `lteNRRCC` | 0.1281s | 0.1408s | -0.0127s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.73 MB | 8.73 MB | 77.3% | 162.0% |
| `f1ap_rel18.6_specs` | 11.71 MB | 11.40 MB | 215.1% | 220.2% |
| `ngap_rel18.6_specs` | 9.09 MB | 9.21 MB | 152.8% | 155.6% |
| `lteNRRCC` | 9.12 MB | 78.77 MB | 95.2% | 155.1% |
<!-- BENCH_RESULTS_END -->
