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
Generated: 2026-03-12T18:33:18.435237+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0965s | 0.0983s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.3005s | 0.3038s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.2180s | 0.2214s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.32 MB | 5.25 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.28 MB | 461.25 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 5.57 MB | 234.75 MB | 0.0% | 83.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0694s | 0.0739s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.1950s | 0.2189s | -0.0239s | improved |
| `ngap_rel18.6_specs` | 0.1475s | 0.1606s | -0.0131s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.90 MB | 4.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.38 MB | 221.76 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 5.13 MB | 252.10 MB | 0.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0707s | 0.0761s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.1930s | 0.2111s | -0.0181s | improved |
| `ngap_rel18.6_specs` | 0.1413s | 0.1546s | -0.0133s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.61 MB | 6.84 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.41 MB | 366.75 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 7.23 MB | 397.51 MB | 0.0% | 92.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0465s | 0.0544s | -0.0079s | improved |
| `f1ap_rel18.6_specs` | 0.1381s | 0.1545s | -0.0164s | improved |
| `ngap_rel18.6_specs` | 0.1001s | 0.1138s | -0.0137s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.12 MB | 4.31 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.08 MB | 410.20 MB | 0.0% | 28.5% |
| `ngap_rel18.6_specs` | 4.55 MB | 3.80 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0875s | 0.0869s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.2711s | 0.2467s | +0.0244s | worse |
| `ngap_rel18.6_specs` | 0.1928s | 0.1795s | +0.0133s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.52 MB | 7.56 MB | 101.4% | 80.9% |
| `f1ap_rel18.6_specs` | 8.05 MB | 376.41 MB | 80.1% | 165.3% |
| `ngap_rel18.6_specs` | 7.88 MB | 281.64 MB | 80.1% | 106.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.1055s | 0.0913s | +0.0142s | worse |
| `f1ap_rel18.6_specs` | 0.3166s | 0.2823s | +0.0343s | worse |
| `ngap_rel18.6_specs` | 0.2374s | 0.2017s | +0.0357s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.95 MB | 9.09 MB | 163.9% | 111.7% |
| `f1ap_rel18.6_specs` | 10.37 MB | 565.32 MB | 228.4% | 103.9% |
| `ngap_rel18.6_specs` | 9.39 MB | 421.57 MB | 118.6% | 165.9% |
<!-- BENCH_RESULTS_END -->
