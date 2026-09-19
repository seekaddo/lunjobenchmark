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
Generated: 2026-09-19T00:07:46.915972+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0356s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1132s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0785s | 0.0793s | -0.0008s | improved |
| `lteNRRCC` | 0.1204s | 0.1206s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 90.5% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0362s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.0956s | 0.0937s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0661s | -0.0003s | improved |
| `lteNRRCC` | 0.1175s | 0.1285s | -0.0110s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 36.44 MB | 85.0% | 108.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.12 MB | 107.4% | 101.8% |
| `ngap_rel18.6_specs` | 17.94 MB | 74.48 MB | 109.5% | 102.5% |
| `lteNRRCC` | 48.48 MB | 66.12 MB | 100.0% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0349s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0901s | 0.0980s | -0.0079s | improved |
| `ngap_rel18.6_specs` | 0.0622s | 0.0692s | -0.0070s | improved |
| `lteNRRCC` | 0.1159s | 0.1140s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.25 MB | 82.6% | 103.8% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.29 MB | 107.1% | 101.9% |
| `ngap_rel18.6_specs` | 24.09 MB | 117.19 MB | 104.3% | 102.4% |
| `lteNRRCC` | 74.50 MB | 102.70 MB | 103.5% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0464s | 0.0242s | +0.0222s | worse |
| `f1ap_rel18.6_specs` | 0.0720s | 0.1627s | -0.0907s | improved |
| `ngap_rel18.6_specs` | 0.0497s | 0.0518s | -0.0021s | improved |
| `lteNRRCC` | 0.0701s | 0.0969s | -0.0268s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.02 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.39 MB | 4.66 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.41 MB | 7.67 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.17 MB | 3.91 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
