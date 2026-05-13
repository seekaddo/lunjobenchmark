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
Generated: 2026-05-13T23:12:12.355704+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0382s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1124s | 0.1180s | -0.0056s | improved |
| `ngap_rel18.6_specs` | 0.0777s | 0.0800s | -0.0023s | improved |
| `lteNRRCC` | 0.1201s | 0.1287s | -0.0086s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.76 MB | 53.55 MB | 18.6% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0344s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0919s | 0.0936s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0651s | 0.0652s | -0.0001s | improved |
| `lteNRRCC` | 0.1250s | 0.1285s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.24 MB | 36.36 MB | 92.6% | 110.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.94 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.64 MB | 111.1% | 104.5% |
| `lteNRRCC` | 48.41 MB | 66.50 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0356s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0960s | 0.0937s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0651s | +0.0016s | worse |
| `lteNRRCC` | 0.1285s | 0.1285s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.75 MB | 89.3% | 110.0% |
| `f1ap_rel18.6_specs` | 35.18 MB | 164.69 MB | 109.1% | 105.0% |
| `ngap_rel18.6_specs` | 23.59 MB | 117.62 MB | 111.1% | 104.2% |
| `lteNRRCC` | 74.84 MB | 102.45 MB | 106.2% | 105.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0170s | 0.0213s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.0673s | 0.0711s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0448s | 0.0454s | -0.0006s | improved |
| `lteNRRCC` | 0.0730s | 0.0867s | -0.0137s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.61 MB | 4.02 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.95 MB | 4.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.44 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.84 MB | 3.53 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0430s | 0.0402s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1135s | 0.1084s | +0.0051s | worse |
| `ngap_rel18.6_specs` | 0.0829s | 0.0770s | +0.0059s | worse |
| `lteNRRCC` | 0.1339s | 0.1394s | -0.0055s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 8.37 MB | 78.0% | 152.9% |
| `f1ap_rel18.6_specs` | 8.67 MB | 8.45 MB | 156.7% | 157.0% |
| `ngap_rel18.6_specs` | 8.17 MB | 9.57 MB | 156.7% | 180.4% |
| `lteNRRCC` | 8.54 MB | 69.10 MB | 78.5% | 106.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0427s | 0.0414s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1223s | 0.1191s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0825s | 0.0831s | -0.0006s | improved |
| `lteNRRCC` | 0.1320s | 0.1317s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.35 MB | 9.07 MB | 81.7% | 83.4% |
| `f1ap_rel18.6_specs` | 10.36 MB | 9.99 MB | 83.0% | 165.6% |
| `ngap_rel18.6_specs` | 9.55 MB | 10.50 MB | 166.9% | 231.1% |
| `lteNRRCC` | 9.29 MB | 98.95 MB | 108.7% | 107.5% |
<!-- BENCH_RESULTS_END -->
