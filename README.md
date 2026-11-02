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
Generated: 2026-11-02T01:25:09.916623+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0408s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1211s | 0.1275s | -0.0064s | improved |
| `ngap_rel18.6_specs` | 0.0853s | 0.0871s | -0.0018s | improved |
| `lteNRRCC` | 0.1274s | 0.1306s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 16.9% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.2% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 103.8% |
| `lteNRRCC` | 72.40 MB | 100.18 MB | 101.6% | 101.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0297s | +0.0076s | worse |
| `f1ap_rel18.6_specs` | 0.1151s | 0.0953s | +0.0198s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0659s | +0.0127s | worse |
| `lteNRRCC` | 0.1285s | 0.0957s | +0.0328s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.79 MB | 34.65 MB | 75.0% | 107.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 107.1% | 101.5% |
| `ngap_rel18.6_specs` | 18.03 MB | 72.65 MB | 104.5% | 102.1% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 101.7% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0555s | 0.0476s | +0.0079s | worse |
| `f1ap_rel18.6_specs` | 0.1687s | 0.1465s | +0.0222s | worse |
| `ngap_rel18.6_specs` | 0.1171s | 0.1023s | +0.0148s | worse |
| `lteNRRCC` | 0.1630s | 0.1470s | +0.0160s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 53.73 MB | 72.7% | 105.1% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.6% | 102.1% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 110.7% | 102.9% |
| `lteNRRCC` | 72.62 MB | 100.36 MB | 101.4% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0304s | 0.0280s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1174s | 0.1104s | +0.0070s | worse |
| `ngap_rel18.6_specs` | 0.0797s | 0.0774s | +0.0023s | worse |
| `lteNRRCC` | 0.1012s | 0.1146s | -0.0134s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.95 MB | 3.64 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.67 MB | 2.88 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.69 MB | 7.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.28 MB | 4.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0400s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1226s | -0.0148s | improved |
| `ngap_rel18.6_specs` | 0.0760s | 0.0825s | -0.0065s | improved |
| `lteNRRCC` | 0.1391s | 0.1444s | -0.0053s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.47 MB | 7.82 MB | 0.0% | 111.4% |
| `f1ap_rel18.6_specs` | 8.18 MB | 8.12 MB | 162.3% | 80.5% |
| `ngap_rel18.6_specs` | 7.67 MB | 7.75 MB | 158.2% | 162.3% |
| `lteNRRCC` | 8.36 MB | 70.55 MB | 103.6% | 156.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0429s | 0.0450s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.1215s | 0.1257s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0855s | 0.0869s | -0.0014s | improved |
| `lteNRRCC` | 0.1319s | 0.1362s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 10.06 MB | 0.0% | 100.5% |
| `f1ap_rel18.6_specs` | 10.25 MB | 10.44 MB | 159.2% | 117.8% |
| `ngap_rel18.6_specs` | 10.45 MB | 10.20 MB | 100.2% | 98.8% |
| `lteNRRCC` | 8.89 MB | 98.90 MB | 181.2% | 162.4% |
<!-- BENCH_RESULTS_END -->
