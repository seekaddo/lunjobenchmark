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
Generated: 2026-03-12T19:01:29.048891+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0999s | 0.0964s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.3077s | 0.3014s | +0.0063s | worse |
| `ngap_rel18.6_specs` | 0.2231s | 0.2195s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.39 MB | 184.39 MB | 105.3% | 103.3% |
| `f1ap_rel18.6_specs` | 32.27 MB | 562.89 MB | 106.7% | 101.8% |
| `ngap_rel18.6_specs` | 22.14 MB | 419.14 MB | 108.3% | 102.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0683s | 0.0746s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.1969s | 0.2219s | -0.0250s | improved |
| `ngap_rel18.6_specs` | 0.1433s | 0.1627s | -0.0194s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.73 MB | 123.45 MB | 92.3% | 106.5% |
| `f1ap_rel18.6_specs` | 22.18 MB | 369.95 MB | 108.8% | 102.8% |
| `ngap_rel18.6_specs` | 16.77 MB | 276.64 MB | 114.3% | 103.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0708s | 0.0707s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1918s | 0.1932s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.1438s | 0.1494s | -0.0056s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.78 MB | 186.33 MB | 15.9% | 106.2% |
| `f1ap_rel18.6_specs` | 34.40 MB | 565.39 MB | 112.9% | 102.7% |
| `ngap_rel18.6_specs` | 23.81 MB | 421.43 MB | 111.1% | 104.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0464s | 0.0464s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1447s | 0.1485s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.1316s | 0.1008s | +0.0308s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.14 MB | 4.11 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.70 MB | 4.17 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.30 MB | 4.39 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0848s | 0.0846s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.2462s | 0.2376s | +0.0086s | worse |
| `ngap_rel18.6_specs` | 0.1802s | 0.1741s | +0.0061s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.44 MB | 7.32 MB | 110.0% | 163.0% |
| `f1ap_rel18.6_specs` | 8.06 MB | 376.42 MB | 101.6% | 112.2% |
| `ngap_rel18.6_specs` | 7.50 MB | 233.82 MB | 81.4% | 107.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0906s | 0.0942s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.2784s | 0.2730s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.1971s | 0.1968s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.70 MB | 8.96 MB | 157.5% | 85.9% |
| `f1ap_rel18.6_specs` | 10.09 MB | 552.05 MB | 95.1% | 216.7% |
| `ngap_rel18.6_specs` | 10.94 MB | 385.80 MB | 223.3% | 105.6% |
<!-- BENCH_RESULTS_END -->
