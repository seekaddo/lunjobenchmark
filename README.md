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
Generated: 2026-10-11T16:13:18.269370+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0349s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1138s | 0.1104s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0779s | 0.0752s | +0.0027s | worse |
| `lteNRRCC` | 0.1231s | 0.1183s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 14.9% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0271s | 0.0355s | -0.0084s | improved |
| `f1ap_rel18.6_specs` | 0.0737s | 0.0948s | -0.0211s | improved |
| `ngap_rel18.6_specs` | 0.0503s | 0.0671s | -0.0168s | improved |
| `lteNRRCC` | 0.0961s | 0.1287s | -0.0326s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 36.59 MB | 55.6% | 104.8% |
| `f1ap_rel18.6_specs` | 22.43 MB | 102.66 MB | 108.7% | 102.3% |
| `ngap_rel18.6_specs` | 18.12 MB | 74.69 MB | 105.3% | 103.0% |
| `lteNRRCC` | 48.73 MB | 66.41 MB | 102.1% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0236s | 0.0365s | -0.0129s | improved |
| `f1ap_rel18.6_specs` | 0.0619s | 0.1014s | -0.0395s | improved |
| `ngap_rel18.6_specs` | 0.0439s | 0.0722s | -0.0283s | improved |
| `lteNRRCC` | 0.0800s | 0.1189s | -0.0389s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 55.72 MB | 73.7% | 105.3% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.53 MB | 100.0% | 102.6% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.71 MB | 106.2% | 100.0% |
| `lteNRRCC` | 74.74 MB | 102.64 MB | 100.0% | 102.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0258s | 0.0272s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0860s | 0.0718s | +0.0142s | worse |
| `ngap_rel18.6_specs` | 0.0602s | 0.0496s | +0.0106s | worse |
| `lteNRRCC` | 0.1094s | 0.0901s | +0.0193s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.48 MB | 7.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.81 MB | 4.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.48 MB | 8.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.88 MB | 1.05 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0307s | 0.0392s | -0.0085s | improved |
| `f1ap_rel18.6_specs` | 0.0781s | 0.1083s | -0.0302s | improved |
| `ngap_rel18.6_specs` | 0.0645s | 0.0762s | -0.0117s | improved |
| `lteNRRCC` | 0.0901s | 0.1459s | -0.0558s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.30 MB | 11.43 MB | 0.0% | 87.3% |
| `f1ap_rel18.6_specs` | 15.69 MB | 14.41 MB | 137.1% | 92.3% |
| `ngap_rel18.6_specs` | 12.19 MB | 11.53 MB | 87.8% | 87.7% |
| `lteNRRCC` | 10.66 MB | 19.70 MB | 96.6% | 107.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0402s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1148s | 0.1216s | -0.0068s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0788s | -0.0010s | improved |
| `lteNRRCC` | 0.1324s | 0.1285s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.13 MB | 10.06 MB | 0.0% | 82.0% |
| `f1ap_rel18.6_specs` | 9.65 MB | 164.16 MB | 76.9% | 150.7% |
| `ngap_rel18.6_specs` | 8.98 MB | 11.09 MB | 150.8% | 209.2% |
| `lteNRRCC` | 8.59 MB | 90.72 MB | 154.6% | 217.3% |
<!-- BENCH_RESULTS_END -->
