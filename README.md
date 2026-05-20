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
Generated: 2026-05-20T23:19:20.632162+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0371s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1141s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0783s | -0.0017s | improved |
| `lteNRRCC` | 0.1198s | 0.1217s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 53.55 MB | 17.3% | 113.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0368s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.0906s | 0.1005s | -0.0099s | improved |
| `ngap_rel18.6_specs` | 0.0637s | 0.0664s | -0.0027s | improved |
| `lteNRRCC` | 0.1229s | 0.1303s | -0.0074s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.00 MB | 18.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.10 MB | 108.8% | 103.4% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.45 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.84 MB | 66.00 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0338s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0983s | 0.0897s | +0.0086s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0626s | +0.0037s | worse |
| `lteNRRCC` | 0.1294s | 0.1160s | +0.0134s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 55.57 MB | 86.2% | 110.0% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.74 MB | 112.5% | 103.3% |
| `ngap_rel18.6_specs` | 24.32 MB | 117.02 MB | 111.1% | 106.7% |
| `lteNRRCC` | 74.94 MB | 102.89 MB | 104.6% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0291s | 0.0205s | +0.0086s | worse |
| `f1ap_rel18.6_specs` | 0.0881s | 0.0722s | +0.0159s | worse |
| `ngap_rel18.6_specs` | 0.0738s | 0.0522s | +0.0216s | worse |
| `lteNRRCC` | 0.0810s | 0.0935s | -0.0125s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.61 MB | 192 KB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.64 MB | 5.55 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 3.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.58 MB | 3.08 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0318s | 0.0401s | -0.0083s | improved |
| `f1ap_rel18.6_specs` | 0.0886s | 0.1087s | -0.0201s | improved |
| `ngap_rel18.6_specs` | 0.0614s | 0.0759s | -0.0145s | improved |
| `lteNRRCC` | 0.1093s | 0.1371s | -0.0278s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.98 MB | 7.82 MB | 143.0% | 135.2% |
| `f1ap_rel18.6_specs` | 8.46 MB | 106.66 MB | 143.0% | 142.9% |
| `ngap_rel18.6_specs` | 8.21 MB | 8.18 MB | 144.0% | 144.7% |
| `lteNRRCC` | 48.64 MB | 50.88 MB | 286.6% | 142.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0400s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1217s | 0.1076s | +0.0141s | worse |
| `ngap_rel18.6_specs` | 0.0854s | 0.0770s | +0.0084s | worse |
| `lteNRRCC` | 0.1385s | 0.1283s | +0.0102s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.95 MB | 9.09 MB | 82.3% | 179.0% |
| `f1ap_rel18.6_specs` | 10.59 MB | 162.68 MB | 102.4% | 161.4% |
| `ngap_rel18.6_specs` | 10.77 MB | 9.35 MB | 222.5% | 163.0% |
| `lteNRRCC` | 72.32 MB | 101.72 MB | 162.5% | 161.1% |
<!-- BENCH_RESULTS_END -->
