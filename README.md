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
Generated: 2026-07-03T12:13:00.855376+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0353s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1109s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0765s | 0.0752s | +0.0013s | worse |
| `lteNRRCC` | 0.1230s | 0.1195s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.61 MB | 53.55 MB | 22.1% | 113.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0213s | +0.0140s | worse |
| `f1ap_rel18.6_specs` | 0.0946s | 0.0594s | +0.0352s | worse |
| `ngap_rel18.6_specs` | 0.0676s | 0.0390s | +0.0286s | worse |
| `lteNRRCC` | 0.1298s | 0.0727s | +0.0571s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 36.43 MB | 19.5% | 103.4% |
| `f1ap_rel18.6_specs` | 22.37 MB | 102.88 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.60 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.41 MB | 65.84 MB | 103.1% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0346s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0904s | +0.0059s | worse |
| `ngap_rel18.6_specs` | 0.0682s | 0.0632s | +0.0050s | worse |
| `lteNRRCC` | 0.1276s | 0.1194s | +0.0082s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 55.86 MB | 92.3% | 110.3% |
| `f1ap_rel18.6_specs` | 34.71 MB | 164.42 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.54 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.33 MB | 102.10 MB | 103.1% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0208s | 0.0223s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0679s | 0.0699s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0459s | 0.0458s | +0.0001s | worse |
| `lteNRRCC` | 0.0793s | 0.0821s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.61 MB | 4.05 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.78 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.83 MB | 3.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.44 MB | 3.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0405s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1127s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0746s | 0.0782s | -0.0036s | improved |
| `lteNRRCC` | 0.1374s | 0.1409s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.87 MB | 7.34 MB | 109.1% | 163.3% |
| `f1ap_rel18.6_specs` | 8.05 MB | 8.62 MB | 82.8% | 0.0% |
| `ngap_rel18.6_specs` | 7.56 MB | 7.48 MB | 80.8% | 167.4% |
| `lteNRRCC` | 51.84 MB | 69.11 MB | 167.2% | 163.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0475s | -0.0074s | improved |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1459s | -0.0302s | improved |
| `ngap_rel18.6_specs` | 0.0806s | 0.1013s | -0.0207s | improved |
| `lteNRRCC` | 0.1302s | 0.1461s | -0.0159s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.78 MB | 8.93 MB | 154.9% | 157.8% |
| `f1ap_rel18.6_specs` | 9.87 MB | 9.75 MB | 79.9% | 78.9% |
| `ngap_rel18.6_specs` | 9.21 MB | 9.08 MB | 156.5% | 78.4% |
| `lteNRRCC` | 8.56 MB | 99.58 MB | 157.7% | 187.7% |
<!-- BENCH_RESULTS_END -->
