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
Generated: 2026-07-20T23:05:30.922514+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0376s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1161s | 0.1167s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0802s | 0.0816s | -0.0014s | improved |
| `lteNRRCC` | 0.1249s | 0.1251s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 22.9% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.9% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 106.7% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0350s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0992s | 0.0990s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0694s | 0.0734s | -0.0040s | improved |
| `lteNRRCC` | 0.1312s | 0.1291s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 35.95 MB | 17.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.14 MB | 102.55 MB | 106.1% | 105.1% |
| `ngap_rel18.6_specs` | 17.58 MB | 74.64 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.29 MB | 65.93 MB | 103.1% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0272s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.0941s | 0.0867s | +0.0074s | worse |
| `ngap_rel18.6_specs` | 0.0669s | 0.0514s | +0.0155s | worse |
| `lteNRRCC` | 0.1203s | 0.0970s | +0.0233s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.65 MB | 15.2% | 110.0% |
| `f1ap_rel18.6_specs` | 35.17 MB | 164.34 MB | 110.0% | 105.2% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.43 MB | 107.7% | 106.5% |
| `lteNRRCC` | 74.69 MB | 102.86 MB | 103.2% | 103.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0207s | 0.0227s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0758s | 0.0733s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0504s | 0.0484s | +0.0020s | worse |
| `lteNRRCC` | 0.0786s | 0.0855s | -0.0069s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.72 MB | 4.12 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.23 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.08 MB | 4.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.16 MB | 3.61 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0330s | +0.0086s | worse |
| `f1ap_rel18.6_specs` | 0.1133s | 0.0907s | +0.0226s | worse |
| `ngap_rel18.6_specs` | 0.0774s | 0.0628s | +0.0146s | worse |
| `lteNRRCC` | 0.1437s | 0.1106s | +0.0331s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.56 MB | 7.02 MB | 154.0% | 161.2% |
| `f1ap_rel18.6_specs` | 8.46 MB | 8.40 MB | 152.0% | 96.0% |
| `ngap_rel18.6_specs` | 7.99 MB | 7.18 MB | 155.7% | 103.8% |
| `lteNRRCC` | 8.04 MB | 54.56 MB | 150.7% | 156.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0378s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1114s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0747s | +0.0019s | worse |
| `lteNRRCC` | 0.1310s | 0.1165s | +0.0145s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 8.66 MB | 155.5% | 94.2% |
| `f1ap_rel18.6_specs` | 9.75 MB | 164.19 MB | 169.7% | 110.0% |
| `ngap_rel18.6_specs` | 9.27 MB | 9.27 MB | 76.6% | 151.0% |
| `lteNRRCC` | 8.80 MB | 73.20 MB | 147.9% | 154.8% |
<!-- BENCH_RESULTS_END -->
