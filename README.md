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
Generated: 2026-05-26T23:15:12.691360+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0365s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1130s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0806s | 0.0781s | +0.0025s | worse |
| `lteNRRCC` | 0.1240s | 0.1232s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.69 MB | 53.55 MB | 8.0% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.9% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0346s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0924s | 0.0917s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0652s | 0.0643s | +0.0009s | worse |
| `lteNRRCC` | 0.1270s | 0.1247s | +0.0023s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 36.62 MB | 22.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.74 MB | 112.1% | 105.1% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.61 MB | 114.8% | 106.8% |
| `lteNRRCC` | 48.67 MB | 66.04 MB | 104.8% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0351s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0937s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0650s | +0.0003s | worse |
| `lteNRRCC` | 0.1265s | 0.1276s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 55.53 MB | 100.0% | 110.0% |
| `f1ap_rel18.6_specs` | 34.42 MB | 163.81 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 24.07 MB | 117.18 MB | 107.4% | 106.8% |
| `lteNRRCC` | 74.41 MB | 102.96 MB | 104.7% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0278s | 0.0342s | -0.0064s | improved |
| `f1ap_rel18.6_specs` | 0.0831s | 0.0945s | -0.0114s | improved |
| `ngap_rel18.6_specs` | 0.0584s | 0.0541s | +0.0043s | worse |
| `lteNRRCC` | 0.0911s | 0.0768s | +0.0143s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.45 MB | 2.64 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.23 MB | 2.02 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 1.53 MB | 4.31 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.48 MB | 4.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0396s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1240s | 0.1065s | +0.0175s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0763s | +0.0023s | worse |
| `lteNRRCC` | 0.1401s | 0.1393s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.75 MB | 83.9% | 83.2% |
| `f1ap_rel18.6_specs` | 8.45 MB | 8.61 MB | 81.5% | 82.6% |
| `ngap_rel18.6_specs` | 8.49 MB | 8.26 MB | 104.4% | 224.6% |
| `lteNRRCC` | 51.83 MB | 69.10 MB | 106.6% | 160.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0441s | -0.0077s | improved |
| `f1ap_rel18.6_specs` | 0.0977s | 0.1276s | -0.0299s | improved |
| `ngap_rel18.6_specs` | 0.0673s | 0.0891s | -0.0218s | improved |
| `lteNRRCC` | 0.1103s | 0.1416s | -0.0313s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.93 MB | 9.95 MB | 105.9% | 142.5% |
| `f1ap_rel18.6_specs` | 11.02 MB | 154.78 MB | 140.2% | 139.7% |
| `ngap_rel18.6_specs` | 10.24 MB | 9.34 MB | 142.3% | 103.6% |
| `lteNRRCC` | 73.77 MB | 77.95 MB | 140.7% | 142.4% |
<!-- BENCH_RESULTS_END -->
