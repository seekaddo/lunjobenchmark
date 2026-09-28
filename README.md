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
Generated: 2026-09-28T00:28:53.140276+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0351s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1093s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0748s | +0.0019s | worse |
| `lteNRRCC` | 0.1197s | 0.1189s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 14.6% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0368s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0994s | 0.1000s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0677s | 0.0723s | -0.0046s | improved |
| `lteNRRCC` | 0.1325s | 0.1328s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.46 MB | 81.5% | 107.1% |
| `f1ap_rel18.6_specs` | 22.37 MB | 103.39 MB | 106.2% | 101.7% |
| `ngap_rel18.6_specs` | 17.89 MB | 74.26 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.52 MB | 65.71 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0292s | +0.0090s | worse |
| `f1ap_rel18.6_specs` | 0.0990s | 0.0769s | +0.0221s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0533s | +0.0159s | worse |
| `lteNRRCC` | 0.1334s | 0.1018s | +0.0316s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.76 MB | 85.2% | 103.3% |
| `f1ap_rel18.6_specs` | 34.39 MB | 164.75 MB | 103.1% | 103.4% |
| `ngap_rel18.6_specs` | 24.07 MB | 117.60 MB | 107.7% | 102.2% |
| `lteNRRCC` | 74.64 MB | 101.84 MB | 101.5% | 102.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0253s | 0.0460s | -0.0207s | improved |
| `f1ap_rel18.6_specs` | 0.0792s | 0.0663s | +0.0129s | worse |
| `ngap_rel18.6_specs` | 0.0489s | 0.0510s | -0.0021s | improved |
| `lteNRRCC` | 0.0802s | 0.0810s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.34 MB | 5.30 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.94 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.86 MB | 5.08 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.20 MB | 7.39 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0385s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.0983s | 0.1056s | -0.0073s | improved |
| `ngap_rel18.6_specs` | 0.0688s | 0.0733s | -0.0045s | improved |
| `lteNRRCC` | 0.1186s | 0.1379s | -0.0193s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.23 MB | 8.02 MB | 123.3% | 201.4% |
| `f1ap_rel18.6_specs` | 8.84 MB | 8.77 MB | 98.9% | 199.1% |
| `ngap_rel18.6_specs` | 8.81 MB | 8.21 MB | 132.4% | 112.0% |
| `lteNRRCC` | 8.64 MB | 68.83 MB | 195.0% | 101.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0461s | 0.0405s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.1292s | 0.1167s | +0.0125s | worse |
| `ngap_rel18.6_specs` | 0.0919s | 0.0795s | +0.0124s | worse |
| `lteNRRCC` | 0.1391s | 0.1294s | +0.0097s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.31 MB | 10.37 MB | 102.1% | 156.9% |
| `f1ap_rel18.6_specs` | 10.55 MB | 132.39 MB | 215.0% | 167.4% |
| `ngap_rel18.6_specs` | 10.16 MB | 10.79 MB | 160.2% | 222.6% |
| `lteNRRCC` | 72.62 MB | 76.79 MB | 216.6% | 105.5% |
<!-- BENCH_RESULTS_END -->
