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
Generated: 2026-04-24T22:49:45.745623+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0345s | +0.0034s | worse |
| `f1ap_rel18.6_specs` | 0.1172s | 0.1098s | +0.0074s | worse |
| `ngap_rel18.6_specs` | 0.0796s | 0.0762s | +0.0034s | worse |
| `lteNRRCC` | 0.1242s | 0.1187s | +0.0055s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 8.6% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0350s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0961s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0662s | 0.0672s | -0.0010s | improved |
| `lteNRRCC` | 0.1265s | 0.1305s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 36.63 MB | 26.5% | 110.0% |
| `f1ap_rel18.6_specs` | 22.04 MB | 102.93 MB | 112.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.55 MB | 74.46 MB | 110.7% | 106.7% |
| `lteNRRCC` | 48.27 MB | 65.99 MB | 104.8% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0286s | 0.0329s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.0760s | 0.0882s | -0.0122s | improved |
| `ngap_rel18.6_specs` | 0.0525s | 0.0618s | -0.0093s | improved |
| `lteNRRCC` | 0.1013s | 0.1161s | -0.0148s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.74 MB | 55.82 MB | 27.4% | 113.0% |
| `f1ap_rel18.6_specs` | 34.62 MB | 164.77 MB | 112.0% | 104.3% |
| `ngap_rel18.6_specs` | 24.38 MB | 117.20 MB | 114.3% | 105.7% |
| `lteNRRCC` | 75.00 MB | 102.29 MB | 104.0% | 105.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0246s | 0.0256s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0631s | 0.0832s | -0.0201s | improved |
| `ngap_rel18.6_specs` | 0.0659s | 0.0482s | +0.0177s | worse |
| `lteNRRCC` | 0.1107s | 0.0809s | +0.0298s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.66 MB | 4.92 MB | 0.9% | 0.0% |
| `f1ap_rel18.6_specs` | 5.64 MB | 4.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 1.11 MB | 5.61 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.03 MB | 4.70 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0378s | -0.0051s | improved |
| `f1ap_rel18.6_specs` | 0.0915s | 0.1032s | -0.0117s | improved |
| `ngap_rel18.6_specs` | 0.0632s | 0.0722s | -0.0090s | improved |
| `lteNRRCC` | 0.1137s | 0.1348s | -0.0211s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.80 MB | 7.90 MB | 213.9% | 104.5% |
| `f1ap_rel18.6_specs` | 8.41 MB | 8.66 MB | 103.5% | 105.2% |
| `ngap_rel18.6_specs` | 7.90 MB | 8.17 MB | 102.5% | 206.5% |
| `lteNRRCC` | 51.27 MB | 63.79 MB | 139.3% | 124.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0369s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.0971s | 0.1032s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0695s | 0.0740s | -0.0045s | improved |
| `lteNRRCC` | 0.1109s | 0.1125s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.09 MB | 10.02 MB | 126.9% | 142.2% |
| `f1ap_rel18.6_specs` | 10.57 MB | 144.36 MB | 116.8% | 142.0% |
| `ngap_rel18.6_specs` | 9.33 MB | 10.25 MB | 132.6% | 141.5% |
| `lteNRRCC` | 73.77 MB | 83.20 MB | 139.8% | 141.5% |
<!-- BENCH_RESULTS_END -->
