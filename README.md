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
Generated: 2026-03-12T18:22:54.763746+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.1008s | 0.0999s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.3045s | 0.3095s | -0.0050s | improved |
| `ngap_rel18.6_specs` | 0.2221s | 0.2253s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.40 MB | 5.40 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.29 MB | 466.30 MB | 0.0% | 95.6% |
| `ngap_rel18.6_specs` | 5.66 MB | 236.85 MB | 0.0% | 91.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0718s | 0.0688s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.1967s | 0.1961s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.1459s | 0.1425s | +0.0034s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.38 MB | 4.67 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.32 MB | 201.25 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 5.06 MB | 242.35 MB | 0.0% | 109.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0726s | 0.0722s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.2012s | 0.2007s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.1459s | 0.1474s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.62 MB | 6.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.97 MB | 354.16 MB | 0.0% | 100.0% |
| `ngap_rel18.6_specs` | 7.87 MB | 378.36 MB | 0.0% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0477s | 0.0462s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1509s | 0.1644s | -0.0135s | improved |
| `ngap_rel18.6_specs` | 0.1082s | 0.1146s | -0.0064s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 4.11 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.53 MB | 4.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.08 MB | 4.39 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0869s | 0.0880s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.2467s | 0.2507s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.1795s | 0.1875s | -0.0080s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 0 KB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 0 KB | 0 KB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 0 KB | 0 KB | 0.0% | 0.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0913s | 0.0941s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.2823s | 0.2771s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.2017s | 0.2017s | -0.0000s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 0 KB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 0 KB | 0 KB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 0 KB | 0 KB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
