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
Generated: 2026-07-22T11:53:02.487038+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0336s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1067s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0749s | 0.0744s | +0.0005s | worse |
| `lteNRRCC` | 0.1181s | 0.1166s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 82.6% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 106.4% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.3% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0269s | +0.0068s | worse |
| `f1ap_rel18.6_specs` | 0.0911s | 0.0719s | +0.0192s | worse |
| `ngap_rel18.6_specs` | 0.0636s | 0.0507s | +0.0129s | worse |
| `lteNRRCC` | 0.1233s | 0.0988s | +0.0245s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.47 MB | 17.4% | 110.7% |
| `f1ap_rel18.6_specs` | 22.31 MB | 103.44 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.11 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.77 MB | 65.90 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0392s | -0.0062s | improved |
| `f1ap_rel18.6_specs` | 0.0884s | 0.1045s | -0.0161s | improved |
| `ngap_rel18.6_specs` | 0.0620s | 0.0719s | -0.0099s | improved |
| `lteNRRCC` | 0.1151s | 0.1187s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 55.71 MB | 84.0% | 111.5% |
| `f1ap_rel18.6_specs` | 34.20 MB | 164.68 MB | 110.3% | 103.6% |
| `ngap_rel18.6_specs` | 24.21 MB | 117.23 MB | 108.3% | 104.9% |
| `lteNRRCC` | 74.84 MB | 102.62 MB | 105.3% | 104.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0306s | 0.0296s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.0862s | 0.0856s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0613s | 0.0576s | +0.0037s | worse |
| `lteNRRCC` | 0.0990s | 0.0770s | +0.0220s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.66 MB | 4.70 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.80 MB | 7.70 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 368 KB | 4.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.89 MB | 4.58 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0418s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1116s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0765s | 0.0769s | -0.0004s | improved |
| `lteNRRCC` | 0.1373s | 0.1410s | -0.0037s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.56 MB | 7.36 MB | 93.3% | 90.1% |
| `f1ap_rel18.6_specs` | 8.55 MB | 106.64 MB | 114.7% | 105.6% |
| `ngap_rel18.6_specs` | 8.18 MB | 7.55 MB | 224.0% | 81.2% |
| `lteNRRCC` | 47.63 MB | 70.55 MB | 160.3% | 161.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0449s | 0.0371s | +0.0078s | worse |
| `f1ap_rel18.6_specs` | 0.1333s | 0.1041s | +0.0292s | worse |
| `ngap_rel18.6_specs` | 0.0932s | 0.0729s | +0.0203s | worse |
| `lteNRRCC` | 0.1315s | 0.1148s | +0.0167s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.09 MB | 10.09 MB | 87.0% | 81.8% |
| `f1ap_rel18.6_specs` | 10.38 MB | 119.15 MB | 112.0% | 162.0% |
| `ngap_rel18.6_specs` | 10.20 MB | 10.51 MB | 156.8% | 79.3% |
| `lteNRRCC` | 73.78 MB | 101.72 MB | 110.2% | 112.2% |
<!-- BENCH_RESULTS_END -->
