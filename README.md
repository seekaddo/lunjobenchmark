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
Generated: 2026-11-05T17:56:17.792360+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0400s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1256s | 0.1223s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0872s | 0.0865s | +0.0007s | worse |
| `lteNRRCC` | 0.1296s | 0.1271s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.75 MB | 53.55 MB | 91.3% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.6% |
| `lteNRRCC` | 72.38 MB | 100.18 MB | 103.2% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0460s | -0.0073s | improved |
| `f1ap_rel18.6_specs` | 0.1169s | 0.1405s | -0.0236s | improved |
| `ngap_rel18.6_specs` | 0.0824s | 0.0962s | -0.0138s | improved |
| `lteNRRCC` | 0.1320s | 0.1555s | -0.0235s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.75 MB | 34.65 MB | 69.2% | 103.6% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 103.3% | 103.0% |
| `ngap_rel18.6_specs` | 18.03 MB | 72.65 MB | 104.3% | 104.1% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 103.3% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0548s | -0.0157s | improved |
| `f1ap_rel18.6_specs` | 0.1200s | 0.1685s | -0.0485s | improved |
| `ngap_rel18.6_specs` | 0.0816s | 0.1149s | -0.0333s | improved |
| `lteNRRCC` | 0.1040s | 0.1622s | -0.0582s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.81 MB | 53.73 MB | 75.0% | 103.8% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 104.2% | 103.0% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 110.5% | 102.2% |
| `lteNRRCC` | 72.56 MB | 100.36 MB | 102.1% | 101.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0485s | -0.0084s | improved |
| `f1ap_rel18.6_specs` | 0.0882s | 0.0750s | +0.0132s | worse |
| `ngap_rel18.6_specs` | 0.0514s | 0.0463s | +0.0051s | worse |
| `lteNRRCC` | 0.0987s | 0.0851s | +0.0136s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.75 MB | 7.88 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.03 MB | 9.20 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.61 MB | 8.62 MB | 0.0% | 0.3% |
| `lteNRRCC` | 7.61 MB | 3.83 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0395s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.0940s | 0.1080s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0767s | -0.0106s | improved |
| `lteNRRCC` | 0.1189s | 0.1377s | -0.0188s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.51 MB | 0.0% | 264.2% |
| `f1ap_rel18.6_specs` | 8.99 MB | 8.86 MB | 133.4% | 133.8% |
| `ngap_rel18.6_specs` | 8.69 MB | 9.12 MB | 233.0% | 122.3% |
| `lteNRRCC` | 51.84 MB | 53.02 MB | 135.7% | 131.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0423s | -0.0078s | improved |
| `f1ap_rel18.6_specs` | 0.1065s | 0.1196s | -0.0131s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0846s | -0.0103s | improved |
| `lteNRRCC` | 0.1149s | 0.1385s | -0.0236s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.66 MB | 0.0% | 112.7% |
| `f1ap_rel18.6_specs` | 11.80 MB | 151.67 MB | 128.4% | 115.3% |
| `ngap_rel18.6_specs` | 9.56 MB | 9.92 MB | 97.1% | 137.6% |
| `lteNRRCC` | 73.77 MB | 87.52 MB | 207.4% | 197.8% |
<!-- BENCH_RESULTS_END -->
