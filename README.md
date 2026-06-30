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
Generated: 2026-06-30T12:16:21.480953+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0346s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1106s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0743s | 0.0758s | -0.0015s | improved |
| `lteNRRCC` | 0.1187s | 0.1183s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 11.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0365s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0937s | 0.1002s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0659s | 0.0686s | -0.0027s | improved |
| `lteNRRCC` | 0.1301s | 0.1326s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.21 MB | 18.7% | 111.1% |
| `f1ap_rel18.6_specs` | 21.34 MB | 103.10 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.55 MB | 107.7% | 107.0% |
| `lteNRRCC` | 48.37 MB | 66.30 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0346s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0923s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0716s | 0.0649s | +0.0067s | worse |
| `lteNRRCC` | 0.1179s | 0.1215s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.42 MB | 54.92 MB | 65.7% | 110.7% |
| `f1ap_rel18.6_specs` | 35.11 MB | 164.62 MB | 110.3% | 105.3% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.17 MB | 112.0% | 109.5% |
| `lteNRRCC` | 74.82 MB | 102.77 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0444s | 0.0241s | +0.0203s | worse |
| `f1ap_rel18.6_specs` | 0.0904s | 0.0685s | +0.0219s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0477s | +0.0186s | worse |
| `lteNRRCC` | 0.0917s | 0.0795s | +0.0122s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.33 MB | 4.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.56 MB | 2.70 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.91 MB | 7.84 MB | 0.0% | 0.0% |
| `lteNRRCC` | 9.44 MB | 7.52 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0394s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1090s | 0.1112s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0773s | -0.0030s | improved |
| `lteNRRCC` | 0.1384s | 0.1385s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.43 MB | 160.0% | 79.4% |
| `f1ap_rel18.6_specs` | 8.10 MB | 8.10 MB | 161.6% | 112.1% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.54 MB | 93.8% | 162.6% |
| `lteNRRCC` | 48.31 MB | 70.55 MB | 162.1% | 106.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0445s | 0.0397s | +0.0048s | worse |
| `f1ap_rel18.6_specs` | 0.1272s | 0.1137s | +0.0135s | worse |
| `ngap_rel18.6_specs` | 0.0868s | 0.0815s | +0.0053s | worse |
| `lteNRRCC` | 0.1415s | 0.1306s | +0.0109s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.21 MB | 9.07 MB | 111.8% | 164.9% |
| `f1ap_rel18.6_specs` | 9.93 MB | 164.18 MB | 163.0% | 105.2% |
| `ngap_rel18.6_specs` | 9.30 MB | 9.30 MB | 159.9% | 162.4% |
| `lteNRRCC` | 72.84 MB | 101.71 MB | 109.4% | 109.4% |
<!-- BENCH_RESULTS_END -->
