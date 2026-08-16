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
Generated: 2026-08-16T22:27:58.157625+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0335s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1083s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0753s | 0.0738s | +0.0015s | worse |
| `lteNRRCC` | 0.1193s | 0.1170s | +0.0023s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 19.8% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0219s | 0.0358s | -0.0139s | improved |
| `f1ap_rel18.6_specs` | 0.0692s | 0.0951s | -0.0259s | improved |
| `ngap_rel18.6_specs` | 0.0458s | 0.0679s | -0.0221s | improved |
| `lteNRRCC` | 0.0826s | 0.1308s | -0.0482s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.37 MB | 36.54 MB | 11.8% | 105.9% |
| `f1ap_rel18.6_specs` | 22.02 MB | 103.45 MB | 105.3% | 102.5% |
| `ngap_rel18.6_specs` | 19.42 MB | 74.21 MB | 100.0% | 100.0% |
| `lteNRRCC` | 48.62 MB | 66.32 MB | 102.6% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0283s | +0.0065s | worse |
| `f1ap_rel18.6_specs` | 0.0944s | 0.0767s | +0.0177s | worse |
| `ngap_rel18.6_specs` | 0.0656s | 0.0525s | +0.0131s | worse |
| `lteNRRCC` | 0.1270s | 0.1023s | +0.0247s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.47 MB | 84.6% | 103.6% |
| `f1ap_rel18.6_specs` | 34.74 MB | 164.64 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 24.50 MB | 117.65 MB | 104.0% | 104.8% |
| `lteNRRCC` | 74.82 MB | 102.87 MB | 103.2% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0234s | 0.0238s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0676s | 0.0660s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0466s | 0.0455s | +0.0011s | worse |
| `lteNRRCC` | 0.0773s | 0.0753s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.08 MB | 4.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 5.08 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.98 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.86 MB | 3.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0385s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1065s | 0.1071s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0754s | 0.0748s | +0.0006s | worse |
| `lteNRRCC` | 0.1380s | 0.1402s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.31 MB | 7.70 MB | 0.0% | 234.8% |
| `f1ap_rel18.6_specs` | 7.96 MB | 8.04 MB | 162.9% | 102.4% |
| `ngap_rel18.6_specs` | 7.87 MB | 7.99 MB | 105.9% | 108.1% |
| `lteNRRCC` | 51.84 MB | 70.55 MB | 167.3% | 161.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0373s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1088s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0744s | +0.0013s | worse |
| `lteNRRCC` | 0.1363s | 0.1475s | -0.0112s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.66 MB | 0.0% | 158.3% |
| `f1ap_rel18.6_specs` | 9.74 MB | 11.02 MB | 159.8% | 228.3% |
| `ngap_rel18.6_specs` | 10.19 MB | 8.83 MB | 106.4% | 160.4% |
| `lteNRRCC` | 9.86 MB | 72.37 MB | 222.2% | 155.2% |
<!-- BENCH_RESULTS_END -->
