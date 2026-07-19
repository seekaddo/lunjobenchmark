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
Generated: 2026-07-19T22:58:31.561733+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0351s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1105s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0768s | -0.0030s | improved |
| `lteNRRCC` | 0.1178s | 0.1205s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 22.7% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0340s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1027s | 0.0914s | +0.0113s | worse |
| `ngap_rel18.6_specs` | 0.0732s | 0.0635s | +0.0097s | worse |
| `lteNRRCC` | 0.1228s | 0.1243s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.56 MB | 36.54 MB | 62.5% | 103.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.43 MB | 106.9% | 104.8% |
| `ngap_rel18.6_specs` | 17.68 MB | 74.64 MB | 108.7% | 106.7% |
| `lteNRRCC` | 48.06 MB | 65.98 MB | 103.4% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0302s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.0915s | 0.0875s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0631s | 0.0553s | +0.0078s | worse |
| `lteNRRCC` | 0.1218s | 0.0994s | +0.0224s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 55.46 MB | 76.7% | 110.7% |
| `f1ap_rel18.6_specs` | 35.26 MB | 164.42 MB | 110.0% | 103.5% |
| `ngap_rel18.6_specs` | 24.43 MB | 117.66 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.33 MB | 102.32 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0266s | 0.0314s | -0.0048s | improved |
| `f1ap_rel18.6_specs` | 0.0684s | 0.0861s | -0.0177s | improved |
| `ngap_rel18.6_specs` | 0.0463s | 0.0552s | -0.0089s | improved |
| `lteNRRCC` | 0.0805s | 0.0863s | -0.0058s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.27 MB | 3.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.97 MB | 5.52 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.55 MB | 5.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.56 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0396s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1070s | 0.1113s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0782s | -0.0037s | improved |
| `lteNRRCC` | 0.1375s | 0.1455s | -0.0080s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.56 MB | 7.50 MB | 158.1% | 90.3% |
| `f1ap_rel18.6_specs` | 8.67 MB | 8.73 MB | 110.1% | 222.6% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.59 MB | 80.4% | 80.3% |
| `lteNRRCC` | 8.47 MB | 51.45 MB | 113.0% | 104.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0425s | 0.0393s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.1162s | 0.1136s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0813s | 0.0804s | +0.0009s | worse |
| `lteNRRCC` | 0.1337s | 0.1375s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.93 MB | 9.07 MB | 75.9% | 89.1% |
| `f1ap_rel18.6_specs` | 11.39 MB | 10.07 MB | 213.7% | 153.6% |
| `ngap_rel18.6_specs` | 9.20 MB | 9.33 MB | 149.3% | 74.8% |
| `lteNRRCC` | 9.23 MB | 98.74 MB | 80.1% | 161.1% |
<!-- BENCH_RESULTS_END -->
