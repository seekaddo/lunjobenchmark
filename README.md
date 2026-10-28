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
Generated: 2026-10-28T01:04:57.474305+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0348s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1104s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0750s | +0.0005s | worse |
| `lteNRRCC` | 0.1196s | 0.1214s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 12.2% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 100.0% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0248s | +0.0120s | worse |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0673s | +0.0278s | worse |
| `ngap_rel18.6_specs` | 0.0661s | 0.0466s | +0.0195s | worse |
| `lteNRRCC` | 0.1306s | 0.0808s | +0.0498s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 36.42 MB | 80.8% | 103.7% |
| `f1ap_rel18.6_specs` | 21.88 MB | 102.92 MB | 100.0% | 101.8% |
| `ngap_rel18.6_specs` | 17.91 MB | 74.54 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.55 MB | 66.30 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0326s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0926s | 0.0893s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0641s | 0.0629s | +0.0012s | worse |
| `lteNRRCC` | 0.1262s | 0.1160s | +0.0102s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.82 MB | 91.3% | 103.7% |
| `f1ap_rel18.6_specs` | 35.17 MB | 164.64 MB | 106.7% | 101.8% |
| `ngap_rel18.6_specs` | 24.35 MB | 117.31 MB | 104.0% | 102.4% |
| `lteNRRCC` | 74.65 MB | 102.69 MB | 103.2% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0357s | -0.0131s | improved |
| `f1ap_rel18.6_specs` | 0.0788s | 0.1213s | -0.0425s | improved |
| `ngap_rel18.6_specs` | 0.0489s | 0.0936s | -0.0447s | improved |
| `lteNRRCC` | 0.0763s | 0.1267s | -0.0504s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.80 MB | 4.02 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.95 MB | 4.11 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.97 MB | 4.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.83 MB | 4.22 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0330s | +0.0077s | worse |
| `f1ap_rel18.6_specs` | 0.1140s | 0.0928s | +0.0212s | worse |
| `ngap_rel18.6_specs` | 0.0784s | 0.0669s | +0.0115s | worse |
| `lteNRRCC` | 0.1404s | 0.1120s | +0.0284s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.13 MB | 7.51 MB | 209.0% | 77.1% |
| `f1ap_rel18.6_specs` | 8.39 MB | 106.66 MB | 77.8% | 159.6% |
| `ngap_rel18.6_specs` | 7.75 MB | 8.12 MB | 78.3% | 91.2% |
| `lteNRRCC` | 51.75 MB | 62.05 MB | 108.8% | 153.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0318s | +0.0061s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.0857s | +0.0253s | worse |
| `ngap_rel18.6_specs` | 0.0755s | 0.0604s | +0.0151s | worse |
| `lteNRRCC` | 0.1306s | 0.0905s | +0.0401s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.61 MB | 8.68 MB | 111.7% | 159.1% |
| `f1ap_rel18.6_specs` | 10.01 MB | 10.09 MB | 147.0% | 153.3% |
| `ngap_rel18.6_specs` | 9.57 MB | 9.04 MB | 157.6% | 180.5% |
| `lteNRRCC` | 9.25 MB | 73.54 MB | 101.8% | 153.5% |
<!-- BENCH_RESULTS_END -->
