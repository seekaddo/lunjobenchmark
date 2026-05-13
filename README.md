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
Generated: 2026-05-13T12:10:30.750992+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0369s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1180s | 0.1140s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0779s | +0.0021s | worse |
| `lteNRRCC` | 0.1287s | 0.1224s | +0.0063s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.84 MB | 53.55 MB | 5.7% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.9% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0363s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0965s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0669s | -0.0017s | improved |
| `lteNRRCC` | 0.1285s | 0.1296s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.09 MB | 36.21 MB | 17.6% | 107.1% |
| `f1ap_rel18.6_specs` | 21.30 MB | 103.29 MB | 112.5% | 105.2% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.68 MB | 107.4% | 106.8% |
| `lteNRRCC` | 47.84 MB | 66.29 MB | 104.7% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0341s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0909s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0651s | 0.0645s | +0.0006s | worse |
| `lteNRRCC` | 0.1285s | 0.1154s | +0.0131s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.53 MB | 96.3% | 110.3% |
| `f1ap_rel18.6_specs` | 35.16 MB | 164.70 MB | 109.4% | 106.8% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.75 MB | 110.7% | 106.7% |
| `lteNRRCC` | 74.93 MB | 102.70 MB | 106.2% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0213s | 0.0374s | -0.0161s | improved |
| `f1ap_rel18.6_specs` | 0.0711s | 0.0722s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0454s | 0.0448s | +0.0006s | worse |
| `lteNRRCC` | 0.0867s | 0.0741s | +0.0126s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.75 MB | 3.89 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.33 MB | 3.89 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 2.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.45 MB | 4.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0441s | -0.0039s | improved |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1202s | -0.0118s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0844s | -0.0074s | improved |
| `lteNRRCC` | 0.1394s | 0.1342s | +0.0052s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.86 MB | 7.38 MB | 226.2% | 80.1% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.04 MB | 159.4% | 160.5% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.54 MB | 181.1% | 160.6% |
| `lteNRRCC` | 49.20 MB | 69.04 MB | 157.4% | 159.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0440s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1191s | 0.1143s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0831s | 0.0804s | +0.0027s | worse |
| `lteNRRCC` | 0.1317s | 0.1283s | +0.0034s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.59 MB | 8.86 MB | 106.8% | 153.7% |
| `f1ap_rel18.6_specs` | 10.14 MB | 164.20 MB | 151.9% | 110.2% |
| `ngap_rel18.6_specs` | 9.21 MB | 9.34 MB | 153.5% | 76.0% |
| `lteNRRCC` | 8.55 MB | 88.95 MB | 152.2% | 155.6% |
<!-- BENCH_RESULTS_END -->
