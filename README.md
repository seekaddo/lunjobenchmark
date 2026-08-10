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
Generated: 2026-08-10T22:45:24.927183+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0367s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1088s | 0.1132s | -0.0044s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0780s | -0.0037s | improved |
| `lteNRRCC` | 0.1185s | 0.1220s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 14.9% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0364s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.0954s | 0.0909s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0660s | 0.0634s | +0.0026s | worse |
| `lteNRRCC` | 0.1182s | 0.1223s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 36.69 MB | 17.8% | 104.0% |
| `f1ap_rel18.6_specs` | 21.84 MB | 102.86 MB | 103.7% | 101.8% |
| `ngap_rel18.6_specs` | 17.68 MB | 74.30 MB | 104.8% | 102.5% |
| `lteNRRCC` | 48.56 MB | 66.43 MB | 101.8% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0340s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0905s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0649s | 0.0648s | +0.0001s | worse |
| `lteNRRCC` | 0.1204s | 0.1169s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.49 MB | 55.76 MB | 70.0% | 107.4% |
| `f1ap_rel18.6_specs` | 34.60 MB | 164.18 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.41 MB | 117.38 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.70 MB | 102.67 MB | 101.7% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0218s | 0.0484s | -0.0266s | improved |
| `f1ap_rel18.6_specs` | 0.0772s | 0.1005s | -0.0233s | improved |
| `ngap_rel18.6_specs` | 0.0579s | 0.0727s | -0.0148s | improved |
| `lteNRRCC` | 0.0921s | 0.1089s | -0.0168s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.42 MB | 3.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.56 MB | 7.48 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.72 MB | 8.38 MB | 0.0% | 1.5% |
| `lteNRRCC` | 7.44 MB | 7.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0380s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1050s | 0.1049s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0727s | 0.0767s | -0.0040s | improved |
| `lteNRRCC` | 0.1398s | 0.1378s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.81 MB | 110.4% | 108.1% |
| `f1ap_rel18.6_specs` | 8.54 MB | 8.04 MB | 117.7% | 102.8% |
| `ngap_rel18.6_specs` | 7.98 MB | 7.54 MB | 112.0% | 162.4% |
| `lteNRRCC` | 48.07 MB | 70.54 MB | 116.4% | 116.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0437s | 0.0383s | +0.0054s | worse |
| `f1ap_rel18.6_specs` | 0.1337s | 0.1116s | +0.0221s | worse |
| `ngap_rel18.6_specs` | 0.0902s | 0.0823s | +0.0079s | worse |
| `lteNRRCC` | 0.1413s | 0.1313s | +0.0100s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 9.71 MB | 0.0% | 156.6% |
| `f1ap_rel18.6_specs` | 10.37 MB | 163.75 MB | 155.5% | 158.4% |
| `ngap_rel18.6_specs` | 10.07 MB | 9.55 MB | 159.0% | 79.2% |
| `lteNRRCC` | 9.21 MB | 101.71 MB | 156.4% | 160.0% |
<!-- BENCH_RESULTS_END -->
