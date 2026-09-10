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
Generated: 2026-09-10T14:13:25.487258+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0359s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1163s | 0.1132s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0794s | 0.0776s | +0.0018s | worse |
| `lteNRRCC` | 0.1239s | 0.1213s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 90.9% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0283s | 0.0344s | -0.0061s | improved |
| `f1ap_rel18.6_specs` | 0.0755s | 0.0932s | -0.0177s | improved |
| `ngap_rel18.6_specs` | 0.0518s | 0.0661s | -0.0143s | improved |
| `lteNRRCC` | 0.0985s | 0.1281s | -0.0296s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.78 MB | 36.62 MB | 85.0% | 104.5% |
| `f1ap_rel18.6_specs` | 21.82 MB | 103.38 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 18.02 MB | 74.55 MB | 110.0% | 102.9% |
| `lteNRRCC` | 48.71 MB | 66.52 MB | 102.1% | 101.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0354s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0905s | 0.0950s | -0.0045s | improved |
| `ngap_rel18.6_specs` | 0.0641s | 0.0654s | -0.0013s | improved |
| `lteNRRCC` | 0.1174s | 0.1199s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 55.29 MB | 79.2% | 107.7% |
| `f1ap_rel18.6_specs` | 35.23 MB | 164.74 MB | 103.6% | 103.7% |
| `ngap_rel18.6_specs` | 24.56 MB | 117.56 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.84 MB | 102.93 MB | 101.8% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0469s | -0.0140s | improved |
| `f1ap_rel18.6_specs` | 0.1025s | 0.0932s | +0.0093s | worse |
| `ngap_rel18.6_specs` | 0.0887s | 0.0614s | +0.0273s | worse |
| `lteNRRCC` | 0.1013s | 0.1009s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.98 MB | 7.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.36 MB | 9.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.73 MB | 2.66 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.66 MB | 7.48 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0379s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1045s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0745s | 0.0731s | +0.0014s | worse |
| `lteNRRCC` | 0.1375s | 0.1362s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.74 MB | 7.30 MB | 111.1% | 84.3% |
| `f1ap_rel18.6_specs` | 8.17 MB | 106.65 MB | 82.4% | 165.8% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.54 MB | 164.2% | 95.3% |
| `lteNRRCC` | 51.21 MB | 50.74 MB | 224.6% | 111.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0384s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1123s | 0.1101s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0818s | 0.0773s | +0.0045s | worse |
| `lteNRRCC` | 0.1398s | 0.1271s | +0.0127s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.59 MB | 8.52 MB | 0.0% | 161.4% |
| `f1ap_rel18.6_specs` | 9.62 MB | 164.20 MB | 159.4% | 160.8% |
| `ngap_rel18.6_specs` | 9.18 MB | 8.96 MB | 148.2% | 80.6% |
| `lteNRRCC` | 8.44 MB | 94.64 MB | 157.3% | 109.9% |
<!-- BENCH_RESULTS_END -->
