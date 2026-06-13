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
Generated: 2026-06-13T11:57:47.915558+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0363s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1140s | 0.1117s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0778s | 0.0772s | +0.0006s | worse |
| `lteNRRCC` | 0.1220s | 0.1207s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 21.6% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0330s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0969s | -0.0051s | improved |
| `ngap_rel18.6_specs` | 0.0636s | 0.0669s | -0.0033s | improved |
| `lteNRRCC` | 0.1232s | 0.1184s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 35.41 MB | 95.8% | 110.7% |
| `f1ap_rel18.6_specs` | 21.33 MB | 102.84 MB | 109.7% | 103.5% |
| `ngap_rel18.6_specs` | 17.64 MB | 74.35 MB | 111.5% | 104.7% |
| `lteNRRCC` | 48.62 MB | 65.88 MB | 104.8% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0362s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0952s | 0.0966s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0650s | 0.0688s | -0.0038s | improved |
| `lteNRRCC` | 0.1268s | 0.1309s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 55.69 MB | 82.8% | 106.9% |
| `f1ap_rel18.6_specs` | 34.00 MB | 163.52 MB | 106.2% | 105.2% |
| `ngap_rel18.6_specs` | 23.95 MB | 117.81 MB | 111.5% | 106.8% |
| `lteNRRCC` | 74.87 MB | 102.96 MB | 103.1% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0223s | 0.0355s | -0.0132s | improved |
| `f1ap_rel18.6_specs` | 0.0679s | 0.0689s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0465s | 0.0489s | -0.0024s | improved |
| `lteNRRCC` | 0.0816s | 0.0774s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.06 MB | 4.89 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.89 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.31 MB | 8.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.17 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0396s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1070s | 0.1091s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0747s | 0.0753s | -0.0006s | improved |
| `lteNRRCC` | 0.1383s | 0.1401s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.37 MB | 79.5% | 160.8% |
| `f1ap_rel18.6_specs` | 8.03 MB | 106.55 MB | 164.7% | 109.7% |
| `ngap_rel18.6_specs` | 7.97 MB | 7.55 MB | 224.4% | 80.4% |
| `lteNRRCC` | 48.50 MB | 70.55 MB | 159.2% | 161.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0421s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1229s | -0.0114s | improved |
| `ngap_rel18.6_specs` | 0.0787s | 0.0884s | -0.0097s | improved |
| `lteNRRCC` | 0.1302s | 0.1329s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.96 MB | 8.92 MB | 147.3% | 153.6% |
| `f1ap_rel18.6_specs` | 9.80 MB | 10.00 MB | 164.5% | 75.6% |
| `ngap_rel18.6_specs` | 9.48 MB | 10.90 MB | 95.8% | 109.7% |
| `lteNRRCC` | 9.54 MB | 91.45 MB | 95.9% | 151.7% |
<!-- BENCH_RESULTS_END -->
