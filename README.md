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
Generated: 2026-05-19T12:46:05.648480+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0375s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1155s | 0.1157s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0788s | 0.0787s | +0.0001s | worse |
| `lteNRRCC` | 0.1234s | 0.1235s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 28.4% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0337s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0956s | 0.0920s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0686s | 0.0638s | +0.0048s | worse |
| `lteNRRCC` | 0.1304s | 0.1237s | +0.0067s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.81 MB | 36.33 MB | 88.9% | 113.8% |
| `f1ap_rel18.6_specs` | 22.22 MB | 103.16 MB | 108.8% | 104.9% |
| `ngap_rel18.6_specs` | 16.61 MB | 73.71 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.65 MB | 66.54 MB | 104.5% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0347s | +0.0043s | worse |
| `f1ap_rel18.6_specs` | 0.1002s | 0.0910s | +0.0092s | worse |
| `ngap_rel18.6_specs` | 0.0715s | 0.0632s | +0.0083s | worse |
| `lteNRRCC` | 0.1355s | 0.1247s | +0.0108s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.80 MB | 55.08 MB | 25.7% | 112.5% |
| `f1ap_rel18.6_specs` | 34.39 MB | 164.75 MB | 108.8% | 106.2% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.36 MB | 110.3% | 106.0% |
| `lteNRRCC` | 74.95 MB | 102.31 MB | 104.5% | 103.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0273s | 0.0345s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0796s | +0.0139s | worse |
| `ngap_rel18.6_specs` | 0.0499s | 0.0570s | -0.0071s | improved |
| `lteNRRCC` | 0.1086s | 0.0856s | +0.0230s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.67 MB | 6.06 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.23 MB | 4.19 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.98 MB | 7.69 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.80 MB | 3.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0452s | 0.0391s | +0.0061s | worse |
| `f1ap_rel18.6_specs` | 0.1251s | 0.1103s | +0.0148s | worse |
| `ngap_rel18.6_specs` | 0.0868s | 0.0772s | +0.0096s | worse |
| `lteNRRCC` | 0.1495s | 0.1378s | +0.0117s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.96 MB | 7.62 MB | 198.7% | 75.4% |
| `f1ap_rel18.6_specs` | 8.23 MB | 106.64 MB | 151.7% | 108.6% |
| `ngap_rel18.6_specs` | 7.87 MB | 8.05 MB | 85.7% | 147.4% |
| `lteNRRCC` | 8.41 MB | 70.55 MB | 146.5% | 106.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0431s | 0.0410s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1257s | 0.1106s | +0.0151s | worse |
| `ngap_rel18.6_specs` | 0.0868s | 0.0763s | +0.0105s | worse |
| `lteNRRCC` | 0.1410s | 0.1280s | +0.0130s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.01 MB | 9.01 MB | 91.0% | 81.6% |
| `f1ap_rel18.6_specs` | 10.16 MB | 145.23 MB | 82.0% | 160.5% |
| `ngap_rel18.6_specs` | 9.41 MB | 9.27 MB | 164.4% | 164.3% |
| `lteNRRCC` | 8.87 MB | 99.77 MB | 161.5% | 108.5% |
<!-- BENCH_RESULTS_END -->
