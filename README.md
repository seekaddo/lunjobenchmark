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
Generated: 2026-08-31T00:21:03.224001+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0366s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1103s | 0.1126s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0768s | -0.0025s | improved |
| `lteNRRCC` | 0.1182s | 0.1209s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 81.8% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0292s | +0.0063s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0764s | +0.0183s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0536s | +0.0131s | worse |
| `lteNRRCC` | 0.1296s | 0.1006s | +0.0290s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 35.93 MB | 80.0% | 103.6% |
| `f1ap_rel18.6_specs` | 22.21 MB | 103.29 MB | 103.1% | 103.5% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.64 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.23 MB | 66.14 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0254s | 0.0333s | -0.0079s | improved |
| `f1ap_rel18.6_specs` | 0.0789s | 0.0898s | -0.0109s | improved |
| `ngap_rel18.6_specs` | 0.0559s | 0.0627s | -0.0068s | improved |
| `lteNRRCC` | 0.0846s | 0.1157s | -0.0311s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 55.89 MB | 43.8% | 105.6% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.42 MB | 105.3% | 100.0% |
| `ngap_rel18.6_specs` | 24.09 MB | 117.58 MB | 106.7% | 100.0% |
| `lteNRRCC` | 74.89 MB | 101.98 MB | 102.6% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0249s | 0.0438s | -0.0189s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0668s | +0.0274s | worse |
| `ngap_rel18.6_specs` | 0.0724s | 0.0462s | +0.0262s | worse |
| `lteNRRCC` | 0.1284s | 0.0766s | +0.0518s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.45 MB | 5.53 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.02 MB | 8.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.80 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.28 MB | 3.69 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0377s | -0.0050s | improved |
| `f1ap_rel18.6_specs` | 0.0899s | 0.1051s | -0.0152s | improved |
| `ngap_rel18.6_specs` | 0.0622s | 0.0735s | -0.0113s | improved |
| `lteNRRCC` | 0.1100s | 0.1353s | -0.0253s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.90 MB | 0.0% | 141.9% |
| `f1ap_rel18.6_specs` | 8.68 MB | 8.74 MB | 140.8% | 139.2% |
| `ngap_rel18.6_specs` | 8.00 MB | 7.99 MB | 104.3% | 129.0% |
| `lteNRRCC` | 8.42 MB | 68.18 MB | 141.3% | 141.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0383s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1027s | 0.1094s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0744s | 0.0758s | -0.0014s | improved |
| `lteNRRCC` | 0.1140s | 0.1253s | -0.0113s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 10.09 MB | 0.0% | 190.2% |
| `f1ap_rel18.6_specs` | 10.78 MB | 164.17 MB | 95.3% | 108.9% |
| `ngap_rel18.6_specs` | 10.10 MB | 10.51 MB | 96.1% | 189.3% |
| `lteNRRCC` | 9.18 MB | 91.65 MB | 191.3% | 189.3% |
<!-- BENCH_RESULTS_END -->
