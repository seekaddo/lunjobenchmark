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
Generated: 2026-03-30T11:10:26.163294+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0374s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1157s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0789s | 0.0796s | -0.0007s | improved |
| `lteNRRCC` | 0.1218s | 0.1239s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 23.5% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 103.8% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0327s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0948s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0674s | 0.0648s | +0.0026s | worse |
| `lteNRRCC` | 0.1300s | 0.1164s | +0.0136s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.24 MB | 36.61 MB | 100.0% | 106.9% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.64 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.44 MB | 74.14 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.80 MB | 66.39 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0334s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0896s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0645s | 0.0621s | +0.0024s | worse |
| `lteNRRCC` | 0.1165s | 0.1167s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.24 MB | 55.85 MB | 82.8% | 110.7% |
| `f1ap_rel18.6_specs` | 34.37 MB | 164.71 MB | 110.3% | 105.3% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.81 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.99 MB | 102.73 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0259s | 0.0255s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1094s | 0.0651s | +0.0443s | worse |
| `ngap_rel18.6_specs` | 0.0436s | 0.0442s | -0.0006s | improved |
| `lteNRRCC` | 0.0965s | 0.0744s | +0.0221s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.70 MB | 4.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.06 MB | 2.48 MB | 0.0% | 0.1% |
| `ngap_rel18.6_specs` | 5.12 MB | 4.42 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.48 MB | 3.97 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0382s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1071s | 0.1054s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0753s | 0.0723s | +0.0030s | worse |
| `lteNRRCC` | 0.1365s | 0.1384s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.74 MB | 7.62 MB | 236.8% | 106.7% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.60 MB | 96.7% | 116.8% |
| `ngap_rel18.6_specs` | 7.61 MB | 8.17 MB | 166.1% | 115.9% |
| `lteNRRCC` | 48.69 MB | 69.22 MB | 107.1% | 115.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0379s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1147s | -0.0072s | improved |
| `ngap_rel18.6_specs` | 0.0728s | 0.0774s | -0.0046s | improved |
| `lteNRRCC` | 0.1233s | 0.1267s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.85 MB | 8.92 MB | 158.6% | 159.1% |
| `f1ap_rel18.6_specs` | 9.67 MB | 10.05 MB | 159.7% | 158.5% |
| `ngap_rel18.6_specs` | 9.07 MB | 10.43 MB | 78.3% | 104.3% |
| `lteNRRCC` | 9.36 MB | 96.20 MB | 98.2% | 155.2% |
<!-- BENCH_RESULTS_END -->
