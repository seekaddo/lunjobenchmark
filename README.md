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
Generated: 2026-03-22T10:36:02.394572+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0361s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1142s | 0.1137s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0780s | 0.0776s | +0.0004s | worse |
| `lteNRRCC` | 0.1230s | 0.1220s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 105.6% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0352s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0942s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0646s | 0.0668s | -0.0022s | improved |
| `lteNRRCC` | 0.1237s | 0.1295s | -0.0058s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.32 MB | 36.23 MB | 23.2% | 110.0% |
| `f1ap_rel18.6_specs` | 22.34 MB | 103.00 MB | 108.8% | 105.1% |
| `ngap_rel18.6_specs` | 16.47 MB | 74.68 MB | 110.7% | 108.9% |
| `lteNRRCC` | 48.68 MB | 65.77 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0362s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0922s | 0.0917s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0643s | 0.0640s | +0.0003s | worse |
| `lteNRRCC` | 0.1177s | 0.1190s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.38 MB | 55.71 MB | 23.6% | 113.8% |
| `f1ap_rel18.6_specs` | 34.66 MB | 164.29 MB | 109.7% | 105.2% |
| `ngap_rel18.6_specs` | 24.58 MB | 117.35 MB | 111.5% | 106.8% |
| `lteNRRCC` | 74.81 MB | 102.59 MB | 105.0% | 105.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0211s | 0.0206s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0709s | 0.0658s | +0.0051s | worse |
| `ngap_rel18.6_specs` | 0.0459s | 0.0407s | +0.0052s | worse |
| `lteNRRCC` | 0.0730s | 0.0682s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.25 MB | 6.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.16 MB | 3.88 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.67 MB | 1.94 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.45 MB | 7.36 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0381s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1043s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0752s | 0.0725s | +0.0027s | worse |
| `lteNRRCC` | 0.1390s | 0.1389s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.77 MB | 7.44 MB | 81.7% | 79.3% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.37 MB | 79.1% | 80.3% |
| `ngap_rel18.6_specs` | 7.99 MB | 7.89 MB | 100.5% | 162.5% |
| `lteNRRCC` | 47.70 MB | 51.34 MB | 107.2% | 156.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0377s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1077s | 0.1062s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0742s | +0.0046s | worse |
| `lteNRRCC` | 0.1255s | 0.1243s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.86 MB | 10.71 MB | 94.7% | 112.9% |
| `f1ap_rel18.6_specs` | 9.65 MB | 164.19 MB | 159.7% | 219.3% |
| `ngap_rel18.6_specs` | 11.01 MB | 9.02 MB | 226.3% | 92.2% |
| `lteNRRCC` | 9.74 MB | 98.82 MB | 235.3% | 106.6% |
<!-- BENCH_RESULTS_END -->
