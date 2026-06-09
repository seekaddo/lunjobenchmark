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
Generated: 2026-06-09T12:43:32.309030+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0352s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1107s | 0.1075s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0734s | +0.0023s | worse |
| `lteNRRCC` | 0.1195s | 0.1186s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 18.8% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0347s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0949s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0672s | -0.0018s | improved |
| `lteNRRCC` | 0.1238s | 0.1295s | -0.0057s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 36.18 MB | 96.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.34 MB | 103.19 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.42 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.59 MB | 66.43 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0354s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0928s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0676s | 0.0657s | +0.0019s | worse |
| `lteNRRCC` | 0.1296s | 0.1278s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.33 MB | 55.55 MB | 86.2% | 110.0% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.55 MB | 109.4% | 105.0% |
| `ngap_rel18.6_specs` | 24.14 MB | 117.24 MB | 111.1% | 106.7% |
| `lteNRRCC` | 73.97 MB | 102.43 MB | 104.6% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0319s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.1091s | 0.0830s | +0.0261s | worse |
| `ngap_rel18.6_specs` | 0.0656s | 0.0641s | +0.0015s | worse |
| `lteNRRCC` | 0.1040s | 0.1061s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.75 MB | 10.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 12.50 MB | 8.66 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.25 MB | 6.86 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.36 MB | 6.67 MB | 0.0% | 2.8% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0395s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1074s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0758s | 0.0755s | +0.0003s | worse |
| `lteNRRCC` | 0.1409s | 0.1377s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.56 MB | 7.50 MB | 79.2% | 157.2% |
| `f1ap_rel18.6_specs` | 8.54 MB | 106.64 MB | 98.8% | 107.4% |
| `ngap_rel18.6_specs` | 8.17 MB | 7.99 MB | 220.1% | 153.9% |
| `lteNRRCC` | 8.35 MB | 57.70 MB | 75.4% | 155.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0409s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1207s | 0.1180s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0825s | 0.0837s | -0.0012s | improved |
| `lteNRRCC` | 0.1461s | 0.1362s | +0.0099s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.07 MB | 9.65 MB | 162.1% | 97.2% |
| `f1ap_rel18.6_specs` | 9.80 MB | 151.48 MB | 174.6% | 110.6% |
| `ngap_rel18.6_specs` | 9.55 MB | 10.75 MB | 196.4% | 107.1% |
| `lteNRRCC` | 73.27 MB | 99.77 MB | 106.3% | 108.8% |
<!-- BENCH_RESULTS_END -->
