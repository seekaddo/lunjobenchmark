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
Generated: 2026-03-16T11:02:06.464236+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0379s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1202s | 0.1172s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0868s | 0.0819s | +0.0049s | worse |
| `lteNRRCC` | 0.1259s | 0.1230s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.42 MB | 55.80 MB | 76.0% | 106.9% |
| `f1ap_rel18.6_specs` | 32.30 MB | 176.92 MB | 110.3% | 102.9% |
| `ngap_rel18.6_specs` | 22.30 MB | 125.80 MB | 113.0% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.06 MB | 103.3% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0358s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1033s | 0.1107s | -0.0074s | improved |
| `ngap_rel18.6_specs` | 0.0703s | 0.0780s | -0.0077s | improved |
| `lteNRRCC` | 0.1213s | 0.1258s | -0.0045s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.52 MB | 38.02 MB | 26.2% | 111.5% |
| `f1ap_rel18.6_specs` | 22.43 MB | 111.89 MB | 103.3% | 103.3% |
| `ngap_rel18.6_specs` | 16.66 MB | 80.39 MB | 108.3% | 106.7% |
| `lteNRRCC` | 48.45 MB | 66.19 MB | 103.3% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0371s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0965s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0663s | 0.0709s | -0.0046s | improved |
| `lteNRRCC` | 0.1155s | 0.1220s | -0.0065s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.73 MB | 58.03 MB | 30.1% | 110.3% |
| `f1ap_rel18.6_specs` | 34.57 MB | 179.35 MB | 109.7% | 105.2% |
| `ngap_rel18.6_specs` | 24.19 MB | 127.95 MB | 111.5% | 106.7% |
| `lteNRRCC` | 74.44 MB | 102.85 MB | 104.9% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0206s | 0.0201s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0623s | 0.0626s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0425s | 0.0426s | -0.0001s | improved |
| `lteNRRCC` | 0.0705s | 0.0697s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.39 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.02 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.84 MB | 5.23 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.70 MB | 3.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0416s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1149s | -0.0041s | improved |
| `ngap_rel18.6_specs` | 0.0784s | 0.0806s | -0.0022s | improved |
| `lteNRRCC` | 0.1427s | 0.1450s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.30 MB | 7.02 MB | 161.1% | 81.1% |
| `f1ap_rel18.6_specs` | 7.92 MB | 105.08 MB | 158.6% | 107.0% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.38 MB | 163.8% | 160.7% |
| `lteNRRCC` | 45.25 MB | 68.69 MB | 161.9% | 159.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0396s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1186s | -0.0080s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0838s | -0.0075s | improved |
| `lteNRRCC` | 0.1258s | 0.1332s | -0.0074s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.55 MB | 10.18 MB | 163.8% | 115.3% |
| `f1ap_rel18.6_specs` | 9.95 MB | 179.22 MB | 101.3% | 115.9% |
| `ngap_rel18.6_specs` | 8.64 MB | 8.76 MB | 81.3% | 166.1% |
| `lteNRRCC` | 8.33 MB | 76.38 MB | 80.1% | 113.7% |
<!-- BENCH_RESULTS_END -->
