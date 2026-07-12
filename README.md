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
Generated: 2026-07-12T22:56:42.251392+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0359s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1123s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0768s | 0.0758s | +0.0010s | worse |
| `lteNRRCC` | 0.1209s | 0.1191s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 22.3% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0373s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0974s | 0.0957s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0676s | 0.0671s | +0.0005s | worse |
| `lteNRRCC` | 0.1326s | 0.1291s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.48 MB | 80.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.39 MB | 102.61 MB | 109.1% | 104.9% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.28 MB | 110.7% | 106.7% |
| `lteNRRCC` | 48.84 MB | 66.23 MB | 104.5% | 105.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0329s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.1014s | 0.0883s | +0.0131s | worse |
| `ngap_rel18.6_specs` | 0.0715s | 0.0613s | +0.0102s | worse |
| `lteNRRCC` | 0.1174s | 0.1139s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.60 MB | 55.61 MB | 76.0% | 111.5% |
| `f1ap_rel18.6_specs` | 34.65 MB | 164.29 MB | 111.1% | 103.3% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.85 MB | 109.1% | 106.8% |
| `lteNRRCC` | 74.84 MB | 102.97 MB | 103.6% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0249s | 0.0220s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.0693s | 0.0684s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0502s | 0.0458s | +0.0044s | worse |
| `lteNRRCC` | 0.0772s | 0.0798s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.95 MB | 3.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 4.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.05 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.98 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0396s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1087s | 0.1168s | -0.0081s | improved |
| `ngap_rel18.6_specs` | 0.0747s | 0.0764s | -0.0017s | improved |
| `lteNRRCC` | 0.1377s | 0.1384s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.34 MB | 162.9% | 168.2% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.40 MB | 157.8% | 106.1% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.55 MB | 81.5% | 165.5% |
| `lteNRRCC` | 46.24 MB | 51.15 MB | 159.9% | 161.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0403s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1163s | -0.0083s | improved |
| `ngap_rel18.6_specs` | 0.0741s | 0.0815s | -0.0074s | improved |
| `lteNRRCC` | 0.1253s | 0.1387s | -0.0134s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.79 MB | 8.72 MB | 157.1% | 160.6% |
| `f1ap_rel18.6_specs` | 9.68 MB | 11.20 MB | 79.4% | 212.0% |
| `ngap_rel18.6_specs` | 9.31 MB | 9.02 MB | 165.7% | 79.9% |
| `lteNRRCC` | 8.62 MB | 72.24 MB | 79.8% | 225.2% |
<!-- BENCH_RESULTS_END -->
