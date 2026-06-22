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
Generated: 2026-06-22T15:27:44.311754+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0360s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1123s | 0.1130s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0769s | -0.0001s | improved |
| `lteNRRCC` | 0.1190s | 0.1211s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 22.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 106.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.3% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0329s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0933s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0684s | 0.0648s | +0.0036s | worse |
| `lteNRRCC` | 0.1264s | 0.1170s | +0.0094s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.38 MB | 88.5% | 106.9% |
| `f1ap_rel18.6_specs` | 22.25 MB | 103.35 MB | 109.1% | 105.0% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.44 MB | 111.1% | 106.5% |
| `lteNRRCC` | 48.55 MB | 66.29 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0338s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0907s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0656s | 0.0631s | +0.0025s | worse |
| `lteNRRCC` | 0.1222s | 0.1171s | +0.0051s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.29 MB | 55.64 MB | 78.6% | 106.9% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.52 MB | 110.0% | 105.3% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.49 MB | 112.0% | 106.8% |
| `lteNRRCC` | 74.91 MB | 102.59 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0188s | 0.0290s | -0.0102s | improved |
| `f1ap_rel18.6_specs` | 0.0662s | 0.0804s | -0.0142s | improved |
| `ngap_rel18.6_specs` | 0.0402s | 0.0602s | -0.0200s | improved |
| `lteNRRCC` | 0.0737s | 0.0761s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.44 MB | 4.44 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.05 MB | 3.84 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.33 MB | 5.30 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.88 MB | 4.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0384s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0998s | 0.1051s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0699s | 0.0761s | -0.0062s | improved |
| `lteNRRCC` | 0.1283s | 0.1370s | -0.0087s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.57 MB | 7.75 MB | 108.1% | 186.6% |
| `f1ap_rel18.6_specs` | 8.44 MB | 8.04 MB | 111.1% | 168.1% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.17 MB | 124.8% | 124.4% |
| `lteNRRCC` | 51.64 MB | 49.25 MB | 122.7% | 120.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0429s | 0.0443s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1220s | 0.1285s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0856s | 0.0881s | -0.0025s | improved |
| `lteNRRCC` | 0.1403s | 0.1346s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.58 MB | 9.65 MB | 160.5% | 80.5% |
| `f1ap_rel18.6_specs` | 10.64 MB | 163.16 MB | 108.7% | 154.5% |
| `ngap_rel18.6_specs` | 10.11 MB | 9.35 MB | 161.6% | 158.7% |
| `lteNRRCC` | 70.63 MB | 101.71 MB | 157.0% | 105.2% |
<!-- BENCH_RESULTS_END -->
