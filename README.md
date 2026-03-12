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
- `bench_results/`: latest and historical benchmark output

## Assumptions

- The benchmark repo has access to release archives named like `voltcc-v<version>-<target>.tar.gz`.
- `preparebin.sh` prefers `./releases/` and falls back to `../releases/` for local nested-repo development.
- The copied upstream benchmark scripts execute the prepared binary from `./zig-out/bin/voltcc`, matching the local `test_semantic` script layout.

## Latest Results

<!-- BENCH_RESULTS_START -->
Generated: 2026-03-12T18:37:07.312468+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0964s | 0.0965s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.3014s | 0.3005s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.2195s | 0.2180s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.34 MB | 5.25 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.09 MB | 456.95 MB | 0.0% | 95.8% |
| `ngap_rel18.6_specs` | 5.70 MB | 234.37 MB | 0.0% | 83.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0746s | 0.0694s | +0.0052s | worse |
| `f1ap_rel18.6_specs` | 0.2219s | 0.1950s | +0.0269s | worse |
| `ngap_rel18.6_specs` | 0.1627s | 0.1475s | +0.0152s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.13 MB | 4.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.80 MB | 174.57 MB | 0.0% | 91.6% |
| `ngap_rel18.6_specs` | 4.43 MB | 189.14 MB | 0.0% | 91.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0707s | 0.0707s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1932s | 0.1930s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.1494s | 0.1413s | +0.0081s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.62 MB | 6.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.80 MB | 366.75 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 7.87 MB | 385.23 MB | 0.0% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0464s | 0.0465s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1485s | 0.1381s | +0.0104s | worse |
| `ngap_rel18.6_specs` | 0.1008s | 0.1001s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.28 MB | 5.05 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.72 MB | 4.14 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.50 MB | 5.55 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0846s | 0.0875s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.2376s | 0.2711s | -0.0335s | improved |
| `ngap_rel18.6_specs` | 0.1741s | 0.1928s | -0.0187s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.59 MB | 7.11 MB | 104.4% | 83.2% |
| `f1ap_rel18.6_specs` | 7.93 MB | 376.36 MB | 155.2% | 164.6% |
| `ngap_rel18.6_specs` | 7.57 MB | 265.64 MB | 101.5% | 111.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0942s | 0.1055s | -0.0113s | improved |
| `f1ap_rel18.6_specs` | 0.2730s | 0.3166s | -0.0436s | improved |
| `ngap_rel18.6_specs` | 0.1968s | 0.2374s | -0.0406s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.36 MB | 8.44 MB | 113.3% | 162.2% |
| `f1ap_rel18.6_specs` | 8.25 MB | 548.50 MB | 233.8% | 183.7% |
| `ngap_rel18.6_specs` | 10.18 MB | 417.37 MB | 95.9% | 232.7% |
<!-- BENCH_RESULTS_END -->
