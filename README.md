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
Generated: 2026-08-22T22:28:41.708012+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0359s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1128s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0768s | +0.0009s | worse |
| `lteNRRCC` | 0.1221s | 0.1204s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 75.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0224s | 0.0350s | -0.0126s | improved |
| `f1ap_rel18.6_specs` | 0.0621s | 0.0943s | -0.0322s | improved |
| `ngap_rel18.6_specs` | 0.0436s | 0.0666s | -0.0230s | improved |
| `lteNRRCC` | 0.0779s | 0.1276s | -0.0497s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 36.52 MB | 34.1% | 100.0% |
| `f1ap_rel18.6_specs` | 22.42 MB | 102.62 MB | 105.0% | 102.6% |
| `ngap_rel18.6_specs` | 18.02 MB | 74.08 MB | 112.5% | 103.6% |
| `lteNRRCC` | 48.75 MB | 66.19 MB | 105.4% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0363s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0905s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0656s | 0.0645s | +0.0011s | worse |
| `lteNRRCC` | 0.1294s | 0.1171s | +0.0123s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.60 MB | 55.82 MB | 80.8% | 103.6% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.52 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 23.47 MB | 117.70 MB | 103.8% | 102.3% |
| `lteNRRCC` | 73.79 MB | 102.94 MB | 101.6% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0177s | 0.0340s | -0.0163s | improved |
| `f1ap_rel18.6_specs` | 0.0698s | 0.0906s | -0.0208s | improved |
| `ngap_rel18.6_specs` | 0.0477s | 0.0569s | -0.0092s | improved |
| `lteNRRCC` | 0.1309s | 0.1053s | +0.0256s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 7.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.53 MB | 9.11 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.33 MB | 4.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.81 MB | 4.55 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0404s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1117s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0787s | 0.0781s | +0.0006s | worse |
| `lteNRRCC` | 0.1429s | 0.1385s | +0.0044s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.70 MB | 7.49 MB | 94.4% | 147.5% |
| `f1ap_rel18.6_specs` | 8.45 MB | 106.64 MB | 151.1% | 153.0% |
| `ngap_rel18.6_specs` | 7.96 MB | 8.12 MB | 152.3% | 93.3% |
| `lteNRRCC` | 48.76 MB | 54.27 MB | 106.4% | 106.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0413s | 0.0378s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.1186s | 0.1088s | +0.0098s | worse |
| `ngap_rel18.6_specs` | 0.0808s | 0.0742s | +0.0066s | worse |
| `lteNRRCC` | 0.1206s | 0.1268s | -0.0062s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.47 MB | 10.10 MB | 110.0% | 178.6% |
| `f1ap_rel18.6_specs` | 10.54 MB | 121.53 MB | 129.6% | 130.8% |
| `ngap_rel18.6_specs` | 10.32 MB | 10.39 MB | 126.5% | 86.0% |
| `lteNRRCC` | 9.18 MB | 73.35 MB | 87.0% | 129.1% |
<!-- BENCH_RESULTS_END -->
