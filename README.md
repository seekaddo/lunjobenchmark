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
Generated: 2026-10-10T15:48:34.202937+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0347s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1078s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0745s | +0.0026s | worse |
| `lteNRRCC` | 0.1211s | 0.1178s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.98 MB | 53.55 MB | 79.2% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0339s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0905s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0673s | 0.0629s | +0.0044s | worse |
| `lteNRRCC` | 0.1291s | 0.1230s | +0.0061s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.25 MB | 80.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.33 MB | 103.36 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.91 MB | 74.67 MB | 104.0% | 102.4% |
| `lteNRRCC` | 48.41 MB | 65.73 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0232s | +0.0136s | worse |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0604s | +0.0359s | worse |
| `ngap_rel18.6_specs` | 0.0651s | 0.0404s | +0.0247s | worse |
| `lteNRRCC` | 0.1207s | 0.0749s | +0.0458s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 55.79 MB | 16.0% | 107.4% |
| `f1ap_rel18.6_specs` | 34.80 MB | 164.70 MB | 107.1% | 103.6% |
| `ngap_rel18.6_specs` | 24.50 MB | 117.12 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.04 MB | 102.94 MB | 101.8% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0275s | 0.0223s | +0.0052s | worse |
| `f1ap_rel18.6_specs` | 0.0968s | 0.1031s | -0.0063s | improved |
| `ngap_rel18.6_specs` | 0.0589s | 0.0868s | -0.0279s | improved |
| `lteNRRCC` | 0.0926s | 0.1268s | -0.0342s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.97 MB | 3.59 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.97 MB | 4.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.02 MB | 4.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.09 MB | 4.28 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0289s | +0.0114s | worse |
| `f1ap_rel18.6_specs` | 0.1115s | 0.0860s | +0.0255s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0574s | +0.0199s | worse |
| `lteNRRCC` | 0.1402s | 0.0931s | +0.0471s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.57 MB | 7.52 MB | 0.0% | 159.6% |
| `f1ap_rel18.6_specs` | 8.69 MB | 8.06 MB | 96.6% | 90.2% |
| `ngap_rel18.6_specs` | 7.87 MB | 8.00 MB | 156.4% | 148.6% |
| `lteNRRCC` | 51.35 MB | 63.25 MB | 105.5% | 105.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0489s | -0.0143s | improved |
| `f1ap_rel18.6_specs` | 0.0987s | 0.1422s | -0.0435s | improved |
| `ngap_rel18.6_specs` | 0.0719s | 0.0985s | -0.0266s | improved |
| `lteNRRCC` | 0.1116s | 0.1395s | -0.0279s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.26 MB | 0.0% | 133.2% |
| `f1ap_rel18.6_specs` | 10.05 MB | 164.14 MB | 206.1% | 107.8% |
| `ngap_rel18.6_specs` | 9.60 MB | 10.55 MB | 101.1% | 137.0% |
| `lteNRRCC` | 9.03 MB | 98.57 MB | 110.8% | 126.7% |
<!-- BENCH_RESULTS_END -->
