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
Generated: 2026-05-22T12:27:35.880314+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0371s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1151s | 0.1150s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0794s | 0.0771s | +0.0023s | worse |
| `lteNRRCC` | 0.1243s | 0.1213s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 26.4% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.1% | 105.6% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.9% | 103.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0331s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0959s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0664s | 0.0636s | +0.0028s | worse |
| `lteNRRCC` | 0.1294s | 0.1217s | +0.0077s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.07 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.38 MB | 109.1% | 106.8% |
| `ngap_rel18.6_specs` | 17.69 MB | 74.45 MB | 111.1% | 104.5% |
| `lteNRRCC` | 48.80 MB | 66.20 MB | 106.2% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0334s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.1003s | 0.0873s | +0.0130s | worse |
| `ngap_rel18.6_specs` | 0.0701s | 0.0617s | +0.0084s | worse |
| `lteNRRCC` | 0.1177s | 0.1157s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.75 MB | 55.59 MB | 79.2% | 107.4% |
| `f1ap_rel18.6_specs` | 35.19 MB | 164.72 MB | 107.1% | 105.1% |
| `ngap_rel18.6_specs` | 24.27 MB | 117.23 MB | 109.1% | 104.5% |
| `lteNRRCC` | 74.11 MB | 102.53 MB | 103.6% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0236s | +0.0130s | worse |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0625s | +0.0325s | worse |
| `ngap_rel18.6_specs` | 0.0712s | 0.0451s | +0.0261s | worse |
| `lteNRRCC` | 0.1085s | 0.0689s | +0.0396s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.73 MB | 2.55 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.53 MB | 4.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.80 MB | 1.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.53 MB | 160 KB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0406s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1078s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0814s | -0.0041s | improved |
| `lteNRRCC` | 0.1388s | 0.1279s | +0.0109s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.98 MB | 7.97 MB | 101.1% | 93.6% |
| `f1ap_rel18.6_specs` | 8.80 MB | 8.55 MB | 93.6% | 166.9% |
| `ngap_rel18.6_specs` | 8.30 MB | 8.24 MB | 106.2% | 82.1% |
| `lteNRRCC` | 47.39 MB | 69.23 MB | 111.8% | 109.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0428s | 0.0428s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1201s | 0.1280s | -0.0079s | improved |
| `ngap_rel18.6_specs` | 0.0828s | 0.0885s | -0.0057s | improved |
| `lteNRRCC` | 0.1379s | 0.1344s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.02 MB | 10.55 MB | 155.5% | 150.6% |
| `f1ap_rel18.6_specs` | 11.07 MB | 164.13 MB | 147.3% | 108.2% |
| `ngap_rel18.6_specs` | 10.10 MB | 10.37 MB | 154.5% | 152.2% |
| `lteNRRCC` | 72.76 MB | 101.70 MB | 154.7% | 109.1% |
<!-- BENCH_RESULTS_END -->
