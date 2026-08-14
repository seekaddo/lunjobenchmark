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
Generated: 2026-08-14T22:29:43.543580+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0360s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1089s | 0.1137s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0782s | -0.0037s | improved |
| `lteNRRCC` | 0.1181s | 0.1213s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 68.0% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0314s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0892s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0660s | 0.0628s | +0.0032s | worse |
| `lteNRRCC` | 0.1332s | 0.1111s | +0.0221s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.55 MB | 36.50 MB | 22.3% | 103.8% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.29 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.30 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.00 MB | 66.50 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0316s | 0.0330s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0893s | +0.0060s | worse |
| `ngap_rel18.6_specs` | 0.0608s | 0.0623s | -0.0015s | improved |
| `lteNRRCC` | 0.0891s | 0.1153s | -0.0262s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.42 MB | 55.62 MB | 10.4% | 104.8% |
| `f1ap_rel18.6_specs` | 35.17 MB | 163.81 MB | 100.0% | 101.9% |
| `ngap_rel18.6_specs` | 24.30 MB | 117.39 MB | 106.2% | 100.0% |
| `lteNRRCC` | 74.53 MB | 102.75 MB | 102.4% | 101.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0312s | 0.0231s | +0.0081s | worse |
| `f1ap_rel18.6_specs` | 0.0860s | 0.0701s | +0.0159s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0490s | +0.0279s | worse |
| `lteNRRCC` | 0.1137s | 0.0783s | +0.0354s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.17 MB | 4.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.00 MB | 9.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.94 MB | 8.91 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.89 MB | 5.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0469s | -0.0061s | improved |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1220s | -0.0074s | improved |
| `ngap_rel18.6_specs` | 0.0796s | 0.0840s | -0.0044s | improved |
| `lteNRRCC` | 0.1412s | 0.1460s | -0.0048s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.98 MB | 0.0% | 212.5% |
| `f1ap_rel18.6_specs` | 8.77 MB | 106.65 MB | 214.4% | 166.9% |
| `ngap_rel18.6_specs` | 7.99 MB | 8.18 MB | 184.4% | 165.5% |
| `lteNRRCC` | 8.48 MB | 51.87 MB | 79.9% | 168.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0416s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1203s | -0.0078s | improved |
| `ngap_rel18.6_specs` | 0.0753s | 0.0825s | -0.0072s | improved |
| `lteNRRCC` | 0.1273s | 0.1374s | -0.0101s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.66 MB | 0.0% | 78.9% |
| `f1ap_rel18.6_specs` | 12.08 MB | 164.17 MB | 112.5% | 158.7% |
| `ngap_rel18.6_specs` | 8.96 MB | 10.50 MB | 91.7% | 225.7% |
| `lteNRRCC` | 8.62 MB | 94.20 MB | 77.8% | 110.2% |
<!-- BENCH_RESULTS_END -->
