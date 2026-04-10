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
Generated: 2026-04-10T22:45:55.680983+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0390s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1184s | -0.0075s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0812s | -0.0054s | improved |
| `lteNRRCC` | 0.1226s | 0.1248s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.72 MB | 53.55 MB | 7.4% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0315s | 0.0355s | -0.0040s | improved |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0943s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0668s | -0.0028s | improved |
| `lteNRRCC` | 0.1148s | 0.1274s | -0.0126s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.36 MB | 36.45 MB | 23.8% | 108.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.61 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.53 MB | 109.1% | 104.9% |
| `lteNRRCC` | 48.54 MB | 66.08 MB | 103.6% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0331s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0886s | 0.0910s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0620s | 0.0625s | -0.0005s | improved |
| `lteNRRCC` | 0.1156s | 0.1161s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.73 MB | 92.0% | 111.1% |
| `f1ap_rel18.6_specs` | 35.27 MB | 163.21 MB | 110.0% | 105.5% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.68 MB | 116.0% | 107.1% |
| `lteNRRCC` | 74.69 MB | 102.54 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0213s | 0.0249s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.0646s | 0.0814s | -0.0168s | improved |
| `ngap_rel18.6_specs` | 0.0431s | 0.0694s | -0.0263s | improved |
| `lteNRRCC` | 0.0729s | 0.0910s | -0.0181s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.33 MB | 5.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.55 MB | 4.22 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.41 MB | 4.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.67 MB | 3.73 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0399s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1163s | 0.1119s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0791s | 0.0783s | +0.0008s | worse |
| `lteNRRCC` | 0.1402s | 0.1394s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.80 MB | 7.68 MB | 82.7% | 84.0% |
| `f1ap_rel18.6_specs` | 8.45 MB | 103.23 MB | 84.3% | 169.0% |
| `ngap_rel18.6_specs` | 8.47 MB | 8.23 MB | 184.1% | 91.1% |
| `lteNRRCC` | 48.31 MB | 69.60 MB | 104.4% | 107.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0428s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.1135s | 0.1187s | -0.0052s | improved |
| `ngap_rel18.6_specs` | 0.0786s | 0.0829s | -0.0043s | improved |
| `lteNRRCC` | 0.1302s | 0.1295s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.64 MB | 8.93 MB | 112.5% | 156.6% |
| `f1ap_rel18.6_specs` | 9.92 MB | 11.75 MB | 77.7% | 214.2% |
| `ngap_rel18.6_specs` | 10.60 MB | 9.26 MB | 217.1% | 153.3% |
| `lteNRRCC` | 8.61 MB | 83.32 MB | 169.6% | 153.3% |
<!-- BENCH_RESULTS_END -->
