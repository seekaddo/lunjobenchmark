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
Generated: 2026-07-26T11:24:04.265254+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0343s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1085s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0749s | +0.0021s | worse |
| `lteNRRCC` | 0.1219s | 0.1190s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 86.4% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0347s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0934s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0658s | +0.0000s | flat |
| `lteNRRCC` | 0.1273s | 0.1261s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 36.68 MB | 76.9% | 107.7% |
| `f1ap_rel18.6_specs` | 22.14 MB | 103.21 MB | 103.2% | 101.6% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.18 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.46 MB | 66.41 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0289s | 0.0401s | -0.0112s | improved |
| `f1ap_rel18.6_specs` | 0.0781s | 0.0925s | -0.0144s | improved |
| `ngap_rel18.6_specs` | 0.0539s | 0.0642s | -0.0103s | improved |
| `lteNRRCC` | 0.1033s | 0.1178s | -0.0145s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.20 MB | 55.51 MB | 78.3% | 104.5% |
| `f1ap_rel18.6_specs` | 34.21 MB | 164.61 MB | 104.2% | 102.1% |
| `ngap_rel18.6_specs` | 24.43 MB | 117.50 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.98 MB | 102.36 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0239s | 0.0221s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.0677s | 0.0664s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0459s | 0.0463s | -0.0004s | improved |
| `lteNRRCC` | 0.0764s | 0.0757s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.12 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.59 MB | 4.55 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.06 MB | 4.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.17 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0394s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1058s | 0.1083s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0780s | 0.0749s | +0.0031s | worse |
| `lteNRRCC` | 0.1366s | 0.1382s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.85 MB | 7.50 MB | 234.4% | 111.6% |
| `f1ap_rel18.6_specs` | 7.97 MB | 8.03 MB | 164.9% | 166.5% |
| `ngap_rel18.6_specs` | 8.23 MB | 7.55 MB | 151.2% | 82.3% |
| `lteNRRCC` | 45.69 MB | 53.07 MB | 163.6% | 117.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0401s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1128s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0803s | -0.0037s | improved |
| `lteNRRCC` | 0.1308s | 0.1296s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.52 MB | 11.04 MB | 171.1% | 208.2% |
| `f1ap_rel18.6_specs` | 10.93 MB | 151.48 MB | 89.3% | 106.1% |
| `ngap_rel18.6_specs` | 9.09 MB | 9.09 MB | 82.1% | 157.5% |
| `lteNRRCC` | 73.78 MB | 82.22 MB | 155.9% | 103.7% |
<!-- BENCH_RESULTS_END -->
