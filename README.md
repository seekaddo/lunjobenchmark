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
Generated: 2026-06-02T14:13:45.744130+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0341s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1113s | 0.1065s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0760s | 0.0743s | +0.0017s | worse |
| `lteNRRCC` | 0.1194s | 0.1175s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 18.4% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0368s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0947s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0664s | -0.0011s | improved |
| `lteNRRCC` | 0.1284s | 0.1286s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 36.63 MB | 65.7% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.98 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.64 MB | 74.45 MB | 111.1% | 106.8% |
| `lteNRRCC` | 47.64 MB | 66.22 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0340s | +0.0055s | worse |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0890s | +0.0071s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0618s | +0.0040s | worse |
| `lteNRRCC` | 0.1279s | 0.1160s | +0.0119s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.46 MB | 96.2% | 110.3% |
| `f1ap_rel18.6_specs` | 34.71 MB | 164.50 MB | 109.4% | 106.9% |
| `ngap_rel18.6_specs` | 23.83 MB | 117.81 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.94 MB | 102.82 MB | 104.7% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0154s | 0.0186s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.0693s | 0.0678s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0471s | 0.0575s | -0.0104s | improved |
| `lteNRRCC` | 0.0782s | 0.0752s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.34 MB | 5.61 MB | 0.6% | 0.0% |
| `f1ap_rel18.6_specs` | 3.89 MB | 3.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.28 MB | 4.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.95 MB | 3.75 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0357s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1008s | +0.0102s | worse |
| `ngap_rel18.6_specs` | 0.0783s | 0.0672s | +0.0111s | worse |
| `lteNRRCC` | 0.1399s | 0.1171s | +0.0228s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.69 MB | 7.82 MB | 172.4% | 172.8% |
| `f1ap_rel18.6_specs` | 8.42 MB | 106.63 MB | 165.0% | 168.5% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.12 MB | 164.9% | 156.5% |
| `lteNRRCC` | 48.70 MB | 70.56 MB | 164.5% | 162.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0463s | 0.0524s | -0.0061s | improved |
| `f1ap_rel18.6_specs` | 0.1288s | 0.1490s | -0.0202s | improved |
| `ngap_rel18.6_specs` | 0.0909s | 0.1063s | -0.0154s | improved |
| `lteNRRCC` | 0.1485s | 0.1438s | +0.0047s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.03 MB | 10.09 MB | 155.8% | 156.6% |
| `f1ap_rel18.6_specs` | 10.51 MB | 12.72 MB | 156.5% | 82.6% |
| `ngap_rel18.6_specs` | 9.21 MB | 9.83 MB | 149.1% | 155.7% |
| `lteNRRCC` | 8.81 MB | 101.72 MB | 158.0% | 108.2% |
<!-- BENCH_RESULTS_END -->
