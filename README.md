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
Generated: 2026-03-13T16:51:26.360099+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0394s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.1209s | 0.1226s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0821s | 0.0849s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.26 MB | 55.64 MB | 105.6% | 103.4% |
| `f1ap_rel18.6_specs` | 32.14 MB | 176.76 MB | 106.9% | 102.9% |
| `ngap_rel18.6_specs` | 22.14 MB | 125.64 MB | 108.7% | 103.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0387s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1020s | 0.1037s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0726s | 0.0740s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.79 MB | 37.75 MB | 92.9% | 109.7% |
| `f1ap_rel18.6_specs` | 22.31 MB | 111.82 MB | 105.6% | 104.8% |
| `ngap_rel18.6_specs` | 16.71 MB | 79.93 MB | 110.0% | 108.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0355s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0948s | 0.0929s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0680s | 0.0659s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.45 MB | 57.87 MB | 69.4% | 110.0% |
| `f1ap_rel18.6_specs` | 34.41 MB | 179.08 MB | 112.9% | 106.8% |
| `ngap_rel18.6_specs` | 24.13 MB | 127.55 MB | 111.1% | 106.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0201s | 0.0250s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.0616s | 0.0715s | -0.0099s | improved |
| `ngap_rel18.6_specs` | 0.0418s | 0.0464s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.52 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.09 MB | 4.70 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.33 MB | 4.72 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0406s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1131s | 0.1130s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0803s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.30 MB | 7.24 MB | 160.0% | 81.6% |
| `f1ap_rel18.6_specs` | 8.18 MB | 115.07 MB | 92.9% | 104.1% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.42 MB | 104.0% | 163.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0442s | 0.0387s | +0.0055s | worse |
| `f1ap_rel18.6_specs` | 0.1267s | 0.1158s | +0.0109s | worse |
| `ngap_rel18.6_specs` | 0.0889s | 0.0802s | +0.0087s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.00 MB | 9.69 MB | 97.3% | 159.3% |
| `f1ap_rel18.6_specs` | 9.96 MB | 179.13 MB | 158.9% | 107.3% |
| `ngap_rel18.6_specs` | 9.28 MB | 10.26 MB | 159.0% | 98.8% |
<!-- BENCH_RESULTS_END -->
