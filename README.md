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
Generated: 2026-03-26T11:00:54.345667+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0378s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1139s | 0.1175s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0796s | -0.0006s | improved |
| `lteNRRCC` | 0.1219s | 0.1241s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.87 MB | 53.55 MB | 24.4% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0324s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0944s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0685s | 0.0646s | +0.0039s | worse |
| `lteNRRCC` | 0.1285s | 0.1162s | +0.0123s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.45 MB | 36.36 MB | 92.3% | 113.8% |
| `f1ap_rel18.6_specs` | 22.32 MB | 102.73 MB | 105.9% | 105.1% |
| `ngap_rel18.6_specs` | 16.27 MB | 74.65 MB | 107.1% | 106.7% |
| `lteNRRCC` | 48.10 MB | 66.30 MB | 104.5% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0330s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0890s | 0.0917s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0609s | 0.0630s | -0.0021s | improved |
| `lteNRRCC` | 0.1149s | 0.1156s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.75 MB | 88.5% | 111.1% |
| `f1ap_rel18.6_specs` | 35.15 MB | 164.65 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 23.86 MB | 117.82 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.09 MB | 102.16 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0192s | 0.0226s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.0592s | 0.0674s | -0.0082s | improved |
| `ngap_rel18.6_specs` | 0.0401s | 0.0734s | -0.0333s | improved |
| `lteNRRCC` | 0.0677s | 0.0952s | -0.0275s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.03 MB | 4.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.67 MB | 5.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.45 MB | 4.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.36 MB | 4.12 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0404s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1064s | 0.1063s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0761s | 0.0749s | +0.0012s | worse |
| `lteNRRCC` | 0.1380s | 0.1371s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.02 MB | 7.56 MB | 165.7% | 108.8% |
| `f1ap_rel18.6_specs` | 7.97 MB | 7.97 MB | 163.6% | 170.6% |
| `ngap_rel18.6_specs` | 8.18 MB | 7.88 MB | 116.3% | 159.6% |
| `lteNRRCC` | 51.64 MB | 51.52 MB | 163.5% | 229.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0440s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.1095s | 0.1176s | -0.0081s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0826s | -0.0048s | improved |
| `lteNRRCC` | 0.1276s | 0.1295s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.78 MB | 10.39 MB | 81.4% | 106.4% |
| `f1ap_rel18.6_specs` | 9.86 MB | 164.18 MB | 81.0% | 108.0% |
| `ngap_rel18.6_specs` | 9.48 MB | 8.95 MB | 151.8% | 161.4% |
| `lteNRRCC` | 73.58 MB | 88.50 MB | 156.4% | 106.6% |
<!-- BENCH_RESULTS_END -->
