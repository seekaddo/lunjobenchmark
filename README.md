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
Generated: 2026-03-16T22:42:17.350150+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0418s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1235s | 0.1304s | -0.0069s | improved |
| `ngap_rel18.6_specs` | 0.0848s | 0.0903s | -0.0055s | improved |
| `lteNRRCC` | 0.1251s | 0.1267s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.53 MB | 55.78 MB | 105.3% | 110.0% |
| `f1ap_rel18.6_specs` | 32.53 MB | 176.91 MB | 106.9% | 102.8% |
| `ngap_rel18.6_specs` | 22.41 MB | 125.78 MB | 113.0% | 103.8% |
| `lteNRRCC` | 72.32 MB | 100.09 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0364s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.0975s | 0.0970s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0674s | 0.0683s | -0.0009s | improved |
| `lteNRRCC` | 0.1164s | 0.1301s | -0.0137s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.55 MB | 37.86 MB | 18.8% | 107.7% |
| `f1ap_rel18.6_specs` | 22.39 MB | 111.93 MB | 107.1% | 103.4% |
| `ngap_rel18.6_specs` | 16.05 MB | 80.14 MB | 113.6% | 107.0% |
| `lteNRRCC` | 48.73 MB | 65.82 MB | 103.5% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0350s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0923s | 0.0922s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0659s | 0.0656s | +0.0003s | worse |
| `lteNRRCC` | 0.1144s | 0.1146s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.31 MB | 57.88 MB | 92.3% | 110.0% |
| `f1ap_rel18.6_specs` | 34.25 MB | 179.27 MB | 110.0% | 105.2% |
| `ngap_rel18.6_specs` | 23.58 MB | 127.07 MB | 112.0% | 106.7% |
| `lteNRRCC` | 74.00 MB | 102.80 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0200s | 0.0287s | -0.0087s | improved |
| `f1ap_rel18.6_specs` | 0.0719s | 0.0934s | -0.0215s | improved |
| `ngap_rel18.6_specs` | 0.0424s | 0.0701s | -0.0277s | improved |
| `lteNRRCC` | 0.0717s | 0.1001s | -0.0284s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.52 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.94 MB | 4.14 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 4.11 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.03 MB | 3.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0408s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1114s | 0.1167s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0782s | 0.0810s | -0.0028s | improved |
| `lteNRRCC` | 0.1266s | 0.1415s | -0.0149s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.79 MB | 7.95 MB | 163.8% | 173.6% |
| `f1ap_rel18.6_specs` | 8.61 MB | 8.49 MB | 163.1% | 163.0% |
| `ngap_rel18.6_specs` | 8.42 MB | 8.22 MB | 238.3% | 118.6% |
| `lteNRRCC` | 8.18 MB | 8.04 MB | 91.5% | 163.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0376s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1203s | 0.1137s | +0.0066s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0789s | +0.0011s | worse |
| `lteNRRCC` | 0.1268s | 0.1246s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.77 MB | 8.77 MB | 161.3% | 161.1% |
| `f1ap_rel18.6_specs` | 9.53 MB | 179.18 MB | 161.4% | 162.1% |
| `ngap_rel18.6_specs` | 10.14 MB | 10.63 MB | 112.3% | 231.9% |
| `lteNRRCC` | 73.82 MB | 94.07 MB | 108.8% | 158.4% |
<!-- BENCH_RESULTS_END -->
