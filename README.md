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
Generated: 2026-08-11T22:51:48.482713+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0338s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1093s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0754s | 0.0741s | +0.0013s | worse |
| `lteNRRCC` | 0.1189s | 0.1188s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 15.3% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0338s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0974s | 0.0965s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0675s | 0.0671s | +0.0004s | worse |
| `lteNRRCC` | 0.1318s | 0.1177s | +0.0141s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 36.49 MB | 72.4% | 107.4% |
| `f1ap_rel18.6_specs` | 22.28 MB | 103.29 MB | 103.1% | 101.7% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.44 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.61 MB | 66.50 MB | 103.1% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0244s | 0.0348s | -0.0104s | improved |
| `f1ap_rel18.6_specs` | 0.0826s | 0.0900s | -0.0074s | improved |
| `ngap_rel18.6_specs` | 0.0561s | 0.0623s | -0.0062s | improved |
| `lteNRRCC` | 0.0912s | 0.1223s | -0.0311s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.25 MB | 55.87 MB | 26.7% | 105.3% |
| `f1ap_rel18.6_specs` | 34.65 MB | 164.61 MB | 100.0% | 100.0% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.00 MB | 106.7% | 100.0% |
| `lteNRRCC` | 74.62 MB | 102.77 MB | 102.6% | 102.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0326s | 0.0297s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.1239s | 0.0845s | +0.0394s | worse |
| `ngap_rel18.6_specs` | 0.0563s | 0.0574s | -0.0011s | improved |
| `lteNRRCC` | 0.1115s | 0.0861s | +0.0254s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.28 MB | 7.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.91 MB | 163.61 MB | 1.2% | 23.7% |
| `ngap_rel18.6_specs` | 7.22 MB | 4.78 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.36 MB | 2.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0426s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.1073s | 0.1150s | -0.0077s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0799s | -0.0044s | improved |
| `lteNRRCC` | 0.1377s | 0.1425s | -0.0048s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.19 MB | 7.31 MB | 0.0% | 165.2% |
| `f1ap_rel18.6_specs` | 7.98 MB | 106.64 MB | 81.9% | 178.8% |
| `ngap_rel18.6_specs` | 8.08 MB | 7.45 MB | 115.0% | 164.9% |
| `lteNRRCC` | 51.84 MB | 51.52 MB | 164.8% | 108.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0423s | -0.0074s | improved |
| `f1ap_rel18.6_specs` | 0.1031s | 0.1153s | -0.0122s | improved |
| `ngap_rel18.6_specs` | 0.0722s | 0.0800s | -0.0078s | improved |
| `lteNRRCC` | 0.1126s | 0.1344s | -0.0218s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.17 MB | 0.0% | 103.6% |
| `f1ap_rel18.6_specs` | 9.99 MB | 156.41 MB | 203.4% | 135.3% |
| `ngap_rel18.6_specs` | 10.25 MB | 10.50 MB | 137.7% | 138.6% |
| `lteNRRCC` | 9.16 MB | 75.75 MB | 137.9% | 139.2% |
<!-- BENCH_RESULTS_END -->
