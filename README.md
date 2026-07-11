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
Generated: 2026-07-11T22:57:05.929990+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0356s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1121s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0776s | -0.0025s | improved |
| `lteNRRCC` | 0.1189s | 0.1215s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 22.4% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0322s | 0.0313s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0940s | 0.0922s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0642s | 0.0641s | +0.0001s | worse |
| `lteNRRCC` | 0.1170s | 0.1147s | +0.0023s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.56 MB | 35.64 MB | 78.3% | 108.3% |
| `f1ap_rel18.6_specs` | 21.90 MB | 103.45 MB | 107.4% | 101.8% |
| `ngap_rel18.6_specs` | 17.68 MB | 73.80 MB | 109.1% | 104.9% |
| `lteNRRCC` | 48.67 MB | 66.21 MB | 103.6% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0296s | +0.0063s | worse |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0765s | +0.0178s | worse |
| `ngap_rel18.6_specs` | 0.0672s | 0.0537s | +0.0135s | worse |
| `lteNRRCC` | 0.1220s | 0.1010s | +0.0210s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 55.74 MB | 82.8% | 106.9% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.51 MB | 110.0% | 105.2% |
| `ngap_rel18.6_specs` | 24.31 MB | 117.68 MB | 107.7% | 109.1% |
| `lteNRRCC` | 74.52 MB | 102.60 MB | 105.0% | 104.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0229s | 0.0255s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0671s | 0.0896s | -0.0225s | improved |
| `ngap_rel18.6_specs` | 0.0481s | 0.0651s | -0.0170s | improved |
| `lteNRRCC` | 0.0902s | 0.0757s | +0.0145s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.56 MB | 4.42 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.03 MB | 5.75 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.95 MB | 4.20 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.72 MB | 4.70 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0519s | 0.0401s | +0.0118s | worse |
| `f1ap_rel18.6_specs` | 0.1156s | 0.1077s | +0.0079s | worse |
| `ngap_rel18.6_specs` | 0.0808s | 0.0758s | +0.0050s | worse |
| `lteNRRCC` | 0.1445s | 0.1388s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.89 MB | 7.91 MB | 160.7% | 111.6% |
| `f1ap_rel18.6_specs` | 8.55 MB | 106.64 MB | 105.2% | 162.0% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.25 MB | 159.4% | 159.5% |
| `lteNRRCC` | 51.84 MB | 70.49 MB | 212.2% | 157.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0435s | 0.0411s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1285s | 0.1176s | +0.0109s | worse |
| `ngap_rel18.6_specs` | 0.0899s | 0.0812s | +0.0087s | worse |
| `lteNRRCC` | 0.1279s | 0.1367s | -0.0088s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.84 MB | 10.03 MB | 175.1% | 171.1% |
| `f1ap_rel18.6_specs` | 10.91 MB | 145.11 MB | 169.8% | 166.9% |
| `ngap_rel18.6_specs` | 10.25 MB | 10.50 MB | 177.7% | 118.7% |
| `lteNRRCC` | 73.27 MB | 99.64 MB | 120.3% | 166.8% |
<!-- BENCH_RESULTS_END -->
