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
Generated: 2026-10-12T19:44:14.003160+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0351s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1105s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0754s | 0.0760s | -0.0006s | improved |
| `lteNRRCC` | 0.1199s | 0.1191s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 90.0% | 100.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0300s | 0.0365s | -0.0065s | improved |
| `f1ap_rel18.6_specs` | 0.0886s | 0.0970s | -0.0084s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0705s | -0.0087s | improved |
| `lteNRRCC` | 0.1086s | 0.1310s | -0.0224s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.83 MB | 36.57 MB | 66.7% | 104.3% |
| `f1ap_rel18.6_specs` | 22.39 MB | 103.31 MB | 104.0% | 102.0% |
| `ngap_rel18.6_specs` | 18.11 MB | 74.54 MB | 105.0% | 102.7% |
| `lteNRRCC` | 48.69 MB | 65.97 MB | 101.9% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0290s | 0.0339s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.0772s | 0.0904s | -0.0132s | improved |
| `ngap_rel18.6_specs` | 0.0538s | 0.0637s | -0.0099s | improved |
| `lteNRRCC` | 0.1026s | 0.1158s | -0.0132s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 55.76 MB | 26.6% | 104.5% |
| `f1ap_rel18.6_specs` | 35.15 MB | 164.38 MB | 104.3% | 100.0% |
| `ngap_rel18.6_specs` | 24.19 MB | 117.66 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.87 MB | 102.57 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0299s | 0.0351s | -0.0052s | improved |
| `f1ap_rel18.6_specs` | 0.0697s | 0.0676s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0439s | 0.0619s | -0.0180s | improved |
| `lteNRRCC` | 0.0772s | 0.0742s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.80 MB | 4.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.67 MB | 2.98 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.45 MB | 4.81 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.84 MB | 3.98 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0391s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.0948s | 0.1090s | -0.0142s | improved |
| `ngap_rel18.6_specs` | 0.0670s | 0.0763s | -0.0093s | improved |
| `lteNRRCC` | 0.1129s | 0.1382s | -0.0253s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.19 MB | 7.79 MB | 0.0% | 204.7% |
| `f1ap_rel18.6_specs` | 8.57 MB | 8.82 MB | 206.5% | 96.2% |
| `ngap_rel18.6_specs` | 8.30 MB | 8.32 MB | 195.0% | 201.2% |
| `lteNRRCC` | 8.69 MB | 67.26 MB | 98.3% | 104.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0404s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1150s | 0.1121s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0791s | +0.0012s | worse |
| `lteNRRCC` | 0.1294s | 0.1304s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.00 MB | 8.69 MB | 0.0% | 157.4% |
| `f1ap_rel18.6_specs` | 9.84 MB | 9.65 MB | 79.7% | 90.5% |
| `ngap_rel18.6_specs` | 9.30 MB | 9.17 MB | 149.2% | 78.7% |
| `lteNRRCC` | 8.46 MB | 99.43 MB | 155.7% | 109.3% |
<!-- BENCH_RESULTS_END -->
