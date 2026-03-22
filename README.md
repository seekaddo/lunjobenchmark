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
Generated: 2026-03-22T22:34:12.397625+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0380s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1155s | 0.1142s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0779s | 0.0780s | -0.0001s | improved |
| `lteNRRCC` | 0.1240s | 0.1230s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 90.5% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0347s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0954s | 0.0912s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0696s | 0.0646s | +0.0050s | worse |
| `lteNRRCC` | 0.1295s | 0.1237s | +0.0058s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.49 MB | 36.34 MB | 26.3% | 110.0% |
| `f1ap_rel18.6_specs` | 22.16 MB | 103.22 MB | 111.8% | 106.5% |
| `ngap_rel18.6_specs` | 16.66 MB | 74.10 MB | 110.3% | 106.4% |
| `lteNRRCC` | 48.58 MB | 66.24 MB | 104.5% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0340s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0890s | 0.0922s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0623s | 0.0643s | -0.0020s | improved |
| `lteNRRCC` | 0.1154s | 0.1177s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.46 MB | 55.89 MB | 85.7% | 110.3% |
| `f1ap_rel18.6_specs` | 35.13 MB | 164.51 MB | 109.7% | 105.3% |
| `ngap_rel18.6_specs` | 24.22 MB | 117.66 MB | 111.5% | 109.3% |
| `lteNRRCC` | 74.80 MB | 102.86 MB | 105.1% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0211s | 0.0211s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0639s | 0.0709s | -0.0070s | improved |
| `ngap_rel18.6_specs` | 0.0456s | 0.0459s | -0.0003s | improved |
| `lteNRRCC` | 0.0733s | 0.0730s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.31 MB | 4.12 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.00 MB | 4.73 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.09 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.80 MB | 4.17 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0400s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1087s | 0.1080s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0732s | 0.0752s | -0.0020s | improved |
| `lteNRRCC` | 0.1365s | 0.1390s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.51 MB | 7.70 MB | 165.4% | 220.5% |
| `f1ap_rel18.6_specs` | 7.90 MB | 8.04 MB | 167.3% | 162.2% |
| `ngap_rel18.6_specs` | 8.00 MB | 7.59 MB | 111.9% | 175.9% |
| `lteNRRCC` | 51.15 MB | 69.11 MB | 162.0% | 106.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0389s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1034s | 0.1077s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0726s | 0.0788s | -0.0062s | improved |
| `lteNRRCC` | 0.1251s | 0.1255s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.85 MB | 10.57 MB | 111.8% | 117.0% |
| `f1ap_rel18.6_specs` | 11.08 MB | 11.83 MB | 116.9% | 112.7% |
| `ngap_rel18.6_specs` | 10.63 MB | 10.88 MB | 116.0% | 117.3% |
| `lteNRRCC` | 72.78 MB | 98.58 MB | 160.3% | 165.2% |
<!-- BENCH_RESULTS_END -->
