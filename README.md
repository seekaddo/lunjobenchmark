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
Generated: 2026-05-09T11:02:42.870218+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0359s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1133s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0773s | -0.0018s | improved |
| `lteNRRCC` | 0.1180s | 0.1234s | -0.0054s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 24.4% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0376s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.0982s | 0.1037s | -0.0055s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0720s | -0.0068s | improved |
| `lteNRRCC` | 0.1280s | 0.1322s | -0.0042s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.51 MB | 88.9% | 106.9% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.93 MB | 109.1% | 103.4% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.61 MB | 111.1% | 106.8% |
| `lteNRRCC` | 47.80 MB | 66.45 MB | 106.2% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0325s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0884s | 0.0889s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0618s | +0.0000s | flat |
| `lteNRRCC` | 0.1169s | 0.1159s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.88 MB | 20.5% | 111.1% |
| `f1ap_rel18.6_specs` | 34.23 MB | 164.18 MB | 113.8% | 105.5% |
| `ngap_rel18.6_specs` | 24.16 MB | 117.80 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.88 MB | 102.93 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0209s | 0.0244s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.0770s | 0.0765s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0726s | 0.0549s | +0.0177s | worse |
| `lteNRRCC` | 0.0734s | 0.0738s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.41 MB | 4.27 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.05 MB | 3.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.84 MB | 4.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.59 MB | 5.48 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0413s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1088s | 0.1176s | -0.0088s | improved |
| `ngap_rel18.6_specs` | 0.0767s | 0.0816s | -0.0049s | improved |
| `lteNRRCC` | 0.1404s | 0.1432s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.37 MB | 159.4% | 161.8% |
| `f1ap_rel18.6_specs` | 8.04 MB | 7.97 MB | 81.6% | 80.4% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.67 MB | 241.5% | 77.0% |
| `lteNRRCC` | 48.81 MB | 69.04 MB | 107.4% | 221.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0490s | -0.0094s | improved |
| `f1ap_rel18.6_specs` | 0.1123s | 0.1349s | -0.0226s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0918s | -0.0152s | improved |
| `lteNRRCC` | 0.1254s | 0.1375s | -0.0121s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.59 MB | 8.59 MB | 157.8% | 158.9% |
| `f1ap_rel18.6_specs` | 9.94 MB | 9.56 MB | 167.9% | 80.5% |
| `ngap_rel18.6_specs` | 9.02 MB | 8.93 MB | 80.6% | 159.4% |
| `lteNRRCC` | 8.50 MB | 92.39 MB | 78.8% | 206.9% |
<!-- BENCH_RESULTS_END -->
