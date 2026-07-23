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
Generated: 2026-07-23T23:03:22.770506+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0365s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1128s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0778s | 0.0773s | +0.0005s | worse |
| `lteNRRCC` | 0.1226s | 0.1207s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 76.0% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0269s | +0.0079s | worse |
| `f1ap_rel18.6_specs` | 0.0949s | 0.0738s | +0.0211s | worse |
| `ngap_rel18.6_specs` | 0.0670s | 0.0516s | +0.0154s | worse |
| `lteNRRCC` | 0.1296s | 0.0970s | +0.0326s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.53 MB | 36.72 MB | 82.1% | 107.1% |
| `f1ap_rel18.6_specs` | 22.22 MB | 103.43 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.70 MB | 111.5% | 104.5% |
| `lteNRRCC` | 48.80 MB | 66.07 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0397s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.0903s | 0.0978s | -0.0075s | improved |
| `ngap_rel18.6_specs` | 0.0626s | 0.0632s | -0.0006s | improved |
| `lteNRRCC` | 0.1158s | 0.1208s | -0.0050s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.50 MB | 55.76 MB | 85.2% | 111.1% |
| `f1ap_rel18.6_specs` | 35.25 MB | 164.22 MB | 106.9% | 105.6% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.49 MB | 115.4% | 104.3% |
| `lteNRRCC` | 74.95 MB | 102.39 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0226s | +0.0190s | worse |
| `f1ap_rel18.6_specs` | 0.1023s | 0.0715s | +0.0308s | worse |
| `ngap_rel18.6_specs` | 0.0812s | 0.0502s | +0.0310s | worse |
| `lteNRRCC` | 0.0926s | 0.0772s | +0.0154s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.12 MB | 960 KB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.17 MB | 5.69 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.58 MB | 2.55 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.50 MB | 5.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0391s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1097s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0757s | +0.0043s | worse |
| `lteNRRCC` | 0.1409s | 0.1392s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.11 MB | 8.04 MB | 159.5% | 154.5% |
| `f1ap_rel18.6_specs` | 9.10 MB | 8.66 MB | 152.5% | 160.3% |
| `ngap_rel18.6_specs` | 8.48 MB | 8.55 MB | 102.7% | 153.1% |
| `lteNRRCC` | 51.26 MB | 51.89 MB | 202.6% | 155.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0392s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1159s | -0.0084s | improved |
| `ngap_rel18.6_specs` | 0.0727s | 0.0828s | -0.0101s | improved |
| `lteNRRCC` | 0.1139s | 0.1266s | -0.0127s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.73 MB | 10.42 MB | 204.1% | 128.2% |
| `f1ap_rel18.6_specs` | 11.16 MB | 164.13 MB | 135.2% | 203.1% |
| `ngap_rel18.6_specs` | 10.83 MB | 10.21 MB | 133.0% | 139.2% |
| `lteNRRCC` | 8.93 MB | 77.77 MB | 97.7% | 198.2% |
<!-- BENCH_RESULTS_END -->
