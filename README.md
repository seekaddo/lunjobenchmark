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
Generated: 2026-09-10T23:56:01.704430+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0379s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1163s | -0.0071s | improved |
| `ngap_rel18.6_specs` | 0.0744s | 0.0794s | -0.0050s | improved |
| `lteNRRCC` | 0.1178s | 0.1239s | -0.0061s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 19.4% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0283s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.0966s | 0.0755s | +0.0211s | worse |
| `ngap_rel18.6_specs` | 0.0679s | 0.0518s | +0.0161s | worse |
| `lteNRRCC` | 0.1298s | 0.0985s | +0.0313s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.55 MB | 76.9% | 103.6% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.38 MB | 106.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.36 MB | 103.8% | 104.7% |
| `lteNRRCC` | 48.74 MB | 66.51 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0345s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0927s | 0.0905s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0651s | 0.0641s | +0.0010s | worse |
| `lteNRRCC` | 0.1262s | 0.1174s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.51 MB | 88.0% | 103.6% |
| `f1ap_rel18.6_specs` | 35.16 MB | 164.71 MB | 106.2% | 101.8% |
| `ngap_rel18.6_specs` | 24.19 MB | 117.19 MB | 108.0% | 104.8% |
| `lteNRRCC` | 74.62 MB | 102.75 MB | 101.6% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0170s | 0.0329s | -0.0159s | improved |
| `f1ap_rel18.6_specs` | 0.0657s | 0.1025s | -0.0368s | improved |
| `ngap_rel18.6_specs` | 0.0485s | 0.0887s | -0.0402s | improved |
| `lteNRRCC` | 0.0798s | 0.1013s | -0.0215s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.38 MB | 7.02 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.81 MB | 4.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.14 MB | 7.42 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0386s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1062s | +0.0068s | worse |
| `ngap_rel18.6_specs` | 0.0762s | 0.0745s | +0.0017s | worse |
| `lteNRRCC` | 0.1377s | 0.1375s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.41 MB | 7.38 MB | 101.9% | 80.6% |
| `f1ap_rel18.6_specs` | 8.04 MB | 106.66 MB | 82.7% | 108.6% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.62 MB | 165.1% | 164.5% |
| `lteNRRCC` | 47.64 MB | 70.56 MB | 163.3% | 159.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0392s | -0.0046s | improved |
| `f1ap_rel18.6_specs` | 0.1025s | 0.1123s | -0.0098s | improved |
| `ngap_rel18.6_specs` | 0.0700s | 0.0818s | -0.0118s | improved |
| `lteNRRCC` | 0.1118s | 0.1398s | -0.0280s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.92 MB | 10.10 MB | 117.8% | 141.2% |
| `f1ap_rel18.6_specs` | 11.06 MB | 157.93 MB | 140.5% | 104.9% |
| `ngap_rel18.6_specs` | 9.16 MB | 10.13 MB | 140.0% | 114.3% |
| `lteNRRCC` | 73.79 MB | 92.82 MB | 103.3% | 115.1% |
<!-- BENCH_RESULTS_END -->
