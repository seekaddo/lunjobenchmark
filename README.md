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
Generated: 2026-07-26T23:03:50.484727+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0369s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1142s | 0.1132s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0801s | 0.0770s | +0.0031s | worse |
| `lteNRRCC` | 0.1241s | 0.1219s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.73 MB | 53.55 MB | 21.5% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0346s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1001s | 0.0939s | +0.0062s | worse |
| `ngap_rel18.6_specs` | 0.0700s | 0.0658s | +0.0042s | worse |
| `lteNRRCC` | 0.1335s | 0.1273s | +0.0062s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 35.95 MB | 16.5% | 103.4% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.07 MB | 103.0% | 103.3% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.11 MB | 107.4% | 106.7% |
| `lteNRRCC` | 48.79 MB | 66.05 MB | 103.1% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0289s | +0.0083s | worse |
| `f1ap_rel18.6_specs` | 0.1050s | 0.0781s | +0.0269s | worse |
| `ngap_rel18.6_specs` | 0.0696s | 0.0539s | +0.0157s | worse |
| `lteNRRCC` | 0.1232s | 0.1033s | +0.0199s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 55.64 MB | 17.7% | 107.1% |
| `f1ap_rel18.6_specs` | 34.71 MB | 164.28 MB | 103.3% | 103.3% |
| `ngap_rel18.6_specs` | 24.38 MB | 117.64 MB | 104.0% | 104.3% |
| `lteNRRCC` | 74.50 MB | 102.94 MB | 103.3% | 102.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0229s | 0.0239s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0687s | 0.0677s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0483s | 0.0459s | +0.0024s | worse |
| `lteNRRCC` | 0.0770s | 0.0764s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.56 MB | 4.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 3.81 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.53 MB | 5.61 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.78 MB | 3.97 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0387s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.1183s | 0.1058s | +0.0125s | worse |
| `ngap_rel18.6_specs` | 0.0834s | 0.0780s | +0.0054s | worse |
| `lteNRRCC` | 0.1472s | 0.1366s | +0.0106s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.68 MB | 7.49 MB | 152.9% | 159.2% |
| `f1ap_rel18.6_specs` | 8.35 MB | 8.09 MB | 226.2% | 155.1% |
| `ngap_rel18.6_specs` | 7.16 MB | 8.16 MB | 95.5% | 148.6% |
| `lteNRRCC` | 8.08 MB | 70.55 MB | 78.6% | 157.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0431s | 0.0394s | +0.0037s | worse |
| `f1ap_rel18.6_specs` | 0.1249s | 0.1108s | +0.0141s | worse |
| `ngap_rel18.6_specs` | 0.0867s | 0.0766s | +0.0101s | worse |
| `lteNRRCC` | 0.1414s | 0.1308s | +0.0106s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.27 MB | 10.15 MB | 108.1% | 221.2% |
| `f1ap_rel18.6_specs` | 11.77 MB | 142.48 MB | 104.5% | 157.4% |
| `ngap_rel18.6_specs` | 9.55 MB | 9.55 MB | 78.3% | 157.6% |
| `lteNRRCC` | 73.15 MB | 83.79 MB | 158.1% | 156.7% |
<!-- BENCH_RESULTS_END -->
