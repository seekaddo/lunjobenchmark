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
Generated: 2026-09-09T14:20:20.312475+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0357s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1097s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0756s | +0.0011s | worse |
| `lteNRRCC` | 0.1207s | 0.1196s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.67 MB | 53.55 MB | 13.5% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0360s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0984s | 0.0987s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0683s | 0.0692s | -0.0009s | improved |
| `lteNRRCC` | 0.1297s | 0.1313s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 36.39 MB | 80.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.32 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.51 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.30 MB | 66.54 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0299s | 0.0284s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0782s | 0.0768s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0530s | 0.0532s | -0.0002s | improved |
| `lteNRRCC` | 0.1015s | 0.1028s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.78 MB | 55.86 MB | 68.0% | 104.5% |
| `f1ap_rel18.6_specs` | 34.78 MB | 163.46 MB | 104.2% | 102.1% |
| `ngap_rel18.6_specs` | 24.51 MB | 117.64 MB | 110.0% | 102.9% |
| `lteNRRCC` | 74.64 MB | 102.52 MB | 104.1% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0253s | +0.0078s | worse |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0835s | +0.0099s | worse |
| `ngap_rel18.6_specs` | 0.0509s | 0.0529s | -0.0020s | improved |
| `lteNRRCC` | 0.0998s | 0.1044s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.41 MB | 10.83 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.00 MB | 4.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.62 MB | 8.59 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.66 MB | 7.73 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0390s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1098s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0772s | 0.0759s | +0.0013s | worse |
| `lteNRRCC` | 0.1444s | 0.1285s | +0.0159s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.73 MB | 7.62 MB | 105.4% | 190.3% |
| `f1ap_rel18.6_specs` | 8.03 MB | 106.64 MB | 159.7% | 157.6% |
| `ngap_rel18.6_specs` | 7.55 MB | 8.23 MB | 90.2% | 223.2% |
| `lteNRRCC` | 51.83 MB | 53.20 MB | 157.5% | 156.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0424s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1261s | 0.1265s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0860s | 0.0865s | -0.0005s | improved |
| `lteNRRCC` | 0.1376s | 0.1318s | +0.0058s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.12 MB | 10.65 MB | 0.0% | 110.3% |
| `f1ap_rel18.6_specs` | 10.09 MB | 163.50 MB | 160.4% | 106.6% |
| `ngap_rel18.6_specs` | 9.34 MB | 10.69 MB | 87.4% | 111.8% |
| `lteNRRCC` | 8.87 MB | 101.68 MB | 158.9% | 177.6% |
<!-- BENCH_RESULTS_END -->
