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
Generated: 2026-03-13T10:47:55.446616+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0386s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1253s | 0.1207s | +0.0046s | worse |
| `ngap_rel18.6_specs` | 0.0861s | 0.0824s | +0.0037s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.54 MB | 55.92 MB | 90.5% | 109.7% |
| `f1ap_rel18.6_specs` | 32.42 MB | 176.92 MB | 106.7% | 104.1% |
| `ngap_rel18.6_specs` | 22.29 MB | 125.92 MB | 112.5% | 105.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0357s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1020s | 0.0991s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0701s | 0.0682s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.79 MB | 37.92 MB | 20.5% | 110.0% |
| `f1ap_rel18.6_specs` | 22.04 MB | 111.69 MB | 108.3% | 104.9% |
| `ngap_rel18.6_specs` | 16.67 MB | 80.44 MB | 110.3% | 108.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0352s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0941s | 0.0927s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0657s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 58.04 MB | 77.4% | 110.0% |
| `f1ap_rel18.6_specs` | 34.40 MB | 179.45 MB | 112.9% | 105.1% |
| `ngap_rel18.6_specs` | 24.37 MB | 128.01 MB | 115.4% | 108.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0237s | 0.0220s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0703s | 0.0738s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0488s | 0.0584s | -0.0096s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.83 MB | 4.61 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.78 MB | 4.70 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 1.12 MB | 4.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0398s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1113s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0786s | 0.0779s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.46 MB | 7.79 MB | 94.0% | 117.9% |
| `f1ap_rel18.6_specs` | 8.54 MB | 115.20 MB | 235.3% | 236.4% |
| `ngap_rel18.6_specs` | 8.13 MB | 8.05 MB | 116.9% | 119.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0385s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1114s | 0.1130s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0772s | 0.0790s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.58 MB | 8.63 MB | 117.3% | 86.3% |
| `f1ap_rel18.6_specs` | 11.85 MB | 177.17 MB | 169.1% | 110.5% |
| `ngap_rel18.6_specs` | 7.14 MB | 8.83 MB | 115.0% | 161.0% |
<!-- BENCH_RESULTS_END -->
