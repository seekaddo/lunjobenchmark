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
Generated: 2026-06-09T23:22:29.885136+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0348s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1107s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0757s | +0.0002s | worse |
| `lteNRRCC` | 0.1171s | 0.1195s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 19.6% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0372s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0918s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0647s | 0.0654s | -0.0007s | improved |
| `lteNRRCC` | 0.1239s | 0.1238s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.73 MB | 10.1% | 110.7% |
| `f1ap_rel18.6_specs` | 22.40 MB | 103.33 MB | 109.4% | 105.4% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.14 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.55 MB | 66.17 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0362s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0950s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0676s | -0.0036s | improved |
| `lteNRRCC` | 0.1264s | 0.1296s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 55.43 MB | 95.8% | 114.3% |
| `f1ap_rel18.6_specs` | 34.16 MB | 164.48 MB | 109.7% | 105.3% |
| `ngap_rel18.6_specs` | 23.84 MB | 117.75 MB | 111.5% | 106.8% |
| `lteNRRCC` | 74.37 MB | 102.62 MB | 104.8% | 104.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0304s | 0.0352s | -0.0048s | improved |
| `f1ap_rel18.6_specs` | 0.0906s | 0.1091s | -0.0185s | improved |
| `ngap_rel18.6_specs` | 0.0570s | 0.0656s | -0.0086s | improved |
| `lteNRRCC` | 0.0834s | 0.1040s | -0.0206s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.53 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.28 MB | 3.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.98 MB | 4.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.81 MB | 2.52 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0404s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1113s | 0.1091s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0763s | 0.0758s | +0.0005s | worse |
| `lteNRRCC` | 0.1392s | 0.1409s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.56 MB | 160.3% | 155.5% |
| `f1ap_rel18.6_specs` | 8.23 MB | 106.63 MB | 154.3% | 162.3% |
| `ngap_rel18.6_specs` | 7.97 MB | 7.98 MB | 227.4% | 99.8% |
| `lteNRRCC` | 7.97 MB | 69.23 MB | 156.4% | 157.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0421s | -0.0069s | improved |
| `f1ap_rel18.6_specs` | 0.1035s | 0.1207s | -0.0172s | improved |
| `ngap_rel18.6_specs` | 0.0716s | 0.0825s | -0.0109s | improved |
| `lteNRRCC` | 0.1123s | 0.1461s | -0.0338s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.47 MB | 9.02 MB | 0.0% | 208.4% |
| `f1ap_rel18.6_specs` | 10.95 MB | 164.20 MB | 137.6% | 106.9% |
| `ngap_rel18.6_specs` | 10.51 MB | 10.63 MB | 113.5% | 276.2% |
| `lteNRRCC` | 9.43 MB | 75.09 MB | 131.7% | 130.1% |
<!-- BENCH_RESULTS_END -->
