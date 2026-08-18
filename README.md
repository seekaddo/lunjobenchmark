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
Generated: 2026-08-18T22:30:27.923567+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0354s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1128s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0760s | -0.0001s | improved |
| `lteNRRCC` | 0.1199s | 0.1199s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 20.7% | 100.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0347s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0952s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0672s | -0.0014s | improved |
| `lteNRRCC` | 0.1281s | 0.1281s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.43 MB | 77.8% | 103.7% |
| `f1ap_rel18.6_specs` | 21.99 MB | 103.48 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.34 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.81 MB | 66.32 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0365s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0915s | 0.0961s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0684s | -0.0031s | improved |
| `lteNRRCC` | 0.1187s | 0.1300s | -0.0113s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 55.69 MB | 19.3% | 103.6% |
| `f1ap_rel18.6_specs` | 35.18 MB | 164.41 MB | 106.9% | 103.6% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.77 MB | 104.2% | 104.8% |
| `lteNRRCC` | 74.60 MB | 102.62 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0507s | 0.0238s | +0.0269s | worse |
| `f1ap_rel18.6_specs` | 0.1049s | 0.0956s | +0.0093s | worse |
| `ngap_rel18.6_specs` | 0.1032s | 0.0745s | +0.0287s | worse |
| `lteNRRCC` | 0.1039s | 0.0914s | +0.0125s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.19 MB | 6.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.12 MB | 7.98 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.34 MB | 6.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.23 MB | 6.45 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0390s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1049s | 0.1087s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0752s | +0.0003s | worse |
| `lteNRRCC` | 0.1418s | 0.1391s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.80 MB | 0.0% | 101.6% |
| `f1ap_rel18.6_specs` | 7.99 MB | 106.65 MB | 155.7% | 186.5% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.58 MB | 99.4% | 81.7% |
| `lteNRRCC` | 45.89 MB | 52.89 MB | 108.4% | 159.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0391s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1170s | -0.0069s | improved |
| `ngap_rel18.6_specs` | 0.0753s | 0.0771s | -0.0018s | improved |
| `lteNRRCC` | 0.1261s | 0.1281s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.72 MB | 0.0% | 79.4% |
| `f1ap_rel18.6_specs` | 9.41 MB | 164.19 MB | 99.9% | 155.1% |
| `ngap_rel18.6_specs` | 9.02 MB | 11.32 MB | 159.6% | 217.9% |
| `lteNRRCC` | 9.05 MB | 76.45 MB | 90.8% | 151.8% |
<!-- BENCH_RESULTS_END -->
