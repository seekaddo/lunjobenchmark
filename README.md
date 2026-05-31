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
Generated: 2026-05-31T11:43:56.366009+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0366s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1151s | 0.1147s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0795s | -0.0007s | improved |
| `lteNRRCC` | 0.1211s | 0.1206s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 25.3% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 115.4% | 105.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0357s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.0952s | 0.0914s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0660s | 0.0649s | +0.0011s | worse |
| `lteNRRCC` | 0.1176s | 0.1230s | -0.0054s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.41 MB | 80.0% | 107.7% |
| `f1ap_rel18.6_specs` | 21.30 MB | 102.50 MB | 106.9% | 105.3% |
| `ngap_rel18.6_specs` | 17.71 MB | 74.57 MB | 108.7% | 107.1% |
| `lteNRRCC` | 48.33 MB | 66.38 MB | 105.3% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0414s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.1015s | 0.1233s | -0.0218s | improved |
| `ngap_rel18.6_specs` | 0.0709s | 0.0854s | -0.0145s | improved |
| `lteNRRCC` | 0.1317s | 0.1313s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.40 MB | 55.62 MB | 96.3% | 109.7% |
| `f1ap_rel18.6_specs` | 34.18 MB | 163.83 MB | 112.1% | 106.7% |
| `ngap_rel18.6_specs` | 24.35 MB | 117.55 MB | 114.8% | 106.4% |
| `lteNRRCC` | 74.83 MB | 102.73 MB | 106.2% | 102.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0281s | +0.0057s | worse |
| `f1ap_rel18.6_specs` | 0.0987s | 0.0908s | +0.0079s | worse |
| `ngap_rel18.6_specs` | 0.0494s | 0.0626s | -0.0132s | improved |
| `lteNRRCC` | 0.0867s | 0.1195s | -0.0328s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.45 MB | 8.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.66 MB | 5.08 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.47 MB | 5.89 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.09 MB | 4.73 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0386s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1076s | 0.1068s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0746s | 0.0754s | -0.0008s | improved |
| `lteNRRCC` | 0.1378s | 0.1376s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.36 MB | 170.7% | 82.2% |
| `f1ap_rel18.6_specs` | 8.92 MB | 7.97 MB | 95.3% | 163.3% |
| `ngap_rel18.6_specs` | 7.53 MB | 7.54 MB | 166.0% | 162.1% |
| `lteNRRCC` | 47.20 MB | 51.39 MB | 158.9% | 158.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0434s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1150s | 0.1263s | -0.0113s | improved |
| `ngap_rel18.6_specs` | 0.0786s | 0.0866s | -0.0080s | improved |
| `lteNRRCC` | 0.1293s | 0.1415s | -0.0122s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.58 MB | 8.97 MB | 149.9% | 149.1% |
| `f1ap_rel18.6_specs` | 9.99 MB | 9.87 MB | 153.5% | 88.6% |
| `ngap_rel18.6_specs` | 9.20 MB | 9.20 MB | 74.4% | 154.1% |
| `lteNRRCC` | 73.46 MB | 99.70 MB | 147.8% | 159.2% |
<!-- BENCH_RESULTS_END -->
