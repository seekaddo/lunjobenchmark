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
Generated: 2026-08-13T11:06:17.816535+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0355s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1100s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0759s | 0.0760s | -0.0001s | improved |
| `lteNRRCC` | 0.1195s | 0.1191s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 90.5% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.3% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0284s | +0.0063s | worse |
| `f1ap_rel18.6_specs` | 0.0949s | 0.0762s | +0.0187s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0550s | +0.0113s | worse |
| `lteNRRCC` | 0.1259s | 0.1019s | +0.0240s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.55 MB | 36.62 MB | 84.0% | 103.7% |
| `f1ap_rel18.6_specs` | 22.25 MB | 103.31 MB | 106.5% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.63 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.50 MB | 66.42 MB | 103.3% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0283s | +0.0060s | worse |
| `f1ap_rel18.6_specs` | 0.0904s | 0.0760s | +0.0144s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0529s | +0.0100s | worse |
| `lteNRRCC` | 0.1166s | 0.1010s | +0.0156s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 55.69 MB | 80.8% | 107.7% |
| `f1ap_rel18.6_specs` | 34.26 MB | 164.60 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 23.94 MB | 117.33 MB | 104.2% | 102.4% |
| `lteNRRCC` | 74.85 MB | 102.95 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0251s | 0.0212s | +0.0039s | worse |
| `f1ap_rel18.6_specs` | 0.0865s | 0.0662s | +0.0203s | worse |
| `ngap_rel18.6_specs` | 0.0592s | 0.0473s | +0.0119s | worse |
| `lteNRRCC` | 0.0970s | 0.0765s | +0.0205s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.41 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.70 MB | 8.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.41 MB | 7.16 MB | 0.6% | 1.6% |
| `lteNRRCC` | 7.50 MB | 7.72 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0351s | +0.0044s | worse |
| `f1ap_rel18.6_specs` | 0.1097s | 0.0951s | +0.0146s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0660s | +0.0111s | worse |
| `lteNRRCC` | 0.1401s | 0.1160s | +0.0241s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.50 MB | 0.0% | 103.9% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.61 MB | 179.8% | 109.4% |
| `ngap_rel18.6_specs` | 7.54 MB | 8.21 MB | 179.2% | 230.7% |
| `lteNRRCC` | 47.50 MB | 69.22 MB | 108.0% | 109.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0482s | 0.0424s | +0.0058s | worse |
| `f1ap_rel18.6_specs` | 0.1353s | 0.1242s | +0.0111s | worse |
| `ngap_rel18.6_specs` | 0.0921s | 0.0854s | +0.0067s | worse |
| `lteNRRCC` | 0.1388s | 0.1378s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 10.15 MB | 0.0% | 174.6% |
| `f1ap_rel18.6_specs` | 11.18 MB | 143.92 MB | 217.5% | 156.2% |
| `ngap_rel18.6_specs` | 10.75 MB | 10.82 MB | 107.4% | 75.9% |
| `lteNRRCC` | 73.78 MB | 89.70 MB | 109.4% | 152.4% |
<!-- BENCH_RESULTS_END -->
