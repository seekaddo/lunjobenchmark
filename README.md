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
Generated: 2026-04-21T11:15:35.624199+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0360s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1167s | 0.1127s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0768s | +0.0018s | worse |
| `lteNRRCC` | 0.1217s | 0.1195s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 29.5% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.9% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0346s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0951s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0668s | -0.0014s | improved |
| `lteNRRCC` | 0.1271s | 0.1256s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.13 MB | 36.59 MB | 31.6% | 110.7% |
| `f1ap_rel18.6_specs` | 22.09 MB | 103.31 MB | 109.4% | 105.4% |
| `ngap_rel18.6_specs` | 16.83 MB | 74.61 MB | 115.4% | 107.0% |
| `lteNRRCC` | 48.45 MB | 66.03 MB | 104.5% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0324s | 0.0335s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0962s | 0.0883s | +0.0079s | worse |
| `ngap_rel18.6_specs` | 0.0662s | 0.0610s | +0.0052s | worse |
| `lteNRRCC` | 0.1139s | 0.1156s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.43 MB | 26.0% | 108.0% |
| `f1ap_rel18.6_specs` | 34.80 MB | 164.67 MB | 111.5% | 103.5% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.06 MB | 114.3% | 107.1% |
| `lteNRRCC` | 74.19 MB | 102.94 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0277s | 0.0169s | +0.0108s | worse |
| `f1ap_rel18.6_specs` | 0.0845s | 0.0798s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0606s | 0.0508s | +0.0098s | worse |
| `lteNRRCC` | 0.0955s | 0.1204s | -0.0249s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.44 MB | 1.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.77 MB | 5.52 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.94 MB | 2.50 MB | 0.0% | 0.0% |
| `lteNRRCC` | 496 KB | 3.36 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0402s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1115s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0788s | -0.0029s | improved |
| `lteNRRCC` | 0.1309s | 0.1400s | -0.0091s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.04 MB | 7.81 MB | 116.8% | 81.8% |
| `f1ap_rel18.6_specs` | 8.54 MB | 8.73 MB | 116.2% | 116.6% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.30 MB | 233.9% | 235.0% |
| `lteNRRCC` | 7.27 MB | 70.55 MB | 235.2% | 173.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0342s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1102s | 0.1048s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0724s | +0.0049s | worse |
| `lteNRRCC` | 0.1302s | 0.1134s | +0.0168s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.44 MB | 8.45 MB | 163.4% | 92.6% |
| `f1ap_rel18.6_specs` | 11.20 MB | 147.29 MB | 93.4% | 108.5% |
| `ngap_rel18.6_specs` | 9.48 MB | 10.81 MB | 107.3% | 116.0% |
| `lteNRRCC` | 73.77 MB | 98.95 MB | 104.6% | 114.4% |
<!-- BENCH_RESULTS_END -->
