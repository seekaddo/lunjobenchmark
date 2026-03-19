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
Generated: 2026-03-19T17:18:41.419164+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0361s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1140s | 0.1159s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0792s | 0.0794s | -0.0002s | improved |
| `lteNRRCC` | 0.1226s | 0.1175s | +0.0051s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 111.1% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0360s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0970s | 0.0976s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0678s | 0.0688s | -0.0010s | improved |
| `lteNRRCC` | 0.1312s | 0.1309s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 36.54 MB | 25.8% | 113.3% |
| `f1ap_rel18.6_specs` | 22.25 MB | 103.33 MB | 111.8% | 105.1% |
| `ngap_rel18.6_specs` | 16.57 MB | 73.89 MB | 110.7% | 108.9% |
| `lteNRRCC` | 47.72 MB | 66.54 MB | 106.1% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0353s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0896s | 0.1002s | -0.0106s | improved |
| `ngap_rel18.6_specs` | 0.0628s | 0.0697s | -0.0069s | improved |
| `lteNRRCC` | 0.1160s | 0.1134s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 55.48 MB | 88.9% | 110.3% |
| `f1ap_rel18.6_specs` | 34.29 MB | 163.74 MB | 113.3% | 105.4% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.56 MB | 111.5% | 107.0% |
| `lteNRRCC` | 75.01 MB | 102.94 MB | 105.0% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0236s | 0.0200s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.0670s | 0.0629s | +0.0041s | worse |
| `ngap_rel18.6_specs` | 0.0464s | 0.0423s | +0.0041s | worse |
| `lteNRRCC` | 0.0756s | 0.0729s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.77 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.92 MB | 9.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 688 KB | 0.0% | 0.0% |
| `lteNRRCC` | 3.94 MB | 3.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0400s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1099s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0774s | 0.0793s | -0.0019s | improved |
| `lteNRRCC` | 0.1394s | 0.1387s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.82 MB | 7.57 MB | 153.8% | 153.5% |
| `f1ap_rel18.6_specs` | 8.55 MB | 8.68 MB | 99.8% | 96.9% |
| `ngap_rel18.6_specs` | 8.06 MB | 7.99 MB | 83.9% | 87.6% |
| `lteNRRCC` | 8.17 MB | 51.03 MB | 152.8% | 106.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0382s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1236s | 0.1157s | +0.0079s | worse |
| `ngap_rel18.6_specs` | 0.0853s | 0.0790s | +0.0063s | worse |
| `lteNRRCC` | 0.1426s | 0.1278s | +0.0148s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.08 MB | 9.62 MB | 82.3% | 80.0% |
| `f1ap_rel18.6_specs` | 10.94 MB | 139.23 MB | 222.1% | 110.8% |
| `ngap_rel18.6_specs` | 9.42 MB | 9.56 MB | 103.6% | 103.1% |
| `lteNRRCC` | 9.37 MB | 99.65 MB | 0.0% | 162.4% |
<!-- BENCH_RESULTS_END -->
