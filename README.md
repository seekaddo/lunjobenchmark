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
Generated: 2026-10-25T14:12:53.051738+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0387s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1195s | -0.0115s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0824s | -0.0074s | improved |
| `lteNRRCC` | 0.1190s | 0.1267s | -0.0077s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 16.7% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0263s | 0.0376s | -0.0113s | improved |
| `f1ap_rel18.6_specs` | 0.0720s | 0.0940s | -0.0220s | improved |
| `ngap_rel18.6_specs` | 0.0502s | 0.0679s | -0.0177s | improved |
| `lteNRRCC` | 0.0966s | 0.1292s | -0.0326s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 36.23 MB | 17.2% | 105.0% |
| `f1ap_rel18.6_specs` | 22.34 MB | 103.41 MB | 104.3% | 102.3% |
| `ngap_rel18.6_specs` | 18.15 MB | 74.47 MB | 105.3% | 103.0% |
| `lteNRRCC` | 48.59 MB | 66.12 MB | 102.1% | 103.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0341s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0976s | 0.0905s | +0.0071s | worse |
| `ngap_rel18.6_specs` | 0.0666s | 0.0614s | +0.0052s | worse |
| `lteNRRCC` | 0.1123s | 0.1162s | -0.0039s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 55.86 MB | 65.4% | 104.2% |
| `f1ap_rel18.6_specs` | 35.14 MB | 164.72 MB | 104.0% | 101.8% |
| `ngap_rel18.6_specs` | 24.25 MB | 117.46 MB | 105.0% | 100.0% |
| `lteNRRCC` | 74.80 MB | 102.30 MB | 101.9% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0233s | 0.0517s | -0.0284s | improved |
| `f1ap_rel18.6_specs` | 0.0974s | 0.0932s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0486s | 0.0757s | -0.0271s | improved |
| `lteNRRCC` | 0.0885s | 0.1128s | -0.0243s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.44 MB | 4.52 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 5.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.64 MB | 5.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.09 MB | 4.28 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0404s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1116s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0792s | 0.0766s | +0.0026s | worse |
| `lteNRRCC` | 0.1288s | 0.1409s | -0.0121s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.01 MB | 8.06 MB | 190.2% | 158.5% |
| `f1ap_rel18.6_specs` | 8.74 MB | 105.01 MB | 78.8% | 110.5% |
| `ngap_rel18.6_specs` | 10.68 MB | 8.47 MB | 122.4% | 96.1% |
| `lteNRRCC` | 8.67 MB | 50.81 MB | 96.3% | 162.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0351s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1101s | 0.0996s | +0.0105s | worse |
| `ngap_rel18.6_specs` | 0.0756s | 0.0707s | +0.0049s | worse |
| `lteNRRCC` | 0.1264s | 0.1108s | +0.0156s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.11 MB | 10.66 MB | 110.6% | 110.7% |
| `f1ap_rel18.6_specs` | 11.34 MB | 11.21 MB | 115.4% | 116.3% |
| `ngap_rel18.6_specs` | 10.95 MB | 10.82 MB | 117.8% | 116.1% |
| `lteNRRCC` | 9.87 MB | 98.63 MB | 233.9% | 230.2% |
<!-- BENCH_RESULTS_END -->
