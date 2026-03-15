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
Generated: 2026-03-15T10:39:00.670720+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0391s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1201s | 0.1231s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0840s | 0.0831s | +0.0009s | worse |
| `lteNRRCC` | 0.1251s | 0.1248s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.42 MB | 55.80 MB | 46.3% | 106.9% |
| `f1ap_rel18.6_specs` | 32.30 MB | 176.92 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.30 MB | 125.80 MB | 112.5% | 103.9% |
| `lteNRRCC` | 72.34 MB | 100.06 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0378s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.0999s | 0.0998s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0680s | 0.0708s | -0.0028s | improved |
| `lteNRRCC` | 0.1200s | 0.1351s | -0.0151s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.67 MB | 37.77 MB | 90.9% | 107.7% |
| `f1ap_rel18.6_specs` | 22.39 MB | 111.96 MB | 106.9% | 103.4% |
| `ngap_rel18.6_specs` | 16.72 MB | 79.66 MB | 113.0% | 104.5% |
| `lteNRRCC` | 48.70 MB | 66.21 MB | 103.4% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0346s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0960s | 0.0933s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0655s | +0.0008s | worse |
| `lteNRRCC` | 0.1177s | 0.1160s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.75 MB | 58.04 MB | 26.3% | 113.8% |
| `f1ap_rel18.6_specs` | 34.75 MB | 178.90 MB | 109.7% | 103.4% |
| `ngap_rel18.6_specs` | 23.75 MB | 127.77 MB | 111.5% | 106.7% |
| `lteNRRCC` | 75.04 MB | 102.89 MB | 105.0% | 102.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0217s | 0.0250s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.0673s | 0.0766s | -0.0093s | improved |
| `ngap_rel18.6_specs` | 0.0465s | 0.0577s | -0.0112s | improved |
| `lteNRRCC` | 0.0750s | 0.1079s | -0.0329s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.97 MB | 4.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.06 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.00 MB | 4.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.92 MB | 4.03 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0412s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1127s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0789s | +0.0001s | worse |
| `lteNRRCC` | 0.1435s | 0.1281s | +0.0154s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.29 MB | 7.44 MB | 82.2% | 102.1% |
| `f1ap_rel18.6_specs` | 8.17 MB | 7.98 MB | 229.8% | 118.4% |
| `ngap_rel18.6_specs` | 7.25 MB | 7.38 MB | 163.8% | 161.9% |
| `lteNRRCC` | 47.86 MB | 68.62 MB | 160.5% | 164.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0405s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1182s | 0.1118s | +0.0064s | worse |
| `ngap_rel18.6_specs` | 0.0838s | 0.0786s | +0.0052s | worse |
| `lteNRRCC` | 0.1285s | 0.1265s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.62 MB | 0.0% | 155.5% |
| `f1ap_rel18.6_specs` | 9.77 MB | 175.63 MB | 158.9% | 105.8% |
| `ngap_rel18.6_specs` | 9.02 MB | 9.02 MB | 169.1% | 155.1% |
| `lteNRRCC` | 8.95 MB | 81.25 MB | 101.3% | 108.4% |
<!-- BENCH_RESULTS_END -->
