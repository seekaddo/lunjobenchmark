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
Generated: 2026-05-27T23:22:22.013173+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0353s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1114s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0767s | +0.0004s | worse |
| `lteNRRCC` | 0.1196s | 0.1209s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.90 MB | 53.55 MB | 10.7% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 108.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0328s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0955s | -0.0049s | improved |
| `ngap_rel18.6_specs` | 0.0632s | 0.0657s | -0.0025s | improved |
| `lteNRRCC` | 0.1289s | 0.1193s | +0.0096s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.43 MB | 35.99 MB | 85.7% | 110.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.36 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.72 MB | 74.30 MB | 111.1% | 109.3% |
| `lteNRRCC` | 48.75 MB | 66.50 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0339s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0903s | 0.0909s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0619s | 0.0636s | -0.0017s | improved |
| `lteNRRCC` | 0.1153s | 0.1173s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.26 MB | 55.72 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 34.72 MB | 164.63 MB | 113.8% | 103.6% |
| `ngap_rel18.6_specs` | 24.30 MB | 117.80 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.88 MB | 102.17 MB | 105.2% | 105.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0240s | 0.0302s | -0.0062s | improved |
| `f1ap_rel18.6_specs` | 0.0866s | 0.0738s | +0.0128s | worse |
| `ngap_rel18.6_specs` | 0.0676s | 0.0482s | +0.0194s | worse |
| `lteNRRCC` | 0.0731s | 0.0838s | -0.0107s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.61 MB | 7.50 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.98 MB | 9.00 MB | 0.0% | 1.3% |
| `ngap_rel18.6_specs` | 2.17 MB | 5.48 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.16 MB | 480 KB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0383s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1065s | 0.1045s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0740s | 0.0732s | +0.0008s | worse |
| `lteNRRCC` | 0.1368s | 0.1357s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.50 MB | 161.8% | 97.2% |
| `f1ap_rel18.6_specs` | 8.45 MB | 8.47 MB | 117.7% | 114.2% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.54 MB | 82.3% | 160.0% |
| `lteNRRCC` | 45.69 MB | 51.99 MB | 163.1% | 107.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0316s | +0.0092s | worse |
| `f1ap_rel18.6_specs` | 0.1168s | 0.0866s | +0.0302s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0614s | +0.0202s | worse |
| `lteNRRCC` | 0.1346s | 0.0926s | +0.0420s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.79 MB | 8.79 MB | 155.6% | 152.7% |
| `f1ap_rel18.6_specs` | 10.18 MB | 9.90 MB | 151.1% | 154.8% |
| `ngap_rel18.6_specs` | 10.19 MB | 10.69 MB | 103.4% | 205.1% |
| `lteNRRCC` | 8.55 MB | 98.82 MB | 151.3% | 146.7% |
<!-- BENCH_RESULTS_END -->
