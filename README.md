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
Generated: 2026-05-01T22:55:47.869706+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0372s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1147s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0782s | 0.0786s | -0.0004s | improved |
| `lteNRRCC` | 0.1224s | 0.1229s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 27.7% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 106.7% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0315s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0924s | 0.0930s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0737s | 0.0652s | +0.0085s | worse |
| `lteNRRCC` | 0.1271s | 0.1154s | +0.0117s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.25 MB | 25.5% | 110.0% |
| `f1ap_rel18.6_specs` | 22.21 MB | 102.96 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.80 MB | 74.49 MB | 114.8% | 106.8% |
| `lteNRRCC` | 48.60 MB | 66.28 MB | 106.3% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0357s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0899s | 0.0959s | -0.0060s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0662s | -0.0022s | improved |
| `lteNRRCC` | 0.1164s | 0.1301s | -0.0137s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.77 MB | 21.5% | 111.1% |
| `f1ap_rel18.6_specs` | 33.74 MB | 164.69 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.68 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.49 MB | 101.97 MB | 105.1% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0198s | 0.0182s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0619s | 0.0674s | -0.0055s | improved |
| `ngap_rel18.6_specs` | 0.0400s | 0.0403s | -0.0003s | improved |
| `lteNRRCC` | 0.0674s | 0.0676s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.06 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.03 MB | 6.77 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.94 MB | 4.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.78 MB | 3.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0412s | -0.0075s | improved |
| `f1ap_rel18.6_specs` | 0.0956s | 0.1100s | -0.0144s | improved |
| `ngap_rel18.6_specs` | 0.0682s | 0.0769s | -0.0087s | improved |
| `lteNRRCC` | 0.1138s | 0.1290s | -0.0152s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.04 MB | 7.89 MB | 138.5% | 139.2% |
| `f1ap_rel18.6_specs` | 8.73 MB | 106.64 MB | 136.8% | 103.0% |
| `ngap_rel18.6_specs` | 8.23 MB | 8.26 MB | 140.0% | 137.1% |
| `lteNRRCC` | 8.66 MB | 65.79 MB | 133.5% | 103.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0389s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1124s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0767s | +0.0003s | worse |
| `lteNRRCC` | 0.1267s | 0.1317s | -0.0050s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.45 MB | 8.57 MB | 160.2% | 160.4% |
| `f1ap_rel18.6_specs` | 10.64 MB | 9.55 MB | 105.5% | 80.0% |
| `ngap_rel18.6_specs` | 9.20 MB | 8.95 MB | 100.2% | 160.5% |
| `lteNRRCC` | 8.43 MB | 86.99 MB | 80.3% | 111.2% |
<!-- BENCH_RESULTS_END -->
