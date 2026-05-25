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
Generated: 2026-05-25T23:12:31.657995+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0378s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1204s | -0.0074s | improved |
| `ngap_rel18.6_specs` | 0.0781s | 0.0819s | -0.0038s | improved |
| `lteNRRCC` | 0.1232s | 0.1250s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 10.2% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0352s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0917s | 0.0936s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0643s | 0.0647s | -0.0004s | improved |
| `lteNRRCC` | 0.1247s | 0.1237s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.62 MB | 96.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.41 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.57 MB | 111.1% | 104.5% |
| `lteNRRCC` | 48.30 MB | 65.55 MB | 106.5% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0349s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0998s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0650s | 0.0687s | -0.0037s | improved |
| `lteNRRCC` | 0.1276s | 0.1156s | +0.0120s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.53 MB | 100.0% | 110.3% |
| `f1ap_rel18.6_specs` | 34.18 MB | 164.54 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.27 MB | 114.8% | 106.7% |
| `lteNRRCC` | 74.93 MB | 102.86 MB | 104.7% | 105.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0504s | -0.0162s | improved |
| `f1ap_rel18.6_specs` | 0.0945s | 0.0865s | +0.0080s | worse |
| `ngap_rel18.6_specs` | 0.0541s | 0.0793s | -0.0252s | improved |
| `lteNRRCC` | 0.0768s | 0.1143s | -0.0375s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.69 MB | 7.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.75 MB | 4.98 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.83 MB | 2.91 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.22 MB | 8.23 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0300s | +0.0096s | worse |
| `f1ap_rel18.6_specs` | 0.1065s | 0.0847s | +0.0218s | worse |
| `ngap_rel18.6_specs` | 0.0763s | 0.0581s | +0.0182s | worse |
| `lteNRRCC` | 0.1393s | 0.0916s | +0.0477s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.96 MB | 7.37 MB | 111.5% | 93.7% |
| `f1ap_rel18.6_specs` | 8.10 MB | 8.11 MB | 98.0% | 162.2% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.55 MB | 165.6% | 162.5% |
| `lteNRRCC` | 50.80 MB | 70.55 MB | 105.8% | 161.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0441s | 0.0373s | +0.0068s | worse |
| `f1ap_rel18.6_specs` | 0.1276s | 0.1059s | +0.0217s | worse |
| `ngap_rel18.6_specs` | 0.0891s | 0.0727s | +0.0164s | worse |
| `lteNRRCC` | 0.1416s | 0.1245s | +0.0171s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.89 MB | 9.64 MB | 158.1% | 159.0% |
| `f1ap_rel18.6_specs` | 10.36 MB | 146.13 MB | 79.9% | 109.9% |
| `ngap_rel18.6_specs` | 10.06 MB | 10.12 MB | 156.8% | 79.9% |
| `lteNRRCC` | 9.67 MB | 75.45 MB | 209.9% | 159.6% |
<!-- BENCH_RESULTS_END -->
