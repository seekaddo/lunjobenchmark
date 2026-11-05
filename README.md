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
Generated: 2026-11-05T02:08:36.463928+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0407s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1223s | 0.1249s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0865s | 0.0850s | +0.0015s | worse |
| `lteNRRCC` | 0.1271s | 0.1305s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 79.2% | 103.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.0% | 103.8% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.3% | 101.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0460s | 0.0386s | +0.0074s | worse |
| `f1ap_rel18.6_specs` | 0.1405s | 0.1171s | +0.0234s | worse |
| `ngap_rel18.6_specs` | 0.0962s | 0.0809s | +0.0153s | worse |
| `lteNRRCC` | 0.1555s | 0.1312s | +0.0243s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 34.65 MB | 73.3% | 102.9% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 102.8% | 102.5% |
| `ngap_rel18.6_specs` | 17.97 MB | 72.65 MB | 107.1% | 103.4% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.7% | 103.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0548s | 0.0539s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1685s | 0.1668s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.1149s | 0.1153s | -0.0004s | improved |
| `lteNRRCC` | 0.1622s | 0.1625s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 53.73 MB | 81.5% | 105.4% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.7% | 101.1% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.1% | 102.9% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 102.7% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0485s | 0.0240s | +0.0245s | worse |
| `f1ap_rel18.6_specs` | 0.0750s | 0.0756s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0463s | 0.0655s | -0.0192s | improved |
| `lteNRRCC` | 0.0851s | 0.0919s | -0.0068s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.77 MB | 4.98 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.08 MB | 4.67 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.41 MB | 5.64 MB | 0.0% | 0.0% |
| `lteNRRCC` | 9.14 MB | 8.05 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0341s | +0.0054s | worse |
| `f1ap_rel18.6_specs` | 0.1080s | 0.0931s | +0.0149s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0643s | +0.0124s | worse |
| `lteNRRCC` | 0.1377s | 0.1118s | +0.0259s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 7.58 MB | 0.0% | 78.3% |
| `f1ap_rel18.6_specs` | 8.38 MB | 8.43 MB | 178.6% | 79.1% |
| `ngap_rel18.6_specs` | 8.25 MB | 8.09 MB | 99.3% | 172.3% |
| `lteNRRCC` | 51.35 MB | 50.82 MB | 163.1% | 219.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0381s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.1196s | 0.1124s | +0.0072s | worse |
| `ngap_rel18.6_specs` | 0.0846s | 0.0843s | +0.0003s | worse |
| `lteNRRCC` | 0.1385s | 0.1282s | +0.0103s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 10.54 MB | 0.0% | 97.5% |
| `f1ap_rel18.6_specs` | 11.21 MB | 164.20 MB | 107.3% | 106.5% |
| `ngap_rel18.6_specs` | 10.95 MB | 11.14 MB | 217.9% | 105.9% |
| `lteNRRCC` | 9.56 MB | 84.64 MB | 109.6% | 215.7% |
<!-- BENCH_RESULTS_END -->
