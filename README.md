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
Generated: 2026-06-11T14:05:29.578065+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0354s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1107s | 0.1106s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0760s | 0.0770s | -0.0010s | improved |
| `lteNRRCC` | 0.1202s | 0.1204s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 23.6% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0344s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0924s | 0.0928s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0655s | 0.0660s | -0.0005s | improved |
| `lteNRRCC` | 0.1274s | 0.1292s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.29 MB | 36.72 MB | 82.1% | 107.1% |
| `f1ap_rel18.6_specs` | 22.16 MB | 102.67 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.65 MB | 74.43 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.71 MB | 66.01 MB | 104.6% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0285s | +0.0061s | worse |
| `f1ap_rel18.6_specs` | 0.0997s | 0.0772s | +0.0225s | worse |
| `ngap_rel18.6_specs` | 0.0694s | 0.0533s | +0.0161s | worse |
| `lteNRRCC` | 0.1184s | 0.1020s | +0.0164s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 55.44 MB | 79.2% | 107.7% |
| `f1ap_rel18.6_specs` | 34.69 MB | 164.71 MB | 107.4% | 101.7% |
| `ngap_rel18.6_specs` | 24.51 MB | 117.87 MB | 114.3% | 104.5% |
| `lteNRRCC` | 74.50 MB | 102.27 MB | 103.6% | 104.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0222s | 0.0199s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0645s | 0.0711s | -0.0066s | improved |
| `ngap_rel18.6_specs` | 0.0449s | 0.0498s | -0.0049s | improved |
| `lteNRRCC` | 0.0789s | 0.0892s | -0.0103s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.73 MB | 4.17 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 3.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.48 MB | 7.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.70 MB | 4.12 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0425s | -0.0037s | improved |
| `f1ap_rel18.6_specs` | 0.1053s | 0.1126s | -0.0073s | improved |
| `ngap_rel18.6_specs` | 0.0734s | 0.0801s | -0.0067s | improved |
| `lteNRRCC` | 0.1364s | 0.1422s | -0.0058s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.74 MB | 233.1% | 117.6% |
| `f1ap_rel18.6_specs` | 8.54 MB | 8.11 MB | 115.8% | 164.7% |
| `ngap_rel18.6_specs` | 7.50 MB | 7.68 MB | 163.9% | 159.9% |
| `lteNRRCC` | 7.84 MB | 50.80 MB | 99.9% | 107.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0342s | +0.0069s | worse |
| `f1ap_rel18.6_specs` | 0.1242s | 0.1010s | +0.0232s | worse |
| `ngap_rel18.6_specs` | 0.0857s | 0.0675s | +0.0182s | worse |
| `lteNRRCC` | 0.1405s | 0.1091s | +0.0314s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.94 MB | 8.94 MB | 164.7% | 82.3% |
| `f1ap_rel18.6_specs` | 10.06 MB | 162.98 MB | 163.9% | 222.7% |
| `ngap_rel18.6_specs` | 10.25 MB | 10.07 MB | 109.6% | 105.6% |
| `lteNRRCC` | 8.88 MB | 83.89 MB | 163.4% | 161.7% |
<!-- BENCH_RESULTS_END -->
