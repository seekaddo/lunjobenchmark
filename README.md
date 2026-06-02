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
Generated: 2026-06-02T23:53:15.083080+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0343s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1113s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0764s | 0.0760s | +0.0004s | worse |
| `lteNRRCC` | 0.1199s | 0.1194s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 21.6% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.2% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0350s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0934s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0673s | 0.0653s | +0.0020s | worse |
| `lteNRRCC` | 0.1293s | 0.1284s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.45 MB | 77.4% | 106.9% |
| `f1ap_rel18.6_specs` | 21.89 MB | 103.16 MB | 109.1% | 103.4% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.69 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.67 MB | 65.73 MB | 103.0% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0395s | -0.0061s | improved |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0961s | -0.0059s | improved |
| `ngap_rel18.6_specs` | 0.0632s | 0.0658s | -0.0026s | improved |
| `lteNRRCC` | 0.1179s | 0.1279s | -0.0100s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.35 MB | 55.86 MB | 16.1% | 110.7% |
| `f1ap_rel18.6_specs` | 35.22 MB | 164.70 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.36 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.69 MB | 102.18 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0273s | 0.0154s | +0.0119s | worse |
| `f1ap_rel18.6_specs` | 0.1034s | 0.0693s | +0.0341s | worse |
| `ngap_rel18.6_specs` | 0.0687s | 0.0471s | +0.0216s | worse |
| `lteNRRCC` | 0.1019s | 0.0782s | +0.0237s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.44 MB | 5.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 10.05 MB | 7.81 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.72 MB | 7.34 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.55 MB | 6.44 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0321s | 0.0399s | -0.0078s | improved |
| `f1ap_rel18.6_specs` | 0.0934s | 0.1110s | -0.0176s | improved |
| `ngap_rel18.6_specs` | 0.0664s | 0.0783s | -0.0119s | improved |
| `lteNRRCC` | 0.1149s | 0.1399s | -0.0250s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.11 MB | 7.80 MB | 140.3% | 208.1% |
| `f1ap_rel18.6_specs` | 8.61 MB | 8.73 MB | 140.6% | 134.8% |
| `ngap_rel18.6_specs` | 8.20 MB | 8.12 MB | 139.8% | 142.1% |
| `lteNRRCC` | 8.54 MB | 68.79 MB | 100.5% | 139.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0438s | 0.0463s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.1241s | 0.1288s | -0.0047s | improved |
| `ngap_rel18.6_specs` | 0.0929s | 0.0909s | +0.0020s | worse |
| `lteNRRCC` | 0.1371s | 0.1485s | -0.0114s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.03 MB | 8.20 MB | 0.0% | 210.3% |
| `f1ap_rel18.6_specs` | 13.67 MB | 155.75 MB | 174.9% | 152.2% |
| `ngap_rel18.6_specs` | 9.34 MB | 10.54 MB | 153.3% | 104.7% |
| `lteNRRCC` | 8.90 MB | 81.58 MB | 143.6% | 111.5% |
<!-- BENCH_RESULTS_END -->
