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
Generated: 2026-09-08T23:58:45.353263+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0364s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1128s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0771s | -0.0015s | improved |
| `lteNRRCC` | 0.1196s | 0.1211s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 14.8% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0349s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0987s | 0.0950s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0669s | +0.0023s | worse |
| `lteNRRCC` | 0.1313s | 0.1280s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.44 MB | 75.9% | 107.1% |
| `f1ap_rel18.6_specs` | 22.12 MB | 102.87 MB | 103.0% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.70 MB | 103.8% | 102.2% |
| `lteNRRCC` | 48.40 MB | 66.36 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0284s | 0.0347s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0768s | 0.0907s | -0.0139s | improved |
| `ngap_rel18.6_specs` | 0.0532s | 0.0639s | -0.0107s | improved |
| `lteNRRCC` | 0.1028s | 0.1175s | -0.0147s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.78 MB | 55.01 MB | 40.5% | 104.5% |
| `f1ap_rel18.6_specs` | 34.30 MB | 164.50 MB | 104.2% | 102.1% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.88 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.70 MB | 102.72 MB | 102.0% | 103.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0253s | 0.0208s | +0.0045s | worse |
| `f1ap_rel18.6_specs` | 0.0835s | 0.0839s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0529s | 0.0696s | -0.0167s | improved |
| `lteNRRCC` | 0.1044s | 0.0923s | +0.0121s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.56 MB | 7.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.81 MB | 4.64 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.59 MB | 7.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.47 MB | 7.53 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0393s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1118s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0814s | -0.0055s | improved |
| `lteNRRCC` | 0.1285s | 0.1434s | -0.0149s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.33 MB | 7.82 MB | 112.3% | 166.1% |
| `f1ap_rel18.6_specs` | 8.45 MB | 8.45 MB | 177.6% | 161.9% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.12 MB | 155.3% | 81.1% |
| `lteNRRCC` | 8.30 MB | 7.80 MB | 83.9% | 161.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0424s | 0.0414s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1265s | 0.1166s | +0.0099s | worse |
| `ngap_rel18.6_specs` | 0.0865s | 0.0844s | +0.0021s | worse |
| `lteNRRCC` | 0.1318s | 0.1261s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.97 MB | 10.15 MB | 115.3% | 118.1% |
| `f1ap_rel18.6_specs` | 10.43 MB | 9.95 MB | 101.4% | 82.4% |
| `ngap_rel18.6_specs` | 10.25 MB | 9.48 MB | 112.9% | 178.6% |
| `lteNRRCC` | 8.93 MB | 98.59 MB | 113.3% | 120.5% |
<!-- BENCH_RESULTS_END -->
