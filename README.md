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
Generated: 2026-10-27T01:20:55.055853+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0373s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1120s | 0.1125s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0777s | -0.0011s | improved |
| `lteNRRCC` | 0.1210s | 0.1211s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.92 MB | 53.55 MB | 79.2% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0253s | +0.0099s | worse |
| `f1ap_rel18.6_specs` | 0.0945s | 0.0691s | +0.0254s | worse |
| `ngap_rel18.6_specs` | 0.0673s | 0.0489s | +0.0184s | worse |
| `lteNRRCC` | 0.1307s | 0.0853s | +0.0454s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.11 MB | 76.9% | 103.7% |
| `f1ap_rel18.6_specs` | 22.31 MB | 103.14 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 18.05 MB | 74.66 MB | 100.0% | 102.4% |
| `lteNRRCC` | 48.58 MB | 65.56 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0346s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0899s | +0.0062s | worse |
| `ngap_rel18.6_specs` | 0.0659s | 0.0632s | +0.0027s | worse |
| `lteNRRCC` | 0.1283s | 0.1175s | +0.0108s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.79 MB | 74.1% | 103.7% |
| `f1ap_rel18.6_specs` | 34.64 MB | 163.76 MB | 103.3% | 103.6% |
| `ngap_rel18.6_specs` | 24.31 MB | 117.73 MB | 104.0% | 104.7% |
| `lteNRRCC` | 74.87 MB | 102.81 MB | 101.6% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0212s | 0.0390s | -0.0178s | improved |
| `f1ap_rel18.6_specs` | 0.0699s | 0.0870s | -0.0171s | improved |
| `ngap_rel18.6_specs` | 0.0534s | 0.0578s | -0.0044s | improved |
| `lteNRRCC` | 0.0755s | 0.0893s | -0.0138s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.28 MB | 2.80 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.83 MB | 8.44 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.98 MB | 4.45 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.56 MB | 3.77 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0434s | 0.0324s | +0.0110s | worse |
| `f1ap_rel18.6_specs` | 0.1126s | 0.0905s | +0.0221s | worse |
| `ngap_rel18.6_specs` | 0.0796s | 0.0684s | +0.0112s | worse |
| `lteNRRCC` | 0.1416s | 0.1106s | +0.0310s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.72 MB | 7.82 MB | 191.0% | 150.0% |
| `f1ap_rel18.6_specs` | 8.99 MB | 8.93 MB | 108.5% | 93.3% |
| `ngap_rel18.6_specs` | 8.25 MB | 8.06 MB | 74.6% | 74.8% |
| `lteNRRCC` | 51.14 MB | 62.11 MB | 152.4% | 105.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0353s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1005s | +0.0087s | worse |
| `ngap_rel18.6_specs` | 0.0746s | 0.0723s | +0.0023s | worse |
| `lteNRRCC` | 0.1290s | 0.1120s | +0.0170s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.74 MB | 8.74 MB | 98.8% | 235.9% |
| `f1ap_rel18.6_specs` | 10.07 MB | 163.38 MB | 158.9% | 158.7% |
| `ngap_rel18.6_specs` | 9.10 MB | 9.10 MB | 156.7% | 79.6% |
| `lteNRRCC` | 8.45 MB | 99.16 MB | 158.2% | 155.8% |
<!-- BENCH_RESULTS_END -->
