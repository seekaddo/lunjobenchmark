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
Generated: 2026-06-16T15:13:45.429397+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0343s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1078s | +0.0068s | worse |
| `ngap_rel18.6_specs` | 0.0780s | 0.0740s | +0.0040s | worse |
| `lteNRRCC` | 0.1224s | 0.1164s | +0.0060s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.79 MB | 53.55 MB | 24.1% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0262s | +0.0090s | worse |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0723s | +0.0220s | worse |
| `ngap_rel18.6_specs` | 0.0656s | 0.0505s | +0.0151s | worse |
| `lteNRRCC` | 0.1284s | 0.0970s | +0.0314s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.37 MB | 19.4% | 107.1% |
| `f1ap_rel18.6_specs` | 21.88 MB | 103.05 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.20 MB | 111.5% | 106.8% |
| `lteNRRCC` | 48.28 MB | 65.46 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0350s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1003s | 0.0938s | +0.0065s | worse |
| `ngap_rel18.6_specs` | 0.0685s | 0.0668s | +0.0017s | worse |
| `lteNRRCC` | 0.1163s | 0.1279s | -0.0116s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 55.48 MB | 81.8% | 108.0% |
| `f1ap_rel18.6_specs` | 34.48 MB | 164.51 MB | 107.7% | 103.4% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.68 MB | 109.5% | 102.3% |
| `lteNRRCC` | 74.82 MB | 102.52 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0498s | 0.0276s | +0.0222s | worse |
| `f1ap_rel18.6_specs` | 0.0696s | 0.0875s | -0.0179s | improved |
| `ngap_rel18.6_specs` | 0.0602s | 0.0642s | -0.0040s | improved |
| `lteNRRCC` | 0.0782s | 0.1038s | -0.0256s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.34 MB | 8.42 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.14 MB | 10.95 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 13.27 MB | 9.89 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.03 MB | 7.64 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0400s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1072s | 0.1085s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0750s | -0.0005s | improved |
| `lteNRRCC` | 0.1397s | 0.1277s | +0.0120s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.49 MB | 7.88 MB | 76.9% | 90.5% |
| `f1ap_rel18.6_specs` | 7.55 MB | 8.16 MB | 98.6% | 79.5% |
| `ngap_rel18.6_specs` | 7.67 MB | 7.86 MB | 88.3% | 171.4% |
| `lteNRRCC` | 50.86 MB | 51.84 MB | 160.5% | 106.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0447s | 0.0351s | +0.0096s | worse |
| `f1ap_rel18.6_specs` | 0.1239s | 0.1021s | +0.0218s | worse |
| `ngap_rel18.6_specs` | 0.0838s | 0.0706s | +0.0132s | worse |
| `lteNRRCC` | 0.1417s | 0.1117s | +0.0300s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.77 MB | 9.70 MB | 78.2% | 78.6% |
| `f1ap_rel18.6_specs` | 10.43 MB | 164.18 MB | 157.5% | 157.8% |
| `ngap_rel18.6_specs` | 9.67 MB | 10.25 MB | 76.4% | 78.6% |
| `lteNRRCC` | 67.98 MB | 74.14 MB | 158.5% | 154.7% |
<!-- BENCH_RESULTS_END -->
