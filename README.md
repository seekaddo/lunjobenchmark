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
Generated: 2026-03-17T22:42:03.255340+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0376s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.1305s | 0.1199s | +0.0106s | worse |
| `ngap_rel18.6_specs` | 0.0894s | 0.0829s | +0.0065s | worse |
| `lteNRRCC` | 0.1296s | 0.1208s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.53 MB | 55.78 MB | 110.0% | 109.4% |
| `f1ap_rel18.6_specs` | 32.53 MB | 176.91 MB | 106.7% | 102.7% |
| `ngap_rel18.6_specs` | 22.41 MB | 125.78 MB | 108.0% | 103.6% |
| `lteNRRCC` | 72.32 MB | 100.09 MB | 105.1% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0363s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0989s | 0.0987s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0695s | 0.0711s | -0.0016s | improved |
| `lteNRRCC` | 0.1309s | 0.1308s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.25 MB | 37.67 MB | 8.3% | 110.0% |
| `f1ap_rel18.6_specs` | 22.18 MB | 111.84 MB | 108.6% | 106.7% |
| `ngap_rel18.6_specs` | 16.72 MB | 80.44 MB | 114.3% | 106.5% |
| `lteNRRCC` | 48.85 MB | 65.41 MB | 106.0% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0348s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0919s | 0.1014s | -0.0095s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0706s | -0.0053s | improved |
| `lteNRRCC` | 0.1150s | 0.1137s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.27 MB | 57.96 MB | 23.5% | 110.3% |
| `f1ap_rel18.6_specs` | 34.80 MB | 179.10 MB | 113.3% | 105.2% |
| `ngap_rel18.6_specs` | 23.69 MB | 127.53 MB | 112.0% | 106.8% |
| `lteNRRCC` | 74.93 MB | 102.52 MB | 103.4% | 105.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0243s | 0.0202s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.0907s | 0.0642s | +0.0265s | worse |
| `ngap_rel18.6_specs` | 0.0540s | 0.0427s | +0.0113s | worse |
| `lteNRRCC` | 0.0913s | 0.0723s | +0.0190s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 6.88 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 11.09 MB | 176 KB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.39 MB | 8.36 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.86 MB | 5.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0409s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1143s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0780s | 0.0795s | -0.0015s | improved |
| `lteNRRCC` | 0.1348s | 0.1267s | +0.0081s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.68 MB | 7.89 MB | 159.0% | 113.7% |
| `f1ap_rel18.6_specs` | 7.89 MB | 8.05 MB | 178.1% | 171.9% |
| `ngap_rel18.6_specs` | 7.89 MB | 7.54 MB | 162.5% | 92.6% |
| `lteNRRCC` | 47.61 MB | 51.44 MB | 109.9% | 162.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0405s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1107s | 0.1180s | -0.0073s | improved |
| `ngap_rel18.6_specs` | 0.0818s | 0.0819s | -0.0001s | improved |
| `lteNRRCC` | 0.1238s | 0.1265s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.43 MB | 8.43 MB | 163.9% | 165.0% |
| `f1ap_rel18.6_specs` | 9.59 MB | 179.18 MB | 164.8% | 164.7% |
| `ngap_rel18.6_specs` | 8.89 MB | 8.83 MB | 165.7% | 162.7% |
| `lteNRRCC` | 8.67 MB | 70.25 MB | 97.5% | 106.3% |
<!-- BENCH_RESULTS_END -->
