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
Generated: 2026-07-15T11:40:41.389603+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0356s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1126s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0772s | 0.0777s | -0.0005s | improved |
| `lteNRRCC` | 0.1212s | 0.1215s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.79 MB | 53.55 MB | 7.9% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0340s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0923s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0670s | 0.0659s | +0.0011s | worse |
| `lteNRRCC` | 0.1252s | 0.1276s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 36.57 MB | 76.7% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.29 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.56 MB | 115.4% | 106.8% |
| `lteNRRCC` | 48.33 MB | 66.45 MB | 104.8% | 105.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0346s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0943s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0634s | 0.0666s | -0.0032s | improved |
| `lteNRRCC` | 0.1176s | 0.1204s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 55.62 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 34.78 MB | 164.40 MB | 110.3% | 107.1% |
| `ngap_rel18.6_specs` | 24.38 MB | 117.73 MB | 108.0% | 106.8% |
| `lteNRRCC` | 74.45 MB | 102.82 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0236s | 0.0235s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0787s | 0.0854s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0519s | 0.0563s | -0.0044s | improved |
| `lteNRRCC` | 0.0719s | 0.1242s | -0.0523s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.16 MB | 8.05 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.97 MB | 8.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.66 MB | 8.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.70 MB | 8.28 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0389s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1133s | 0.1068s | +0.0065s | worse |
| `ngap_rel18.6_specs` | 0.0779s | 0.0736s | +0.0043s | worse |
| `lteNRRCC` | 0.1393s | 0.1403s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.82 MB | 7.75 MB | 80.6% | 166.2% |
| `f1ap_rel18.6_specs` | 8.18 MB | 8.55 MB | 105.7% | 167.8% |
| `ngap_rel18.6_specs` | 7.99 MB | 8.06 MB | 165.2% | 84.0% |
| `lteNRRCC` | 47.32 MB | 49.77 MB | 164.0% | 107.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0354s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.1124s | 0.1055s | +0.0069s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0701s | +0.0066s | worse |
| `lteNRRCC` | 0.1269s | 0.1129s | +0.0140s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.65 MB | 8.72 MB | 181.5% | 158.9% |
| `f1ap_rel18.6_specs` | 11.27 MB | 9.68 MB | 110.9% | 159.1% |
| `ngap_rel18.6_specs` | 9.21 MB | 8.96 MB | 78.1% | 159.9% |
| `lteNRRCC` | 8.43 MB | 84.48 MB | 88.9% | 112.1% |
<!-- BENCH_RESULTS_END -->
