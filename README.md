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
Generated: 2026-09-05T13:21:11.680135+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0353s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1070s | 0.1108s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0739s | 0.0758s | -0.0019s | improved |
| `lteNRRCC` | 0.1174s | 0.1197s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 15.0% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0352s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0966s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0662s | 0.0684s | -0.0022s | improved |
| `lteNRRCC` | 0.1294s | 0.1290s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 36.50 MB | 74.1% | 107.4% |
| `f1ap_rel18.6_specs` | 22.17 MB | 103.44 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.64 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.48 MB | 66.24 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0337s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1020s | 0.0906s | +0.0114s | worse |
| `ngap_rel18.6_specs` | 0.0710s | 0.0632s | +0.0078s | worse |
| `lteNRRCC` | 0.1184s | 0.1166s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.75 MB | 68.0% | 104.0% |
| `f1ap_rel18.6_specs` | 34.31 MB | 164.33 MB | 103.8% | 101.7% |
| `ngap_rel18.6_specs` | 23.91 MB | 117.56 MB | 104.5% | 104.7% |
| `lteNRRCC` | 75.02 MB | 102.92 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0280s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.1034s | 0.1102s | -0.0068s | improved |
| `ngap_rel18.6_specs` | 0.0476s | 0.0754s | -0.0278s | improved |
| `lteNRRCC` | 0.0901s | 0.1116s | -0.0215s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.56 MB | 5.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.09 MB | 3.14 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.88 MB | 5.33 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.17 MB | 10.36 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0458s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1268s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0792s | 0.0875s | -0.0083s | improved |
| `lteNRRCC` | 0.1452s | 0.1468s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.70 MB | 7.64 MB | 89.0% | 102.3% |
| `f1ap_rel18.6_specs` | 8.93 MB | 8.56 MB | 108.1% | 152.2% |
| `ngap_rel18.6_specs` | 8.19 MB | 7.91 MB | 199.6% | 77.7% |
| `lteNRRCC` | 8.37 MB | 57.44 MB | 77.6% | 151.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0383s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.1199s | 0.1116s | +0.0083s | worse |
| `ngap_rel18.6_specs` | 0.0812s | 0.0774s | +0.0038s | worse |
| `lteNRRCC` | 0.1330s | 0.1275s | +0.0055s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 8.94 MB | 0.0% | 150.6% |
| `f1ap_rel18.6_specs` | 11.71 MB | 164.20 MB | 107.4% | 151.7% |
| `ngap_rel18.6_specs` | 10.26 MB | 9.35 MB | 100.8% | 151.3% |
| `lteNRRCC` | 8.69 MB | 78.55 MB | 152.4% | 108.4% |
<!-- BENCH_RESULTS_END -->
