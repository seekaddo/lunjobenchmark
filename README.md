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
Generated: 2026-08-26T10:41:07.487452+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0362s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1127s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0744s | 0.0785s | -0.0041s | improved |
| `lteNRRCC` | 0.1194s | 0.1220s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 8.0% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0336s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0974s | 0.0911s | +0.0063s | worse |
| `ngap_rel18.6_specs` | 0.0687s | 0.0641s | +0.0046s | worse |
| `lteNRRCC` | 0.1199s | 0.1222s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 36.71 MB | 81.8% | 104.0% |
| `f1ap_rel18.6_specs` | 22.34 MB | 102.61 MB | 103.6% | 101.7% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.55 MB | 104.5% | 102.4% |
| `lteNRRCC` | 48.39 MB | 66.12 MB | 101.8% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0356s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0926s | 0.0928s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0649s | -0.0010s | improved |
| `lteNRRCC` | 0.1162s | 0.1272s | -0.0110s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.32 MB | 76.9% | 107.7% |
| `f1ap_rel18.6_specs` | 34.71 MB | 164.47 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.53 MB | 117.82 MB | 104.3% | 102.4% |
| `lteNRRCC` | 74.81 MB | 102.80 MB | 103.4% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0233s | 0.0333s | -0.0100s | improved |
| `f1ap_rel18.6_specs` | 0.0703s | 0.0937s | -0.0234s | improved |
| `ngap_rel18.6_specs` | 0.0482s | 0.0640s | -0.0158s | improved |
| `lteNRRCC` | 0.0787s | 0.1011s | -0.0224s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.44 MB | 4.38 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.58 MB | 4.58 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.44 MB | 4.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.09 MB | 4.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0421s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1182s | -0.0107s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0818s | -0.0063s | improved |
| `lteNRRCC` | 0.1425s | 0.1439s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.69 MB | 7.82 MB | 223.2% | 224.7% |
| `f1ap_rel18.6_specs` | 8.08 MB | 8.68 MB | 160.1% | 231.5% |
| `ngap_rel18.6_specs` | 7.65 MB | 7.91 MB | 156.6% | 94.5% |
| `lteNRRCC` | 48.56 MB | 69.23 MB | 106.3% | 153.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0427s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1148s | 0.1216s | -0.0068s | improved |
| `ngap_rel18.6_specs` | 0.0793s | 0.0840s | -0.0047s | improved |
| `lteNRRCC` | 0.1151s | 0.1245s | -0.0094s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.13 MB | 10.29 MB | 128.0% | 260.6% |
| `f1ap_rel18.6_specs` | 10.38 MB | 140.04 MB | 130.6% | 185.5% |
| `ngap_rel18.6_specs` | 9.59 MB | 9.82 MB | 92.0% | 189.2% |
| `lteNRRCC` | 8.94 MB | 72.73 MB | 130.3% | 129.2% |
<!-- BENCH_RESULTS_END -->
