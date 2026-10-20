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
Generated: 2026-10-20T14:53:26.329896+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0392s | -0.0030s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1207s | -0.0090s | improved |
| `ngap_rel18.6_specs` | 0.0773s | 0.0818s | -0.0045s | improved |
| `lteNRRCC` | 0.1205s | 0.1261s | -0.0056s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 69.2% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 100.0% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0484s | 0.0462s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1425s | 0.1413s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.1012s | 0.0977s | +0.0035s | worse |
| `lteNRRCC` | 0.1559s | 0.1558s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 34.65 MB | 73.3% | 108.1% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.6% | 102.5% |
| `ngap_rel18.6_specs` | 17.91 MB | 72.65 MB | 106.7% | 103.3% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 102.7% | 102.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0220s | +0.0121s | worse |
| `f1ap_rel18.6_specs` | 0.0908s | 0.0621s | +0.0287s | worse |
| `ngap_rel18.6_specs` | 0.0635s | 0.0438s | +0.0197s | worse |
| `lteNRRCC` | 0.1184s | 0.0781s | +0.0403s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.77 MB | 74.1% | 103.8% |
| `f1ap_rel18.6_specs` | 34.35 MB | 164.28 MB | 103.6% | 103.7% |
| `ngap_rel18.6_specs` | 24.50 MB | 117.80 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.75 MB | 102.66 MB | 103.5% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0217s | 0.0250s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.0759s | 0.0651s | +0.0108s | worse |
| `ngap_rel18.6_specs` | 0.0731s | 0.0493s | +0.0238s | worse |
| `lteNRRCC` | 0.0778s | 0.0837s | -0.0059s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 4.22 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.75 MB | 5.14 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.56 MB | 4.39 MB | 1.3% | 0.0% |
| `lteNRRCC` | 4.12 MB | 4.89 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0419s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1087s | 0.1126s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0789s | -0.0038s | improved |
| `lteNRRCC` | 0.1391s | 0.1390s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.59 MB | 7.46 MB | 0.0% | 151.0% |
| `f1ap_rel18.6_specs` | 8.40 MB | 8.33 MB | 93.1% | 78.9% |
| `ngap_rel18.6_specs` | 7.64 MB | 7.95 MB | 78.0% | 78.2% |
| `lteNRRCC` | 51.73 MB | 58.02 MB | 215.2% | 178.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0407s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1210s | 0.1199s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0830s | 0.0839s | -0.0009s | improved |
| `lteNRRCC` | 0.1306s | 0.1341s | -0.0035s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.85 MB | 0.0% | 78.4% |
| `f1ap_rel18.6_specs` | 9.96 MB | 10.91 MB | 141.7% | 163.7% |
| `ngap_rel18.6_specs` | 9.26 MB | 9.33 MB | 75.4% | 85.8% |
| `lteNRRCC` | 8.68 MB | 99.00 MB | 75.9% | 104.6% |
<!-- BENCH_RESULTS_END -->
