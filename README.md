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
Generated: 2026-09-06T13:30:56.462301+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0350s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1093s | 0.1116s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0757s | 0.0754s | +0.0003s | worse |
| `lteNRRCC` | 0.1195s | 0.1201s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 19.6% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 104.3% |
| `lteNRRCC` | 72.32 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0229s | 0.0369s | -0.0140s | improved |
| `f1ap_rel18.6_specs` | 0.0653s | 0.0961s | -0.0308s | improved |
| `ngap_rel18.6_specs` | 0.0469s | 0.0682s | -0.0213s | improved |
| `lteNRRCC` | 0.0762s | 0.1301s | -0.0539s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.58 MB | 36.71 MB | 10.1% | 100.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.74 MB | 104.8% | 102.6% |
| `ngap_rel18.6_specs` | 18.06 MB | 73.80 MB | 105.9% | 103.4% |
| `lteNRRCC` | 48.59 MB | 65.79 MB | 105.1% | 102.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0351s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0900s | 0.0941s | -0.0041s | improved |
| `ngap_rel18.6_specs` | 0.0633s | 0.0689s | -0.0056s | improved |
| `lteNRRCC` | 0.1180s | 0.1286s | -0.0106s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.61 MB | 83.3% | 107.7% |
| `f1ap_rel18.6_specs` | 34.66 MB | 164.63 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.42 MB | 117.77 MB | 104.2% | 102.4% |
| `lteNRRCC` | 74.76 MB | 101.97 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0246s | 0.0314s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.0720s | 0.0690s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0610s | 0.0507s | +0.0103s | worse |
| `lteNRRCC` | 0.0805s | 0.0862s | -0.0057s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.72 MB | 8.22 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.05 MB | 3.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.88 MB | 7.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.72 MB | 7.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0366s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1073s | 0.1011s | +0.0062s | worse |
| `ngap_rel18.6_specs` | 0.0734s | 0.0708s | +0.0026s | worse |
| `lteNRRCC` | 0.1369s | 0.1098s | +0.0271s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.57 MB | 7.34 MB | 201.3% | 83.6% |
| `f1ap_rel18.6_specs` | 8.04 MB | 106.64 MB | 164.9% | 230.6% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.30 MB | 227.2% | 103.1% |
| `lteNRRCC` | 51.84 MB | 69.62 MB | 109.3% | 161.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0446s | 0.0418s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1114s | 0.1243s | -0.0129s | improved |
| `ngap_rel18.6_specs` | 0.0779s | 0.0846s | -0.0067s | improved |
| `lteNRRCC` | 0.1271s | 0.1383s | -0.0112s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.91 MB | 8.27 MB | 113.4% | 162.4% |
| `f1ap_rel18.6_specs` | 9.66 MB | 164.20 MB | 161.5% | 163.6% |
| `ngap_rel18.6_specs` | 8.77 MB | 10.66 MB | 160.5% | 115.9% |
| `lteNRRCC` | 9.30 MB | 77.33 MB | 117.3% | 159.6% |
<!-- BENCH_RESULTS_END -->
