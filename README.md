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
Generated: 2026-03-14T22:34:36.213409+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0370s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1231s | 0.1174s | +0.0057s | worse |
| `ngap_rel18.6_specs` | 0.0831s | 0.0820s | +0.0011s | worse |
| `lteNRRCC` | 0.1248s | 0.1245s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.42 MB | 55.80 MB | 100.0% | 110.7% |
| `f1ap_rel18.6_specs` | 32.30 MB | 176.92 MB | 107.1% | 102.9% |
| `ngap_rel18.6_specs` | 22.30 MB | 125.80 MB | 108.7% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.06 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0370s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0998s | 0.0990s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0708s | 0.0701s | +0.0007s | worse |
| `lteNRRCC` | 0.1351s | 0.1337s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.79 MB | 37.45 MB | 28.3% | 109.7% |
| `f1ap_rel18.6_specs` | 22.20 MB | 111.83 MB | 105.6% | 106.3% |
| `ngap_rel18.6_specs` | 16.45 MB | 80.50 MB | 113.8% | 108.3% |
| `lteNRRCC` | 48.66 MB | 66.03 MB | 104.3% | 103.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0357s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0932s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0655s | 0.0665s | -0.0010s | improved |
| `lteNRRCC` | 0.1160s | 0.1169s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.75 MB | 58.00 MB | 92.3% | 110.3% |
| `f1ap_rel18.6_specs` | 34.59 MB | 178.84 MB | 109.7% | 107.0% |
| `ngap_rel18.6_specs` | 23.50 MB | 128.13 MB | 111.5% | 109.1% |
| `lteNRRCC` | 74.55 MB | 102.76 MB | 105.0% | 105.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0250s | 0.0220s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.0766s | 0.0680s | +0.0086s | worse |
| `ngap_rel18.6_specs` | 0.0577s | 0.0472s | +0.0105s | worse |
| `lteNRRCC` | 0.1079s | 0.0746s | +0.0333s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.53 MB | 3.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.48 MB | 2.92 MB | 1.5% | 0.0% |
| `lteNRRCC` | 3.66 MB | 4.30 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0403s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1110s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0776s | +0.0013s | worse |
| `lteNRRCC` | 0.1281s | 0.1409s | -0.0128s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.80 MB | 7.75 MB | 243.2% | 123.1% |
| `f1ap_rel18.6_specs` | 8.10 MB | 8.32 MB | 120.7% | 117.1% |
| `ngap_rel18.6_specs` | 7.87 MB | 8.10 MB | 121.7% | 122.5% |
| `lteNRRCC` | 7.93 MB | 68.92 MB | 119.8% | 242.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0392s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1117s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0762s | +0.0024s | worse |
| `lteNRRCC` | 0.1265s | 0.1249s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.67 MB | 9.05 MB | 113.3% | 98.0% |
| `f1ap_rel18.6_specs` | 9.41 MB | 179.23 MB | 178.2% | 160.1% |
| `ngap_rel18.6_specs` | 9.09 MB | 8.96 MB | 90.5% | 79.9% |
| `lteNRRCC` | 73.07 MB | 98.64 MB | 159.5% | 109.9% |
<!-- BENCH_RESULTS_END -->
