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
Generated: 2026-09-07T15:42:06.639774+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0345s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1120s | 0.1081s | +0.0039s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0732s | +0.0025s | worse |
| `lteNRRCC` | 0.1203s | 0.1164s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 78.3% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0326s | 0.0353s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0947s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0665s | -0.0013s | improved |
| `lteNRRCC` | 0.1153s | 0.1328s | -0.0175s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 36.52 MB | 77.3% | 104.2% |
| `f1ap_rel18.6_specs` | 22.42 MB | 103.50 MB | 107.7% | 101.8% |
| `ngap_rel18.6_specs` | 17.99 MB | 74.37 MB | 104.8% | 102.5% |
| `lteNRRCC` | 48.34 MB | 65.71 MB | 101.8% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0286s | 0.0346s | -0.0060s | improved |
| `f1ap_rel18.6_specs` | 0.0753s | 0.0919s | -0.0166s | improved |
| `ngap_rel18.6_specs` | 0.0528s | 0.0649s | -0.0121s | improved |
| `lteNRRCC` | 0.1018s | 0.1191s | -0.0173s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 55.38 MB | 85.0% | 109.1% |
| `f1ap_rel18.6_specs` | 35.13 MB | 164.58 MB | 104.2% | 104.3% |
| `ngap_rel18.6_specs` | 23.76 MB | 117.87 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.96 MB | 102.71 MB | 102.0% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0217s | 0.0296s | -0.0079s | improved |
| `f1ap_rel18.6_specs` | 0.0638s | 0.1024s | -0.0386s | improved |
| `ngap_rel18.6_specs` | 0.0513s | 0.0681s | -0.0168s | improved |
| `lteNRRCC` | 0.0782s | 0.1190s | -0.0408s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.58 MB | 7.69 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.27 MB | 7.80 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.02 MB | 4.34 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.22 MB | 4.05 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0394s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.0955s | 0.1063s | -0.0108s | improved |
| `ngap_rel18.6_specs` | 0.0676s | 0.0759s | -0.0083s | improved |
| `lteNRRCC` | 0.1133s | 0.1368s | -0.0235s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.42 MB | 8.40 MB | 126.1% | 96.8% |
| `f1ap_rel18.6_specs` | 8.95 MB | 106.65 MB | 99.1% | 106.5% |
| `ngap_rel18.6_specs` | 8.43 MB | 8.49 MB | 100.1% | 98.0% |
| `lteNRRCC` | 8.60 MB | 59.11 MB | 118.9% | 193.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0390s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1201s | 0.1111s | +0.0090s | worse |
| `ngap_rel18.6_specs` | 0.0831s | 0.0782s | +0.0049s | worse |
| `lteNRRCC` | 0.1376s | 0.1288s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.98 MB | 9.54 MB | 103.6% | 162.5% |
| `f1ap_rel18.6_specs` | 10.19 MB | 164.20 MB | 162.2% | 216.4% |
| `ngap_rel18.6_specs` | 10.09 MB | 10.10 MB | 157.4% | 155.9% |
| `lteNRRCC` | 73.28 MB | 80.52 MB | 155.9% | 160.2% |
<!-- BENCH_RESULTS_END -->
