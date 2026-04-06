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
Generated: 2026-04-06T22:45:09.609579+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0368s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1121s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0747s | 0.0771s | -0.0024s | improved |
| `lteNRRCC` | 0.1171s | 0.1220s | -0.0049s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.86 MB | 53.55 MB | 28.4% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0327s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.0940s | 0.0934s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0660s | 0.0654s | +0.0006s | worse |
| `lteNRRCC` | 0.1276s | 0.1167s | +0.0109s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.64 MB | 96.0% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.73 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.62 MB | 74.67 MB | 111.5% | 104.5% |
| `lteNRRCC` | 48.13 MB | 66.50 MB | 103.1% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0342s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0919s | 0.0980s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0634s | 0.0683s | -0.0049s | improved |
| `lteNRRCC` | 0.1149s | 0.1150s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.46 MB | 18.6% | 111.1% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.75 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.78 MB | 112.5% | 107.0% |
| `lteNRRCC` | 74.86 MB | 102.46 MB | 105.3% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0220s | 0.0261s | -0.0041s | improved |
| `f1ap_rel18.6_specs` | 0.0641s | 0.0657s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0478s | 0.0564s | -0.0086s | improved |
| `lteNRRCC` | 0.0759s | 0.0760s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.86 MB | 3.53 MB | 0.7% | 0.0% |
| `f1ap_rel18.6_specs` | 3.11 MB | 4.78 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 192 KB | 0.0% | 0.0% |
| `lteNRRCC` | 3.88 MB | 3.56 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0395s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1079s | 0.1117s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0777s | -0.0019s | improved |
| `lteNRRCC` | 0.1373s | 0.1303s | +0.0070s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.29 MB | 7.56 MB | 164.2% | 157.3% |
| `f1ap_rel18.6_specs` | 8.67 MB | 8.79 MB | 216.1% | 217.6% |
| `ngap_rel18.6_specs` | 7.88 MB | 7.89 MB | 159.8% | 153.2% |
| `lteNRRCC` | 8.04 MB | 58.48 MB | 160.3% | 159.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0431s | 0.0438s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1234s | 0.1252s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0876s | 0.0876s | +0.0000s | flat |
| `lteNRRCC` | 0.1329s | 0.1315s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.69 MB | 10.82 MB | 159.3% | 226.6% |
| `f1ap_rel18.6_specs` | 10.28 MB | 10.48 MB | 156.1% | 158.4% |
| `ngap_rel18.6_specs` | 10.17 MB | 10.03 MB | 160.2% | 88.9% |
| `lteNRRCC` | 8.92 MB | 9.11 MB | 162.3% | 100.7% |
<!-- BENCH_RESULTS_END -->
