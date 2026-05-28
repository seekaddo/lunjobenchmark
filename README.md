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
Generated: 2026-05-28T13:57:59.985899+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0365s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1118s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0771s | -0.0012s | improved |
| `lteNRRCC` | 0.1196s | 0.1196s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.94 MB | 53.55 MB | 19.4% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0352s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0940s | 0.0906s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0632s | +0.0031s | worse |
| `lteNRRCC` | 0.1283s | 0.1289s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.36 MB | 36.54 MB | 77.4% | 110.7% |
| `f1ap_rel18.6_specs` | 21.74 MB | 102.89 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.05 MB | 107.4% | 107.0% |
| `lteNRRCC` | 48.68 MB | 66.35 MB | 104.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0334s | +0.0078s | worse |
| `f1ap_rel18.6_specs` | 0.1027s | 0.0903s | +0.0124s | worse |
| `ngap_rel18.6_specs` | 0.0723s | 0.0619s | +0.0104s | worse |
| `lteNRRCC` | 0.1371s | 0.1153s | +0.0218s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.40 MB | 55.45 MB | 23.5% | 109.1% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.77 MB | 108.6% | 106.1% |
| `ngap_rel18.6_specs` | 24.11 MB | 117.80 MB | 110.0% | 105.8% |
| `lteNRRCC` | 74.11 MB | 102.04 MB | 106.0% | 103.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0240s | +0.0177s | worse |
| `f1ap_rel18.6_specs` | 0.0670s | 0.0866s | -0.0196s | improved |
| `ngap_rel18.6_specs` | 0.0477s | 0.0676s | -0.0199s | improved |
| `lteNRRCC` | 0.0823s | 0.0731s | +0.0092s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 8.08 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.56 MB | 5.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.72 MB | 5.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.03 MB | 3.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0393s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1129s | 0.1065s | +0.0064s | worse |
| `ngap_rel18.6_specs` | 0.0837s | 0.0740s | +0.0097s | worse |
| `lteNRRCC` | 0.1486s | 0.1368s | +0.0118s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.75 MB | 8.05 MB | 113.5% | 179.5% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.12 MB | 149.6% | 92.1% |
| `ngap_rel18.6_specs` | 6.99 MB | 7.62 MB | 200.2% | 175.0% |
| `lteNRRCC` | 8.30 MB | 48.91 MB | 101.2% | 113.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0408s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1150s | 0.1168s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0788s | 0.0816s | -0.0028s | improved |
| `lteNRRCC` | 0.1297s | 0.1346s | -0.0049s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.79 MB | 8.93 MB | 155.4% | 147.3% |
| `f1ap_rel18.6_specs` | 9.94 MB | 10.57 MB | 158.2% | 101.0% |
| `ngap_rel18.6_specs` | 8.95 MB | 11.12 MB | 159.1% | 219.2% |
| `lteNRRCC` | 8.62 MB | 99.38 MB | 75.9% | 108.0% |
<!-- BENCH_RESULTS_END -->
