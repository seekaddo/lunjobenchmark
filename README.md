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
Generated: 2026-05-03T22:53:32.531844+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0362s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1111s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0750s | 0.0778s | -0.0028s | improved |
| `lteNRRCC` | 0.1193s | 0.1229s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 27.2% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0344s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0933s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0661s | 0.0656s | +0.0005s | worse |
| `lteNRRCC` | 0.1267s | 0.1258s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.18 MB | 26.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.03 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.65 MB | 74.12 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.57 MB | 65.41 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0337s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0908s | 0.0901s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0633s | 0.0622s | +0.0011s | worse |
| `lteNRRCC` | 0.1162s | 0.1153s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.29 MB | 31.2% | 110.7% |
| `f1ap_rel18.6_specs` | 34.45 MB | 164.36 MB | 110.0% | 107.1% |
| `ngap_rel18.6_specs` | 24.57 MB | 117.77 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.92 MB | 102.68 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0249s | 0.0196s | +0.0053s | worse |
| `f1ap_rel18.6_specs` | 0.0734s | 0.0625s | +0.0109s | worse |
| `ngap_rel18.6_specs` | 0.0472s | 0.0474s | -0.0002s | improved |
| `lteNRRCC` | 0.0738s | 0.0770s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.31 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.08 MB | 4.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.31 MB | 8.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.12 MB | 4.00 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0392s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1057s | 0.1059s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0740s | 0.0745s | -0.0005s | improved |
| `lteNRRCC` | 0.1373s | 0.1381s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.75 MB | 164.2% | 235.1% |
| `f1ap_rel18.6_specs` | 7.90 MB | 106.64 MB | 165.7% | 164.8% |
| `ngap_rel18.6_specs` | 8.17 MB | 7.49 MB | 92.7% | 162.4% |
| `lteNRRCC` | 47.82 MB | 69.10 MB | 105.3% | 111.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0375s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.1193s | 0.1084s | +0.0109s | worse |
| `ngap_rel18.6_specs` | 0.0815s | 0.0735s | +0.0080s | worse |
| `lteNRRCC` | 0.1365s | 0.1226s | +0.0139s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.07 MB | 8.93 MB | 164.2% | 165.3% |
| `f1ap_rel18.6_specs` | 9.80 MB | 150.84 MB | 164.5% | 163.0% |
| `ngap_rel18.6_specs` | 9.20 MB | 9.33 MB | 164.6% | 159.8% |
| `lteNRRCC` | 8.67 MB | 80.20 MB | 81.4% | 164.3% |
<!-- BENCH_RESULTS_END -->
