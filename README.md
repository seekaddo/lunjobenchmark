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
Generated: 2026-10-19T00:04:11.157361+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0387s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1188s | -0.0091s | improved |
| `ngap_rel18.6_specs` | 0.0749s | 0.0815s | -0.0066s | improved |
| `lteNRRCC` | 0.1224s | 0.1257s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 73.1% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 104.3% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.6% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0334s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0965s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0670s | 0.0657s | +0.0013s | worse |
| `lteNRRCC` | 0.1296s | 0.1178s | +0.0118s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.64 MB | 74.1% | 107.7% |
| `f1ap_rel18.6_specs` | 22.26 MB | 103.29 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 18.05 MB | 74.46 MB | 104.0% | 102.4% |
| `lteNRRCC` | 48.53 MB | 66.28 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0327s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0885s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0618s | 0.0617s | +0.0001s | worse |
| `lteNRRCC` | 0.1168s | 0.1157s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.77 MB | 22.0% | 103.8% |
| `f1ap_rel18.6_specs` | 34.51 MB | 163.79 MB | 107.1% | 100.0% |
| `ngap_rel18.6_specs` | 24.53 MB | 117.86 MB | 104.2% | 102.5% |
| `lteNRRCC` | 74.86 MB | 102.76 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0237s | 0.0291s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.0793s | 0.0764s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0467s | 0.0534s | -0.0067s | improved |
| `lteNRRCC` | 0.0774s | 0.0960s | -0.0186s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.88 MB | 4.50 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.00 MB | 9.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.70 MB | 8.17 MB | 0.9% | 0.0% |
| `lteNRRCC` | 7.44 MB | 7.34 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0411s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.1087s | 0.1148s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0766s | -0.0016s | improved |
| `lteNRRCC` | 0.1402s | 0.1405s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.96 MB | 7.35 MB | 0.0% | 161.2% |
| `f1ap_rel18.6_specs` | 7.99 MB | 8.27 MB | 161.0% | 97.7% |
| `ngap_rel18.6_specs` | 7.52 MB | 7.52 MB | 81.0% | 81.5% |
| `lteNRRCC` | 46.60 MB | 49.62 MB | 109.9% | 156.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0447s | 0.0388s | +0.0059s | worse |
| `f1ap_rel18.6_specs` | 0.1294s | 0.1132s | +0.0162s | worse |
| `ngap_rel18.6_specs` | 0.0884s | 0.0790s | +0.0094s | worse |
| `lteNRRCC` | 0.1325s | 0.1300s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.12 MB | 10.05 MB | 0.0% | 159.9% |
| `f1ap_rel18.6_specs` | 10.61 MB | 126.05 MB | 111.0% | 112.2% |
| `ngap_rel18.6_specs` | 10.16 MB | 10.49 MB | 159.2% | 176.4% |
| `lteNRRCC` | 70.66 MB | 77.04 MB | 113.4% | 105.6% |
<!-- BENCH_RESULTS_END -->
