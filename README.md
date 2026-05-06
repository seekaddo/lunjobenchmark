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
Generated: 2026-05-06T11:54:46.157897+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0370s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1142s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0757s | 0.0776s | -0.0019s | improved |
| `lteNRRCC` | 0.1193s | 0.1221s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 7.7% | 113.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 106.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.3% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0368s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0945s | 0.0992s | -0.0047s | improved |
| `ngap_rel18.6_specs` | 0.0670s | 0.0694s | -0.0024s | improved |
| `lteNRRCC` | 0.1304s | 0.1335s | -0.0031s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 36.43 MB | 100.0% | 114.3% |
| `f1ap_rel18.6_specs` | 21.94 MB | 103.26 MB | 106.1% | 103.4% |
| `ngap_rel18.6_specs` | 16.68 MB | 74.64 MB | 111.1% | 109.1% |
| `lteNRRCC` | 48.67 MB | 66.48 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0342s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0877s | 0.0990s | -0.0113s | improved |
| `ngap_rel18.6_specs` | 0.0616s | 0.0674s | -0.0058s | improved |
| `lteNRRCC` | 0.1144s | 0.1162s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.76 MB | 95.8% | 107.4% |
| `f1ap_rel18.6_specs` | 34.47 MB | 164.55 MB | 106.9% | 105.5% |
| `ngap_rel18.6_specs` | 23.89 MB | 117.18 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.90 MB | 102.85 MB | 103.4% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0205s | 0.0193s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0735s | 0.0600s | +0.0135s | worse |
| `ngap_rel18.6_specs` | 0.0515s | 0.0401s | +0.0114s | worse |
| `lteNRRCC` | 0.0854s | 0.0766s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.58 MB | 4.55 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.62 MB | 4.30 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.41 MB | 4.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.72 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0402s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1074s | 0.1068s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0747s | 0.0796s | -0.0049s | improved |
| `lteNRRCC` | 0.1358s | 0.1375s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.38 MB | 7.36 MB | 165.9% | 92.8% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.04 MB | 163.8% | 164.1% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.68 MB | 81.7% | 164.1% |
| `lteNRRCC` | 45.51 MB | 51.96 MB | 160.8% | 106.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0426s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.1154s | 0.1370s | -0.0216s | improved |
| `ngap_rel18.6_specs` | 0.0808s | 0.0898s | -0.0090s | improved |
| `lteNRRCC` | 0.1307s | 0.1369s | -0.0062s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.78 MB | 9.39 MB | 109.6% | 101.5% |
| `f1ap_rel18.6_specs` | 9.48 MB | 10.43 MB | 159.8% | 97.8% |
| `ngap_rel18.6_specs` | 8.96 MB | 9.14 MB | 159.5% | 76.9% |
| `lteNRRCC` | 73.34 MB | 84.39 MB | 157.4% | 106.1% |
<!-- BENCH_RESULTS_END -->
