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
Generated: 2026-06-29T14:12:15.393051+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0339s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1096s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0744s | 0.0755s | -0.0011s | improved |
| `lteNRRCC` | 0.1184s | 0.1188s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 18.3% | 111.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.3% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0323s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.0945s | 0.0922s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0664s | 0.0643s | +0.0021s | worse |
| `lteNRRCC` | 0.1294s | 0.1150s | +0.0144s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 36.62 MB | 79.3% | 107.1% |
| `f1ap_rel18.6_specs` | 22.41 MB | 103.40 MB | 106.2% | 105.3% |
| `ngap_rel18.6_specs` | 17.71 MB | 74.47 MB | 107.4% | 107.0% |
| `lteNRRCC` | 48.59 MB | 65.95 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0328s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0990s | 0.0906s | +0.0084s | worse |
| `ngap_rel18.6_specs` | 0.0677s | 0.0618s | +0.0059s | worse |
| `lteNRRCC` | 0.1173s | 0.1162s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 55.60 MB | 77.3% | 108.0% |
| `f1ap_rel18.6_specs` | 34.09 MB | 163.70 MB | 107.7% | 103.6% |
| `ngap_rel18.6_specs` | 24.29 MB | 117.66 MB | 109.5% | 104.8% |
| `lteNRRCC` | 74.82 MB | 102.71 MB | 103.7% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0195s | 0.0212s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1166s | 0.0702s | +0.0464s | worse |
| `ngap_rel18.6_specs` | 0.0519s | 0.0489s | +0.0030s | worse |
| `lteNRRCC` | 0.0842s | 0.0813s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.62 MB | 7.17 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.16 MB | 8.66 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.31 MB | 8.45 MB | 1.1% | 0.0% |
| `lteNRRCC` | 7.50 MB | 7.53 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0431s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1367s | -0.0235s | improved |
| `ngap_rel18.6_specs` | 0.0781s | 0.1043s | -0.0262s | improved |
| `lteNRRCC` | 0.1413s | 0.1404s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.83 MB | 7.89 MB | 160.3% | 148.2% |
| `f1ap_rel18.6_specs` | 8.73 MB | 106.57 MB | 160.2% | 153.6% |
| `ngap_rel18.6_specs` | 8.23 MB | 8.49 MB | 79.2% | 155.1% |
| `lteNRRCC` | 50.74 MB | 70.55 MB | 160.2% | 157.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0449s | -0.0057s | improved |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1322s | -0.0190s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0968s | -0.0190s | improved |
| `lteNRRCC` | 0.1290s | 0.1474s | -0.0184s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.58 MB | 8.65 MB | 157.2% | 157.9% |
| `f1ap_rel18.6_specs` | 9.86 MB | 11.13 MB | 80.3% | 111.9% |
| `ngap_rel18.6_specs` | 9.12 MB | 9.07 MB | 159.0% | 155.7% |
| `lteNRRCC` | 8.61 MB | 79.20 MB | 77.8% | 225.1% |
<!-- BENCH_RESULTS_END -->
