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
Generated: 2026-08-30T00:01:43.675922+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0359s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1118s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0778s | 0.0772s | +0.0006s | worse |
| `lteNRRCC` | 0.1222s | 0.1205s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 87.0% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 100.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0289s | 0.0238s | +0.0051s | worse |
| `f1ap_rel18.6_specs` | 0.0787s | 0.0709s | +0.0078s | worse |
| `ngap_rel18.6_specs` | 0.0534s | 0.0476s | +0.0058s | worse |
| `lteNRRCC` | 0.1016s | 0.0883s | +0.0133s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.05 MB | 71.4% | 105.0% |
| `f1ap_rel18.6_specs` | 22.37 MB | 103.26 MB | 104.2% | 102.3% |
| `ngap_rel18.6_specs` | 18.02 MB | 73.94 MB | 100.0% | 103.0% |
| `lteNRRCC` | 48.81 MB | 66.28 MB | 104.4% | 101.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0349s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0923s | 0.0929s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0651s | 0.0646s | +0.0005s | worse |
| `lteNRRCC` | 0.1224s | 0.1278s | -0.0054s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.72 MB | 83.3% | 107.4% |
| `f1ap_rel18.6_specs` | 34.64 MB | 163.70 MB | 103.4% | 103.6% |
| `ngap_rel18.6_specs` | 24.47 MB | 117.48 MB | 104.2% | 104.8% |
| `lteNRRCC` | 74.51 MB | 102.35 MB | 101.7% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0194s | 0.0256s | -0.0062s | improved |
| `f1ap_rel18.6_specs` | 0.0670s | 0.0671s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0458s | 0.0475s | -0.0017s | improved |
| `lteNRRCC` | 0.0751s | 0.0783s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.06 MB | 4.06 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.94 MB | 5.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.39 MB | 4.00 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.72 MB | 4.33 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0308s | 0.0397s | -0.0089s | improved |
| `f1ap_rel18.6_specs` | 0.0853s | 0.1073s | -0.0220s | improved |
| `ngap_rel18.6_specs` | 0.0588s | 0.0748s | -0.0160s | improved |
| `lteNRRCC` | 0.0947s | 0.1389s | -0.0442s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 38.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 24.53 MB | 67.62 MB | 84.8% | 94.5% |
| `ngap_rel18.6_specs` | 17.93 MB | 39.86 MB | 54.2% | 129.1% |
| `lteNRRCC` | 15.07 MB | 14.81 MB | 129.2% | 161.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0398s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1112s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0806s | -0.0030s | improved |
| `lteNRRCC` | 0.1276s | 0.1282s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.12 MB | 8.59 MB | 0.0% | 158.6% |
| `f1ap_rel18.6_specs` | 9.62 MB | 9.62 MB | 77.7% | 92.4% |
| `ngap_rel18.6_specs` | 9.05 MB | 8.96 MB | 158.4% | 157.3% |
| `lteNRRCC` | 9.99 MB | 87.02 MB | 110.6% | 111.9% |
<!-- BENCH_RESULTS_END -->
