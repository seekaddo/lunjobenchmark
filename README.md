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
Generated: 2026-05-06T22:57:47.703431+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0361s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1149s | 0.1109s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0782s | 0.0757s | +0.0025s | worse |
| `lteNRRCC` | 0.1234s | 0.1193s | +0.0041s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.94 MB | 53.55 MB | 29.5% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0346s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.0887s | 0.0945s | -0.0058s | improved |
| `ngap_rel18.6_specs` | 0.0635s | 0.0670s | -0.0035s | improved |
| `lteNRRCC` | 0.1228s | 0.1304s | -0.0076s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.25 MB | 76.7% | 107.4% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.39 MB | 106.5% | 105.5% |
| `ngap_rel18.6_specs` | 16.51 MB | 74.61 MB | 112.0% | 107.3% |
| `lteNRRCC` | 48.20 MB | 66.42 MB | 103.1% | 104.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0327s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0908s | 0.0877s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0626s | 0.0616s | +0.0010s | worse |
| `lteNRRCC` | 0.1210s | 0.1144s | +0.0066s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.78 MB | 75.0% | 110.7% |
| `f1ap_rel18.6_specs` | 35.26 MB | 164.62 MB | 109.7% | 105.3% |
| `ngap_rel18.6_specs` | 24.29 MB | 117.81 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.81 MB | 102.95 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0230s | 0.0205s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.0710s | 0.0735s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0499s | 0.0515s | -0.0016s | improved |
| `lteNRRCC` | 0.0844s | 0.0854s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.44 MB | 4.73 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.89 MB | 4.19 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.47 MB | 4.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.11 MB | 5.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0391s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1073s | 0.1074s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0747s | -0.0002s | improved |
| `lteNRRCC` | 0.1382s | 0.1358s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.81 MB | 173.3% | 117.6% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.57 MB | 81.5% | 231.8% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.61 MB | 170.3% | 161.1% |
| `lteNRRCC` | 7.91 MB | 48.88 MB | 162.7% | 161.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0392s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1154s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0796s | 0.0808s | -0.0012s | improved |
| `lteNRRCC` | 0.1279s | 0.1307s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.72 MB | 8.58 MB | 79.8% | 157.8% |
| `f1ap_rel18.6_specs` | 9.75 MB | 164.14 MB | 174.0% | 112.4% |
| `ngap_rel18.6_specs` | 10.88 MB | 10.54 MB | 111.2% | 224.4% |
| `lteNRRCC` | 73.78 MB | 87.48 MB | 155.6% | 107.8% |
<!-- BENCH_RESULTS_END -->
