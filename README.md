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
Generated: 2026-07-24T23:07:41.169322+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0360s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1108s | +0.0049s | worse |
| `ngap_rel18.6_specs` | 0.0787s | 0.0762s | +0.0025s | worse |
| `lteNRRCC` | 0.1239s | 0.1199s | +0.0040s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.63 MB | 53.55 MB | 18.8% | 103.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.0% | 101.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0349s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0913s | 0.0941s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0637s | 0.0663s | -0.0026s | improved |
| `lteNRRCC` | 0.1230s | 0.1271s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.03 MB | 36.01 MB | 75.0% | 103.7% |
| `f1ap_rel18.6_specs` | 22.04 MB | 103.12 MB | 103.2% | 101.7% |
| `ngap_rel18.6_specs` | 17.58 MB | 74.67 MB | 104.0% | 102.4% |
| `lteNRRCC` | 48.60 MB | 66.03 MB | 103.3% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0369s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.0911s | 0.0966s | -0.0055s | improved |
| `ngap_rel18.6_specs` | 0.0647s | 0.0665s | -0.0018s | improved |
| `lteNRRCC` | 0.1185s | 0.1292s | -0.0107s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.31 MB | 55.84 MB | 76.9% | 107.7% |
| `f1ap_rel18.6_specs` | 34.81 MB | 164.59 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.29 MB | 117.80 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.46 MB | 102.86 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0206s | 0.0227s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.0682s | 0.0724s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0471s | 0.0479s | -0.0008s | improved |
| `lteNRRCC` | 0.1034s | 0.0774s | +0.0260s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.14 MB | 8.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.06 MB | 8.55 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.23 MB | 8.45 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.31 MB | 8.09 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0406s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1081s | 0.1138s | -0.0057s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0779s | -0.0010s | improved |
| `lteNRRCC` | 0.1390s | 0.1416s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.73 MB | 7.49 MB | 152.9% | 78.9% |
| `f1ap_rel18.6_specs` | 8.78 MB | 8.16 MB | 109.5% | 160.8% |
| `ngap_rel18.6_specs` | 7.98 MB | 8.10 MB | 78.2% | 232.5% |
| `lteNRRCC` | 49.76 MB | 69.21 MB | 155.3% | 158.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0339s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.1095s | 0.1018s | +0.0077s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0672s | +0.0117s | worse |
| `lteNRRCC` | 0.1276s | 0.1092s | +0.0184s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.45 MB | 8.77 MB | 108.4% | 156.7% |
| `f1ap_rel18.6_specs` | 9.84 MB | 164.18 MB | 150.6% | 159.9% |
| `ngap_rel18.6_specs` | 8.76 MB | 8.89 MB | 157.4% | 78.0% |
| `lteNRRCC` | 8.68 MB | 92.38 MB | 76.0% | 227.4% |
<!-- BENCH_RESULTS_END -->
