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
Generated: 2026-08-04T23:09:02.838229+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0353s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1095s | +0.0035s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0746s | +0.0024s | worse |
| `lteNRRCC` | 0.1209s | 0.1191s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 20.0% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0356s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0978s | 0.0965s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0709s | 0.0671s | +0.0038s | worse |
| `lteNRRCC` | 0.1301s | 0.1305s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 36.70 MB | 72.4% | 107.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.28 MB | 106.2% | 103.4% |
| `ngap_rel18.6_specs` | 17.62 MB | 73.93 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.80 MB | 65.76 MB | 101.5% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0354s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0886s | 0.0934s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0617s | 0.0668s | -0.0051s | improved |
| `lteNRRCC` | 0.1164s | 0.1184s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.31 MB | 73.1% | 103.8% |
| `f1ap_rel18.6_specs` | 35.23 MB | 164.29 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 24.35 MB | 117.59 MB | 108.7% | 105.0% |
| `lteNRRCC` | 74.77 MB | 102.40 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0233s | 0.0252s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0685s | 0.0768s | -0.0083s | improved |
| `ngap_rel18.6_specs` | 0.0479s | 0.0499s | -0.0020s | improved |
| `lteNRRCC` | 0.0773s | 0.0772s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.09 MB | 5.25 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.56 MB | 6.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.52 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.89 MB | 3.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0398s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1077s | 0.1144s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0788s | -0.0019s | improved |
| `lteNRRCC` | 0.1219s | 0.1432s | -0.0213s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.05 MB | 0.0% | 113.6% |
| `f1ap_rel18.6_specs` | 8.80 MB | 106.65 MB | 113.4% | 119.8% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.37 MB | 227.1% | 102.7% |
| `lteNRRCC` | 49.14 MB | 51.52 MB | 239.8% | 105.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0576s | -0.0194s | improved |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1390s | -0.0271s | improved |
| `ngap_rel18.6_specs` | 0.0828s | 0.0982s | -0.0154s | improved |
| `lteNRRCC` | 0.1144s | 0.1365s | -0.0221s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.09 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 10.74 MB | 131.23 MB | 0.0% | 134.0% |
| `ngap_rel18.6_specs` | 9.45 MB | 10.50 MB | 131.4% | 265.4% |
| `lteNRRCC` | 73.03 MB | 76.02 MB | 133.6% | 182.0% |
<!-- BENCH_RESULTS_END -->
