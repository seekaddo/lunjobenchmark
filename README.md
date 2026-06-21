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
Generated: 2026-06-21T23:22:05.778391+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0372s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1142s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0765s | +0.0004s | worse |
| `lteNRRCC` | 0.1211s | 0.1219s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 21.1% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0357s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0985s | -0.0052s | improved |
| `ngap_rel18.6_specs` | 0.0648s | 0.0706s | -0.0058s | improved |
| `lteNRRCC` | 0.1170s | 0.1333s | -0.0163s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 36.36 MB | 86.4% | 108.3% |
| `f1ap_rel18.6_specs` | 21.99 MB | 103.41 MB | 107.4% | 103.6% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.39 MB | 109.1% | 104.9% |
| `lteNRRCC` | 48.10 MB | 66.33 MB | 103.6% | 104.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0364s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0907s | 0.0955s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0631s | 0.0675s | -0.0044s | improved |
| `lteNRRCC` | 0.1171s | 0.1294s | -0.0123s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 54.93 MB | 22.5% | 111.1% |
| `f1ap_rel18.6_specs` | 35.22 MB | 163.80 MB | 110.3% | 105.2% |
| `ngap_rel18.6_specs` | 23.47 MB | 117.34 MB | 112.5% | 104.8% |
| `lteNRRCC` | 74.53 MB | 102.57 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0290s | 0.0288s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0804s | 0.0603s | +0.0201s | worse |
| `ngap_rel18.6_specs` | 0.0602s | 0.0402s | +0.0200s | worse |
| `lteNRRCC` | 0.0761s | 0.0669s | +0.0092s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.39 MB | 8.22 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.06 MB | 9.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.47 MB | 8.22 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.39 MB | 7.50 MB | 0.9% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0336s | +0.0048s | worse |
| `f1ap_rel18.6_specs` | 0.1051s | 0.0946s | +0.0105s | worse |
| `ngap_rel18.6_specs` | 0.0761s | 0.0652s | +0.0109s | worse |
| `lteNRRCC` | 0.1370s | 0.1125s | +0.0245s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.82 MB | 7.38 MB | 115.4% | 82.2% |
| `f1ap_rel18.6_specs` | 7.90 MB | 8.17 MB | 163.8% | 97.7% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.55 MB | 164.1% | 164.0% |
| `lteNRRCC` | 47.45 MB | 50.81 MB | 105.3% | 117.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0443s | 0.0397s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.1285s | 0.1263s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0881s | 0.0798s | +0.0083s | worse |
| `lteNRRCC` | 0.1346s | 0.1307s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.92 MB | 8.78 MB | 169.5% | 95.9% |
| `f1ap_rel18.6_specs` | 10.05 MB | 10.05 MB | 83.9% | 165.9% |
| `ngap_rel18.6_specs` | 9.40 MB | 10.49 MB | 164.5% | 235.7% |
| `lteNRRCC` | 8.61 MB | 8.73 MB | 82.8% | 166.2% |
<!-- BENCH_RESULTS_END -->
