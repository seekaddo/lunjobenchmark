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
Generated: 2026-04-30T11:44:37.443593+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0359s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1150s | 0.1141s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0796s | 0.0803s | -0.0007s | improved |
| `lteNRRCC` | 0.1236s | 0.1222s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 12.9% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 105.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 115.4% | 105.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0353s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0926s | 0.0956s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0677s | -0.0028s | improved |
| `lteNRRCC` | 0.1248s | 0.1291s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 36.71 MB | 89.3% | 110.3% |
| `f1ap_rel18.6_specs` | 21.73 MB | 103.26 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.39 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.32 MB | 65.89 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0279s | +0.0054s | worse |
| `f1ap_rel18.6_specs` | 0.0881s | 0.0754s | +0.0127s | worse |
| `ngap_rel18.6_specs` | 0.0612s | 0.0526s | +0.0086s | worse |
| `lteNRRCC` | 0.1150s | 0.1018s | +0.0132s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.09 MB | 55.89 MB | 100.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.66 MB | 164.55 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.75 MB | 112.5% | 109.8% |
| `lteNRRCC` | 74.90 MB | 102.42 MB | 105.3% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0259s | 0.0226s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.0680s | 0.0634s | +0.0046s | worse |
| `ngap_rel18.6_specs` | 0.0493s | 0.0433s | +0.0060s | worse |
| `lteNRRCC` | 0.0825s | 0.0729s | +0.0096s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.64 MB | 4.89 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.08 MB | 1.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 5.33 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.42 MB | 4.83 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0433s | 0.0454s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.1210s | 0.1509s | -0.0299s | improved |
| `ngap_rel18.6_specs` | 0.0857s | 0.0782s | +0.0075s | worse |
| `lteNRRCC` | 0.1474s | 0.1639s | -0.0165s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.09 MB | 8.11 MB | 74.3% | 77.9% |
| `f1ap_rel18.6_specs` | 8.79 MB | 106.63 MB | 76.8% | 108.1% |
| `ngap_rel18.6_specs` | 8.42 MB | 8.48 MB | 197.1% | 101.8% |
| `lteNRRCC` | 8.53 MB | 52.25 MB | 153.3% | 154.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0417s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1054s | 0.1186s | -0.0132s | improved |
| `ngap_rel18.6_specs` | 0.0725s | 0.0823s | -0.0098s | improved |
| `lteNRRCC` | 0.1266s | 0.1375s | -0.0109s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.50 MB | 8.65 MB | 80.4% | 159.1% |
| `f1ap_rel18.6_specs` | 11.20 MB | 164.19 MB | 232.9% | 110.0% |
| `ngap_rel18.6_specs` | 9.02 MB | 10.88 MB | 159.8% | 114.2% |
| `lteNRRCC` | 73.77 MB | 73.07 MB | 158.3% | 158.5% |
<!-- BENCH_RESULTS_END -->
