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
Generated: 2026-06-01T23:39:53.852777+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0376s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.1065s | 0.1153s | -0.0088s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0789s | -0.0046s | improved |
| `lteNRRCC` | 0.1175s | 0.1227s | -0.0052s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 20.6% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0368s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0990s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0664s | 0.0698s | -0.0034s | improved |
| `lteNRRCC` | 0.1286s | 0.1326s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.21 MB | 36.09 MB | 79.3% | 110.7% |
| `f1ap_rel18.6_specs` | 21.64 MB | 103.03 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.39 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.79 MB | 66.20 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0347s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0890s | 0.0922s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0637s | -0.0019s | improved |
| `lteNRRCC` | 0.1160s | 0.1184s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.38 MB | 16.2% | 111.1% |
| `f1ap_rel18.6_specs` | 35.26 MB | 164.77 MB | 110.3% | 107.4% |
| `ngap_rel18.6_specs` | 24.11 MB | 117.80 MB | 112.5% | 107.0% |
| `lteNRRCC` | 75.02 MB | 102.51 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0186s | 0.0312s | -0.0126s | improved |
| `f1ap_rel18.6_specs` | 0.0678s | 0.0661s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0575s | 0.0434s | +0.0141s | worse |
| `lteNRRCC` | 0.0752s | 0.0684s | +0.0068s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.48 MB | 4.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.58 MB | 4.02 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.92 MB | 4.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.83 MB | 3.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0428s | -0.0071s | improved |
| `f1ap_rel18.6_specs` | 0.1008s | 0.1062s | -0.0054s | improved |
| `ngap_rel18.6_specs` | 0.0672s | 0.0748s | -0.0076s | improved |
| `lteNRRCC` | 0.1171s | 0.1260s | -0.0089s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.90 MB | 140.6% | 133.6% |
| `f1ap_rel18.6_specs` | 8.44 MB | 106.65 MB | 101.6% | 113.5% |
| `ngap_rel18.6_specs` | 8.11 MB | 7.98 MB | 211.9% | 105.3% |
| `lteNRRCC` | 8.29 MB | 53.32 MB | 101.5% | 142.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0524s | 0.0391s | +0.0133s | worse |
| `f1ap_rel18.6_specs` | 0.1490s | 0.1158s | +0.0332s | worse |
| `ngap_rel18.6_specs` | 0.1063s | 0.0805s | +0.0258s | worse |
| `lteNRRCC` | 0.1438s | 0.1319s | +0.0119s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.07 MB | 10.14 MB | 157.7% | 96.0% |
| `f1ap_rel18.6_specs` | 9.86 MB | 10.12 MB | 156.2% | 159.2% |
| `ngap_rel18.6_specs` | 9.26 MB | 9.40 MB | 76.5% | 98.4% |
| `lteNRRCC` | 8.30 MB | 101.67 MB | 109.5% | 150.9% |
<!-- BENCH_RESULTS_END -->
