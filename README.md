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
Generated: 2026-07-22T23:10:33.676095+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0343s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1083s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0753s | 0.0749s | +0.0004s | worse |
| `lteNRRCC` | 0.1200s | 0.1181s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 22.0% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 106.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0337s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0927s | 0.0911s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0652s | 0.0636s | +0.0016s | worse |
| `lteNRRCC` | 0.1285s | 0.1233s | +0.0052s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.70 MB | 79.3% | 110.7% |
| `f1ap_rel18.6_specs` | 21.91 MB | 103.15 MB | 106.2% | 103.5% |
| `ngap_rel18.6_specs` | 17.62 MB | 73.67 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.21 MB | 66.07 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0330s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0883s | 0.0884s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0620s | 0.0620s | +0.0000s | flat |
| `lteNRRCC` | 0.1160s | 0.1151s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 55.83 MB | 22.0% | 107.4% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.28 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 23.93 MB | 117.83 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.61 MB | 102.65 MB | 105.3% | 105.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0450s | 0.0306s | +0.0144s | worse |
| `f1ap_rel18.6_specs` | 0.0733s | 0.0862s | -0.0129s | improved |
| `ngap_rel18.6_specs` | 0.0538s | 0.0613s | -0.0075s | improved |
| `lteNRRCC` | 0.0836s | 0.0990s | -0.0154s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.38 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.55 MB | 9.88 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.19 MB | 8.45 MB | 0.0% | 0.0% |
| `lteNRRCC` | 1.09 MB | 5.06 MB | 0.0% | 0.9% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0406s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1098s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0765s | -0.0015s | improved |
| `lteNRRCC` | 0.1399s | 0.1373s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.98 MB | 7.63 MB | 216.5% | 97.2% |
| `f1ap_rel18.6_specs` | 8.42 MB | 106.65 MB | 156.3% | 160.6% |
| `ngap_rel18.6_specs` | 7.93 MB | 8.12 MB | 78.3% | 108.6% |
| `lteNRRCC` | 50.82 MB | 51.86 MB | 107.2% | 217.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0449s | -0.0084s | improved |
| `f1ap_rel18.6_specs` | 0.1021s | 0.1333s | -0.0312s | improved |
| `ngap_rel18.6_specs` | 0.0722s | 0.0932s | -0.0210s | improved |
| `lteNRRCC` | 0.1130s | 0.1315s | -0.0185s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.73 MB | 10.08 MB | 133.0% | 124.4% |
| `f1ap_rel18.6_specs` | 9.99 MB | 136.16 MB | 217.8% | 112.5% |
| `ngap_rel18.6_specs` | 9.33 MB | 9.34 MB | 200.5% | 199.2% |
| `lteNRRCC` | 9.23 MB | 83.64 MB | 194.7% | 103.3% |
<!-- BENCH_RESULTS_END -->
