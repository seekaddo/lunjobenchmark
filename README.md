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
Generated: 2026-05-31T23:09:04.684497+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0366s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1151s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0788s | -0.0010s | improved |
| `lteNRRCC` | 0.1182s | 0.1211s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 18.8% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0328s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0952s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0660s | -0.0011s | improved |
| `lteNRRCC` | 0.1154s | 0.1176s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 36.73 MB | 85.7% | 112.5% |
| `f1ap_rel18.6_specs` | 22.35 MB | 103.33 MB | 107.4% | 103.6% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.38 MB | 109.1% | 104.9% |
| `lteNRRCC` | 48.70 MB | 66.30 MB | 103.6% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0383s | -0.0052s | improved |
| `f1ap_rel18.6_specs` | 0.0893s | 0.1015s | -0.0122s | improved |
| `ngap_rel18.6_specs` | 0.0624s | 0.0709s | -0.0085s | improved |
| `lteNRRCC` | 0.1149s | 0.1317s | -0.0168s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.49 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 34.62 MB | 164.48 MB | 110.0% | 105.5% |
| `ngap_rel18.6_specs` | 24.16 MB | 117.62 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.32 MB | 102.86 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0285s | 0.0338s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.0799s | 0.0987s | -0.0188s | improved |
| `ngap_rel18.6_specs` | 0.0488s | 0.0494s | -0.0006s | improved |
| `lteNRRCC` | 0.0796s | 0.0867s | -0.0071s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.91 MB | 7.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.86 MB | 9.22 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.42 MB | 4.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.23 MB | 4.03 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0387s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1044s | 0.1076s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0746s | -0.0008s | improved |
| `lteNRRCC` | 0.1370s | 0.1378s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.37 MB | 115.2% | 81.6% |
| `f1ap_rel18.6_specs` | 8.61 MB | 8.11 MB | 224.8% | 164.4% |
| `ngap_rel18.6_specs` | 8.18 MB | 7.99 MB | 116.1% | 79.1% |
| `lteNRRCC` | 51.83 MB | 49.52 MB | 162.8% | 159.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0396s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1192s | 0.1150s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0820s | 0.0786s | +0.0034s | worse |
| `lteNRRCC` | 0.1376s | 0.1293s | +0.0083s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.65 MB | 8.98 MB | 156.5% | 164.5% |
| `f1ap_rel18.6_specs` | 10.17 MB | 160.11 MB | 162.9% | 163.9% |
| `ngap_rel18.6_specs` | 10.06 MB | 9.33 MB | 95.0% | 163.0% |
| `lteNRRCC` | 70.44 MB | 99.58 MB | 107.1% | 156.5% |
<!-- BENCH_RESULTS_END -->
