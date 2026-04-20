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
Generated: 2026-04-20T22:53:58.945720+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0371s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1130s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0790s | -0.0022s | improved |
| `lteNRRCC` | 0.1195s | 0.1281s | -0.0086s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.92 MB | 53.55 MB | 7.0% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0344s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0934s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0668s | 0.0658s | +0.0010s | worse |
| `lteNRRCC` | 0.1256s | 0.1299s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.26 MB | 25.0% | 110.0% |
| `f1ap_rel18.6_specs` | 22.36 MB | 103.02 MB | 112.1% | 103.3% |
| `ngap_rel18.6_specs` | 16.53 MB | 74.64 MB | 110.7% | 106.7% |
| `lteNRRCC` | 48.54 MB | 66.52 MB | 104.6% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0329s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0883s | 0.0882s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0610s | 0.0619s | -0.0009s | improved |
| `lteNRRCC` | 0.1156s | 0.1156s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.88 MB | 92.0% | 111.1% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.63 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.39 MB | 117.70 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.84 MB | 102.50 MB | 103.4% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0169s | 0.0260s | -0.0091s | improved |
| `f1ap_rel18.6_specs` | 0.0798s | 0.0810s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0508s | 0.0559s | -0.0051s | improved |
| `lteNRRCC` | 0.1204s | 0.1003s | +0.0201s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.44 MB | 7.12 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.83 MB | 9.42 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.23 MB | 10.53 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.56 MB | 7.05 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0455s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1160s | -0.0045s | improved |
| `ngap_rel18.6_specs` | 0.0788s | 0.0857s | -0.0069s | improved |
| `lteNRRCC` | 0.1400s | 0.1322s | +0.0078s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.96 MB | 7.97 MB | 96.0% | 80.5% |
| `f1ap_rel18.6_specs` | 8.66 MB | 8.73 MB | 157.7% | 80.5% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.17 MB | 163.1% | 82.2% |
| `lteNRRCC` | 49.70 MB | 51.71 MB | 161.9% | 111.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0395s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.1048s | 0.1152s | -0.0104s | improved |
| `ngap_rel18.6_specs` | 0.0724s | 0.0813s | -0.0089s | improved |
| `lteNRRCC` | 0.1134s | 0.1288s | -0.0154s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.02 MB | 9.84 MB | 196.8% | 98.4% |
| `f1ap_rel18.6_specs` | 10.30 MB | 156.35 MB | 99.8% | 128.8% |
| `ngap_rel18.6_specs` | 9.55 MB | 10.69 MB | 97.1% | 139.6% |
| `lteNRRCC` | 9.11 MB | 81.58 MB | 141.3% | 143.5% |
<!-- BENCH_RESULTS_END -->
