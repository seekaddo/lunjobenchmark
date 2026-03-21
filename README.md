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
Generated: 2026-03-21T10:35:58.607865+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0364s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.1214s | 0.1133s | +0.0081s | worse |
| `ngap_rel18.6_specs` | 0.0832s | 0.0785s | +0.0047s | worse |
| `lteNRRCC` | 0.1273s | 0.1227s | +0.0046s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 110.5% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 103.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 103.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0358s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0955s | 0.0931s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0674s | 0.0648s | +0.0026s | worse |
| `lteNRRCC` | 0.1302s | 0.1272s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.49 MB | 36.24 MB | 27.7% | 113.3% |
| `f1ap_rel18.6_specs` | 22.32 MB | 102.87 MB | 111.8% | 105.1% |
| `ngap_rel18.6_specs` | 16.34 MB | 73.30 MB | 114.3% | 108.9% |
| `lteNRRCC` | 48.80 MB | 66.41 MB | 106.1% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0362s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0940s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0666s | 0.0657s | +0.0009s | worse |
| `lteNRRCC` | 0.1203s | 0.1287s | -0.0084s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.31 MB | 55.50 MB | 31.4% | 109.7% |
| `f1ap_rel18.6_specs` | 33.74 MB | 164.31 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.25 MB | 117.79 MB | 111.1% | 106.7% |
| `lteNRRCC` | 74.95 MB | 102.61 MB | 105.0% | 105.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0210s | +0.0183s | worse |
| `f1ap_rel18.6_specs` | 0.0992s | 0.0655s | +0.0337s | worse |
| `ngap_rel18.6_specs` | 0.0605s | 0.0438s | +0.0167s | worse |
| `lteNRRCC` | 0.0953s | 0.0736s | +0.0217s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.98 MB | 5.94 MB | 0.0% | 1.3% |
| `f1ap_rel18.6_specs` | 6.89 MB | 5.50 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.03 MB | 3.33 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0385s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1129s | 0.1058s | +0.0071s | worse |
| `ngap_rel18.6_specs` | 0.0736s | 0.0737s | -0.0001s | improved |
| `lteNRRCC` | 0.1375s | 0.1380s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.38 MB | 0.0% | 164.8% |
| `f1ap_rel18.6_specs` | 8.62 MB | 8.18 MB | 107.1% | 157.6% |
| `ngap_rel18.6_specs` | 8.05 MB | 7.90 MB | 101.7% | 109.4% |
| `lteNRRCC` | 48.58 MB | 51.03 MB | 157.9% | 161.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0370s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1078s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0746s | 0.0741s | +0.0005s | worse |
| `lteNRRCC` | 0.1259s | 0.1252s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.65 MB | 8.59 MB | 79.7% | 161.8% |
| `f1ap_rel18.6_specs` | 8.67 MB | 9.68 MB | 107.6% | 79.0% |
| `ngap_rel18.6_specs` | 10.38 MB | 9.02 MB | 108.8% | 159.4% |
| `lteNRRCC` | 73.77 MB | 81.96 MB | 155.9% | 223.5% |
<!-- BENCH_RESULTS_END -->
