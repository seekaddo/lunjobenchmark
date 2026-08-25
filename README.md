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
Generated: 2026-08-25T22:33:47.708714+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0372s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1141s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0785s | 0.0780s | +0.0005s | worse |
| `lteNRRCC` | 0.1220s | 0.1216s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 79.2% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0370s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.0911s | 0.0947s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0641s | 0.0659s | -0.0018s | improved |
| `lteNRRCC` | 0.1222s | 0.1288s | -0.0066s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.59 MB | 87.5% | 103.7% |
| `f1ap_rel18.6_specs` | 22.27 MB | 103.31 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.04 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.67 MB | 66.18 MB | 103.3% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0355s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0928s | 0.1018s | -0.0090s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0706s | -0.0057s | improved |
| `lteNRRCC` | 0.1272s | 0.1171s | +0.0101s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 55.42 MB | 84.0% | 107.4% |
| `f1ap_rel18.6_specs` | 35.23 MB | 164.57 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 23.53 MB | 117.25 MB | 108.0% | 104.8% |
| `lteNRRCC` | 75.02 MB | 102.84 MB | 101.6% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0262s | +0.0071s | worse |
| `f1ap_rel18.6_specs` | 0.0937s | 0.0942s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0548s | +0.0092s | worse |
| `lteNRRCC` | 0.1011s | 0.0978s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.56 MB | 4.30 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.94 MB | 7.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.52 MB | 7.23 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.06 MB | 1.58 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0410s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1182s | 0.1128s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0818s | 0.0776s | +0.0042s | worse |
| `lteNRRCC` | 0.1439s | 0.1397s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.69 MB | 7.97 MB | 97.4% | 110.5% |
| `f1ap_rel18.6_specs` | 8.92 MB | 106.64 MB | 211.1% | 108.0% |
| `ngap_rel18.6_specs` | 8.45 MB | 8.33 MB | 107.5% | 89.2% |
| `lteNRRCC` | 51.68 MB | 51.63 MB | 203.3% | 108.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0427s | 0.0399s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1216s | 0.1108s | +0.0108s | worse |
| `ngap_rel18.6_specs` | 0.0840s | 0.0779s | +0.0061s | worse |
| `lteNRRCC` | 0.1245s | 0.1282s | -0.0037s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.22 MB | 10.28 MB | 0.0% | 125.7% |
| `f1ap_rel18.6_specs` | 10.58 MB | 147.73 MB | 167.5% | 186.5% |
| `ngap_rel18.6_specs` | 9.56 MB | 10.37 MB | 85.1% | 173.1% |
| `lteNRRCC` | 9.18 MB | 101.72 MB | 117.2% | 110.5% |
<!-- BENCH_RESULTS_END -->
