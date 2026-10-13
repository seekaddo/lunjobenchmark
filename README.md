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
Generated: 2026-10-13T02:56:48.248137+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0357s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.1172s | 0.1106s | +0.0066s | worse |
| `ngap_rel18.6_specs` | 0.0798s | 0.0754s | +0.0044s | worse |
| `lteNRRCC` | 0.1253s | 0.1199s | +0.0054s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 18.7% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 103.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0300s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.0940s | 0.0886s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0670s | 0.0618s | +0.0052s | worse |
| `lteNRRCC` | 0.1303s | 0.1086s | +0.0217s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.42 MB | 36.59 MB | 71.4% | 107.7% |
| `f1ap_rel18.6_specs` | 22.41 MB | 103.47 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.41 MB | 108.0% | 104.8% |
| `lteNRRCC` | 48.73 MB | 65.56 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0290s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.0907s | 0.0772s | +0.0135s | worse |
| `ngap_rel18.6_specs` | 0.0628s | 0.0538s | +0.0090s | worse |
| `lteNRRCC` | 0.1175s | 0.1026s | +0.0149s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 55.21 MB | 83.3% | 103.8% |
| `f1ap_rel18.6_specs` | 35.17 MB | 163.63 MB | 103.6% | 103.7% |
| `ngap_rel18.6_specs` | 24.26 MB | 117.45 MB | 104.3% | 102.4% |
| `lteNRRCC` | 74.45 MB | 102.47 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0164s | 0.0299s | -0.0135s | improved |
| `f1ap_rel18.6_specs` | 0.0686s | 0.0697s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0684s | 0.0439s | +0.0245s | worse |
| `lteNRRCC` | 0.0752s | 0.0772s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.98 MB | 5.02 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.23 MB | 9.23 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.77 MB | 5.91 MB | 0.0% | 0.9% |
| `lteNRRCC` | 7.25 MB | 8.08 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0337s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.1132s | 0.0948s | +0.0184s | worse |
| `ngap_rel18.6_specs` | 0.0792s | 0.0670s | +0.0122s | worse |
| `lteNRRCC` | 0.1419s | 0.1129s | +0.0290s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.58 MB | 7.81 MB | 0.0% | 80.5% |
| `f1ap_rel18.6_specs` | 8.82 MB | 8.95 MB | 154.7% | 166.1% |
| `ngap_rel18.6_specs` | 8.20 MB | 8.48 MB | 97.6% | 97.9% |
| `lteNRRCC` | 8.57 MB | 52.73 MB | 154.8% | 154.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0427s | 0.0393s | +0.0034s | worse |
| `f1ap_rel18.6_specs` | 0.1294s | 0.1150s | +0.0144s | worse |
| `ngap_rel18.6_specs` | 0.0938s | 0.0803s | +0.0135s | worse |
| `lteNRRCC` | 0.1303s | 0.1294s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.19 MB | 0.0% | 106.8% |
| `f1ap_rel18.6_specs` | 10.55 MB | 117.50 MB | 117.9% | 229.6% |
| `ngap_rel18.6_specs` | 10.42 MB | 10.04 MB | 114.0% | 176.9% |
| `lteNRRCC` | 9.27 MB | 75.25 MB | 231.0% | 163.5% |
<!-- BENCH_RESULTS_END -->
