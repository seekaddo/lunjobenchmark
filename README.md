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
Generated: 2026-11-03T03:24:39.949785+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0393s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1258s | 0.1211s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0867s | 0.0828s | +0.0039s | worse |
| `lteNRRCC` | 0.1310s | 0.1261s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.81 MB | 53.55 MB | 76.9% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 103.6% |
| `lteNRRCC` | 72.41 MB | 100.18 MB | 103.3% | 101.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0440s | 0.0481s | -0.0041s | improved |
| `f1ap_rel18.6_specs` | 0.1391s | 0.1473s | -0.0082s | improved |
| `ngap_rel18.6_specs` | 0.0939s | 0.0982s | -0.0043s | improved |
| `lteNRRCC` | 0.1526s | 0.1581s | -0.0055s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.67 MB | 34.65 MB | 81.5% | 109.4% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.7% | 101.2% |
| `ngap_rel18.6_specs` | 17.97 MB | 72.65 MB | 107.4% | 103.5% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 102.8% | 102.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0532s | 0.0378s | +0.0154s | worse |
| `f1ap_rel18.6_specs` | 0.1641s | 0.1157s | +0.0484s | worse |
| `ngap_rel18.6_specs` | 0.1133s | 0.0781s | +0.0352s | worse |
| `lteNRRCC` | 0.1616s | 0.1107s | +0.0509s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 53.73 MB | 73.3% | 102.7% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.7% | 102.2% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.4% | 102.9% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 102.7% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0290s | 0.0319s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.0810s | 0.0918s | -0.0108s | improved |
| `ngap_rel18.6_specs` | 0.0567s | 0.0581s | -0.0014s | improved |
| `lteNRRCC` | 0.1133s | 0.0833s | +0.0300s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.98 MB | 7.70 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.05 MB | 8.66 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.00 MB | 6.89 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.83 MB | 4.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0420s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1130s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0782s | 0.0820s | -0.0038s | improved |
| `lteNRRCC` | 0.1384s | 0.1286s | +0.0098s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.32 MB | 7.51 MB | 91.7% | 79.3% |
| `f1ap_rel18.6_specs` | 8.43 MB | 8.12 MB | 224.9% | 172.8% |
| `ngap_rel18.6_specs` | 8.31 MB | 7.62 MB | 228.7% | 79.7% |
| `lteNRRCC` | 8.18 MB | 52.01 MB | 78.5% | 155.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0397s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1126s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0835s | 0.0806s | +0.0029s | worse |
| `lteNRRCC` | 0.1307s | 0.1334s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 8.87 MB | 0.0% | 199.7% |
| `f1ap_rel18.6_specs` | 9.75 MB | 164.20 MB | 157.8% | 156.1% |
| `ngap_rel18.6_specs` | 10.64 MB | 9.56 MB | 109.1% | 112.8% |
| `lteNRRCC` | 8.44 MB | 87.05 MB | 157.1% | 157.0% |
<!-- BENCH_RESULTS_END -->
