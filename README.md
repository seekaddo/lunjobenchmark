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
Generated: 2026-10-12T01:12:46.959751+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0363s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1138s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0760s | 0.0779s | -0.0019s | improved |
| `lteNRRCC` | 0.1191s | 0.1231s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 14.3% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.3% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 100.0% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0271s | +0.0094s | worse |
| `f1ap_rel18.6_specs` | 0.0970s | 0.0737s | +0.0233s | worse |
| `ngap_rel18.6_specs` | 0.0705s | 0.0503s | +0.0202s | worse |
| `lteNRRCC` | 0.1310s | 0.0961s | +0.0349s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.63 MB | 36.36 MB | 56.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.18 MB | 103.49 MB | 103.2% | 101.7% |
| `ngap_rel18.6_specs` | 17.99 MB | 74.45 MB | 108.0% | 104.5% |
| `lteNRRCC` | 48.55 MB | 66.40 MB | 103.1% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0236s | +0.0103s | worse |
| `f1ap_rel18.6_specs` | 0.0904s | 0.0619s | +0.0285s | worse |
| `ngap_rel18.6_specs` | 0.0637s | 0.0439s | +0.0198s | worse |
| `lteNRRCC` | 0.1158s | 0.0800s | +0.0358s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.46 MB | 70.4% | 103.8% |
| `f1ap_rel18.6_specs` | 34.62 MB | 164.77 MB | 103.4% | 101.9% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.70 MB | 104.3% | 102.6% |
| `lteNRRCC` | 74.72 MB | 102.29 MB | 103.6% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0258s | +0.0093s | worse |
| `f1ap_rel18.6_specs` | 0.0676s | 0.0860s | -0.0184s | improved |
| `ngap_rel18.6_specs` | 0.0619s | 0.0602s | +0.0017s | worse |
| `lteNRRCC` | 0.0742s | 0.1094s | -0.0352s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.66 MB | 6.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.55 MB | 9.09 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.73 MB | 8.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.48 MB | 6.50 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0307s | +0.0084s | worse |
| `f1ap_rel18.6_specs` | 0.1090s | 0.0781s | +0.0309s | worse |
| `ngap_rel18.6_specs` | 0.0763s | 0.0645s | +0.0118s | worse |
| `lteNRRCC` | 0.1382s | 0.0901s | +0.0481s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.43 MB | 7.27 MB | 0.0% | 164.1% |
| `f1ap_rel18.6_specs` | 8.59 MB | 8.52 MB | 232.8% | 234.9% |
| `ngap_rel18.6_specs` | 8.15 MB | 7.52 MB | 116.9% | 83.3% |
| `lteNRRCC` | 48.55 MB | 50.84 MB | 160.1% | 105.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0411s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1121s | 0.1148s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0791s | 0.0778s | +0.0013s | worse |
| `lteNRRCC` | 0.1304s | 0.1324s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.13 MB | 8.84 MB | 0.0% | 153.4% |
| `f1ap_rel18.6_specs` | 9.97 MB | 164.16 MB | 77.9% | 157.3% |
| `ngap_rel18.6_specs` | 9.30 MB | 11.04 MB | 77.1% | 218.2% |
| `lteNRRCC` | 10.02 MB | 98.55 MB | 107.8% | 154.3% |
<!-- BENCH_RESULTS_END -->
