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
Generated: 2026-06-16T23:41:16.332587+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0362s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1146s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0780s | -0.0030s | improved |
| `lteNRRCC` | 0.1177s | 0.1224s | -0.0047s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 20.2% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 104.2% |
| `lteNRRCC` | 72.32 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0352s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.0929s | 0.0943s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0656s | -0.0007s | improved |
| `lteNRRCC` | 0.1236s | 0.1284s | -0.0048s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.69 MB | 21.4% | 110.7% |
| `f1ap_rel18.6_specs` | 22.33 MB | 103.15 MB | 106.1% | 105.3% |
| `ngap_rel18.6_specs` | 17.64 MB | 74.65 MB | 111.5% | 104.5% |
| `lteNRRCC` | 48.80 MB | 66.27 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0343s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0881s | 0.1003s | -0.0122s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0685s | -0.0067s | improved |
| `lteNRRCC` | 0.1148s | 0.1163s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.43 MB | 55.21 MB | 88.0% | 111.1% |
| `f1ap_rel18.6_specs` | 35.17 MB | 164.76 MB | 110.3% | 103.6% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.68 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.89 MB | 102.48 MB | 105.3% | 106.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0228s | 0.0498s | -0.0270s | improved |
| `f1ap_rel18.6_specs` | 0.0674s | 0.0696s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0473s | 0.0602s | -0.0129s | improved |
| `lteNRRCC` | 0.0768s | 0.0782s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.44 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.03 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.58 MB | 4.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.59 MB | 3.75 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0395s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1192s | 0.1072s | +0.0120s | worse |
| `ngap_rel18.6_specs` | 0.0824s | 0.0745s | +0.0079s | worse |
| `lteNRRCC` | 0.1437s | 0.1397s | +0.0040s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.69 MB | 7.81 MB | 92.4% | 102.3% |
| `f1ap_rel18.6_specs` | 8.23 MB | 106.63 MB | 83.5% | 166.5% |
| `ngap_rel18.6_specs` | 8.29 MB | 7.98 MB | 224.7% | 83.3% |
| `lteNRRCC` | 8.54 MB | 69.30 MB | 149.0% | 164.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0298s | 0.0447s | -0.0149s | improved |
| `f1ap_rel18.6_specs` | 0.0841s | 0.1239s | -0.0398s | improved |
| `ngap_rel18.6_specs` | 0.0595s | 0.0838s | -0.0243s | improved |
| `lteNRRCC` | 0.0894s | 0.1417s | -0.0523s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 52.03 MB | 107.8% | 111.6% |
| `f1ap_rel18.6_specs` | 23.69 MB | 164.14 MB | 147.4% | 111.1% |
| `ngap_rel18.6_specs` | 21.77 MB | 117.74 MB | 83.8% | 84.0% |
| `lteNRRCC` | 18.68 MB | 18.75 MB | 92.2% | 93.0% |
<!-- BENCH_RESULTS_END -->
