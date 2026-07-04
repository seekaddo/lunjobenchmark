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
Generated: 2026-07-04T11:39:10.079950+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0350s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1094s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0758s | 0.0755s | +0.0003s | worse |
| `lteNRRCC` | 0.1196s | 0.1188s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.79 MB | 53.55 MB | 21.9% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 106.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0341s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0970s | 0.0927s | +0.0043s | worse |
| `ngap_rel18.6_specs` | 0.0661s | 0.0648s | +0.0013s | worse |
| `lteNRRCC` | 0.1305s | 0.1314s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 36.28 MB | 85.2% | 106.9% |
| `f1ap_rel18.6_specs` | 22.41 MB | 102.74 MB | 109.4% | 103.4% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.52 MB | 111.5% | 106.8% |
| `lteNRRCC` | 47.79 MB | 66.46 MB | 103.1% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0330s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0901s | 0.0888s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0620s | +0.0009s | worse |
| `lteNRRCC` | 0.1216s | 0.1157s | +0.0059s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 55.78 MB | 91.7% | 111.1% |
| `f1ap_rel18.6_specs` | 35.10 MB | 164.19 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.45 MB | 117.70 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.90 MB | 102.92 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0228s | 0.0226s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0705s | 0.0674s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0603s | 0.0466s | +0.0137s | worse |
| `lteNRRCC` | 0.1022s | 0.0764s | +0.0258s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.95 MB | 5.39 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.52 MB | 2.88 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.09 MB | 4.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.05 MB | 3.75 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0396s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1084s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0794s | 0.0748s | +0.0046s | worse |
| `lteNRRCC` | 0.1301s | 0.1396s | -0.0095s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.11 MB | 7.85 MB | 116.7% | 83.1% |
| `f1ap_rel18.6_specs` | 8.55 MB | 8.67 MB | 117.2% | 80.9% |
| `ngap_rel18.6_specs` | 7.92 MB | 8.36 MB | 163.6% | 120.7% |
| `lteNRRCC` | 8.22 MB | 8.60 MB | 163.5% | 0.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0484s | 0.0403s | +0.0081s | worse |
| `f1ap_rel18.6_specs` | 0.1303s | 0.1293s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0924s | 0.0876s | +0.0048s | worse |
| `lteNRRCC` | 0.1348s | 0.1328s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.57 MB | 8.97 MB | 81.1% | 176.5% |
| `f1ap_rel18.6_specs` | 10.50 MB | 10.50 MB | 116.0% | 161.5% |
| `ngap_rel18.6_specs` | 9.14 MB | 10.07 MB | 95.4% | 159.2% |
| `lteNRRCC` | 8.74 MB | 9.14 MB | 157.0% | 165.2% |
<!-- BENCH_RESULTS_END -->
