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
Generated: 2026-03-14T06:42:20.452884+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0361s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.1219s | 0.1174s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0839s | 0.0815s | +0.0024s | worse |
| `lteNRRCC` | 0.1265s | 0.1223s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.41 MB | 55.79 MB | 105.6% | 106.9% |
| `f1ap_rel18.6_specs` | 32.29 MB | 176.91 MB | 106.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.29 MB | 125.79 MB | 108.3% | 103.8% |
| `lteNRRCC` | 72.34 MB | 99.97 MB | 103.3% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0367s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0982s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0701s | 0.0686s | +0.0015s | worse |
| `lteNRRCC` | 0.1273s | 0.1292s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.27 MB | 37.62 MB | 96.3% | 109.7% |
| `f1ap_rel18.6_specs` | 22.43 MB | 111.89 MB | 108.6% | 104.9% |
| `ngap_rel18.6_specs` | 16.85 MB | 80.51 MB | 113.8% | 108.5% |
| `lteNRRCC` | 48.75 MB | 66.32 MB | 106.1% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0347s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.0979s | 0.0918s | +0.0061s | worse |
| `ngap_rel18.6_specs` | 0.0701s | 0.0654s | +0.0047s | worse |
| `lteNRRCC` | 0.1290s | 0.1167s | +0.0123s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.46 MB | 57.43 MB | 35.6% | 112.5% |
| `f1ap_rel18.6_specs` | 34.12 MB | 179.06 MB | 108.6% | 104.8% |
| `ngap_rel18.6_specs` | 23.72 MB | 127.96 MB | 113.8% | 106.2% |
| `lteNRRCC` | 74.60 MB | 102.74 MB | 106.0% | 105.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0241s | 0.0292s | -0.0051s | improved |
| `f1ap_rel18.6_specs` | 0.0788s | 0.0693s | +0.0095s | worse |
| `ngap_rel18.6_specs` | 0.0504s | 0.0508s | -0.0004s | improved |
| `lteNRRCC` | 0.0801s | 0.0775s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.77 MB | 4.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 9.09 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.05 MB | 4.17 MB | 0.0% | 0.0% |
| `lteNRRCC` | 1.09 MB | 3.53 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0432s | 0.0410s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1166s | 0.1176s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0816s | 0.0806s | +0.0010s | worse |
| `lteNRRCC` | 0.1434s | 0.1484s | -0.0050s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.91 MB | 7.83 MB | 217.5% | 213.6% |
| `f1ap_rel18.6_specs` | 8.00 MB | 8.09 MB | 165.8% | 156.5% |
| `ngap_rel18.6_specs` | 7.63 MB | 7.69 MB | 153.9% | 97.7% |
| `lteNRRCC` | 45.89 MB | 52.36 MB | 107.9% | 214.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0393s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1105s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0764s | 0.0779s | -0.0015s | improved |
| `lteNRRCC` | 0.1266s | 0.1295s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.58 MB | 8.20 MB | 100.1% | 162.9% |
| `f1ap_rel18.6_specs` | 10.66 MB | 176.93 MB | 103.5% | 163.8% |
| `ngap_rel18.6_specs` | 8.72 MB | 8.72 MB | 162.1% | 92.4% |
| `lteNRRCC` | 69.12 MB | 78.94 MB | 160.1% | 107.7% |
<!-- BENCH_RESULTS_END -->
