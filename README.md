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
Generated: 2026-04-08T11:07:19.566616+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0364s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.1217s | 0.1116s | +0.0101s | worse |
| `ngap_rel18.6_specs` | 0.0826s | 0.0757s | +0.0069s | worse |
| `lteNRRCC` | 0.1264s | 0.1210s | +0.0054s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 25.6% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.5% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 103.5% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0347s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0979s | 0.0929s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0689s | 0.0661s | +0.0028s | worse |
| `lteNRRCC` | 0.1335s | 0.1277s | +0.0058s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 36.59 MB | 96.3% | 113.3% |
| `f1ap_rel18.6_specs` | 22.29 MB | 103.01 MB | 112.1% | 106.6% |
| `ngap_rel18.6_specs` | 16.81 MB | 74.47 MB | 110.7% | 106.4% |
| `lteNRRCC` | 48.51 MB | 66.48 MB | 104.5% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0322s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.0946s | 0.0865s | +0.0081s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0606s | +0.0057s | worse |
| `lteNRRCC` | 0.1301s | 0.1138s | +0.0163s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.70 MB | 92.6% | 110.3% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.42 MB | 109.1% | 105.0% |
| `ngap_rel18.6_specs` | 24.39 MB | 117.88 MB | 107.1% | 108.7% |
| `lteNRRCC` | 74.66 MB | 102.93 MB | 104.6% | 103.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0257s | 0.0410s | -0.0153s | improved |
| `f1ap_rel18.6_specs` | 0.0746s | 0.1187s | -0.0441s | improved |
| `ngap_rel18.6_specs` | 0.0520s | 0.0592s | -0.0072s | improved |
| `lteNRRCC` | 0.0851s | 0.1079s | -0.0228s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.67 MB | 4.53 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.22 MB | 8.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 4.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.58 MB | 5.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0394s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1061s | 0.1058s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0753s | 0.0733s | +0.0020s | worse |
| `lteNRRCC` | 0.1366s | 0.1380s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.34 MB | 7.41 MB | 172.5% | 82.3% |
| `f1ap_rel18.6_specs` | 7.96 MB | 106.64 MB | 162.9% | 106.7% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.54 MB | 161.5% | 81.4% |
| `lteNRRCC` | 51.70 MB | 69.15 MB | 104.2% | 111.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0394s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1107s | 0.1098s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0795s | 0.0759s | +0.0036s | worse |
| `lteNRRCC` | 0.1272s | 0.1271s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.64 MB | 8.57 MB | 113.6% | 160.6% |
| `f1ap_rel18.6_specs` | 9.61 MB | 164.18 MB | 179.1% | 121.5% |
| `ngap_rel18.6_specs` | 9.14 MB | 9.26 MB | 99.2% | 98.5% |
| `lteNRRCC` | 8.86 MB | 99.77 MB | 165.7% | 107.8% |
<!-- BENCH_RESULTS_END -->
