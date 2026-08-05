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
Generated: 2026-08-05T12:03:32.231781+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0362s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1130s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0770s | -0.0002s | improved |
| `lteNRRCC` | 0.1207s | 0.1209s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 90.5% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0263s | 0.0378s | -0.0115s | improved |
| `f1ap_rel18.6_specs` | 0.0722s | 0.0978s | -0.0256s | improved |
| `ngap_rel18.6_specs` | 0.0496s | 0.0709s | -0.0213s | improved |
| `lteNRRCC` | 0.0965s | 0.1301s | -0.0336s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.23 MB | 36.73 MB | 72.0% | 104.8% |
| `f1ap_rel18.6_specs` | 22.34 MB | 102.61 MB | 100.0% | 102.3% |
| `ngap_rel18.6_specs` | 19.11 MB | 74.43 MB | 110.5% | 103.0% |
| `lteNRRCC` | 48.81 MB | 66.07 MB | 102.0% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0334s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0997s | 0.0886s | +0.0111s | worse |
| `ngap_rel18.6_specs` | 0.0679s | 0.0617s | +0.0062s | worse |
| `lteNRRCC` | 0.1216s | 0.1164s | +0.0052s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 55.70 MB | 53.1% | 104.2% |
| `f1ap_rel18.6_specs` | 34.04 MB | 164.75 MB | 104.0% | 101.8% |
| `ngap_rel18.6_specs` | 24.18 MB | 117.76 MB | 104.8% | 104.9% |
| `lteNRRCC` | 74.68 MB | 102.45 MB | 101.9% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0275s | 0.0233s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.0744s | 0.0685s | +0.0059s | worse |
| `ngap_rel18.6_specs` | 0.0523s | 0.0479s | +0.0044s | worse |
| `lteNRRCC` | 0.0805s | 0.0773s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.73 MB | 7.66 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.12 MB | 10.77 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.28 MB | 8.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.30 MB | 7.52 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0397s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1053s | 0.1077s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0726s | 0.0769s | -0.0043s | improved |
| `lteNRRCC` | 0.1438s | 0.1219s | +0.0219s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.75 MB | 0.0% | 117.1% |
| `f1ap_rel18.6_specs` | 8.61 MB | 106.65 MB | 238.2% | 104.9% |
| `ngap_rel18.6_specs` | 8.05 MB | 7.41 MB | 238.8% | 98.9% |
| `lteNRRCC` | 51.83 MB | 70.55 MB | 165.3% | 164.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0382s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1139s | 0.1119s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0791s | 0.0828s | -0.0037s | improved |
| `lteNRRCC` | 0.1293s | 0.1144s | +0.0149s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.79 MB | 0.0% | 158.8% |
| `f1ap_rel18.6_specs` | 9.75 MB | 159.42 MB | 159.5% | 157.8% |
| `ngap_rel18.6_specs` | 9.09 MB | 9.02 MB | 156.5% | 173.6% |
| `lteNRRCC` | 9.24 MB | 92.82 MB | 103.4% | 157.9% |
<!-- BENCH_RESULTS_END -->
