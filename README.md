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
Generated: 2026-03-12T18:28:59.858265+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0983s | 0.1008s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.3038s | 0.3045s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.2214s | 0.2221s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.30 MB | 5.33 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.28 MB | 464.97 MB | 0.0% | 91.6% |
| `ngap_rel18.6_specs` | 5.66 MB | 238.68 MB | 0.0% | 91.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0739s | 0.0718s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.2189s | 0.1967s | +0.0222s | worse |
| `ngap_rel18.6_specs` | 0.1606s | 0.1459s | +0.0147s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.34 MB | 4.39 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.03 MB | 176.09 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 4.69 MB | 198.22 MB | 0.0% | 109.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0761s | 0.0726s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.2111s | 0.2012s | +0.0099s | worse |
| `ngap_rel18.6_specs` | 0.1546s | 0.1459s | +0.0087s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.63 MB | 6.71 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.46 MB | 347.25 MB | 0.0% | 92.3% |
| `ngap_rel18.6_specs` | 7.66 MB | 355.36 MB | 0.0% | 92.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0544s | 0.0477s | +0.0067s | worse |
| `f1ap_rel18.6_specs` | 0.1545s | 0.1509s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.1138s | 0.1082s | +0.0056s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.03 MB | 5.80 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.41 MB | 9.11 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.94 MB | 6.84 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
