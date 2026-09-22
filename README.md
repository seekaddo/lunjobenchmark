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
Generated: 2026-09-22T14:35:38.204159+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0353s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1089s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0753s | 0.0757s | -0.0004s | improved |
| `lteNRRCC` | 0.1192s | 0.1196s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 72.0% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0352s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0982s | 0.0953s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0696s | 0.0689s | +0.0007s | worse |
| `lteNRRCC` | 0.1317s | 0.1291s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.41 MB | 75.9% | 107.1% |
| `f1ap_rel18.6_specs` | 22.31 MB | 103.08 MB | 103.1% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.25 MB | 103.8% | 104.5% |
| `lteNRRCC` | 47.67 MB | 66.05 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0334s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0905s | 0.0898s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0630s | 0.0622s | +0.0008s | worse |
| `lteNRRCC` | 0.1179s | 0.1180s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 55.66 MB | 66.7% | 107.7% |
| `f1ap_rel18.6_specs` | 34.55 MB | 164.48 MB | 103.6% | 103.7% |
| `ngap_rel18.6_specs` | 24.11 MB | 117.44 MB | 108.7% | 105.0% |
| `lteNRRCC` | 74.87 MB | 102.86 MB | 103.5% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0310s | 0.0332s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1063s | 0.0858s | +0.0205s | worse |
| `ngap_rel18.6_specs` | 0.0717s | 0.0916s | -0.0199s | improved |
| `lteNRRCC` | 0.0860s | 0.1053s | -0.0193s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.33 MB | 8.00 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.03 MB | 9.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.38 MB | 464 KB | 0.0% | 0.0% |
| `lteNRRCC` | 8.53 MB | 6.95 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0390s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1150s | 0.1069s | +0.0081s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0737s | +0.0063s | worse |
| `lteNRRCC` | 0.1431s | 0.1375s | +0.0056s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.53 MB | 8.48 MB | 0.0% | 210.7% |
| `f1ap_rel18.6_specs` | 8.77 MB | 8.71 MB | 160.0% | 162.0% |
| `ngap_rel18.6_specs` | 8.24 MB | 8.34 MB | 103.1% | 158.2% |
| `lteNRRCC` | 51.81 MB | 70.53 MB | 212.1% | 217.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0308s | +0.0077s | worse |
| `f1ap_rel18.6_specs` | 0.1142s | 0.0858s | +0.0284s | worse |
| `ngap_rel18.6_specs` | 0.0756s | 0.0589s | +0.0167s | worse |
| `lteNRRCC` | 0.1263s | 0.0894s | +0.0369s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.23 MB | 0.0% | 101.6% |
| `f1ap_rel18.6_specs` | 10.90 MB | 11.31 MB | 230.0% | 114.9% |
| `ngap_rel18.6_specs` | 10.44 MB | 10.55 MB | 115.9% | 110.9% |
| `lteNRRCC` | 8.36 MB | 92.44 MB | 173.9% | 106.3% |
<!-- BENCH_RESULTS_END -->
