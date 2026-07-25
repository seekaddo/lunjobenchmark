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
Generated: 2026-07-25T23:00:05.826000+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0362s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1149s | -0.0064s | improved |
| `ngap_rel18.6_specs` | 0.0749s | 0.0771s | -0.0022s | improved |
| `lteNRRCC` | 0.1190s | 0.1213s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 15.8% | 107.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 100.0% | 100.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0361s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0971s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0682s | -0.0024s | improved |
| `lteNRRCC` | 0.1261s | 0.1312s | -0.0051s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 36.71 MB | 75.0% | 107.4% |
| `f1ap_rel18.6_specs` | 22.31 MB | 103.48 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.62 MB | 73.88 MB | 103.8% | 104.7% |
| `lteNRRCC` | 48.36 MB | 65.89 MB | 103.3% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0337s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0896s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0642s | 0.0628s | +0.0014s | worse |
| `lteNRRCC` | 0.1178s | 0.1187s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.34 MB | 55.50 MB | 72.4% | 107.4% |
| `f1ap_rel18.6_specs` | 35.14 MB | 164.61 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.79 MB | 108.3% | 102.4% |
| `lteNRRCC` | 74.81 MB | 102.85 MB | 101.8% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0221s | 0.0201s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0664s | 0.0660s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0463s | 0.0451s | +0.0012s | worse |
| `lteNRRCC` | 0.0757s | 0.0700s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.78 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.06 MB | 4.66 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.42 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.45 MB | 5.06 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0333s | +0.0061s | worse |
| `f1ap_rel18.6_specs` | 0.1083s | 0.0928s | +0.0155s | worse |
| `ngap_rel18.6_specs` | 0.0749s | 0.0639s | +0.0110s | worse |
| `lteNRRCC` | 0.1382s | 0.1122s | +0.0260s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.67 MB | 7.35 MB | 0.0% | 89.9% |
| `f1ap_rel18.6_specs` | 8.91 MB | 8.66 MB | 106.3% | 217.2% |
| `ngap_rel18.6_specs` | 7.50 MB | 7.67 MB | 80.4% | 159.9% |
| `lteNRRCC` | 51.83 MB | 70.55 MB | 106.8% | 157.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0406s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1155s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0803s | 0.0799s | +0.0004s | worse |
| `lteNRRCC` | 0.1296s | 0.1313s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.91 MB | 10.91 MB | 106.8% | 219.1% |
| `f1ap_rel18.6_specs` | 9.93 MB | 164.19 MB | 149.3% | 148.2% |
| `ngap_rel18.6_specs` | 10.40 MB | 9.27 MB | 96.8% | 151.0% |
| `lteNRRCC` | 8.81 MB | 74.13 MB | 148.3% | 146.2% |
<!-- BENCH_RESULTS_END -->
