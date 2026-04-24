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
Generated: 2026-04-24T11:13:50.214625+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0373s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1153s | -0.0055s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0792s | -0.0030s | improved |
| `lteNRRCC` | 0.1187s | 0.1230s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 11.1% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0345s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0936s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0672s | 0.0662s | +0.0010s | worse |
| `lteNRRCC` | 0.1305s | 0.1290s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.21 MB | 36.47 MB | 96.0% | 110.7% |
| `f1ap_rel18.6_specs` | 22.26 MB | 103.19 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.52 MB | 73.82 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.84 MB | 66.18 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0347s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0882s | 0.0915s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0640s | -0.0022s | improved |
| `lteNRRCC` | 0.1161s | 0.1176s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.24 MB | 55.51 MB | 27.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.63 MB | 164.38 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.57 MB | 117.59 MB | 116.7% | 107.1% |
| `lteNRRCC` | 74.83 MB | 102.05 MB | 103.4% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0256s | 0.0186s | +0.0070s | worse |
| `f1ap_rel18.6_specs` | 0.0832s | 0.0597s | +0.0235s | worse |
| `ngap_rel18.6_specs` | 0.0482s | 0.0402s | +0.0080s | worse |
| `lteNRRCC` | 0.0809s | 0.0679s | +0.0130s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 624 KB | 4.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.05 MB | 608 KB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.88 MB | 2.91 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.98 MB | 4.23 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0335s | +0.0043s | worse |
| `f1ap_rel18.6_specs` | 0.1032s | 0.0935s | +0.0097s | worse |
| `ngap_rel18.6_specs` | 0.0722s | 0.0666s | +0.0056s | worse |
| `lteNRRCC` | 0.1348s | 0.1118s | +0.0230s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.56 MB | 7.34 MB | 92.3% | 166.2% |
| `f1ap_rel18.6_specs` | 8.41 MB | 106.64 MB | 116.5% | 167.5% |
| `ngap_rel18.6_specs` | 7.34 MB | 7.98 MB | 204.2% | 119.5% |
| `lteNRRCC` | 49.57 MB | 55.07 MB | 116.7% | 237.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0411s | -0.0042s | improved |
| `f1ap_rel18.6_specs` | 0.1032s | 0.1160s | -0.0128s | improved |
| `ngap_rel18.6_specs` | 0.0740s | 0.0810s | -0.0070s | improved |
| `lteNRRCC` | 0.1125s | 0.1321s | -0.0196s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.77 MB | 10.39 MB | 99.4% | 106.3% |
| `f1ap_rel18.6_specs` | 10.49 MB | 156.41 MB | 97.3% | 187.7% |
| `ngap_rel18.6_specs` | 9.44 MB | 10.14 MB | 192.7% | 96.3% |
| `lteNRRCC` | 9.23 MB | 97.94 MB | 198.9% | 107.1% |
<!-- BENCH_RESULTS_END -->
