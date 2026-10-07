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
Generated: 2026-10-07T17:22:26.738152+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0392s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1152s | 0.1199s | -0.0047s | improved |
| `ngap_rel18.6_specs` | 0.0794s | 0.0807s | -0.0013s | improved |
| `lteNRRCC` | 0.1242s | 0.1235s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 76.9% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0246s | 0.0351s | -0.0105s | improved |
| `f1ap_rel18.6_specs` | 0.0593s | 0.1013s | -0.0420s | improved |
| `ngap_rel18.6_specs` | 0.0445s | 0.0703s | -0.0258s | improved |
| `lteNRRCC` | 0.0766s | 0.1229s | -0.0463s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 36.61 MB | 75.0% | 100.0% |
| `f1ap_rel18.6_specs` | 21.83 MB | 103.05 MB | 105.3% | 102.8% |
| `ngap_rel18.6_specs` | 18.03 MB | 74.62 MB | 106.7% | 107.7% |
| `lteNRRCC` | 48.74 MB | 65.96 MB | 102.8% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0346s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0940s | 0.1003s | -0.0063s | improved |
| `ngap_rel18.6_specs` | 0.0644s | 0.0667s | -0.0023s | improved |
| `lteNRRCC` | 0.1204s | 0.1184s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.57 MB | 16.4% | 107.4% |
| `f1ap_rel18.6_specs` | 34.75 MB | 163.37 MB | 107.1% | 103.0% |
| `ngap_rel18.6_specs` | 24.12 MB | 117.83 MB | 104.2% | 107.8% |
| `lteNRRCC` | 74.83 MB | 102.25 MB | 103.5% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0587s | 0.0188s | +0.0399s | worse |
| `f1ap_rel18.6_specs` | 0.0793s | 0.0900s | -0.0107s | improved |
| `ngap_rel18.6_specs` | 0.0497s | 0.0622s | -0.0125s | improved |
| `lteNRRCC` | 0.0931s | 0.1006s | -0.0075s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.78 MB | 6.34 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 10.97 MB | 4.20 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.02 MB | 6.67 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.33 MB | 3.97 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0387s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1107s | 0.1082s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0757s | +0.0000s | flat |
| `lteNRRCC` | 0.1298s | 0.1372s | -0.0074s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.29 MB | 7.64 MB | 0.0% | 115.3% |
| `f1ap_rel18.6_specs` | 8.63 MB | 8.34 MB | 113.7% | 160.4% |
| `ngap_rel18.6_specs` | 8.16 MB | 8.39 MB | 155.9% | 155.9% |
| `lteNRRCC` | 8.03 MB | 8.75 MB | 98.1% | 231.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0349s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0987s | 0.1031s | -0.0044s | improved |
| `ngap_rel18.6_specs` | 0.0676s | 0.0710s | -0.0034s | improved |
| `lteNRRCC` | 0.1113s | 0.1173s | -0.0060s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 9.69 MB | 0.0% | 202.8% |
| `f1ap_rel18.6_specs` | 10.92 MB | 164.16 MB | 137.3% | 133.6% |
| `ngap_rel18.6_specs` | 10.07 MB | 10.60 MB | 207.5% | 136.0% |
| `lteNRRCC` | 73.74 MB | 98.56 MB | 200.5% | 115.7% |
<!-- BENCH_RESULTS_END -->
