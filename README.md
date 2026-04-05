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
Generated: 2026-04-05T10:42:56.269841+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0385s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.1129s | 0.1178s | -0.0049s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0797s | -0.0021s | improved |
| `lteNRRCC` | 0.1215s | 0.1253s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 25.0% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.1% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0341s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0924s | 0.0925s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0654s | +0.0003s | worse |
| `lteNRRCC` | 0.1287s | 0.1283s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.26 MB | 36.70 MB | 96.0% | 107.1% |
| `f1ap_rel18.6_specs` | 21.69 MB | 103.48 MB | 106.2% | 103.5% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.07 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.37 MB | 65.93 MB | 104.7% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0328s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0911s | 0.0884s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0638s | 0.0622s | +0.0016s | worse |
| `lteNRRCC` | 0.1166s | 0.1158s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.69 MB | 88.9% | 110.7% |
| `f1ap_rel18.6_specs` | 35.18 MB | 164.65 MB | 110.0% | 107.1% |
| `ngap_rel18.6_specs` | 24.07 MB | 117.61 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.95 MB | 102.93 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0194s | 0.0220s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0643s | 0.0725s | -0.0082s | improved |
| `ngap_rel18.6_specs` | 0.0399s | 0.0465s | -0.0066s | improved |
| `lteNRRCC` | 0.0731s | 0.0683s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.17 MB | 3.73 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.12 MB | 4.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 3.67 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0389s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1061s | 0.1083s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0762s | -0.0024s | improved |
| `lteNRRCC` | 0.1385s | 0.1377s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.74 MB | 7.37 MB | 114.4% | 81.3% |
| `f1ap_rel18.6_specs` | 8.10 MB | 8.66 MB | 97.1% | 213.9% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.61 MB | 82.2% | 161.3% |
| `lteNRRCC` | 51.83 MB | 49.44 MB | 163.1% | 159.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0422s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1174s | -0.0099s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0819s | -0.0074s | improved |
| `lteNRRCC` | 0.1242s | 0.1288s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.78 MB | 10.14 MB | 160.6% | 218.4% |
| `f1ap_rel18.6_specs` | 9.50 MB | 9.93 MB | 92.5% | 161.0% |
| `ngap_rel18.6_specs` | 9.55 MB | 8.95 MB | 105.5% | 158.7% |
| `lteNRRCC` | 8.49 MB | 97.12 MB | 78.8% | 158.4% |
<!-- BENCH_RESULTS_END -->
