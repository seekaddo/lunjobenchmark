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
Generated: 2026-10-22T00:32:58.206810+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0381s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1217s | 0.1188s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0845s | 0.0819s | +0.0026s | worse |
| `lteNRRCC` | 0.1264s | 0.1265s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.98 MB | 53.55 MB | 66.7% | 103.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 101.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0396s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1238s | -0.0081s | improved |
| `ngap_rel18.6_specs` | 0.0804s | 0.0820s | -0.0016s | improved |
| `lteNRRCC` | 0.1303s | 0.1288s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 34.65 MB | 64.3% | 107.4% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 18.14 MB | 72.65 MB | 104.5% | 102.1% |
| `lteNRRCC` | 46.66 MB | 64.21 MB | 101.7% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0431s | 0.0565s | -0.0134s | improved |
| `f1ap_rel18.6_specs` | 0.0968s | 0.1686s | -0.0718s | improved |
| `ngap_rel18.6_specs` | 0.0671s | 0.1213s | -0.0542s | improved |
| `lteNRRCC` | 0.1297s | 0.1643s | -0.0346s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.71 MB | 87.5% | 107.1% |
| `f1ap_rel18.6_specs` | 35.16 MB | 164.68 MB | 106.7% | 103.5% |
| `ngap_rel18.6_specs` | 24.31 MB | 117.75 MB | 108.0% | 104.7% |
| `lteNRRCC` | 74.59 MB | 102.86 MB | 101.6% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0518s | 0.0361s | +0.0157s | worse |
| `f1ap_rel18.6_specs` | 0.0917s | 0.1106s | -0.0189s | improved |
| `ngap_rel18.6_specs` | 0.0704s | 0.0537s | +0.0167s | worse |
| `lteNRRCC` | 0.0760s | 0.0868s | -0.0108s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 7.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.92 MB | 8.67 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.81 MB | 8.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.34 MB | 7.56 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0374s | -0.0040s | improved |
| `f1ap_rel18.6_specs` | 0.0955s | 0.1043s | -0.0088s | improved |
| `ngap_rel18.6_specs` | 0.0655s | 0.0722s | -0.0067s | improved |
| `lteNRRCC` | 0.1133s | 0.1140s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.30 MB | 7.93 MB | 0.0% | 139.9% |
| `f1ap_rel18.6_specs` | 8.70 MB | 8.76 MB | 123.0% | 121.9% |
| `ngap_rel18.6_specs` | 8.32 MB | 8.26 MB | 134.7% | 213.7% |
| `lteNRRCC` | 8.44 MB | 51.95 MB | 99.4% | 104.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0387s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1135s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0778s | -0.0007s | improved |
| `lteNRRCC` | 0.1291s | 0.1251s | +0.0040s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 8.83 MB | 0.0% | 154.9% |
| `f1ap_rel18.6_specs` | 10.28 MB | 9.97 MB | 99.0% | 79.1% |
| `ngap_rel18.6_specs` | 8.75 MB | 10.50 MB | 158.7% | 111.0% |
| `lteNRRCC` | 73.75 MB | 72.44 MB | 174.8% | 159.0% |
<!-- BENCH_RESULTS_END -->
