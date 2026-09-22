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
Generated: 2026-09-22T00:41:39.195846+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0354s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1089s | 0.1115s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0757s | 0.0755s | +0.0002s | worse |
| `lteNRRCC` | 0.1196s | 0.1221s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.75 MB | 53.55 MB | 85.7% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0372s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0998s | -0.0045s | improved |
| `ngap_rel18.6_specs` | 0.0689s | 0.0698s | -0.0009s | improved |
| `lteNRRCC` | 0.1291s | 0.1336s | -0.0045s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.51 MB | 75.0% | 107.4% |
| `f1ap_rel18.6_specs` | 22.41 MB | 103.20 MB | 103.1% | 103.5% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.66 MB | 103.8% | 104.4% |
| `lteNRRCC` | 48.81 MB | 66.51 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0270s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.0898s | 0.0875s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0622s | 0.0614s | +0.0008s | worse |
| `lteNRRCC` | 0.1180s | 0.1056s | +0.0124s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.39 MB | 79.2% | 103.8% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.37 MB | 107.1% | 103.7% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.66 MB | 108.7% | 102.5% |
| `lteNRRCC` | 75.03 MB | 102.18 MB | 101.8% | 102.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0345s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0858s | 0.1225s | -0.0367s | improved |
| `ngap_rel18.6_specs` | 0.0916s | 0.1042s | -0.0126s | improved |
| `lteNRRCC` | 0.1053s | 0.1231s | -0.0178s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.62 MB | 8.69 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.44 MB | 7.23 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.66 MB | 7.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.23 MB | 6.58 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0412s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1069s | 0.1118s | -0.0049s | improved |
| `ngap_rel18.6_specs` | 0.0737s | 0.0785s | -0.0048s | improved |
| `lteNRRCC` | 0.1375s | 0.1410s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.72 MB | 7.34 MB | 0.0% | 179.4% |
| `f1ap_rel18.6_specs` | 8.14 MB | 8.01 MB | 136.4% | 162.5% |
| `ngap_rel18.6_specs` | 7.59 MB | 7.59 MB | 159.5% | 159.0% |
| `lteNRRCC` | 51.37 MB | 51.68 MB | 157.4% | 159.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0308s | 0.0390s | -0.0082s | improved |
| `f1ap_rel18.6_specs` | 0.0858s | 0.1139s | -0.0281s | improved |
| `ngap_rel18.6_specs` | 0.0589s | 0.0777s | -0.0188s | improved |
| `lteNRRCC` | 0.0894s | 0.1292s | -0.0398s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 44.94 MB | 0.0% | 129.9% |
| `f1ap_rel18.6_specs` | 28.12 MB | 12.92 MB | 132.7% | 140.2% |
| `ngap_rel18.6_specs` | 19.66 MB | 31.30 MB | 86.3% | 121.1% |
| `lteNRRCC` | 18.41 MB | 23.78 MB | 87.8% | 139.8% |
<!-- BENCH_RESULTS_END -->
