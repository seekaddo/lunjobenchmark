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
Generated: 2026-04-15T11:07:47.775831+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0374s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.1273s | 0.1163s | +0.0110s | worse |
| `ngap_rel18.6_specs` | 0.0873s | 0.0810s | +0.0063s | worse |
| `lteNRRCC` | 0.1288s | 0.1234s | +0.0054s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.83 MB | 53.55 MB | 7.6% | 108.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.1% | 105.4% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.8% | 105.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0342s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0925s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0682s | 0.0649s | +0.0033s | worse |
| `lteNRRCC` | 0.1306s | 0.1275s | +0.0031s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.29 MB | 36.46 MB | 96.2% | 106.9% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.47 MB | 109.1% | 105.0% |
| `ngap_rel18.6_specs` | 16.55 MB | 74.58 MB | 114.8% | 106.7% |
| `lteNRRCC` | 48.72 MB | 66.24 MB | 104.5% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0344s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0907s | 0.0992s | -0.0085s | improved |
| `ngap_rel18.6_specs` | 0.0635s | 0.0696s | -0.0061s | improved |
| `lteNRRCC` | 0.1170s | 0.1157s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.38 MB | 27.0% | 107.1% |
| `f1ap_rel18.6_specs` | 35.12 MB | 164.36 MB | 110.0% | 105.3% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.69 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.93 MB | 102.16 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0274s | +0.0088s | worse |
| `f1ap_rel18.6_specs` | 0.0843s | 0.0635s | +0.0208s | worse |
| `ngap_rel18.6_specs` | 0.0552s | 0.0603s | -0.0051s | improved |
| `lteNRRCC` | 0.0727s | 0.0880s | -0.0153s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.53 MB | 4.48 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 4.19 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.38 MB | 4.05 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.20 MB | 7.22 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0333s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.1074s | 0.0907s | +0.0167s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0644s | +0.0144s | worse |
| `lteNRRCC` | 0.1370s | 0.1116s | +0.0254s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.68 MB | 7.36 MB | 108.6% | 82.6% |
| `f1ap_rel18.6_specs` | 7.96 MB | 106.64 MB | 164.8% | 107.5% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.54 MB | 83.8% | 164.4% |
| `lteNRRCC` | 47.23 MB | 51.95 MB | 165.2% | 231.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0379s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.1207s | 0.1051s | +0.0156s | worse |
| `ngap_rel18.6_specs` | 0.0820s | 0.0735s | +0.0085s | worse |
| `lteNRRCC` | 0.1301s | 0.1236s | +0.0065s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.83 MB | 9.64 MB | 116.9% | 162.6% |
| `f1ap_rel18.6_specs` | 11.03 MB | 10.50 MB | 106.4% | 118.9% |
| `ngap_rel18.6_specs` | 9.92 MB | 10.18 MB | 117.9% | 119.7% |
| `lteNRRCC` | 8.68 MB | 98.75 MB | 83.4% | 118.5% |
<!-- BENCH_RESULTS_END -->
