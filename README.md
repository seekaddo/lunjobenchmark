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
Generated: 2026-08-16T10:28:50.853031+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0342s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1068s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0738s | 0.0730s | +0.0008s | worse |
| `lteNRRCC` | 0.1170s | 0.1158s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 81.0% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0256s | +0.0102s | worse |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0776s | +0.0175s | worse |
| `ngap_rel18.6_specs` | 0.0679s | 0.0519s | +0.0160s | worse |
| `lteNRRCC` | 0.1308s | 0.0985s | +0.0323s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 36.02 MB | 80.0% | 103.7% |
| `f1ap_rel18.6_specs` | 22.14 MB | 103.48 MB | 103.1% | 101.8% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.65 MB | 104.0% | 102.3% |
| `lteNRRCC` | 48.48 MB | 66.24 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0283s | 0.0346s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0767s | 0.1062s | -0.0295s | improved |
| `ngap_rel18.6_specs` | 0.0525s | 0.0695s | -0.0170s | improved |
| `lteNRRCC` | 0.1023s | 0.1164s | -0.0141s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.42 MB | 55.84 MB | 79.2% | 104.5% |
| `f1ap_rel18.6_specs` | 35.12 MB | 164.21 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 24.45 MB | 117.26 MB | 105.0% | 105.3% |
| `lteNRRCC` | 74.88 MB | 102.78 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0238s | 0.0217s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0660s | 0.0697s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0455s | 0.0431s | +0.0024s | worse |
| `lteNRRCC` | 0.0753s | 0.0747s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.47 MB | 4.30 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.06 MB | 4.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.88 MB | 6.30 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.28 MB | 4.08 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0325s | +0.0060s | worse |
| `f1ap_rel18.6_specs` | 0.1071s | 0.0933s | +0.0138s | worse |
| `ngap_rel18.6_specs` | 0.0748s | 0.0676s | +0.0072s | worse |
| `lteNRRCC` | 0.1402s | 0.0996s | +0.0406s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.36 MB | 0.0% | 164.6% |
| `f1ap_rel18.6_specs` | 8.23 MB | 8.03 MB | 162.8% | 163.7% |
| `ngap_rel18.6_specs` | 7.61 MB | 8.17 MB | 163.1% | 223.1% |
| `lteNRRCC` | 48.69 MB | 51.33 MB | 110.9% | 108.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0416s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.1088s | 0.1128s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0744s | 0.0794s | -0.0050s | improved |
| `lteNRRCC` | 0.1475s | 0.1308s | +0.0167s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.57 MB | 0.0% | 103.8% |
| `f1ap_rel18.6_specs` | 11.70 MB | 10.93 MB | 204.5% | 116.3% |
| `ngap_rel18.6_specs` | 8.96 MB | 8.96 MB | 159.8% | 79.8% |
| `lteNRRCC` | 8.50 MB | 98.14 MB | 159.5% | 116.1% |
<!-- BENCH_RESULTS_END -->
