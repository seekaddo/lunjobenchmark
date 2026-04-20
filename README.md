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
Generated: 2026-04-20T11:24:15.932260+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0350s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1121s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0773s | +0.0017s | worse |
| `lteNRRCC` | 0.1281s | 0.1214s | +0.0067s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.84 MB | 53.55 MB | 6.6% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 105.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0342s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0943s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0667s | -0.0009s | improved |
| `lteNRRCC` | 0.1299s | 0.1310s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.01 MB | 88.5% | 110.7% |
| `f1ap_rel18.6_specs` | 22.25 MB | 102.70 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.70 MB | 74.66 MB | 111.1% | 107.0% |
| `lteNRRCC` | 48.32 MB | 66.34 MB | 104.6% | 105.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0359s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.0882s | 0.1021s | -0.0139s | improved |
| `ngap_rel18.6_specs` | 0.0619s | 0.0713s | -0.0094s | improved |
| `lteNRRCC` | 0.1156s | 0.1199s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.69 MB | 100.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.41 MB | 164.73 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 23.73 MB | 117.58 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.67 MB | 102.43 MB | 105.2% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0260s | 0.0309s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.0810s | 0.0717s | +0.0093s | worse |
| `ngap_rel18.6_specs` | 0.0559s | 0.0488s | +0.0071s | worse |
| `lteNRRCC` | 0.1003s | 0.0845s | +0.0158s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.12 MB | 3.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.11 MB | 4.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.47 MB | 4.73 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.66 MB | 1.41 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0455s | 0.0395s | +0.0060s | worse |
| `f1ap_rel18.6_specs` | 0.1160s | 0.1055s | +0.0105s | worse |
| `ngap_rel18.6_specs` | 0.0857s | 0.0749s | +0.0108s | worse |
| `lteNRRCC` | 0.1322s | 0.1366s | -0.0044s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.97 MB | 7.97 MB | 155.9% | 88.3% |
| `f1ap_rel18.6_specs` | 8.60 MB | 8.70 MB | 152.1% | 77.1% |
| `ngap_rel18.6_specs` | 9.02 MB | 11.32 MB | 76.4% | 221.9% |
| `lteNRRCC` | 8.01 MB | 70.16 MB | 159.5% | 154.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0384s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1152s | 0.1082s | +0.0070s | worse |
| `ngap_rel18.6_specs` | 0.0813s | 0.0778s | +0.0035s | worse |
| `lteNRRCC` | 0.1288s | 0.1251s | +0.0037s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.82 MB | 8.93 MB | 89.5% | 155.1% |
| `f1ap_rel18.6_specs` | 10.08 MB | 9.81 MB | 157.2% | 156.4% |
| `ngap_rel18.6_specs` | 9.21 MB | 9.34 MB | 78.3% | 153.7% |
| `lteNRRCC` | 73.78 MB | 99.75 MB | 150.1% | 154.4% |
<!-- BENCH_RESULTS_END -->
