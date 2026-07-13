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
Generated: 2026-07-13T23:01:17.104318+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0346s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1082s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0762s | 0.0750s | +0.0012s | worse |
| `lteNRRCC` | 0.1207s | 0.1174s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 20.6% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0367s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0977s | 0.1016s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0684s | 0.0719s | -0.0035s | improved |
| `lteNRRCC` | 0.1268s | 0.1331s | -0.0063s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.27 MB | 36.54 MB | 82.8% | 110.0% |
| `f1ap_rel18.6_specs` | 22.41 MB | 102.84 MB | 106.1% | 104.9% |
| `ngap_rel18.6_specs` | 17.48 MB | 74.45 MB | 111.1% | 108.7% |
| `lteNRRCC` | 48.68 MB | 66.15 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0274s | 0.0359s | -0.0085s | improved |
| `f1ap_rel18.6_specs` | 0.0884s | 0.0938s | -0.0054s | improved |
| `ngap_rel18.6_specs` | 0.0585s | 0.0656s | -0.0071s | improved |
| `lteNRRCC` | 0.0998s | 0.1196s | -0.0198s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.27 MB | 55.84 MB | 65.5% | 104.5% |
| `f1ap_rel18.6_specs` | 35.12 MB | 164.37 MB | 113.6% | 102.0% |
| `ngap_rel18.6_specs` | 23.95 MB | 117.67 MB | 105.3% | 105.6% |
| `lteNRRCC` | 74.85 MB | 102.24 MB | 104.2% | 103.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0459s | 0.0226s | +0.0233s | worse |
| `f1ap_rel18.6_specs` | 0.0693s | 0.0772s | -0.0079s | improved |
| `ngap_rel18.6_specs` | 0.0493s | 0.0586s | -0.0093s | improved |
| `lteNRRCC` | 0.0812s | 0.0884s | -0.0072s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.33 MB | 7.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 3.95 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.33 MB | 4.81 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.56 MB | 4.59 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0415s | -0.0081s | improved |
| `f1ap_rel18.6_specs` | 0.0916s | 0.1146s | -0.0230s | improved |
| `ngap_rel18.6_specs` | 0.0622s | 0.0800s | -0.0178s | improved |
| `lteNRRCC` | 0.1104s | 0.1416s | -0.0312s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.39 MB | 7.90 MB | 139.5% | 143.7% |
| `f1ap_rel18.6_specs` | 8.17 MB | 8.61 MB | 217.7% | 142.9% |
| `ngap_rel18.6_specs` | 7.93 MB | 7.99 MB | 211.8% | 115.5% |
| `lteNRRCC` | 8.35 MB | 67.92 MB | 141.3% | 142.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0436s | 0.0415s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1214s | 0.1178s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0871s | 0.0828s | +0.0043s | worse |
| `lteNRRCC` | 0.1409s | 0.1366s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.79 MB | 10.79 MB | 153.1% | 190.5% |
| `f1ap_rel18.6_specs` | 11.07 MB | 149.80 MB | 150.8% | 108.2% |
| `ngap_rel18.6_specs` | 10.64 MB | 10.77 MB | 75.1% | 199.2% |
| `lteNRRCC` | 9.37 MB | 101.72 MB | 149.1% | 157.2% |
<!-- BENCH_RESULTS_END -->
