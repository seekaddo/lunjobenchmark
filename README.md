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
Generated: 2026-08-14T11:01:45.470137+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0405s | -0.0045s | improved |
| `f1ap_rel18.6_specs` | 0.1137s | 0.1132s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0782s | 0.0775s | +0.0007s | worse |
| `lteNRRCC` | 0.1213s | 0.1206s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 73.1% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0314s | 0.0263s | +0.0051s | worse |
| `f1ap_rel18.6_specs` | 0.0892s | 0.0727s | +0.0165s | worse |
| `ngap_rel18.6_specs` | 0.0628s | 0.0509s | +0.0119s | worse |
| `lteNRRCC` | 0.1111s | 0.0961s | +0.0150s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.34 MB | 35.68 MB | 12.8% | 104.3% |
| `f1ap_rel18.6_specs` | 22.37 MB | 103.38 MB | 100.0% | 101.9% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.66 MB | 104.8% | 105.1% |
| `lteNRRCC` | 48.41 MB | 66.42 MB | 101.9% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0334s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0893s | 0.0896s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0623s | 0.0636s | -0.0013s | improved |
| `lteNRRCC` | 0.1153s | 0.1171s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.68 MB | 73.1% | 103.8% |
| `f1ap_rel18.6_specs` | 34.37 MB | 164.50 MB | 103.4% | 101.9% |
| `ngap_rel18.6_specs` | 24.56 MB | 117.81 MB | 104.3% | 102.4% |
| `lteNRRCC` | 74.64 MB | 102.82 MB | 103.6% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0231s | 0.0283s | -0.0052s | improved |
| `f1ap_rel18.6_specs` | 0.0701s | 0.0824s | -0.0123s | improved |
| `ngap_rel18.6_specs` | 0.0490s | 0.0566s | -0.0076s | improved |
| `lteNRRCC` | 0.0783s | 0.1003s | -0.0220s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.33 MB | 6.73 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.33 MB | 5.64 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.83 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.05 MB | 4.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0469s | 0.0387s | +0.0082s | worse |
| `f1ap_rel18.6_specs` | 0.1220s | 0.1106s | +0.0114s | worse |
| `ngap_rel18.6_specs` | 0.0840s | 0.0777s | +0.0063s | worse |
| `lteNRRCC` | 0.1460s | 0.1375s | +0.0085s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 8.52 MB | 0.0% | 148.0% |
| `f1ap_rel18.6_specs` | 8.86 MB | 106.66 MB | 147.5% | 152.1% |
| `ngap_rel18.6_specs` | 8.50 MB | 8.44 MB | 153.9% | 151.0% |
| `lteNRRCC` | 51.20 MB | 62.87 MB | 148.1% | 152.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0482s | -0.0066s | improved |
| `f1ap_rel18.6_specs` | 0.1203s | 0.1353s | -0.0150s | improved |
| `ngap_rel18.6_specs` | 0.0825s | 0.0921s | -0.0096s | improved |
| `lteNRRCC` | 0.1374s | 0.1388s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 9.65 MB | 0.0% | 98.7% |
| `f1ap_rel18.6_specs` | 10.05 MB | 163.87 MB | 81.8% | 165.2% |
| `ngap_rel18.6_specs` | 9.33 MB | 9.33 MB | 163.1% | 165.2% |
| `lteNRRCC` | 73.77 MB | 100.26 MB | 100.3% | 163.1% |
<!-- BENCH_RESULTS_END -->
