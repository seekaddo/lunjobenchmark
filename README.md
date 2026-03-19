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
Generated: 2026-03-19T22:37:25.882964+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0368s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1171s | -0.0054s | improved |
| `ngap_rel18.6_specs` | 0.0774s | 0.0816s | -0.0042s | improved |
| `lteNRRCC` | 0.1206s | 0.1255s | -0.0049s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 105.9% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.3% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0367s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0948s | 0.0994s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.0664s | 0.0698s | -0.0034s | improved |
| `lteNRRCC` | 0.1300s | 0.1339s | -0.0039s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 36.53 MB | 26.9% | 113.8% |
| `f1ap_rel18.6_specs` | 21.50 MB | 103.23 MB | 108.8% | 105.1% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.07 MB | 114.3% | 108.9% |
| `lteNRRCC` | 48.27 MB | 66.19 MB | 106.1% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0346s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0892s | 0.0899s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0629s | 0.0630s | -0.0001s | improved |
| `lteNRRCC` | 0.1173s | 0.1165s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.46 MB | 55.69 MB | 92.3% | 110.3% |
| `f1ap_rel18.6_specs` | 35.11 MB | 164.63 MB | 109.7% | 105.3% |
| `ngap_rel18.6_specs` | 24.47 MB | 117.80 MB | 111.5% | 109.3% |
| `lteNRRCC` | 74.78 MB | 102.73 MB | 106.8% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0288s | 0.0249s | +0.0039s | worse |
| `f1ap_rel18.6_specs` | 0.0988s | 0.0777s | +0.0211s | worse |
| `ngap_rel18.6_specs` | 0.0693s | 0.0494s | +0.0199s | worse |
| `lteNRRCC` | 0.1026s | 0.0989s | +0.0037s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.69 MB | 8.27 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.62 MB | 6.89 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 464 KB | 1.91 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.67 MB | 4.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0395s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1057s | 0.1085s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0736s | 0.0763s | -0.0027s | improved |
| `lteNRRCC` | 0.1372s | 0.1381s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.45 MB | 7.32 MB | 80.4% | 82.4% |
| `f1ap_rel18.6_specs` | 8.44 MB | 7.95 MB | 157.2% | 81.9% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.62 MB | 161.6% | 83.0% |
| `lteNRRCC` | 46.82 MB | 52.00 MB | 105.1% | 107.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0394s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1164s | 0.1147s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0783s | 0.0794s | -0.0011s | improved |
| `lteNRRCC` | 0.1287s | 0.1281s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.78 MB | 9.08 MB | 100.7% | 86.2% |
| `f1ap_rel18.6_specs` | 11.59 MB | 9.72 MB | 215.0% | 80.4% |
| `ngap_rel18.6_specs` | 9.13 MB | 10.11 MB | 76.2% | 157.6% |
| `lteNRRCC` | 8.58 MB | 101.68 MB | 151.4% | 108.3% |
<!-- BENCH_RESULTS_END -->
