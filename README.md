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
Generated: 2026-10-13T17:29:08.182272+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0386s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1172s | -0.0060s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0798s | -0.0039s | improved |
| `lteNRRCC` | 0.1192s | 0.1253s | -0.0061s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.77 MB | 53.55 MB | 81.8% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 100.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0347s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0940s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0636s | 0.0670s | -0.0034s | improved |
| `lteNRRCC` | 0.1227s | 0.1303s | -0.0076s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.22 MB | 76.9% | 107.7% |
| `f1ap_rel18.6_specs` | 22.39 MB | 103.30 MB | 103.3% | 103.6% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.01 MB | 104.0% | 102.4% |
| `lteNRRCC` | 48.58 MB | 66.41 MB | 101.6% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0346s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0976s | 0.0907s | +0.0069s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0628s | +0.0035s | worse |
| `lteNRRCC` | 0.1289s | 0.1175s | +0.0114s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.63 MB | 55.55 MB | 72.4% | 103.6% |
| `f1ap_rel18.6_specs` | 34.34 MB | 164.38 MB | 103.2% | 101.7% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.41 MB | 107.7% | 102.3% |
| `lteNRRCC` | 74.41 MB | 102.39 MB | 101.6% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0413s | 0.0164s | +0.0249s | worse |
| `f1ap_rel18.6_specs` | 0.1083s | 0.0686s | +0.0397s | worse |
| `ngap_rel18.6_specs` | 0.0726s | 0.0684s | +0.0042s | worse |
| `lteNRRCC` | 0.0985s | 0.0752s | +0.0233s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.73 MB | 5.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.56 MB | 5.56 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.41 MB | 7.42 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.11 MB | 9.16 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0311s | 0.0412s | -0.0101s | improved |
| `f1ap_rel18.6_specs` | 0.0838s | 0.1132s | -0.0294s | improved |
| `ngap_rel18.6_specs` | 0.0611s | 0.0792s | -0.0181s | improved |
| `lteNRRCC` | 0.0958s | 0.1419s | -0.0461s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.30 MB | 22.00 MB | 0.0% | 147.6% |
| `f1ap_rel18.6_specs` | 15.11 MB | 13.10 MB | 74.0% | 158.8% |
| `ngap_rel18.6_specs` | 10.19 MB | 12.89 MB | 94.2% | 154.5% |
| `lteNRRCC` | 12.21 MB | 15.15 MB | 85.5% | 137.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0427s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1294s | -0.0164s | improved |
| `ngap_rel18.6_specs` | 0.0806s | 0.0938s | -0.0132s | improved |
| `lteNRRCC` | 0.1261s | 0.1303s | -0.0042s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 9.76 MB | 0.0% | 99.2% |
| `f1ap_rel18.6_specs` | 9.66 MB | 11.68 MB | 161.3% | 183.5% |
| `ngap_rel18.6_specs` | 10.48 MB | 9.12 MB | 227.4% | 78.8% |
| `lteNRRCC` | 73.76 MB | 99.00 MB | 153.1% | 106.7% |
<!-- BENCH_RESULTS_END -->
