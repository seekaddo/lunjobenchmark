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
Generated: 2026-05-14T11:57:30.960463+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0360s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1171s | 0.1124s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0796s | 0.0777s | +0.0019s | worse |
| `lteNRRCC` | 0.1245s | 0.1201s | +0.0044s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 27.4% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.5% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.1% | 105.6% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.9% | 105.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0343s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0991s | 0.0919s | +0.0072s | worse |
| `ngap_rel18.6_specs` | 0.0706s | 0.0651s | +0.0055s | worse |
| `lteNRRCC` | 0.1322s | 0.1250s | +0.0072s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 36.55 MB | 96.2% | 110.3% |
| `f1ap_rel18.6_specs` | 22.35 MB | 103.36 MB | 109.1% | 105.0% |
| `ngap_rel18.6_specs` | 16.23 MB | 74.07 MB | 111.1% | 104.3% |
| `lteNRRCC` | 47.92 MB | 66.38 MB | 104.5% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0376s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0960s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0667s | -0.0010s | improved |
| `lteNRRCC` | 0.1192s | 0.1285s | -0.0093s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.28 MB | 100.0% | 110.3% |
| `f1ap_rel18.6_specs` | 34.61 MB | 164.57 MB | 109.7% | 105.2% |
| `ngap_rel18.6_specs` | 24.41 MB | 117.41 MB | 111.5% | 109.1% |
| `lteNRRCC` | 74.96 MB | 102.91 MB | 104.8% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0258s | 0.0170s | +0.0088s | worse |
| `f1ap_rel18.6_specs` | 0.0801s | 0.0673s | +0.0128s | worse |
| `ngap_rel18.6_specs` | 0.0510s | 0.0448s | +0.0062s | worse |
| `lteNRRCC` | 0.0794s | 0.0730s | +0.0064s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.95 MB | 4.44 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.62 MB | 3.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.45 MB | 4.42 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.77 MB | 3.59 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0430s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1135s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0748s | 0.0829s | -0.0081s | improved |
| `lteNRRCC` | 0.1388s | 0.1339s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.35 MB | 7.96 MB | 181.4% | 110.3% |
| `f1ap_rel18.6_specs` | 7.97 MB | 8.44 MB | 98.7% | 111.6% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.58 MB | 82.1% | 161.5% |
| `lteNRRCC` | 47.25 MB | 57.20 MB | 109.4% | 110.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0427s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1240s | 0.1223s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0857s | 0.0825s | +0.0032s | worse |
| `lteNRRCC` | 0.1408s | 0.1320s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.94 MB | 9.55 MB | 163.1% | 161.9% |
| `f1ap_rel18.6_specs` | 10.24 MB | 161.10 MB | 164.5% | 163.8% |
| `ngap_rel18.6_specs` | 9.48 MB | 9.41 MB | 92.0% | 160.1% |
| `lteNRRCC` | 70.30 MB | 101.70 MB | 157.4% | 152.8% |
<!-- BENCH_RESULTS_END -->
