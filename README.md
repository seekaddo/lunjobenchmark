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
Generated: 2026-05-21T23:08:45.554690+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0364s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1150s | 0.1139s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0786s | -0.0015s | improved |
| `lteNRRCC` | 0.1213s | 0.1219s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 12.8% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 106.7% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0347s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0959s | 0.0926s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0636s | 0.0651s | -0.0015s | improved |
| `lteNRRCC` | 0.1217s | 0.1268s | -0.0051s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.50 MB | 89.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.25 MB | 103.22 MB | 112.1% | 105.3% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.59 MB | 111.1% | 107.0% |
| `lteNRRCC` | 48.77 MB | 66.09 MB | 104.8% | 105.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0335s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0873s | 0.0888s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0617s | 0.0625s | -0.0008s | improved |
| `lteNRRCC` | 0.1157s | 0.1154s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.84 MB | 52.4% | 111.1% |
| `f1ap_rel18.6_specs` | 34.67 MB | 164.67 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.19 MB | 117.65 MB | 108.0% | 104.8% |
| `lteNRRCC` | 74.96 MB | 102.95 MB | 105.3% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0236s | 0.0269s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.0625s | 0.0810s | -0.0185s | improved |
| `ngap_rel18.6_specs` | 0.0451s | 0.0507s | -0.0056s | improved |
| `lteNRRCC` | 0.0689s | 0.0839s | -0.0150s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.48 MB | 3.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 4.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.42 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.94 MB | 4.44 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0329s | +0.0077s | worse |
| `f1ap_rel18.6_specs` | 0.1078s | 0.0909s | +0.0169s | worse |
| `ngap_rel18.6_specs` | 0.0814s | 0.0636s | +0.0178s | worse |
| `lteNRRCC` | 0.1279s | 0.1110s | +0.0169s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.96 MB | 7.82 MB | 232.8% | 81.3% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.43 MB | 82.4% | 166.4% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.07 MB | 172.5% | 170.7% |
| `lteNRRCC` | 8.16 MB | 69.10 MB | 91.5% | 158.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0428s | 0.0399s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.1280s | 0.1091s | +0.0189s | worse |
| `ngap_rel18.6_specs` | 0.0885s | 0.0764s | +0.0121s | worse |
| `lteNRRCC` | 0.1344s | 0.1292s | +0.0052s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.64 MB | 9.76 MB | 138.7% | 159.1% |
| `f1ap_rel18.6_specs` | 10.29 MB | 10.29 MB | 164.3% | 80.4% |
| `ngap_rel18.6_specs` | 10.07 MB | 9.40 MB | 172.8% | 177.1% |
| `lteNRRCC` | 10.98 MB | 99.01 MB | 85.1% | 116.8% |
<!-- BENCH_RESULTS_END -->
