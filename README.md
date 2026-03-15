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
Generated: 2026-03-15T22:36:30.282584+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0381s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1172s | 0.1201s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0819s | 0.0840s | -0.0021s | improved |
| `lteNRRCC` | 0.1230s | 0.1251s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.42 MB | 55.80 MB | 36.0% | 106.9% |
| `f1ap_rel18.6_specs` | 32.30 MB | 176.92 MB | 106.9% | 102.9% |
| `ngap_rel18.6_specs` | 22.30 MB | 125.80 MB | 108.7% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.06 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0335s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1107s | 0.0999s | +0.0108s | worse |
| `ngap_rel18.6_specs` | 0.0780s | 0.0680s | +0.0100s | worse |
| `lteNRRCC` | 0.1258s | 0.1200s | +0.0058s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.85 MB | 37.68 MB | 95.2% | 107.4% |
| `f1ap_rel18.6_specs` | 22.25 MB | 111.87 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 16.14 MB | 80.18 MB | 113.0% | 104.3% |
| `lteNRRCC` | 48.81 MB | 66.45 MB | 103.3% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0361s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.0965s | 0.0960s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0709s | 0.0663s | +0.0046s | worse |
| `lteNRRCC` | 0.1220s | 0.1177s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.68 MB | 58.00 MB | 27.3% | 109.7% |
| `f1ap_rel18.6_specs` | 34.41 MB | 179.29 MB | 112.5% | 106.7% |
| `ngap_rel18.6_specs` | 24.51 MB | 127.79 MB | 111.1% | 108.5% |
| `lteNRRCC` | 74.52 MB | 102.85 MB | 106.6% | 104.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0201s | 0.0217s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0626s | 0.0673s | -0.0047s | improved |
| `ngap_rel18.6_specs` | 0.0426s | 0.0465s | -0.0039s | improved |
| `lteNRRCC` | 0.0697s | 0.0750s | -0.0053s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.80 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 4.02 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 3.84 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.00 MB | 4.08 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0397s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1149s | 0.1111s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0806s | 0.0790s | +0.0016s | worse |
| `lteNRRCC` | 0.1450s | 0.1435s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.57 MB | 7.36 MB | 106.7% | 92.2% |
| `f1ap_rel18.6_specs` | 8.24 MB | 8.12 MB | 224.7% | 94.0% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.48 MB | 159.2% | 158.0% |
| `lteNRRCC` | 49.20 MB | 69.07 MB | 109.2% | 105.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0415s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1186s | 0.1182s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0838s | 0.0838s | +0.0000s | flat |
| `lteNRRCC` | 0.1332s | 0.1285s | +0.0047s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.33 MB | 0.0% | 226.3% |
| `f1ap_rel18.6_specs` | 11.28 MB | 179.21 MB | 229.7% | 117.3% |
| `ngap_rel18.6_specs` | 11.00 MB | 10.31 MB | 111.8% | 117.5% |
| `lteNRRCC` | 9.45 MB | 72.79 MB | 231.0% | 158.6% |
<!-- BENCH_RESULTS_END -->
