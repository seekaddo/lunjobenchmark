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
Generated: 2026-06-29T23:04:15.098096+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0341s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1092s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0758s | 0.0744s | +0.0014s | worse |
| `lteNRRCC` | 0.1183s | 0.1184s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 22.0% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0358s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1002s | 0.0945s | +0.0057s | worse |
| `ngap_rel18.6_specs` | 0.0686s | 0.0664s | +0.0022s | worse |
| `lteNRRCC` | 0.1326s | 0.1294s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 36.63 MB | 88.9% | 106.9% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.39 MB | 109.1% | 104.9% |
| `ngap_rel18.6_specs` | 17.73 MB | 74.59 MB | 111.1% | 106.5% |
| `lteNRRCC` | 48.66 MB | 66.36 MB | 105.9% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0342s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0923s | 0.0990s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0677s | -0.0028s | improved |
| `lteNRRCC` | 0.1215s | 0.1173s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 55.40 MB | 79.3% | 110.7% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.46 MB | 106.7% | 105.3% |
| `ngap_rel18.6_specs` | 24.26 MB | 117.54 MB | 108.0% | 107.1% |
| `lteNRRCC` | 75.00 MB | 102.74 MB | 105.1% | 105.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0241s | 0.0195s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.0685s | 0.1166s | -0.0481s | improved |
| `ngap_rel18.6_specs` | 0.0477s | 0.0519s | -0.0042s | improved |
| `lteNRRCC` | 0.0795s | 0.0842s | -0.0047s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.95 MB | 6.11 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 5.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.61 MB | 5.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.75 MB | 4.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0406s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1132s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0773s | 0.0781s | -0.0008s | improved |
| `lteNRRCC` | 0.1385s | 0.1413s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.57 MB | 6.74 MB | 99.0% | 220.7% |
| `f1ap_rel18.6_specs` | 8.43 MB | 106.57 MB | 114.0% | 114.5% |
| `ngap_rel18.6_specs` | 7.36 MB | 7.61 MB | 98.4% | 83.7% |
| `lteNRRCC` | 46.37 MB | 70.55 MB | 161.5% | 165.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0392s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1137s | 0.1132s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0815s | 0.0778s | +0.0037s | worse |
| `lteNRRCC` | 0.1306s | 0.1290s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.33 MB | 8.93 MB | 178.8% | 97.6% |
| `f1ap_rel18.6_specs` | 11.26 MB | 164.20 MB | 109.3% | 227.8% |
| `ngap_rel18.6_specs` | 10.32 MB | 9.02 MB | 113.5% | 159.6% |
| `lteNRRCC` | 8.31 MB | 96.14 MB | 156.0% | 116.8% |
<!-- BENCH_RESULTS_END -->
