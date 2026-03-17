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
Generated: 2026-03-17T10:58:43.022615+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0390s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1199s | 0.1235s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0829s | 0.0848s | -0.0019s | improved |
| `lteNRRCC` | 0.1208s | 0.1251s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.53 MB | 55.78 MB | 105.6% | 107.1% |
| `f1ap_rel18.6_specs` | 32.53 MB | 176.91 MB | 107.1% | 102.9% |
| `ngap_rel18.6_specs` | 22.41 MB | 125.78 MB | 108.7% | 103.9% |
| `lteNRRCC` | 72.32 MB | 100.09 MB | 103.5% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0333s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.0987s | 0.0975s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0711s | 0.0674s | +0.0037s | worse |
| `lteNRRCC` | 0.1308s | 0.1164s | +0.0144s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.28 MB | 37.47 MB | 92.6% | 110.0% |
| `f1ap_rel18.6_specs` | 22.29 MB | 111.80 MB | 108.8% | 104.9% |
| `ngap_rel18.6_specs` | 16.84 MB | 80.41 MB | 114.3% | 106.5% |
| `lteNRRCC` | 48.41 MB | 66.34 MB | 106.0% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0355s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1014s | 0.0923s | +0.0091s | worse |
| `ngap_rel18.6_specs` | 0.0706s | 0.0659s | +0.0047s | worse |
| `lteNRRCC` | 0.1137s | 0.1144s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.56 MB | 57.00 MB | 90.5% | 107.7% |
| `f1ap_rel18.6_specs` | 34.12 MB | 178.82 MB | 107.4% | 103.3% |
| `ngap_rel18.6_specs` | 23.66 MB | 128.02 MB | 109.1% | 104.4% |
| `lteNRRCC` | 74.75 MB | 102.80 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0202s | 0.0200s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0642s | 0.0719s | -0.0077s | improved |
| `ngap_rel18.6_specs` | 0.0427s | 0.0424s | +0.0003s | worse |
| `lteNRRCC` | 0.0723s | 0.0717s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.34 MB | 3.84 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 3.77 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.89 MB | 4.33 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.88 MB | 3.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0406s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1114s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0795s | 0.0782s | +0.0013s | worse |
| `lteNRRCC` | 0.1267s | 0.1266s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.02 MB | 7.42 MB | 80.0% | 230.4% |
| `f1ap_rel18.6_specs` | 8.42 MB | 8.68 MB | 160.1% | 81.0% |
| `ngap_rel18.6_specs` | 8.04 MB | 8.29 MB | 79.8% | 159.9% |
| `lteNRRCC` | 8.24 MB | 8.43 MB | 150.4% | 80.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0393s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1180s | 0.1203s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0819s | 0.0800s | +0.0019s | worse |
| `lteNRRCC` | 0.1265s | 0.1268s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.94 MB | 11.06 MB | 98.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.79 MB | 179.18 MB | 159.4% | 232.0% |
| `ngap_rel18.6_specs` | 8.71 MB | 9.21 MB | 81.0% | 157.4% |
| `lteNRRCC` | 8.55 MB | 96.18 MB | 155.3% | 105.3% |
<!-- BENCH_RESULTS_END -->
