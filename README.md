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
Generated: 2026-05-12T23:09:12.143660+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0381s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1140s | 0.1172s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0779s | 0.0793s | -0.0014s | improved |
| `lteNRRCC` | 0.1224s | 0.1247s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 8.4% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0351s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0965s | 0.0911s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0669s | 0.0637s | +0.0032s | worse |
| `lteNRRCC` | 0.1296s | 0.1230s | +0.0066s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.29 MB | 36.24 MB | 96.2% | 110.3% |
| `f1ap_rel18.6_specs` | 22.39 MB | 102.89 MB | 112.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.86 MB | 74.31 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.36 MB | 65.90 MB | 103.0% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0339s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0909s | 0.0902s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0645s | 0.0628s | +0.0017s | worse |
| `lteNRRCC` | 0.1154s | 0.1182s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.39 MB | 23.8% | 110.7% |
| `f1ap_rel18.6_specs` | 34.75 MB | 164.77 MB | 113.8% | 103.6% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.45 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.60 MB | 102.11 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0193s | +0.0181s | worse |
| `f1ap_rel18.6_specs` | 0.0722s | 0.0586s | +0.0136s | worse |
| `ngap_rel18.6_specs` | 0.0448s | 0.0406s | +0.0042s | worse |
| `lteNRRCC` | 0.0741s | 0.0671s | +0.0070s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 3.62 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.02 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.22 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.94 MB | 3.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0441s | 0.0340s | +0.0101s | worse |
| `f1ap_rel18.6_specs` | 0.1202s | 0.0962s | +0.0240s | worse |
| `ngap_rel18.6_specs` | 0.0844s | 0.0671s | +0.0173s | worse |
| `lteNRRCC` | 0.1342s | 0.1146s | +0.0196s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.77 MB | 7.97 MB | 80.3% | 107.3% |
| `f1ap_rel18.6_specs` | 8.46 MB | 8.61 MB | 79.1% | 81.4% |
| `ngap_rel18.6_specs` | 7.91 MB | 7.99 MB | 159.2% | 162.5% |
| `lteNRRCC` | 7.83 MB | 69.29 MB | 172.9% | 170.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0440s | 0.0407s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1176s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0804s | 0.0832s | -0.0028s | improved |
| `lteNRRCC` | 0.1283s | 0.1321s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.13 MB | 8.86 MB | 0.0% | 150.2% |
| `f1ap_rel18.6_specs` | 11.21 MB | 10.06 MB | 101.4% | 152.4% |
| `ngap_rel18.6_specs` | 9.15 MB | 9.21 MB | 72.7% | 156.2% |
| `lteNRRCC` | 73.46 MB | 99.58 MB | 151.0% | 107.5% |
<!-- BENCH_RESULTS_END -->
