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
Generated: 2026-08-28T06:03:11.999966+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0364s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1131s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0772s | 0.0769s | +0.0003s | worse |
| `lteNRRCC` | 0.1212s | 0.1210s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.73 MB | 53.55 MB | 76.0% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0264s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.0940s | 0.0762s | +0.0178s | worse |
| `ngap_rel18.6_specs` | 0.0661s | 0.0498s | +0.0163s | worse |
| `lteNRRCC` | 0.1315s | 0.0964s | +0.0351s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.06 MB | 80.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.15 MB | 103.1% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.20 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.81 MB | 66.51 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0289s | +0.0051s | worse |
| `f1ap_rel18.6_specs` | 0.0889s | 0.0764s | +0.0125s | worse |
| `ngap_rel18.6_specs` | 0.0607s | 0.0536s | +0.0071s | worse |
| `lteNRRCC` | 0.1147s | 0.1021s | +0.0126s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 55.30 MB | 76.0% | 108.0% |
| `f1ap_rel18.6_specs` | 35.16 MB | 164.54 MB | 107.4% | 103.8% |
| `ngap_rel18.6_specs` | 24.12 MB | 117.68 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.62 MB | 102.93 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0238s | 0.0229s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0696s | 0.0690s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0494s | 0.0517s | -0.0023s | improved |
| `lteNRRCC` | 0.0788s | 0.0774s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.00 MB | 4.31 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.00 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 3.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.88 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0429s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.1050s | 0.1059s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0735s | 0.0747s | -0.0012s | improved |
| `lteNRRCC` | 0.1367s | 0.1554s | -0.0187s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.47 MB | 7.30 MB | 112.7% | 83.8% |
| `f1ap_rel18.6_specs` | 7.88 MB | 106.66 MB | 166.4% | 164.7% |
| `ngap_rel18.6_specs` | 7.39 MB | 7.48 MB | 165.8% | 165.3% |
| `lteNRRCC` | 46.89 MB | 68.98 MB | 106.9% | 106.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0400s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1210s | -0.0106s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0844s | -0.0075s | improved |
| `lteNRRCC` | 0.1262s | 0.1202s | +0.0060s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 9.01 MB | 0.0% | 171.4% |
| `f1ap_rel18.6_specs` | 11.03 MB | 9.75 MB | 228.8% | 80.2% |
| `ngap_rel18.6_specs` | 9.09 MB | 8.96 MB | 170.6% | 167.0% |
| `lteNRRCC` | 9.55 MB | 80.21 MB | 118.1% | 106.3% |
<!-- BENCH_RESULTS_END -->
