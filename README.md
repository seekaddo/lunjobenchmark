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
Generated: 2026-10-21T00:29:21.894636+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0362s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1117s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0773s | +0.0016s | worse |
| `lteNRRCC` | 0.1214s | 0.1205s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.98 MB | 53.55 MB | 82.6% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0216s | 0.0484s | -0.0268s | improved |
| `f1ap_rel18.6_specs` | 0.0603s | 0.1425s | -0.0822s | improved |
| `ngap_rel18.6_specs` | 0.0403s | 0.1012s | -0.0609s | improved |
| `lteNRRCC` | 0.0741s | 0.1559s | -0.0818s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 36.73 MB | 65.0% | 100.0% |
| `f1ap_rel18.6_specs` | 21.65 MB | 103.18 MB | 105.6% | 100.0% |
| `ngap_rel18.6_specs` | 18.03 MB | 73.47 MB | 106.7% | 103.8% |
| `lteNRRCC` | 48.08 MB | 65.76 MB | 105.7% | 102.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0552s | 0.0341s | +0.0211s | worse |
| `f1ap_rel18.6_specs` | 0.1660s | 0.0908s | +0.0752s | worse |
| `ngap_rel18.6_specs` | 0.1149s | 0.0635s | +0.0514s | worse |
| `lteNRRCC` | 0.1654s | 0.1184s | +0.0470s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.66 MB | 53.73 MB | 71.0% | 105.1% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.7% | 102.1% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.1% | 102.9% |
| `lteNRRCC` | 72.62 MB | 100.36 MB | 101.3% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0154s | 0.0217s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0982s | 0.0759s | +0.0223s | worse |
| `ngap_rel18.6_specs` | 0.0559s | 0.0731s | -0.0172s | improved |
| `lteNRRCC` | 0.0951s | 0.0778s | +0.0173s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.27 MB | 4.22 MB | 0.0% | 0.6% |
| `f1ap_rel18.6_specs` | 5.06 MB | 10.73 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.47 MB | 8.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.95 MB | 7.59 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0401s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.1043s | 0.1087s | -0.0044s | improved |
| `ngap_rel18.6_specs` | 0.0722s | 0.0751s | -0.0029s | improved |
| `lteNRRCC` | 0.1140s | 0.1391s | -0.0251s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.31 MB | 8.36 MB | 0.0% | 124.0% |
| `f1ap_rel18.6_specs` | 8.77 MB | 8.70 MB | 240.3% | 117.6% |
| `ngap_rel18.6_specs` | 8.33 MB | 8.33 MB | 87.5% | 86.1% |
| `lteNRRCC` | 8.57 MB | 55.23 MB | 87.2% | 108.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0466s | 0.0403s | +0.0063s | worse |
| `f1ap_rel18.6_specs` | 0.1382s | 0.1210s | +0.0172s | worse |
| `ngap_rel18.6_specs` | 0.0983s | 0.0830s | +0.0153s | worse |
| `lteNRRCC` | 0.1405s | 0.1306s | +0.0099s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.26 MB | 0.0% | 151.4% |
| `f1ap_rel18.6_specs` | 11.18 MB | 133.96 MB | 94.6% | 107.9% |
| `ngap_rel18.6_specs` | 10.44 MB | 10.36 MB | 155.2% | 77.2% |
| `lteNRRCC` | 73.75 MB | 79.75 MB | 151.4% | 110.5% |
<!-- BENCH_RESULTS_END -->
