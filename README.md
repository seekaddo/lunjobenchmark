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
Generated: 2026-07-24T11:47:22.150815+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0368s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1147s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0778s | -0.0016s | improved |
| `lteNRRCC` | 0.1199s | 0.1226s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.61 MB | 53.55 MB | 18.3% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0348s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0941s | 0.0949s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0663s | 0.0670s | -0.0007s | improved |
| `lteNRRCC` | 0.1271s | 0.1296s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.50 MB | 76.9% | 107.7% |
| `f1ap_rel18.6_specs` | 22.45 MB | 103.38 MB | 103.2% | 100.0% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.67 MB | 104.0% | 102.4% |
| `lteNRRCC` | 47.91 MB | 66.44 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0329s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.0966s | 0.0903s | +0.0063s | worse |
| `ngap_rel18.6_specs` | 0.0665s | 0.0626s | +0.0039s | worse |
| `lteNRRCC` | 0.1292s | 0.1158s | +0.0134s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 55.81 MB | 84.0% | 103.6% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.46 MB | 103.2% | 103.5% |
| `ngap_rel18.6_specs` | 23.91 MB | 117.74 MB | 103.8% | 102.3% |
| `lteNRRCC` | 75.01 MB | 102.93 MB | 101.6% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0227s | 0.0416s | -0.0189s | improved |
| `f1ap_rel18.6_specs` | 0.0724s | 0.1023s | -0.0299s | improved |
| `ngap_rel18.6_specs` | 0.0479s | 0.0812s | -0.0333s | improved |
| `lteNRRCC` | 0.0774s | 0.0926s | -0.0152s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.31 MB | 4.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.59 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.80 MB | 4.77 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.81 MB | 3.97 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0408s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1138s | 0.1130s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0779s | 0.0800s | -0.0021s | improved |
| `lteNRRCC` | 0.1416s | 0.1409s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.04 MB | 7.75 MB | 154.7% | 91.7% |
| `f1ap_rel18.6_specs` | 8.92 MB | 105.68 MB | 109.3% | 104.3% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.11 MB | 81.1% | 82.1% |
| `lteNRRCC` | 8.72 MB | 51.39 MB | 108.9% | 106.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0403s | -0.0064s | improved |
| `f1ap_rel18.6_specs` | 0.1018s | 0.1075s | -0.0057s | improved |
| `ngap_rel18.6_specs` | 0.0672s | 0.0727s | -0.0055s | improved |
| `lteNRRCC` | 0.1092s | 0.1139s | -0.0047s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.27 MB | 0.0% | 138.2% |
| `f1ap_rel18.6_specs` | 11.14 MB | 161.91 MB | 139.1% | 203.8% |
| `ngap_rel18.6_specs` | 9.55 MB | 9.27 MB | 99.5% | 105.3% |
| `lteNRRCC` | 8.68 MB | 93.20 MB | 203.3% | 143.7% |
<!-- BENCH_RESULTS_END -->
