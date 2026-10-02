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
Generated: 2026-10-02T01:30:07.957619+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0366s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1140s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0785s | -0.0017s | improved |
| `lteNRRCC` | 0.1190s | 0.1223s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 78.3% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0266s | 0.0319s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.0723s | 0.0950s | -0.0227s | improved |
| `ngap_rel18.6_specs` | 0.0505s | 0.0644s | -0.0139s | improved |
| `lteNRRCC` | 0.0969s | 0.1174s | -0.0205s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 36.00 MB | 13.7% | 110.0% |
| `f1ap_rel18.6_specs` | 21.85 MB | 103.47 MB | 108.7% | 102.3% |
| `ngap_rel18.6_specs` | 18.11 MB | 74.71 MB | 110.5% | 103.0% |
| `lteNRRCC` | 48.60 MB | 66.27 MB | 102.1% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0344s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0988s | 0.0899s | +0.0089s | worse |
| `ngap_rel18.6_specs` | 0.0702s | 0.0623s | +0.0079s | worse |
| `lteNRRCC` | 0.1147s | 0.1182s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 55.72 MB | 73.9% | 104.0% |
| `f1ap_rel18.6_specs` | 35.20 MB | 163.55 MB | 103.8% | 101.7% |
| `ngap_rel18.6_specs` | 24.33 MB | 117.42 MB | 104.8% | 104.8% |
| `lteNRRCC` | 74.80 MB | 102.74 MB | 101.9% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0377s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0796s | 0.1208s | -0.0412s | improved |
| `ngap_rel18.6_specs` | 0.0564s | 0.1079s | -0.0515s | improved |
| `lteNRRCC` | 0.0853s | 0.1114s | -0.0261s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.55 MB | 8.06 MB | 0.6% | 0.0% |
| `f1ap_rel18.6_specs` | 8.67 MB | 9.19 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 9.98 MB | 8.31 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.95 MB | 6.31 MB | 0.0% | 2.1% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0452s | 0.0334s | +0.0118s | worse |
| `f1ap_rel18.6_specs` | 0.1145s | 0.0942s | +0.0203s | worse |
| `ngap_rel18.6_specs` | 0.0810s | 0.0641s | +0.0169s | worse |
| `lteNRRCC` | 0.1347s | 0.1124s | +0.0223s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.30 MB | 7.85 MB | 0.0% | 164.5% |
| `f1ap_rel18.6_specs` | 8.57 MB | 8.81 MB | 161.5% | 230.5% |
| `ngap_rel18.6_specs` | 8.32 MB | 8.39 MB | 99.9% | 112.1% |
| `lteNRRCC` | 10.08 MB | 8.25 MB | 134.6% | 159.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0407s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1224s | 0.1181s | +0.0043s | worse |
| `ngap_rel18.6_specs` | 0.0860s | 0.0841s | +0.0019s | worse |
| `lteNRRCC` | 0.1196s | 0.1088s | +0.0108s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.22 MB | 0.0% | 131.1% |
| `f1ap_rel18.6_specs` | 10.55 MB | 122.93 MB | 132.5% | 265.5% |
| `ngap_rel18.6_specs` | 10.42 MB | 10.23 MB | 130.6% | 131.5% |
| `lteNRRCC` | 73.75 MB | 95.12 MB | 133.1% | 119.7% |
<!-- BENCH_RESULTS_END -->
