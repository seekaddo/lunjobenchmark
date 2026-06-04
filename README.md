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
Generated: 2026-06-04T12:48:01.372261+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0374s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.1074s | 0.1148s | -0.0074s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0786s | -0.0048s | improved |
| `lteNRRCC` | 0.1166s | 0.1223s | -0.0057s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 25.0% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 104.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0352s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.0989s | 0.0941s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0697s | 0.0668s | +0.0029s | worse |
| `lteNRRCC` | 0.1313s | 0.1301s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.09 MB | 80.6% | 110.0% |
| `f1ap_rel18.6_specs` | 22.16 MB | 103.40 MB | 108.8% | 106.7% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.09 MB | 114.3% | 106.4% |
| `lteNRRCC` | 48.73 MB | 66.46 MB | 106.1% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0355s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0912s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0652s | 0.0654s | -0.0002s | improved |
| `lteNRRCC` | 0.1269s | 0.1165s | +0.0104s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.82 MB | 25.8% | 110.3% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.77 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.08 MB | 117.62 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.80 MB | 102.11 MB | 104.7% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0190s | 0.0248s | -0.0058s | improved |
| `f1ap_rel18.6_specs` | 0.0684s | 0.0842s | -0.0158s | improved |
| `ngap_rel18.6_specs` | 0.0482s | 0.0518s | -0.0036s | improved |
| `lteNRRCC` | 0.0789s | 0.0855s | -0.0066s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.97 MB | 5.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.89 MB | 3.86 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.12 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.11 MB | 3.73 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0405s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1119s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0763s | +0.0003s | worse |
| `lteNRRCC` | 0.1386s | 0.1391s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.56 MB | 160.3% | 173.0% |
| `f1ap_rel18.6_specs` | 8.42 MB | 106.64 MB | 156.3% | 158.4% |
| `ngap_rel18.6_specs` | 8.05 MB | 7.98 MB | 146.2% | 155.1% |
| `lteNRRCC` | 8.22 MB | 59.84 MB | 99.8% | 157.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0454s | 0.0438s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1290s | 0.1274s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0921s | 0.0876s | +0.0045s | worse |
| `lteNRRCC` | 0.1446s | 0.1349s | +0.0097s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.02 MB | 9.65 MB | 86.1% | 158.4% |
| `f1ap_rel18.6_specs` | 10.11 MB | 146.72 MB | 155.0% | 155.1% |
| `ngap_rel18.6_specs` | 10.44 MB | 10.11 MB | 150.1% | 151.4% |
| `lteNRRCC` | 73.15 MB | 85.89 MB | 173.4% | 151.3% |
<!-- BENCH_RESULTS_END -->
