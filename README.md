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
Generated: 2026-05-08T11:25:08.529027+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0373s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1138s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0793s | -0.0022s | improved |
| `lteNRRCC` | 0.1198s | 0.1232s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.84 MB | 53.55 MB | 7.1% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0345s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0939s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0677s | -0.0014s | improved |
| `lteNRRCC` | 0.1282s | 0.1291s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 36.48 MB | 18.9% | 110.7% |
| `f1ap_rel18.6_specs` | 22.36 MB | 102.46 MB | 106.1% | 106.9% |
| `ngap_rel18.6_specs` | 16.67 MB | 74.09 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.75 MB | 66.42 MB | 103.0% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0331s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0883s | 0.0898s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0621s | 0.0625s | -0.0004s | improved |
| `lteNRRCC` | 0.1148s | 0.1167s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.02 MB | 96.0% | 107.1% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.56 MB | 110.0% | 105.5% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.18 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.66 MB | 102.39 MB | 106.9% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0206s | 0.0263s | -0.0057s | improved |
| `f1ap_rel18.6_specs` | 0.0644s | 0.0857s | -0.0213s | improved |
| `ngap_rel18.6_specs` | 0.0434s | 0.0553s | -0.0119s | improved |
| `lteNRRCC` | 0.0724s | 0.1153s | -0.0429s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.56 MB | 4.64 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.17 MB | 4.17 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 4.33 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0388s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1062s | +0.0072s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0763s | +0.0037s | worse |
| `lteNRRCC` | 0.1293s | 0.1384s | -0.0091s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.56 MB | 8.56 MB | 114.9% | 108.1% |
| `f1ap_rel18.6_specs` | 8.60 MB | 8.73 MB | 158.3% | 98.1% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.29 MB | 155.1% | 161.8% |
| `lteNRRCC` | 8.60 MB | 8.54 MB | 88.4% | 77.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0408s | -0.0071s | improved |
| `f1ap_rel18.6_specs` | 0.1030s | 0.1185s | -0.0155s | improved |
| `ngap_rel18.6_specs` | 0.0732s | 0.0832s | -0.0100s | improved |
| `lteNRRCC` | 0.1124s | 0.1311s | -0.0187s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.90 MB | 9.54 MB | 100.8% | 205.4% |
| `f1ap_rel18.6_specs` | 10.14 MB | 164.19 MB | 210.9% | 140.3% |
| `ngap_rel18.6_specs` | 10.41 MB | 10.25 MB | 136.4% | 140.7% |
| `lteNRRCC` | 9.14 MB | 82.67 MB | 90.5% | 140.4% |
<!-- BENCH_RESULTS_END -->
