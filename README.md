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
Generated: 2026-07-15T23:02:57.392443+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0374s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1132s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0772s | -0.0001s | improved |
| `lteNRRCC` | 0.1207s | 0.1212s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 21.3% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0343s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0935s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0663s | 0.0670s | -0.0007s | improved |
| `lteNRRCC` | 0.1284s | 0.1252s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 36.33 MB | 16.9% | 111.1% |
| `f1ap_rel18.6_specs` | 22.01 MB | 103.07 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.23 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.16 MB | 66.25 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0347s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0959s | 0.0906s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0688s | 0.0634s | +0.0054s | worse |
| `lteNRRCC` | 0.1212s | 0.1176s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.21 MB | 55.81 MB | 18.8% | 113.8% |
| `f1ap_rel18.6_specs` | 34.53 MB | 164.21 MB | 106.5% | 103.3% |
| `ngap_rel18.6_specs` | 24.27 MB | 117.89 MB | 111.5% | 106.5% |
| `lteNRRCC` | 74.68 MB | 102.87 MB | 105.0% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0187s | 0.0236s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.0705s | 0.0787s | -0.0082s | improved |
| `ngap_rel18.6_specs` | 0.0527s | 0.0519s | +0.0008s | worse |
| `lteNRRCC` | 0.0975s | 0.0719s | +0.0256s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.61 MB | 3.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.36 MB | 8.09 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.19 MB | 8.34 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.34 MB | 6.58 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0431s | 0.0403s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1178s | 0.1133s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0822s | 0.0779s | +0.0043s | worse |
| `lteNRRCC` | 0.1426s | 0.1393s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.98 MB | 7.70 MB | 160.5% | 167.9% |
| `f1ap_rel18.6_specs` | 8.45 MB | 106.65 MB | 164.6% | 168.3% |
| `ngap_rel18.6_specs` | 8.25 MB | 8.18 MB | 95.6% | 166.0% |
| `lteNRRCC` | 50.82 MB | 70.55 MB | 161.7% | 165.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0450s | 0.0386s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.1267s | 0.1124s | +0.0143s | worse |
| `ngap_rel18.6_specs` | 0.0858s | 0.0767s | +0.0091s | worse |
| `lteNRRCC` | 0.1413s | 0.1269s | +0.0144s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.71 MB | 10.09 MB | 156.8% | 95.6% |
| `f1ap_rel18.6_specs` | 10.06 MB | 124.21 MB | 160.2% | 115.1% |
| `ngap_rel18.6_specs` | 10.82 MB | 9.41 MB | 210.8% | 160.2% |
| `lteNRRCC` | 66.42 MB | 101.68 MB | 108.6% | 157.3% |
<!-- BENCH_RESULTS_END -->
