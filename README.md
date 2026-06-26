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
Generated: 2026-06-26T12:17:45.327906+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0356s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1110s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0766s | +0.0003s | worse |
| `lteNRRCC` | 0.1230s | 0.1201s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 20.8% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.1% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0366s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0985s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0667s | 0.0690s | -0.0023s | improved |
| `lteNRRCC` | 0.1324s | 0.1310s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 36.39 MB | 88.5% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.46 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 17.73 MB | 74.64 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.63 MB | 65.80 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0350s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0942s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0631s | 0.0662s | -0.0031s | improved |
| `lteNRRCC` | 0.1183s | 0.1281s | -0.0098s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 55.52 MB | 73.3% | 111.1% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.62 MB | 110.3% | 103.6% |
| `ngap_rel18.6_specs` | 24.41 MB | 116.88 MB | 116.7% | 107.0% |
| `lteNRRCC` | 74.83 MB | 102.85 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0245s | 0.0275s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.0683s | 0.1001s | -0.0318s | improved |
| `ngap_rel18.6_specs` | 0.0519s | 0.0578s | -0.0059s | improved |
| `lteNRRCC` | 0.0772s | 0.0933s | -0.0161s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.05 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.56 MB | 4.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.14 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.17 MB | 5.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0397s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1089s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0773s | -0.0007s | improved |
| `lteNRRCC` | 0.1385s | 0.1393s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.50 MB | 228.8% | 95.8% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.03 MB | 80.1% | 160.6% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.47 MB | 81.6% | 82.9% |
| `lteNRRCC` | 49.64 MB | 50.74 MB | 155.7% | 159.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0390s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1132s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0795s | 0.0775s | +0.0020s | worse |
| `lteNRRCC` | 0.1310s | 0.1275s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.79 MB | 9.71 MB | 77.5% | 177.3% |
| `f1ap_rel18.6_specs` | 10.10 MB | 164.20 MB | 88.4% | 172.2% |
| `ngap_rel18.6_specs` | 9.08 MB | 9.14 MB | 155.6% | 154.1% |
| `lteNRRCC` | 8.68 MB | 73.52 MB | 151.8% | 151.9% |
<!-- BENCH_RESULTS_END -->
