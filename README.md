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
Generated: 2026-05-17T11:15:31.600645+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0367s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1141s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0765s | 0.0795s | -0.0030s | improved |
| `lteNRRCC` | 0.1203s | 0.1216s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.88 MB | 53.55 MB | 10.7% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 105.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0316s | 0.0322s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0919s | 0.0950s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0642s | 0.0646s | -0.0004s | improved |
| `lteNRRCC` | 0.1150s | 0.1158s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.67 MB | 36.41 MB | 19.0% | 108.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.12 MB | 107.1% | 105.5% |
| `ngap_rel18.6_specs` | 16.64 MB | 74.43 MB | 108.3% | 107.3% |
| `lteNRRCC` | 48.71 MB | 66.35 MB | 105.4% | 104.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0350s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1012s | 0.0926s | +0.0086s | worse |
| `ngap_rel18.6_specs` | 0.0700s | 0.0652s | +0.0048s | worse |
| `lteNRRCC` | 0.1179s | 0.1272s | -0.0093s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.73 MB | 55.85 MB | 86.4% | 107.7% |
| `f1ap_rel18.6_specs` | 34.63 MB | 164.73 MB | 107.4% | 103.4% |
| `ngap_rel18.6_specs` | 24.49 MB | 117.58 MB | 109.1% | 104.7% |
| `lteNRRCC` | 74.15 MB | 102.72 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0255s | 0.0330s | -0.0075s | improved |
| `f1ap_rel18.6_specs` | 0.0717s | 0.0690s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0483s | 0.0478s | +0.0005s | worse |
| `lteNRRCC` | 0.0764s | 0.0738s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.00 MB | 4.05 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.00 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.64 MB | 8.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.05 MB | 3.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0404s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1072s | 0.1111s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0767s | -0.0009s | improved |
| `lteNRRCC` | 0.1391s | 0.1394s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.35 MB | 7.38 MB | 81.9% | 162.6% |
| `f1ap_rel18.6_specs` | 8.55 MB | 8.04 MB | 218.6% | 166.8% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.55 MB | 81.6% | 163.3% |
| `lteNRRCC` | 44.41 MB | 51.99 MB | 108.7% | 104.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0423s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.1041s | 0.1245s | -0.0204s | improved |
| `ngap_rel18.6_specs` | 0.0737s | 0.0902s | -0.0165s | improved |
| `lteNRRCC` | 0.1134s | 0.1333s | -0.0199s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.91 MB | 10.16 MB | 97.3% | 106.5% |
| `f1ap_rel18.6_specs` | 10.95 MB | 146.36 MB | 113.5% | 107.3% |
| `ngap_rel18.6_specs` | 10.13 MB | 9.25 MB | 96.4% | 121.5% |
| `lteNRRCC` | 9.18 MB | 74.95 MB | 192.9% | 285.8% |
<!-- BENCH_RESULTS_END -->
