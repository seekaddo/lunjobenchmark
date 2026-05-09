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
Generated: 2026-05-09T22:55:02.269951+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0354s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1142s | 0.1104s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0783s | 0.0755s | +0.0028s | worse |
| `lteNRRCC` | 0.1225s | 0.1180s | +0.0045s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.94 MB | 53.55 MB | 29.1% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 116.0% | 103.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0346s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0922s | 0.0982s | -0.0060s | improved |
| `ngap_rel18.6_specs` | 0.0648s | 0.0652s | -0.0004s | improved |
| `lteNRRCC` | 0.1281s | 0.1280s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.46 MB | 27.3% | 107.1% |
| `f1ap_rel18.6_specs` | 22.38 MB | 103.48 MB | 109.4% | 105.4% |
| `ngap_rel18.6_specs` | 16.76 MB | 74.47 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.44 MB | 66.51 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0331s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0984s | 0.0884s | +0.0100s | worse |
| `ngap_rel18.6_specs` | 0.0693s | 0.0618s | +0.0075s | worse |
| `lteNRRCC` | 0.1159s | 0.1169s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.33 MB | 55.72 MB | 23.8% | 107.7% |
| `f1ap_rel18.6_specs` | 35.14 MB | 163.82 MB | 111.1% | 103.4% |
| `ngap_rel18.6_specs` | 24.51 MB | 117.78 MB | 109.1% | 104.7% |
| `lteNRRCC` | 74.50 MB | 102.91 MB | 105.5% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0208s | 0.0209s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0693s | 0.0770s | -0.0077s | improved |
| `ngap_rel18.6_specs` | 0.0396s | 0.0726s | -0.0330s | improved |
| `lteNRRCC` | 0.0676s | 0.0734s | -0.0058s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.33 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.81 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.88 MB | 3.61 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0397s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1088s | +0.0055s | worse |
| `ngap_rel18.6_specs` | 0.0797s | 0.0767s | +0.0030s | worse |
| `lteNRRCC` | 0.1409s | 0.1404s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.97 MB | 8.04 MB | 79.8% | 157.6% |
| `f1ap_rel18.6_specs` | 8.67 MB | 98.74 MB | 166.8% | 105.9% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.36 MB | 211.9% | 158.5% |
| `lteNRRCC` | 51.27 MB | 69.11 MB | 157.7% | 158.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0396s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1123s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0766s | +0.0003s | worse |
| `lteNRRCC` | 0.1244s | 0.1254s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.72 MB | 8.66 MB | 103.8% | 157.1% |
| `f1ap_rel18.6_specs` | 11.96 MB | 164.20 MB | 141.4% | 107.5% |
| `ngap_rel18.6_specs` | 8.90 MB | 8.96 MB | 78.4% | 167.5% |
| `lteNRRCC` | 8.57 MB | 97.71 MB | 77.9% | 108.3% |
<!-- BENCH_RESULTS_END -->
