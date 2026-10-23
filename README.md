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
Generated: 2026-10-23T00:30:12.017547+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0359s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1165s | 0.1104s | +0.0061s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0770s | +0.0030s | worse |
| `lteNRRCC` | 0.1232s | 0.1197s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.98 MB | 53.55 MB | 71.4% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0266s | 0.0294s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.0728s | 0.0909s | -0.0181s | improved |
| `ngap_rel18.6_specs` | 0.0513s | 0.0643s | -0.0130s | improved |
| `lteNRRCC` | 0.0967s | 0.0955s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.52 MB | 69.6% | 100.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.31 MB | 100.0% | 104.5% |
| `ngap_rel18.6_specs` | 18.03 MB | 74.61 MB | 100.0% | 103.0% |
| `lteNRRCC` | 48.34 MB | 65.92 MB | 104.3% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0283s | 0.0359s | -0.0076s | improved |
| `f1ap_rel18.6_specs` | 0.0745s | 0.0936s | -0.0191s | improved |
| `ngap_rel18.6_specs` | 0.0518s | 0.0646s | -0.0128s | improved |
| `lteNRRCC` | 0.1016s | 0.1204s | -0.0188s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 55.07 MB | 72.7% | 104.8% |
| `f1ap_rel18.6_specs` | 34.47 MB | 164.73 MB | 104.3% | 102.2% |
| `ngap_rel18.6_specs` | 24.51 MB | 117.75 MB | 110.5% | 103.0% |
| `lteNRRCC` | 74.43 MB | 102.32 MB | 102.1% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0142s | 0.0270s | -0.0128s | improved |
| `f1ap_rel18.6_specs` | 0.0683s | 0.0752s | -0.0069s | improved |
| `ngap_rel18.6_specs` | 0.0603s | 0.0502s | +0.0101s | worse |
| `lteNRRCC` | 0.0859s | 0.0826s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.98 MB | 3.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.20 MB | 9.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.62 MB | 7.27 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.08 MB | 7.64 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0362s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0872s | 0.0981s | -0.0109s | improved |
| `ngap_rel18.6_specs` | 0.0610s | 0.0667s | -0.0057s | improved |
| `lteNRRCC` | 0.0965s | 0.1065s | -0.0100s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 18.26 MB | 0.0% | 149.0% |
| `f1ap_rel18.6_specs` | 14.91 MB | 106.66 MB | 85.8% | 0.0% |
| `ngap_rel18.6_specs` | 17.93 MB | 14.99 MB | 0.0% | 205.6% |
| `lteNRRCC` | 18.72 MB | 12.28 MB | 107.3% | 99.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0407s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1189s | 0.1171s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0847s | 0.0807s | +0.0040s | worse |
| `lteNRRCC` | 0.1354s | 0.1311s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.66 MB | 0.0% | 88.7% |
| `f1ap_rel18.6_specs` | 9.88 MB | 164.20 MB | 152.8% | 94.3% |
| `ngap_rel18.6_specs` | 9.28 MB | 10.58 MB | 147.5% | 225.5% |
| `lteNRRCC` | 9.69 MB | 85.78 MB | 211.8% | 148.2% |
<!-- BENCH_RESULTS_END -->
