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
Generated: 2026-09-01T01:10:33.164029+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0358s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1119s | -0.0041s | improved |
| `ngap_rel18.6_specs` | 0.0746s | 0.0777s | -0.0031s | improved |
| `lteNRRCC` | 0.1179s | 0.1214s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 14.3% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0311s | 0.0197s | +0.0114s | worse |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0548s | +0.0364s | worse |
| `ngap_rel18.6_specs` | 0.0616s | 0.0387s | +0.0229s | worse |
| `lteNRRCC` | 0.1106s | 0.0700s | +0.0406s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 36.71 MB | 77.3% | 104.3% |
| `f1ap_rel18.6_specs` | 22.29 MB | 102.95 MB | 103.8% | 103.8% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.40 MB | 104.8% | 102.6% |
| `lteNRRCC` | 48.84 MB | 66.41 MB | 103.8% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0374s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0908s | 0.0975s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0625s | 0.0699s | -0.0074s | improved |
| `lteNRRCC` | 0.1166s | 0.1225s | -0.0059s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.25 MB | 71.4% | 103.8% |
| `f1ap_rel18.6_specs` | 34.68 MB | 163.72 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.30 MB | 117.34 MB | 104.2% | 104.9% |
| `lteNRRCC` | 74.96 MB | 102.61 MB | 101.8% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0250s | +0.0078s | worse |
| `f1ap_rel18.6_specs` | 0.1138s | 0.0769s | +0.0369s | worse |
| `ngap_rel18.6_specs` | 0.0634s | 0.0548s | +0.0086s | worse |
| `lteNRRCC` | 0.1098s | 0.0876s | +0.0222s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.16 MB | 9.41 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.34 MB | 1.19 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.31 MB | 4.17 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.17 MB | 4.12 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0452s | 0.0427s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.1254s | 0.1102s | +0.0152s | worse |
| `ngap_rel18.6_specs` | 0.0870s | 0.0788s | +0.0082s | worse |
| `lteNRRCC` | 0.1584s | 0.1378s | +0.0206s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.19 MB | 7.81 MB | 0.0% | 144.8% |
| `f1ap_rel18.6_specs` | 8.62 MB | 8.42 MB | 154.5% | 72.9% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.12 MB | 139.0% | 144.4% |
| `lteNRRCC` | 46.95 MB | 68.93 MB | 189.7% | 144.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0433s | -0.0061s | improved |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1268s | -0.0184s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0862s | -0.0086s | improved |
| `lteNRRCC` | 0.1228s | 0.1287s | -0.0059s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.79 MB | 0.0% | 160.8% |
| `f1ap_rel18.6_specs` | 10.12 MB | 11.27 MB | 160.3% | 225.7% |
| `ngap_rel18.6_specs` | 9.21 MB | 10.95 MB | 161.2% | 113.9% |
| `lteNRRCC` | 8.62 MB | 98.57 MB | 160.5% | 157.6% |
<!-- BENCH_RESULTS_END -->
