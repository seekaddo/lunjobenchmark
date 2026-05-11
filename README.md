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
Generated: 2026-05-11T23:01:52.588538+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0371s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1139s | 0.1135s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0794s | -0.0025s | improved |
| `lteNRRCC` | 0.1215s | 0.1222s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.90 MB | 53.55 MB | 6.6% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0338s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0905s | 0.0918s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0644s | 0.0643s | +0.0001s | worse |
| `lteNRRCC` | 0.1245s | 0.1243s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.29 MB | 36.07 MB | 83.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.05 MB | 103.44 MB | 112.5% | 105.3% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.42 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.45 MB | 66.04 MB | 104.8% | 105.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0341s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0890s | 0.0913s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0619s | 0.0629s | -0.0010s | improved |
| `lteNRRCC` | 0.1163s | 0.1179s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.68 MB | 100.0% | 107.4% |
| `f1ap_rel18.6_specs` | 34.75 MB | 164.32 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.30 MB | 117.52 MB | 112.5% | 104.8% |
| `lteNRRCC` | 74.97 MB | 102.79 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0256s | 0.0224s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0733s | 0.0659s | +0.0074s | worse |
| `ngap_rel18.6_specs` | 0.0391s | 0.0436s | -0.0045s | improved |
| `lteNRRCC` | 0.0684s | 0.0721s | -0.0037s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.97 MB | 3.69 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.08 MB | 9.19 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.77 MB | 4.17 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.20 MB | 992 KB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0403s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1071s | 0.1090s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0749s | +0.0003s | worse |
| `lteNRRCC` | 0.1399s | 0.1392s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.69 MB | 7.59 MB | 107.9% | 111.4% |
| `f1ap_rel18.6_specs` | 8.55 MB | 106.64 MB | 114.0% | 162.7% |
| `ngap_rel18.6_specs` | 7.55 MB | 8.08 MB | 163.3% | 115.3% |
| `lteNRRCC` | 8.35 MB | 70.55 MB | 107.2% | 169.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0428s | -0.0041s | improved |
| `f1ap_rel18.6_specs` | 0.1124s | 0.1241s | -0.0117s | improved |
| `ngap_rel18.6_specs` | 0.0775s | 0.0854s | -0.0079s | improved |
| `lteNRRCC` | 0.1293s | 0.1337s | -0.0044s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.39 MB | 8.58 MB | 160.9% | 79.7% |
| `f1ap_rel18.6_specs` | 9.59 MB | 164.19 MB | 159.9% | 160.5% |
| `ngap_rel18.6_specs` | 8.95 MB | 9.08 MB | 158.0% | 155.5% |
| `lteNRRCC` | 9.36 MB | 98.95 MB | 230.6% | 109.6% |
<!-- BENCH_RESULTS_END -->
