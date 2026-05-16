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
Generated: 2026-05-16T22:55:19.389270+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0353s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1141s | 0.1103s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0795s | 0.0752s | +0.0043s | worse |
| `lteNRRCC` | 0.1216s | 0.1166s | +0.0050s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 29.6% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0322s | 0.0348s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0943s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0646s | 0.0687s | -0.0041s | improved |
| `lteNRRCC` | 0.1158s | 0.1271s | -0.0113s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.78 MB | 36.23 MB | 24.7% | 107.4% |
| `f1ap_rel18.6_specs` | 22.23 MB | 103.46 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 16.35 MB | 74.30 MB | 113.0% | 104.8% |
| `lteNRRCC` | 48.64 MB | 66.21 MB | 105.3% | 102.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0339s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0926s | 0.0879s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0652s | 0.0610s | +0.0042s | worse |
| `lteNRRCC` | 0.1272s | 0.1151s | +0.0121s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.82 MB | 54.92 MB | 14.9% | 110.3% |
| `f1ap_rel18.6_specs` | 35.23 MB | 164.57 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 23.75 MB | 117.66 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.99 MB | 102.96 MB | 104.7% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0374s | -0.0044s | improved |
| `f1ap_rel18.6_specs` | 0.0690s | 0.0694s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0478s | 0.0418s | +0.0060s | worse |
| `lteNRRCC` | 0.0738s | 0.0702s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.50 MB | 3.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.58 MB | 4.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.19 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.14 MB | 3.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0400s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1067s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0751s | +0.0016s | worse |
| `lteNRRCC` | 0.1394s | 0.1370s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.05 MB | 7.69 MB | 108.0% | 83.8% |
| `f1ap_rel18.6_specs` | 8.42 MB | 104.81 MB | 176.4% | 167.8% |
| `ngap_rel18.6_specs` | 7.89 MB | 7.93 MB | 83.8% | 168.3% |
| `lteNRRCC` | 50.81 MB | 51.52 MB | 107.4% | 108.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0424s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1245s | 0.1251s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0902s | 0.0867s | +0.0035s | worse |
| `lteNRRCC` | 0.1333s | 0.1335s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.08 MB | 9.84 MB | 81.1% | 113.6% |
| `f1ap_rel18.6_specs` | 9.72 MB | 10.28 MB | 98.7% | 167.5% |
| `ngap_rel18.6_specs` | 9.41 MB | 9.49 MB | 159.1% | 159.9% |
| `lteNRRCC` | 8.62 MB | 98.96 MB | 161.6% | 161.0% |
<!-- BENCH_RESULTS_END -->
