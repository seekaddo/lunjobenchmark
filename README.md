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
Generated: 2026-04-03T22:41:49.362926+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0359s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1158s | 0.1150s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0801s | 0.0803s | -0.0002s | improved |
| `lteNRRCC` | 0.1240s | 0.1213s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.46 MB | 53.55 MB | 5.1% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0341s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0928s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0664s | 0.0657s | +0.0007s | worse |
| `lteNRRCC` | 0.1276s | 0.1286s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.48 MB | 26.6% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.04 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 16.76 MB | 74.66 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.34 MB | 65.95 MB | 103.1% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0325s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0990s | 0.0878s | +0.0112s | worse |
| `ngap_rel18.6_specs` | 0.0687s | 0.0615s | +0.0072s | worse |
| `lteNRRCC` | 0.1153s | 0.1148s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.36 MB | 55.59 MB | 19.4% | 107.7% |
| `f1ap_rel18.6_specs` | 35.10 MB | 163.81 MB | 107.4% | 105.3% |
| `ngap_rel18.6_specs` | 24.09 MB | 117.63 MB | 109.1% | 102.3% |
| `lteNRRCC` | 74.59 MB | 102.45 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0297s | 0.0319s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0696s | 0.0640s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0580s | 0.0438s | +0.0142s | worse |
| `lteNRRCC` | 0.0768s | 0.0779s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.25 MB | 4.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.59 MB | 5.48 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 960 KB | 1.55 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.55 MB | 3.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0331s | +0.0060s | worse |
| `f1ap_rel18.6_specs` | 0.1046s | 0.0942s | +0.0104s | worse |
| `ngap_rel18.6_specs` | 0.0734s | 0.0648s | +0.0086s | worse |
| `lteNRRCC` | 0.1354s | 0.1121s | +0.0233s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.36 MB | 164.9% | 171.6% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.17 MB | 95.3% | 101.0% |
| `ngap_rel18.6_specs` | 7.39 MB | 7.54 MB | 166.4% | 166.7% |
| `lteNRRCC` | 48.24 MB | 49.12 MB | 163.0% | 103.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0449s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1237s | -0.0131s | improved |
| `ngap_rel18.6_specs` | 0.0761s | 0.0859s | -0.0098s | improved |
| `lteNRRCC` | 0.1251s | 0.1321s | -0.0070s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.33 MB | 8.94 MB | 81.6% | 150.6% |
| `f1ap_rel18.6_specs` | 10.57 MB | 11.14 MB | 99.5% | 231.6% |
| `ngap_rel18.6_specs` | 8.96 MB | 9.21 MB | 79.8% | 180.9% |
| `lteNRRCC` | 8.56 MB | 99.56 MB | 79.2% | 157.3% |
<!-- BENCH_RESULTS_END -->
