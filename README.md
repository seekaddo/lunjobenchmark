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
Generated: 2026-04-17T22:51:23.339126+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0370s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1113s | 0.1167s | -0.0054s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0803s | -0.0025s | improved |
| `lteNRRCC` | 0.1207s | 0.1234s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.88 MB | 53.55 MB | 27.5% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 116.0% | 105.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 106.7% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0326s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.1006s | -0.0069s | improved |
| `ngap_rel18.6_specs` | 0.0663s | 0.0699s | -0.0036s | improved |
| `lteNRRCC` | 0.1317s | 0.1208s | +0.0109s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 35.90 MB | 92.3% | 110.7% |
| `f1ap_rel18.6_specs` | 22.36 MB | 102.97 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.80 MB | 74.59 MB | 111.1% | 104.5% |
| `lteNRRCC` | 48.80 MB | 66.07 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0344s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0904s | +0.0035s | worse |
| `ngap_rel18.6_specs` | 0.0649s | 0.0638s | +0.0011s | worse |
| `lteNRRCC` | 0.1274s | 0.1181s | +0.0093s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.72 MB | 89.3% | 113.3% |
| `f1ap_rel18.6_specs` | 34.64 MB | 164.77 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 23.59 MB | 117.82 MB | 111.1% | 108.7% |
| `lteNRRCC` | 74.86 MB | 101.75 MB | 104.7% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0202s | 0.0517s | -0.0315s | improved |
| `f1ap_rel18.6_specs` | 0.0663s | 0.1084s | -0.0421s | improved |
| `ngap_rel18.6_specs` | 0.0463s | 0.0811s | -0.0348s | improved |
| `lteNRRCC` | 0.0748s | 0.1158s | -0.0410s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 3.55 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.91 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.62 MB | 512 KB | 0.0% | 0.0% |
| `lteNRRCC` | 4.72 MB | 5.31 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0398s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1084s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0735s | 0.0781s | -0.0046s | improved |
| `lteNRRCC` | 0.1361s | 0.1273s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.29 MB | 164.2% | 166.7% |
| `f1ap_rel18.6_specs` | 8.11 MB | 7.88 MB | 110.6% | 165.2% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.47 MB | 164.2% | 96.3% |
| `lteNRRCC` | 51.21 MB | 68.91 MB | 169.4% | 103.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0420s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1154s | -0.0050s | improved |
| `ngap_rel18.6_specs` | 0.0809s | 0.0801s | +0.0008s | worse |
| `lteNRRCC` | 0.1260s | 0.1357s | -0.0097s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.52 MB | 8.58 MB | 225.1% | 79.7% |
| `f1ap_rel18.6_specs` | 11.45 MB | 164.20 MB | 115.1% | 107.1% |
| `ngap_rel18.6_specs` | 8.89 MB | 8.77 MB | 155.7% | 159.5% |
| `lteNRRCC` | 8.62 MB | 82.92 MB | 153.2% | 152.0% |
<!-- BENCH_RESULTS_END -->
