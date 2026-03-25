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
Generated: 2026-03-25T22:45:50.315763+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0365s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1175s | 0.1122s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0796s | 0.0784s | +0.0012s | worse |
| `lteNRRCC` | 0.1241s | 0.1214s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.94 MB | 53.55 MB | 26.6% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.5% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 114.8% | 107.4% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.8% | 105.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0324s | 0.0365s | -0.0041s | improved |
| `f1ap_rel18.6_specs` | 0.0944s | 0.0956s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0646s | 0.0682s | -0.0036s | improved |
| `lteNRRCC` | 0.1162s | 0.1296s | -0.0134s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.34 MB | 36.60 MB | 87.0% | 108.0% |
| `f1ap_rel18.6_specs` | 22.21 MB | 103.36 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 16.57 MB | 73.86 MB | 113.6% | 107.3% |
| `lteNRRCC` | 48.52 MB | 66.44 MB | 103.6% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0338s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0917s | 0.0902s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0630s | 0.0640s | -0.0010s | improved |
| `lteNRRCC` | 0.1156s | 0.1184s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.23 MB | 55.88 MB | 95.8% | 114.8% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.46 MB | 110.0% | 105.5% |
| `ngap_rel18.6_specs` | 24.05 MB | 117.72 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.82 MB | 102.67 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0195s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.0674s | 0.0583s | +0.0091s | worse |
| `ngap_rel18.6_specs` | 0.0734s | 0.0457s | +0.0277s | worse |
| `lteNRRCC` | 0.0952s | 0.0743s | +0.0209s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.50 MB | 7.09 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.14 MB | 1.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.89 MB | 3.73 MB | 0.0% | 0.0% |
| `lteNRRCC` | 1.28 MB | 1.77 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0388s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1063s | 0.1054s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0749s | 0.0744s | +0.0005s | worse |
| `lteNRRCC` | 0.1371s | 0.1379s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.68 MB | 7.49 MB | 111.6% | 80.5% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.23 MB | 160.2% | 168.9% |
| `ngap_rel18.6_specs` | 7.57 MB | 7.61 MB | 79.7% | 160.7% |
| `lteNRRCC` | 47.50 MB | 51.07 MB | 161.6% | 102.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0440s | 0.0382s | +0.0058s | worse |
| `f1ap_rel18.6_specs` | 0.1176s | 0.1122s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0826s | 0.0770s | +0.0056s | worse |
| `lteNRRCC` | 0.1295s | 0.1289s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.06 MB | 9.70 MB | 93.1% | 162.7% |
| `f1ap_rel18.6_specs` | 10.05 MB | 10.63 MB | 166.9% | 100.3% |
| `ngap_rel18.6_specs` | 9.86 MB | 10.49 MB | 225.3% | 110.2% |
| `lteNRRCC` | 9.35 MB | 99.57 MB | 118.5% | 110.4% |
<!-- BENCH_RESULTS_END -->
