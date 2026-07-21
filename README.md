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
Generated: 2026-07-21T23:03:13.855955+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0346s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1067s | 0.1074s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0744s | 0.0736s | +0.0008s | worse |
| `lteNRRCC` | 0.1166s | 0.1164s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 67.9% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.7% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.3% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0269s | 0.0333s | -0.0064s | improved |
| `f1ap_rel18.6_specs` | 0.0719s | 0.0912s | -0.0193s | improved |
| `ngap_rel18.6_specs` | 0.0507s | 0.0638s | -0.0131s | improved |
| `lteNRRCC` | 0.0988s | 0.1224s | -0.0236s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.21 MB | 36.23 MB | 13.5% | 109.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.46 MB | 108.0% | 104.4% |
| `ngap_rel18.6_specs` | 19.20 MB | 74.11 MB | 115.0% | 105.9% |
| `lteNRRCC` | 48.81 MB | 65.99 MB | 104.2% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0366s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1045s | 0.0953s | +0.0092s | worse |
| `ngap_rel18.6_specs` | 0.0719s | 0.0660s | +0.0059s | worse |
| `lteNRRCC` | 0.1187s | 0.1306s | -0.0119s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.43 MB | 55.46 MB | 73.1% | 107.4% |
| `f1ap_rel18.6_specs` | 35.16 MB | 163.54 MB | 107.1% | 105.0% |
| `ngap_rel18.6_specs` | 23.62 MB | 117.66 MB | 109.1% | 106.8% |
| `lteNRRCC` | 74.73 MB | 102.90 MB | 103.6% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0296s | 0.0257s | +0.0039s | worse |
| `f1ap_rel18.6_specs` | 0.0856s | 0.0757s | +0.0099s | worse |
| `ngap_rel18.6_specs` | 0.0576s | 0.0476s | +0.0100s | worse |
| `lteNRRCC` | 0.0770s | 0.0708s | +0.0062s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.72 MB | 4.70 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.03 MB | 8.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 7.69 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.48 MB | 5.41 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0418s | 0.0415s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1155s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0782s | -0.0013s | improved |
| `lteNRRCC` | 0.1410s | 0.1270s | +0.0140s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.69 MB | 7.75 MB | 153.9% | 152.1% |
| `f1ap_rel18.6_specs` | 8.52 MB | 8.18 MB | 98.0% | 150.6% |
| `ngap_rel18.6_specs` | 7.90 MB | 7.91 MB | 156.6% | 156.1% |
| `lteNRRCC` | 47.51 MB | 58.86 MB | 111.2% | 107.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0394s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1041s | 0.1109s | -0.0068s | improved |
| `ngap_rel18.6_specs` | 0.0729s | 0.0791s | -0.0062s | improved |
| `lteNRRCC` | 0.1148s | 0.1257s | -0.0109s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.53 MB | 9.77 MB | 132.4% | 107.1% |
| `f1ap_rel18.6_specs` | 10.57 MB | 142.79 MB | 126.5% | 108.3% |
| `ngap_rel18.6_specs` | 10.12 MB | 10.81 MB | 101.7% | 134.7% |
| `lteNRRCC` | 8.90 MB | 82.70 MB | 101.1% | 197.2% |
<!-- BENCH_RESULTS_END -->
