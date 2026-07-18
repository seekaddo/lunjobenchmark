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
Generated: 2026-07-18T11:09:45.295572+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0358s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1109s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0760s | +0.0007s | worse |
| `lteNRRCC` | 0.1206s | 0.1201s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 22.6% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0363s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0946s | 0.0971s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0664s | 0.0709s | -0.0045s | improved |
| `lteNRRCC` | 0.1296s | 0.1326s | -0.0030s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.17 MB | 36.43 MB | 82.8% | 106.9% |
| `f1ap_rel18.6_specs` | 22.01 MB | 103.46 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.63 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.48 MB | 65.60 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0351s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0927s | 0.0936s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0647s | +0.0005s | worse |
| `lteNRRCC` | 0.1191s | 0.1272s | -0.0081s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.33 MB | 55.46 MB | 79.3% | 107.1% |
| `f1ap_rel18.6_specs` | 34.55 MB | 164.35 MB | 113.8% | 105.3% |
| `ngap_rel18.6_specs` | 24.50 MB | 117.85 MB | 112.5% | 107.1% |
| `lteNRRCC` | 74.63 MB | 102.84 MB | 103.4% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0234s | 0.0434s | -0.0200s | improved |
| `f1ap_rel18.6_specs` | 0.0670s | 0.1008s | -0.0338s | improved |
| `ngap_rel18.6_specs` | 0.0466s | 0.0681s | -0.0215s | improved |
| `lteNRRCC` | 0.0800s | 0.1155s | -0.0355s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.86 MB | 5.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.03 MB | 5.02 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.31 MB | 5.58 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.30 MB | 3.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0330s | +0.0087s | worse |
| `f1ap_rel18.6_specs` | 0.1138s | 0.0925s | +0.0213s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0667s | +0.0133s | worse |
| `lteNRRCC` | 0.1475s | 0.1234s | +0.0241s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 8.62 MB | 149.8% | 187.3% |
| `f1ap_rel18.6_specs` | 8.46 MB | 8.61 MB | 143.9% | 146.2% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.09 MB | 145.7% | 145.2% |
| `lteNRRCC` | 8.47 MB | 51.93 MB | 144.7% | 146.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0407s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1205s | 0.1154s | +0.0051s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0864s | -0.0098s | improved |
| `lteNRRCC` | 0.1009s | 0.1059s | -0.0050s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.21 MB | 10.46 MB | 144.0% | 155.4% |
| `f1ap_rel18.6_specs` | 10.24 MB | 126.03 MB | 113.3% | 118.6% |
| `ngap_rel18.6_specs` | 9.74 MB | 10.52 MB | 151.2% | 0.0% |
| `lteNRRCC` | 73.78 MB | 84.89 MB | 153.2% | 153.4% |
<!-- BENCH_RESULTS_END -->
