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
Generated: 2026-10-02T16:11:09.731720+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0352s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1106s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0768s | +0.0003s | worse |
| `lteNRRCC` | 0.1208s | 0.1190s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 82.6% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0266s | +0.0109s | worse |
| `f1ap_rel18.6_specs` | 0.0972s | 0.0723s | +0.0249s | worse |
| `ngap_rel18.6_specs` | 0.0701s | 0.0505s | +0.0196s | worse |
| `lteNRRCC` | 0.1328s | 0.0969s | +0.0359s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 36.54 MB | 70.0% | 107.1% |
| `f1ap_rel18.6_specs` | 21.90 MB | 103.38 MB | 103.1% | 101.6% |
| `ngap_rel18.6_specs` | 18.06 MB | 74.50 MB | 103.8% | 104.5% |
| `lteNRRCC` | 48.56 MB | 66.31 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0341s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0988s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0672s | 0.0702s | -0.0030s | improved |
| `lteNRRCC` | 0.1298s | 0.1147s | +0.0151s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.66 MB | 80.8% | 103.6% |
| `f1ap_rel18.6_specs` | 34.65 MB | 163.45 MB | 106.7% | 103.5% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.48 MB | 104.0% | 102.3% |
| `lteNRRCC` | 74.98 MB | 102.02 MB | 103.2% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0366s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0849s | 0.0796s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0699s | 0.0564s | +0.0135s | worse |
| `lteNRRCC` | 0.0938s | 0.0853s | +0.0085s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.72 MB | 7.12 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.41 MB | 7.22 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.00 MB | 5.94 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.73 MB | 6.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0452s | -0.0047s | improved |
| `f1ap_rel18.6_specs` | 0.1148s | 0.1145s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0810s | -0.0021s | improved |
| `lteNRRCC` | 0.1406s | 0.1347s | +0.0059s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.26 MB | 7.96 MB | 0.0% | 160.1% |
| `f1ap_rel18.6_specs` | 8.69 MB | 8.82 MB | 97.0% | 165.8% |
| `ngap_rel18.6_specs` | 8.45 MB | 8.38 MB | 104.7% | 220.8% |
| `lteNRRCC` | 49.58 MB | 70.51 MB | 160.1% | 105.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0408s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1163s | 0.1224s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0817s | 0.0860s | -0.0043s | improved |
| `lteNRRCC` | 0.1270s | 0.1196s | +0.0074s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 8.38 MB | 0.0% | 176.5% |
| `f1ap_rel18.6_specs` | 11.31 MB | 9.60 MB | 233.0% | 95.2% |
| `ngap_rel18.6_specs` | 8.75 MB | 8.93 MB | 92.8% | 178.0% |
| `lteNRRCC` | 8.73 MB | 75.62 MB | 98.3% | 152.7% |
<!-- BENCH_RESULTS_END -->
