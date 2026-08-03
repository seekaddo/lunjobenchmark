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
Generated: 2026-08-03T23:10:32.557818+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0349s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1081s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0752s | 0.0743s | +0.0009s | worse |
| `lteNRRCC` | 0.1194s | 0.1189s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.60 MB | 53.55 MB | 81.8% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0358s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0927s | 0.0962s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0677s | -0.0024s | improved |
| `lteNRRCC` | 0.1256s | 0.1302s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.19 MB | 36.68 MB | 18.0% | 103.6% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.37 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.35 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.83 MB | 65.89 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0352s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0944s | 0.0938s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0660s | 0.0651s | +0.0009s | worse |
| `lteNRRCC` | 0.1283s | 0.1187s | +0.0096s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.49 MB | 55.68 MB | 77.8% | 103.6% |
| `f1ap_rel18.6_specs` | 34.33 MB | 164.48 MB | 106.7% | 103.5% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.24 MB | 108.0% | 104.8% |
| `lteNRRCC` | 74.77 MB | 102.65 MB | 103.2% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0239s | 0.0183s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.0716s | 0.0774s | -0.0058s | improved |
| `ngap_rel18.6_specs` | 0.0495s | 0.0516s | -0.0021s | improved |
| `lteNRRCC` | 0.0805s | 0.0917s | -0.0112s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.27 MB | 4.31 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 5.69 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.48 MB | 2.94 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.83 MB | 4.08 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0415s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1127s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0790s | -0.0023s | improved |
| `lteNRRCC` | 0.1409s | 0.1394s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.50 MB | 0.0% | 80.8% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.24 MB | 79.3% | 78.2% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.88 MB | 171.3% | 154.9% |
| `lteNRRCC` | 51.09 MB | 52.00 MB | 153.0% | 106.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0414s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1215s | -0.0098s | improved |
| `ngap_rel18.6_specs` | 0.0790s | 0.0849s | -0.0059s | improved |
| `lteNRRCC` | 0.1281s | 0.1370s | -0.0089s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.66 MB | 0.0% | 156.9% |
| `f1ap_rel18.6_specs` | 9.74 MB | 164.19 MB | 160.7% | 159.0% |
| `ngap_rel18.6_specs` | 8.76 MB | 10.36 MB | 160.7% | 111.7% |
| `lteNRRCC` | 8.55 MB | 74.05 MB | 158.2% | 109.2% |
<!-- BENCH_RESULTS_END -->
