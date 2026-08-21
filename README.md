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
Generated: 2026-08-21T10:36:39.957143+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0353s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1071s | 0.1096s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0734s | 0.0756s | -0.0022s | improved |
| `lteNRRCC` | 0.1173s | 0.1197s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 81.0% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 104.4% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0274s | 0.0373s | -0.0099s | improved |
| `f1ap_rel18.6_specs` | 0.0789s | 0.0960s | -0.0171s | improved |
| `ngap_rel18.6_specs` | 0.0520s | 0.0675s | -0.0155s | improved |
| `lteNRRCC` | 0.1022s | 0.1295s | -0.0273s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 36.67 MB | 44.4% | 104.8% |
| `f1ap_rel18.6_specs` | 22.18 MB | 103.20 MB | 104.2% | 102.3% |
| `ngap_rel18.6_specs` | 18.02 MB | 73.87 MB | 105.3% | 103.0% |
| `lteNRRCC` | 48.61 MB | 66.14 MB | 100.0% | 101.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0238s | 0.0353s | -0.0115s | improved |
| `f1ap_rel18.6_specs` | 0.0744s | 0.0884s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0511s | 0.0620s | -0.0109s | improved |
| `lteNRRCC` | 0.0970s | 0.1153s | -0.0183s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 55.38 MB | 12.3% | 100.0% |
| `f1ap_rel18.6_specs` | 34.41 MB | 163.84 MB | 104.8% | 102.2% |
| `ngap_rel18.6_specs` | 24.45 MB | 117.59 MB | 105.9% | 103.2% |
| `lteNRRCC` | 74.57 MB | 102.52 MB | 102.3% | 101.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0222s | 0.0168s | +0.0054s | worse |
| `f1ap_rel18.6_specs` | 0.0668s | 0.0651s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0452s | 0.0439s | +0.0013s | worse |
| `lteNRRCC` | 0.0753s | 0.0758s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.97 MB | 3.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.19 MB | 4.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.50 MB | 2.95 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.38 MB | 4.61 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0400s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1133s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0844s | -0.0086s | improved |
| `lteNRRCC` | 0.1371s | 0.1389s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.82 MB | 7.50 MB | 113.0% | 78.8% |
| `f1ap_rel18.6_specs` | 8.15 MB | 8.36 MB | 156.7% | 101.1% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.91 MB | 176.0% | 95.3% |
| `lteNRRCC` | 49.72 MB | 50.74 MB | 159.8% | 108.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0400s | -0.0064s | improved |
| `f1ap_rel18.6_specs` | 0.0854s | 0.1152s | -0.0298s | improved |
| `ngap_rel18.6_specs` | 0.0602s | 0.0771s | -0.0169s | improved |
| `lteNRRCC` | 0.0902s | 0.1287s | -0.0385s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 31.04 MB | 0.0% | 160.8% |
| `f1ap_rel18.6_specs` | 25.40 MB | 24.27 MB | 147.3% | 76.4% |
| `ngap_rel18.6_specs` | 15.20 MB | 14.78 MB | 111.1% | 114.9% |
| `lteNRRCC` | 22.42 MB | 19.48 MB | 128.2% | 84.9% |
<!-- BENCH_RESULTS_END -->
