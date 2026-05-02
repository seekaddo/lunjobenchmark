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
Generated: 2026-05-02T10:58:04.010215+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0371s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1144s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0757s | 0.0782s | -0.0025s | improved |
| `lteNRRCC` | 0.1204s | 0.1224s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 28.2% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0337s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.0924s | 0.0924s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0639s | 0.0737s | -0.0098s | improved |
| `lteNRRCC` | 0.1236s | 0.1271s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.26 MB | 36.70 MB | 28.7% | 110.3% |
| `f1ap_rel18.6_specs` | 21.79 MB | 103.37 MB | 109.4% | 107.0% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.55 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.68 MB | 65.32 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0337s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0908s | 0.0899s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0625s | 0.0640s | -0.0015s | improved |
| `lteNRRCC` | 0.1160s | 0.1164s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.21 MB | 63.2% | 110.7% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.54 MB | 110.0% | 103.6% |
| `ngap_rel18.6_specs` | 24.05 MB | 117.80 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.35 MB | 102.63 MB | 104.8% | 105.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0228s | 0.0198s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.0808s | 0.0619s | +0.0189s | worse |
| `ngap_rel18.6_specs` | 0.0446s | 0.0400s | +0.0046s | worse |
| `lteNRRCC` | 0.0734s | 0.0674s | +0.0060s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 4.02 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.92 MB | 4.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.42 MB | 5.67 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.92 MB | 3.97 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0337s | +0.0058s | worse |
| `f1ap_rel18.6_specs` | 0.1093s | 0.0956s | +0.0137s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0682s | +0.0085s | worse |
| `lteNRRCC` | 0.1438s | 0.1138s | +0.0300s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.81 MB | 89.4% | 86.3% |
| `f1ap_rel18.6_specs` | 8.41 MB | 8.43 MB | 92.9% | 100.8% |
| `ngap_rel18.6_specs` | 7.91 MB | 7.67 MB | 157.4% | 178.0% |
| `lteNRRCC` | 8.16 MB | 49.77 MB | 154.6% | 155.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0392s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1107s | 0.1118s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0860s | 0.0770s | +0.0090s | worse |
| `lteNRRCC` | 0.1319s | 0.1267s | +0.0052s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.02 MB | 8.45 MB | 116.3% | 161.9% |
| `f1ap_rel18.6_specs` | 9.61 MB | 162.27 MB | 156.4% | 162.9% |
| `ngap_rel18.6_specs` | 8.70 MB | 10.69 MB | 80.2% | 226.3% |
| `lteNRRCC` | 72.45 MB | 88.88 MB | 153.7% | 106.0% |
<!-- BENCH_RESULTS_END -->
