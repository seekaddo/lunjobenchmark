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
Generated: 2026-08-22T10:29:55.522242+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0368s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1154s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0793s | -0.0025s | improved |
| `lteNRRCC` | 0.1204s | 0.1244s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 90.5% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0365s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0918s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0666s | 0.0651s | +0.0015s | worse |
| `lteNRRCC` | 0.1276s | 0.1284s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.72 MB | 22.6% | 107.4% |
| `f1ap_rel18.6_specs` | 22.29 MB | 103.12 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.20 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.66 MB | 66.28 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0363s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0905s | 0.0987s | -0.0082s | improved |
| `ngap_rel18.6_specs` | 0.0645s | 0.0663s | -0.0018s | improved |
| `lteNRRCC` | 0.1171s | 0.1207s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.57 MB | 76.9% | 107.7% |
| `f1ap_rel18.6_specs` | 34.63 MB | 164.52 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.56 MB | 117.81 MB | 104.3% | 102.4% |
| `lteNRRCC` | 74.66 MB | 102.62 MB | 103.5% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0231s | +0.0109s | worse |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0672s | +0.0234s | worse |
| `ngap_rel18.6_specs` | 0.0569s | 0.0454s | +0.0115s | worse |
| `lteNRRCC` | 0.1053s | 0.0772s | +0.0281s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.62 MB | 6.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.62 MB | 1.28 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.47 MB | 6.70 MB | 0.0% | 0.0% |
| `lteNRRCC` | 1.92 MB | 4.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0389s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1065s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0781s | 0.0742s | +0.0039s | worse |
| `lteNRRCC` | 0.1385s | 0.1381s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.83 MB | 7.03 MB | 108.0% | 158.8% |
| `f1ap_rel18.6_specs` | 8.46 MB | 106.64 MB | 97.8% | 183.8% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.14 MB | 81.4% | 82.8% |
| `lteNRRCC` | 49.27 MB | 52.46 MB | 163.3% | 111.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0383s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1088s | 0.1133s | -0.0045s | improved |
| `ngap_rel18.6_specs` | 0.0742s | 0.0800s | -0.0058s | improved |
| `lteNRRCC` | 0.1268s | 0.1313s | -0.0045s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.66 MB | 8.21 MB | 106.4% | 163.1% |
| `f1ap_rel18.6_specs` | 9.66 MB | 9.48 MB | 162.5% | 162.7% |
| `ngap_rel18.6_specs` | 9.21 MB | 8.77 MB | 103.3% | 162.5% |
| `lteNRRCC` | 9.35 MB | 99.16 MB | 111.1% | 106.5% |
<!-- BENCH_RESULTS_END -->
