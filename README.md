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
Generated: 2026-06-30T23:18:55.943344+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0351s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1089s | 0.1118s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0743s | +0.0007s | worse |
| `lteNRRCC` | 0.1186s | 0.1187s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 18.9% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.3% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0345s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0937s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0659s | -0.0006s | improved |
| `lteNRRCC` | 0.1272s | 0.1301s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 35.95 MB | 88.5% | 111.1% |
| `f1ap_rel18.6_specs` | 22.01 MB | 103.30 MB | 109.7% | 105.4% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.12 MB | 107.7% | 107.1% |
| `lteNRRCC` | 48.66 MB | 65.39 MB | 104.7% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0346s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0999s | 0.0937s | +0.0062s | worse |
| `ngap_rel18.6_specs` | 0.0689s | 0.0716s | -0.0027s | improved |
| `lteNRRCC` | 0.1163s | 0.1179s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.42 MB | 54.86 MB | 85.7% | 103.8% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.62 MB | 107.4% | 101.7% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.42 MB | 109.5% | 104.7% |
| `lteNRRCC` | 74.95 MB | 102.34 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0239s | 0.0444s | -0.0205s | improved |
| `f1ap_rel18.6_specs` | 0.0665s | 0.0904s | -0.0239s | improved |
| `ngap_rel18.6_specs` | 0.0470s | 0.0663s | -0.0193s | improved |
| `lteNRRCC` | 0.0765s | 0.0917s | -0.0152s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.80 MB | 4.27 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.66 MB | 3.88 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.19 MB | 4.42 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.48 MB | 7.69 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0388s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1053s | 0.1090s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0736s | 0.0743s | -0.0007s | improved |
| `lteNRRCC` | 0.1355s | 0.1384s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.34 MB | 7.43 MB | 83.4% | 164.5% |
| `f1ap_rel18.6_specs` | 8.54 MB | 8.04 MB | 229.1% | 83.1% |
| `ngap_rel18.6_specs` | 7.45 MB | 8.17 MB | 163.4% | 233.3% |
| `lteNRRCC` | 48.50 MB | 51.45 MB | 155.0% | 107.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0445s | -0.0056s | improved |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1272s | -0.0188s | improved |
| `ngap_rel18.6_specs` | 0.0765s | 0.0868s | -0.0103s | improved |
| `lteNRRCC` | 0.1251s | 0.1415s | -0.0164s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.79 MB | 8.66 MB | 160.6% | 158.2% |
| `f1ap_rel18.6_specs` | 9.97 MB | 10.65 MB | 160.2% | 110.5% |
| `ngap_rel18.6_specs` | 8.90 MB | 8.96 MB | 88.1% | 156.3% |
| `lteNRRCC` | 72.78 MB | 74.15 MB | 157.0% | 156.2% |
<!-- BENCH_RESULTS_END -->
