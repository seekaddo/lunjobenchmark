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
Generated: 2026-08-12T11:03:54.201798+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0350s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1066s | 0.1105s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0741s | 0.0754s | -0.0013s | improved |
| `lteNRRCC` | 0.1180s | 0.1189s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 77.3% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 100.0% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0267s | 0.0360s | -0.0093s | improved |
| `f1ap_rel18.6_specs` | 0.0755s | 0.0974s | -0.0219s | improved |
| `ngap_rel18.6_specs` | 0.0514s | 0.0675s | -0.0161s | improved |
| `lteNRRCC` | 0.0961s | 0.1318s | -0.0357s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.42 MB | 35.65 MB | 29.3% | 105.0% |
| `f1ap_rel18.6_specs` | 22.09 MB | 103.36 MB | 104.3% | 102.1% |
| `ngap_rel18.6_specs` | 19.39 MB | 73.71 MB | 110.0% | 103.1% |
| `lteNRRCC` | 48.66 MB | 66.16 MB | 102.2% | 101.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0284s | 0.0244s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.0761s | 0.0826s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0587s | 0.0561s | +0.0026s | worse |
| `lteNRRCC` | 0.1015s | 0.0912s | +0.0103s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.37 MB | 55.57 MB | 66.7% | 104.5% |
| `f1ap_rel18.6_specs` | 34.62 MB | 164.51 MB | 104.2% | 100.0% |
| `ngap_rel18.6_specs` | 24.04 MB | 117.86 MB | 105.0% | 105.9% |
| `lteNRRCC` | 74.79 MB | 102.79 MB | 102.0% | 103.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0326s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.0799s | 0.1239s | -0.0440s | improved |
| `ngap_rel18.6_specs` | 0.0446s | 0.0563s | -0.0117s | improved |
| `lteNRRCC` | 0.0764s | 0.1115s | -0.0351s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.75 MB | 4.34 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 4.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.83 MB | 4.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.66 MB | 4.42 MB | 0.3% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0384s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1060s | 0.1073s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0732s | 0.0755s | -0.0023s | improved |
| `lteNRRCC` | 0.1363s | 0.1377s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.36 MB | 0.0% | 81.3% |
| `f1ap_rel18.6_specs` | 8.11 MB | 7.98 MB | 164.0% | 165.1% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.55 MB | 173.2% | 163.5% |
| `lteNRRCC` | 48.70 MB | 48.57 MB | 108.9% | 166.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0349s | +0.0066s | worse |
| `f1ap_rel18.6_specs` | 0.1293s | 0.1031s | +0.0262s | worse |
| `ngap_rel18.6_specs` | 0.0839s | 0.0722s | +0.0117s | worse |
| `lteNRRCC` | 0.1406s | 0.1126s | +0.0280s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 9.52 MB | 0.0% | 160.5% |
| `f1ap_rel18.6_specs` | 11.05 MB | 164.20 MB | 216.0% | 108.0% |
| `ngap_rel18.6_specs` | 9.21 MB | 10.45 MB | 176.3% | 154.5% |
| `lteNRRCC` | 73.78 MB | 101.72 MB | 220.3% | 170.3% |
<!-- BENCH_RESULTS_END -->
