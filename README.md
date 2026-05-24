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
Generated: 2026-05-24T11:21:07.503820+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0360s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1165s | 0.1123s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0802s | 0.0769s | +0.0033s | worse |
| `lteNRRCC` | 0.1246s | 0.1213s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 7.8% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.9% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0332s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.0971s | 0.0973s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0688s | 0.0648s | +0.0040s | worse |
| `lteNRRCC` | 0.1310s | 0.1163s | +0.0147s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.22 MB | 36.57 MB | 80.6% | 106.9% |
| `f1ap_rel18.6_specs` | 22.36 MB | 102.89 MB | 108.8% | 105.1% |
| `ngap_rel18.6_specs` | 17.66 MB | 74.48 MB | 111.1% | 106.5% |
| `lteNRRCC` | 48.48 MB | 65.86 MB | 103.0% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0282s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.0928s | 0.0759s | +0.0169s | worse |
| `ngap_rel18.6_specs` | 0.0651s | 0.0522s | +0.0129s | worse |
| `lteNRRCC` | 0.1273s | 0.1047s | +0.0226s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.67 MB | 22.9% | 113.8% |
| `f1ap_rel18.6_specs` | 34.66 MB | 164.70 MB | 112.5% | 105.2% |
| `ngap_rel18.6_specs` | 24.47 MB | 117.67 MB | 114.8% | 109.1% |
| `lteNRRCC` | 74.79 MB | 102.69 MB | 106.2% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0234s | 0.0493s | -0.0259s | improved |
| `f1ap_rel18.6_specs` | 0.0783s | 0.0656s | +0.0127s | worse |
| `ngap_rel18.6_specs` | 0.0498s | 0.0525s | -0.0027s | improved |
| `lteNRRCC` | 0.0740s | 0.0968s | -0.0228s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.41 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.08 MB | 3.14 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.95 MB | 3.94 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.95 MB | 3.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0431s | 0.0423s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1179s | 0.1175s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0833s | 0.0824s | +0.0009s | worse |
| `lteNRRCC` | 0.1458s | 0.1513s | -0.0055s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.11 MB | 7.97 MB | 154.8% | 157.6% |
| `f1ap_rel18.6_specs` | 8.45 MB | 105.38 MB | 80.8% | 104.8% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.17 MB | 93.6% | 162.2% |
| `lteNRRCC` | 46.66 MB | 69.11 MB | 102.5% | 110.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0347s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0952s | 0.1086s | -0.0134s | improved |
| `ngap_rel18.6_specs` | 0.0667s | 0.0691s | -0.0024s | improved |
| `lteNRRCC` | 0.1132s | 0.1108s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.64 MB | 10.08 MB | 122.0% | 142.7% |
| `f1ap_rel18.6_specs` | 10.43 MB | 164.18 MB | 141.2% | 142.2% |
| `ngap_rel18.6_specs` | 10.04 MB | 10.18 MB | 0.0% | 137.6% |
| `lteNRRCC` | 9.11 MB | 86.50 MB | 140.3% | 140.9% |
<!-- BENCH_RESULTS_END -->
