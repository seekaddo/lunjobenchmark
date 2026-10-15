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
Generated: 2026-10-15T14:47:51.008703+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0347s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1106s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0759s | -0.0003s | improved |
| `lteNRRCC` | 0.1194s | 0.1186s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 85.7% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0345s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0939s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0656s | +0.0001s | worse |
| `lteNRRCC` | 0.1300s | 0.1294s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.63 MB | 36.53 MB | 76.9% | 107.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.54 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 18.01 MB | 73.92 MB | 104.0% | 102.4% |
| `lteNRRCC` | 48.80 MB | 65.29 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0340s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0912s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0639s | 0.0636s | +0.0003s | worse |
| `lteNRRCC` | 0.1201s | 0.1165s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.70 MB | 76.0% | 103.7% |
| `f1ap_rel18.6_specs` | 34.40 MB | 164.08 MB | 110.0% | 101.9% |
| `ngap_rel18.6_specs` | 24.10 MB | 116.89 MB | 104.3% | 105.0% |
| `lteNRRCC` | 74.98 MB | 102.68 MB | 101.7% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0320s | 0.0323s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0702s | 0.0989s | -0.0287s | improved |
| `ngap_rel18.6_specs` | 0.0565s | 0.0519s | +0.0046s | worse |
| `lteNRRCC` | 0.1081s | 0.1174s | -0.0093s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.69 MB | 8.11 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.55 MB | 3.80 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.41 MB | 3.56 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.31 MB | 6.97 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0400s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.1045s | 0.1099s | -0.0054s | improved |
| `ngap_rel18.6_specs` | 0.0722s | 0.0766s | -0.0044s | improved |
| `lteNRRCC` | 0.1109s | 0.1380s | -0.0271s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.31 MB | 8.37 MB | 0.0% | 258.6% |
| `f1ap_rel18.6_specs` | 8.70 MB | 8.76 MB | 134.6% | 127.6% |
| `ngap_rel18.6_specs` | 8.34 MB | 8.33 MB | 125.6% | 134.8% |
| `lteNRRCC` | 8.45 MB | 53.48 MB | 124.4% | 136.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0441s | 0.0376s | +0.0065s | worse |
| `f1ap_rel18.6_specs` | 0.1234s | 0.1120s | +0.0114s | worse |
| `ngap_rel18.6_specs` | 0.0869s | 0.0774s | +0.0095s | worse |
| `lteNRRCC` | 0.1357s | 0.1275s | +0.0082s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.13 MB | 9.53 MB | 0.0% | 146.5% |
| `f1ap_rel18.6_specs` | 10.00 MB | 10.48 MB | 148.9% | 144.2% |
| `ngap_rel18.6_specs` | 10.50 MB | 9.39 MB | 90.5% | 166.6% |
| `lteNRRCC` | 8.60 MB | 92.79 MB | 144.9% | 111.0% |
<!-- BENCH_RESULTS_END -->
