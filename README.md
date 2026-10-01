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
Generated: 2026-10-01T16:58:21.568783+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0369s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1140s | 0.1137s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0785s | 0.0802s | -0.0017s | improved |
| `lteNRRCC` | 0.1223s | 0.1221s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 14.2% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0319s | 0.0357s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0931s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0644s | 0.0655s | -0.0011s | improved |
| `lteNRRCC` | 0.1174s | 0.1289s | -0.0115s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 36.73 MB | 72.7% | 104.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.49 MB | 103.8% | 101.9% |
| `ngap_rel18.6_specs` | 18.07 MB | 74.71 MB | 104.8% | 102.6% |
| `lteNRRCC` | 48.25 MB | 66.41 MB | 103.6% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0352s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0899s | 0.0942s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0623s | 0.0654s | -0.0031s | improved |
| `lteNRRCC` | 0.1182s | 0.1289s | -0.0107s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.84 MB | 79.2% | 103.8% |
| `f1ap_rel18.6_specs` | 34.80 MB | 163.65 MB | 103.6% | 101.8% |
| `ngap_rel18.6_specs` | 24.43 MB | 117.40 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.88 MB | 102.64 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0312s | +0.0065s | worse |
| `f1ap_rel18.6_specs` | 0.1208s | 0.1155s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.1079s | 0.0689s | +0.0390s | worse |
| `lteNRRCC` | 0.1114s | 0.1083s | +0.0031s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.53 MB | 5.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.83 MB | 9.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.88 MB | 5.62 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.06 MB | 6.58 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0374s | -0.0040s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0940s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0641s | 0.0646s | -0.0005s | improved |
| `lteNRRCC` | 0.1124s | 0.1005s | +0.0119s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.07 MB | 7.93 MB | 0.0% | 116.2% |
| `f1ap_rel18.6_specs` | 8.75 MB | 8.63 MB | 137.4% | 138.1% |
| `ngap_rel18.6_specs` | 8.25 MB | 8.32 MB | 137.3% | 137.7% |
| `lteNRRCC` | 51.79 MB | 59.94 MB | 208.5% | 201.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0310s | +0.0097s | worse |
| `f1ap_rel18.6_specs` | 0.1181s | 0.0920s | +0.0261s | worse |
| `ngap_rel18.6_specs` | 0.0841s | 0.0640s | +0.0201s | worse |
| `lteNRRCC` | 0.1088s | 0.0941s | +0.0147s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.91 MB | 11.09 MB | 0.0% | 209.3% |
| `f1ap_rel18.6_specs` | 11.12 MB | 123.93 MB | 196.2% | 109.5% |
| `ngap_rel18.6_specs` | 10.29 MB | 10.86 MB | 139.5% | 101.2% |
| `lteNRRCC` | 9.77 MB | 99.31 MB | 99.4% | 111.2% |
<!-- BENCH_RESULTS_END -->
