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
Generated: 2026-06-20T12:03:10.122020+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0339s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1083s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0734s | 0.0738s | -0.0004s | improved |
| `lteNRRCC` | 0.1174s | 0.1186s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 23.3% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 106.4% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.3% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0317s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0968s | 0.0924s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0683s | 0.0644s | +0.0039s | worse |
| `lteNRRCC` | 0.1182s | 0.1143s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 35.75 MB | 18.9% | 107.7% |
| `f1ap_rel18.6_specs` | 22.36 MB | 103.47 MB | 107.1% | 103.5% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.47 MB | 108.7% | 104.8% |
| `lteNRRCC` | 48.68 MB | 66.34 MB | 103.4% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0362s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1003s | 0.0971s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0689s | 0.0666s | +0.0023s | worse |
| `lteNRRCC` | 0.1148s | 0.1280s | -0.0132s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.15 MB | 12.0% | 111.5% |
| `f1ap_rel18.6_specs` | 34.57 MB | 164.65 MB | 107.4% | 103.4% |
| `ngap_rel18.6_specs` | 24.18 MB | 117.54 MB | 109.1% | 104.7% |
| `lteNRRCC` | 74.89 MB | 102.94 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0177s | 0.0196s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0709s | 0.0732s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0477s | 0.0432s | +0.0045s | worse |
| `lteNRRCC` | 0.0761s | 0.1168s | -0.0407s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.69 MB | 5.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.33 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.61 MB | 4.84 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.09 MB | 2.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0298s | 0.0403s | -0.0105s | improved |
| `f1ap_rel18.6_specs` | 0.0826s | 0.1136s | -0.0310s | improved |
| `ngap_rel18.6_specs` | 0.0577s | 0.0787s | -0.0210s | improved |
| `lteNRRCC` | 0.0940s | 0.1283s | -0.0343s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 14.50 MB | 96.5% | 96.6% |
| `f1ap_rel18.6_specs` | 17.09 MB | 42.99 MB | 121.6% | 117.5% |
| `ngap_rel18.6_specs` | 11.84 MB | 17.17 MB | 94.9% | 122.8% |
| `lteNRRCC` | 18.49 MB | 16.87 MB | 106.0% | 128.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0428s | 0.0346s | +0.0082s | worse |
| `f1ap_rel18.6_specs` | 0.1244s | 0.1028s | +0.0216s | worse |
| `ngap_rel18.6_specs` | 0.0871s | 0.0705s | +0.0166s | worse |
| `lteNRRCC` | 0.1404s | 0.1127s | +0.0277s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.93 MB | 8.93 MB | 176.5% | 182.7% |
| `f1ap_rel18.6_specs` | 10.11 MB | 153.91 MB | 81.0% | 160.1% |
| `ngap_rel18.6_specs` | 9.02 MB | 10.05 MB | 164.3% | 158.8% |
| `lteNRRCC` | 68.48 MB | 86.07 MB | 109.2% | 162.1% |
<!-- BENCH_RESULTS_END -->
