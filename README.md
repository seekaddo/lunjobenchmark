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
Generated: 2026-09-24T14:50:13.389600+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0358s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1117s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0771s | -0.0019s | improved |
| `lteNRRCC` | 0.1173s | 0.1206s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 78.3% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.6% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0325s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0921s | 0.0938s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0661s | -0.0007s | improved |
| `lteNRRCC` | 0.1274s | 0.1201s | +0.0073s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.37 MB | 80.0% | 103.8% |
| `f1ap_rel18.6_specs` | 21.82 MB | 103.04 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 73.49 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.01 MB | 66.33 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0295s | 0.0368s | -0.0073s | improved |
| `f1ap_rel18.6_specs` | 0.0795s | 0.0966s | -0.0171s | improved |
| `ngap_rel18.6_specs` | 0.0529s | 0.0674s | -0.0145s | improved |
| `lteNRRCC` | 0.1028s | 0.1290s | -0.0262s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 55.37 MB | 62.1% | 104.5% |
| `f1ap_rel18.6_specs` | 35.20 MB | 163.18 MB | 108.3% | 102.1% |
| `ngap_rel18.6_specs` | 24.36 MB | 117.67 MB | 105.0% | 105.7% |
| `lteNRRCC` | 74.90 MB | 101.91 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0429s | 0.0294s | +0.0135s | worse |
| `f1ap_rel18.6_specs` | 0.1167s | 0.1219s | -0.0052s | improved |
| `ngap_rel18.6_specs` | 0.0699s | 0.0801s | -0.0102s | improved |
| `lteNRRCC` | 0.1046s | 0.1176s | -0.0130s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.31 MB | 4.42 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.67 MB | 8.92 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.91 MB | 3.77 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.02 MB | 4.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0401s | -0.0060s | improved |
| `f1ap_rel18.6_specs` | 0.0916s | 0.1075s | -0.0159s | improved |
| `ngap_rel18.6_specs` | 0.0633s | 0.0752s | -0.0119s | improved |
| `lteNRRCC` | 0.1163s | 0.1383s | -0.0220s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.03 MB | 0.0% | 274.8% |
| `f1ap_rel18.6_specs` | 8.72 MB | 106.63 MB | 114.8% | 143.4% |
| `ngap_rel18.6_specs` | 8.16 MB | 8.35 MB | 124.3% | 141.2% |
| `lteNRRCC` | 50.78 MB | 68.46 MB | 180.0% | 108.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0448s | 0.0378s | +0.0070s | worse |
| `f1ap_rel18.6_specs` | 0.1222s | 0.1085s | +0.0137s | worse |
| `ngap_rel18.6_specs` | 0.0865s | 0.0741s | +0.0124s | worse |
| `lteNRRCC` | 0.1308s | 0.1271s | +0.0037s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.14 MB | 9.43 MB | 0.0% | 165.6% |
| `f1ap_rel18.6_specs` | 10.28 MB | 10.00 MB | 164.5% | 117.1% |
| `ngap_rel18.6_specs` | 9.32 MB | 10.03 MB | 164.7% | 136.1% |
| `lteNRRCC` | 8.85 MB | 101.68 MB | 162.6% | 110.0% |
<!-- BENCH_RESULTS_END -->
