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
Generated: 2026-08-01T23:00:08.935683+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0351s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1119s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0772s | +0.0004s | worse |
| `lteNRRCC` | 0.1207s | 0.1197s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 81.8% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0280s | 0.0351s | -0.0071s | improved |
| `f1ap_rel18.6_specs` | 0.0749s | 0.0962s | -0.0213s | improved |
| `ngap_rel18.6_specs` | 0.0514s | 0.0668s | -0.0154s | improved |
| `lteNRRCC` | 0.0983s | 0.1300s | -0.0317s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.21 MB | 36.28 MB | 78.3% | 104.5% |
| `f1ap_rel18.6_specs` | 21.99 MB | 102.74 MB | 104.2% | 100.0% |
| `ngap_rel18.6_specs` | 19.21 MB | 74.57 MB | 100.0% | 103.0% |
| `lteNRRCC` | 48.62 MB | 66.43 MB | 102.1% | 101.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0345s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0916s | 0.0916s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0689s | 0.0632s | +0.0057s | worse |
| `lteNRRCC` | 0.1149s | 0.1173s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 55.56 MB | 65.5% | 103.8% |
| `f1ap_rel18.6_specs` | 35.23 MB | 164.66 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.78 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.54 MB | 102.84 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0243s | 0.0190s | +0.0053s | worse |
| `f1ap_rel18.6_specs` | 0.0872s | 0.0669s | +0.0203s | worse |
| `ngap_rel18.6_specs` | 0.0584s | 0.0415s | +0.0169s | worse |
| `lteNRRCC` | 0.0959s | 0.0717s | +0.0242s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.06 MB | 4.61 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 8.52 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.12 MB | 7.36 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.08 MB | 7.50 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0408s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1041s | 0.1109s | -0.0068s | improved |
| `ngap_rel18.6_specs` | 0.0727s | 0.0798s | -0.0071s | improved |
| `lteNRRCC` | 0.1362s | 0.1555s | -0.0193s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.07 MB | 7.31 MB | 0.0% | 83.0% |
| `f1ap_rel18.6_specs` | 8.04 MB | 106.66 MB | 166.5% | 167.2% |
| `ngap_rel18.6_specs` | 7.48 MB | 8.00 MB | 165.2% | 109.6% |
| `lteNRRCC` | 49.66 MB | 70.56 MB | 104.1% | 165.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0407s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1181s | -0.0097s | improved |
| `ngap_rel18.6_specs` | 0.0733s | 0.0805s | -0.0072s | improved |
| `lteNRRCC` | 0.1240s | 0.1318s | -0.0078s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.04 MB | 10.46 MB | 0.0% | 116.2% |
| `f1ap_rel18.6_specs` | 9.75 MB | 164.20 MB | 164.5% | 116.8% |
| `ngap_rel18.6_specs` | 10.07 MB | 8.96 MB | 108.5% | 92.6% |
| `lteNRRCC` | 8.50 MB | 77.46 MB | 80.4% | 157.0% |
<!-- BENCH_RESULTS_END -->
