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
Generated: 2026-06-05T23:16:29.010480+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0374s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1144s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0789s | 0.0787s | +0.0002s | worse |
| `lteNRRCC` | 0.1207s | 0.1224s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 18.8% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 105.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0372s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.0915s | 0.0944s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0641s | 0.0670s | -0.0029s | improved |
| `lteNRRCC` | 0.1228s | 0.1279s | -0.0051s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 36.49 MB | 92.3% | 109.1% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.34 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.47 MB | 111.1% | 104.5% |
| `lteNRRCC` | 47.88 MB | 65.53 MB | 104.8% | 105.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0392s | -0.0056s | improved |
| `f1ap_rel18.6_specs` | 0.0905s | 0.1020s | -0.0115s | improved |
| `ngap_rel18.6_specs` | 0.0633s | 0.0719s | -0.0086s | improved |
| `lteNRRCC` | 0.1187s | 0.1339s | -0.0152s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.28 MB | 55.79 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 35.11 MB | 164.33 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 23.56 MB | 117.60 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.79 MB | 102.41 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0215s | +0.0178s | worse |
| `f1ap_rel18.6_specs` | 0.0648s | 0.1108s | -0.0460s | improved |
| `ngap_rel18.6_specs` | 0.0594s | 0.0658s | -0.0064s | improved |
| `lteNRRCC` | 0.0777s | 0.1046s | -0.0269s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.39 MB | 5.61 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.38 MB | 4.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.50 MB | 5.22 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.75 MB | 4.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0448s | 0.0400s | +0.0048s | worse |
| `f1ap_rel18.6_specs` | 0.1226s | 0.1099s | +0.0127s | worse |
| `ngap_rel18.6_specs` | 0.0902s | 0.0774s | +0.0128s | worse |
| `lteNRRCC` | 0.1470s | 0.1384s | +0.0086s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.56 MB | 7.88 MB | 103.5% | 163.0% |
| `f1ap_rel18.6_specs` | 7.86 MB | 102.82 MB | 102.3% | 207.7% |
| `ngap_rel18.6_specs` | 8.30 MB | 8.30 MB | 103.2% | 111.0% |
| `lteNRRCC` | 50.90 MB | 54.82 MB | 111.6% | 109.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0366s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1072s | 0.1002s | +0.0070s | worse |
| `ngap_rel18.6_specs` | 0.0742s | 0.0704s | +0.0038s | worse |
| `lteNRRCC` | 0.1141s | 0.1135s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.00 MB | 9.09 MB | 102.3% | 205.2% |
| `f1ap_rel18.6_specs` | 10.50 MB | 10.57 MB | 138.1% | 97.5% |
| `ngap_rel18.6_specs` | 9.26 MB | 9.41 MB | 203.1% | 99.4% |
| `lteNRRCC` | 8.86 MB | 90.50 MB | 99.2% | 111.7% |
<!-- BENCH_RESULTS_END -->
