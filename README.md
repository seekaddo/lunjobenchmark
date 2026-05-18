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
Generated: 2026-05-18T23:11:59.623685+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0347s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1125s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0787s | 0.0780s | +0.0007s | worse |
| `lteNRRCC` | 0.1235s | 0.1199s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 9.6% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.5% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 104.8% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0339s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0920s | 0.0917s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0638s | 0.0640s | -0.0002s | improved |
| `lteNRRCC` | 0.1237s | 0.1238s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.79 MB | 36.69 MB | 92.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.35 MB | 103.00 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.63 MB | 73.91 MB | 111.1% | 104.5% |
| `lteNRRCC` | 48.69 MB | 66.38 MB | 104.8% | 105.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0327s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0910s | 0.0890s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0632s | 0.0619s | +0.0013s | worse |
| `lteNRRCC` | 0.1247s | 0.1156s | +0.0091s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.82 MB | 55.87 MB | 34.3% | 110.7% |
| `f1ap_rel18.6_specs` | 34.64 MB | 164.40 MB | 110.0% | 103.6% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.37 MB | 108.0% | 104.8% |
| `lteNRRCC` | 74.75 MB | 102.86 MB | 103.4% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0336s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0796s | 0.0732s | +0.0064s | worse |
| `ngap_rel18.6_specs` | 0.0570s | 0.0475s | +0.0095s | worse |
| `lteNRRCC` | 0.0856s | 0.0981s | -0.0125s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.20 MB | 4.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.36 MB | 4.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.19 MB | 3.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.55 MB | 4.50 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0441s | -0.0050s | improved |
| `f1ap_rel18.6_specs` | 0.1103s | 0.1192s | -0.0089s | improved |
| `ngap_rel18.6_specs` | 0.0772s | 0.0799s | -0.0027s | improved |
| `lteNRRCC` | 0.1378s | 0.1418s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.50 MB | 80.7% | 80.5% |
| `f1ap_rel18.6_specs` | 8.10 MB | 8.61 MB | 160.3% | 228.0% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.18 MB | 114.9% | 229.1% |
| `lteNRRCC` | 8.22 MB | 68.18 MB | 166.2% | 157.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0388s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1130s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0784s | -0.0021s | improved |
| `lteNRRCC` | 0.1280s | 0.1281s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.27 MB | 8.47 MB | 166.4% | 160.0% |
| `f1ap_rel18.6_specs` | 11.34 MB | 9.75 MB | 111.1% | 175.6% |
| `ngap_rel18.6_specs` | 10.49 MB | 8.71 MB | 233.2% | 162.8% |
| `lteNRRCC` | 73.78 MB | 87.40 MB | 109.0% | 175.1% |
<!-- BENCH_RESULTS_END -->
