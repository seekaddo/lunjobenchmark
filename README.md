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
Generated: 2026-09-24T00:21:19.046655+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0370s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1133s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0778s | -0.0007s | improved |
| `lteNRRCC` | 0.1206s | 0.1214s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 63.3% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0325s | 0.0361s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0979s | -0.0041s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0684s | -0.0023s | improved |
| `lteNRRCC` | 0.1201s | 0.1323s | -0.0122s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.49 MB | 7.6% | 104.2% |
| `f1ap_rel18.6_specs` | 22.42 MB | 102.75 MB | 103.7% | 101.8% |
| `ngap_rel18.6_specs` | 17.99 MB | 74.54 MB | 104.8% | 102.5% |
| `lteNRRCC` | 48.77 MB | 66.40 MB | 100.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0346s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0966s | 0.0913s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0674s | 0.0649s | +0.0025s | worse |
| `lteNRRCC` | 0.1290s | 0.1183s | +0.0107s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 55.76 MB | 84.6% | 106.9% |
| `f1ap_rel18.6_specs` | 34.75 MB | 164.32 MB | 106.5% | 103.4% |
| `ngap_rel18.6_specs` | 24.55 MB | 116.89 MB | 103.8% | 102.3% |
| `lteNRRCC` | 74.51 MB | 102.88 MB | 103.2% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0294s | 0.0275s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1219s | 0.0953s | +0.0266s | worse |
| `ngap_rel18.6_specs` | 0.0801s | 0.0657s | +0.0144s | worse |
| `lteNRRCC` | 0.1176s | 0.0995s | +0.0181s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.81 MB | 5.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.09 MB | 8.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 832 KB | 8.91 MB | 0.0% | 0.0% |
| `lteNRRCC` | 9.38 MB | 4.89 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0426s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1115s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0793s | -0.0041s | improved |
| `lteNRRCC` | 0.1383s | 0.1277s | +0.0106s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.32 MB | 7.41 MB | 224.6% | 242.5% |
| `f1ap_rel18.6_specs` | 8.09 MB | 106.62 MB | 160.0% | 163.3% |
| `ngap_rel18.6_specs` | 7.53 MB | 7.59 MB | 159.8% | 91.0% |
| `lteNRRCC` | 51.73 MB | 51.00 MB | 106.3% | 226.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0430s | -0.0052s | improved |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1229s | -0.0144s | improved |
| `ngap_rel18.6_specs` | 0.0741s | 0.0840s | -0.0099s | improved |
| `lteNRRCC` | 0.1271s | 0.1348s | -0.0077s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.33 MB | 0.0% | 161.3% |
| `f1ap_rel18.6_specs` | 10.07 MB | 9.48 MB | 157.8% | 93.7% |
| `ngap_rel18.6_specs` | 8.95 MB | 10.67 MB | 161.4% | 110.6% |
| `lteNRRCC` | 8.62 MB | 85.57 MB | 158.0% | 106.9% |
<!-- BENCH_RESULTS_END -->
