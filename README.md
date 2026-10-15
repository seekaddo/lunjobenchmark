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
Generated: 2026-10-15T00:23:13.933475+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0384s | -0.0037s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1183s | -0.0077s | improved |
| `ngap_rel18.6_specs` | 0.0759s | 0.0803s | -0.0044s | improved |
| `lteNRRCC` | 0.1186s | 0.1241s | -0.0055s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 75.0% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0344s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0997s | -0.0058s | improved |
| `ngap_rel18.6_specs` | 0.0656s | 0.0704s | -0.0048s | improved |
| `lteNRRCC` | 0.1294s | 0.1211s | +0.0083s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.64 MB | 79.2% | 107.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.07 MB | 106.7% | 101.8% |
| `ngap_rel18.6_specs` | 18.05 MB | 74.45 MB | 104.0% | 102.4% |
| `lteNRRCC` | 47.80 MB | 66.50 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0341s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0908s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0636s | 0.0631s | +0.0005s | worse |
| `lteNRRCC` | 0.1165s | 0.1188s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.79 MB | 76.0% | 104.0% |
| `f1ap_rel18.6_specs` | 35.10 MB | 164.77 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 23.89 MB | 117.12 MB | 104.3% | 105.0% |
| `lteNRRCC` | 74.88 MB | 101.88 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0323s | 0.0321s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0989s | 0.1146s | -0.0157s | improved |
| `ngap_rel18.6_specs` | 0.0519s | 0.0725s | -0.0206s | improved |
| `lteNRRCC` | 0.1174s | 0.0857s | +0.0317s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.84 MB | 3.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.66 MB | 12.28 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.67 MB | 4.00 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.61 MB | 6.08 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0390s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1055s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0732s | +0.0034s | worse |
| `lteNRRCC` | 0.1380s | 0.1372s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.41 MB | 7.33 MB | 217.0% | 181.7% |
| `f1ap_rel18.6_specs` | 8.08 MB | 8.01 MB | 166.0% | 158.2% |
| `ngap_rel18.6_specs` | 7.64 MB | 7.52 MB | 81.5% | 164.1% |
| `lteNRRCC` | 8.51 MB | 51.97 MB | 230.7% | 159.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0402s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1120s | 0.1117s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0774s | 0.0794s | -0.0020s | improved |
| `lteNRRCC` | 0.1275s | 0.1353s | -0.0078s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.13 MB | 9.53 MB | 0.0% | 99.2% |
| `f1ap_rel18.6_specs` | 11.30 MB | 164.16 MB | 115.6% | 176.8% |
| `ngap_rel18.6_specs` | 10.79 MB | 9.11 MB | 232.7% | 90.0% |
| `lteNRRCC` | 8.66 MB | 99.05 MB | 153.5% | 107.4% |
<!-- BENCH_RESULTS_END -->
