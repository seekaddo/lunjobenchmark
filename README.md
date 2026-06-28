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
Generated: 2026-06-28T23:11:54.296588+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0365s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1114s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0765s | -0.0010s | improved |
| `lteNRRCC` | 0.1188s | 0.1202s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 20.6% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 106.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0323s | 0.0334s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0922s | 0.0894s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0643s | 0.0631s | +0.0012s | worse |
| `lteNRRCC` | 0.1150s | 0.1214s | -0.0064s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.53 MB | 36.61 MB | 72.0% | 108.3% |
| `f1ap_rel18.6_specs` | 21.82 MB | 102.90 MB | 107.4% | 105.6% |
| `ngap_rel18.6_specs` | 17.83 MB | 74.35 MB | 109.1% | 105.0% |
| `lteNRRCC` | 48.63 MB | 66.52 MB | 103.6% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0336s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0910s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0623s | -0.0005s | improved |
| `lteNRRCC` | 0.1162s | 0.1164s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 55.75 MB | 78.6% | 107.4% |
| `f1ap_rel18.6_specs` | 34.59 MB | 164.39 MB | 106.9% | 105.6% |
| `ngap_rel18.6_specs` | 24.42 MB | 117.53 MB | 108.3% | 104.9% |
| `lteNRRCC` | 74.82 MB | 102.80 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0212s | 0.0545s | -0.0333s | improved |
| `f1ap_rel18.6_specs` | 0.0702s | 0.0789s | -0.0087s | improved |
| `ngap_rel18.6_specs` | 0.0489s | 0.0513s | -0.0024s | improved |
| `lteNRRCC` | 0.0813s | 0.0746s | +0.0067s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.75 MB | 4.38 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.00 MB | 4.17 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.98 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.30 MB | 4.55 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0431s | 0.0400s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.1367s | 0.1065s | +0.0302s | worse |
| `ngap_rel18.6_specs` | 0.1043s | 0.0769s | +0.0274s | worse |
| `lteNRRCC` | 0.1404s | 0.1365s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 7.35 MB | 163.7% | 165.4% |
| `f1ap_rel18.6_specs` | 8.39 MB | 8.12 MB | 98.4% | 163.6% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.69 MB | 162.4% | 97.9% |
| `lteNRRCC` | 51.72 MB | 56.77 MB | 156.7% | 108.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0449s | 0.0408s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1322s | 0.1080s | +0.0242s | worse |
| `ngap_rel18.6_specs` | 0.0968s | 0.0762s | +0.0206s | worse |
| `lteNRRCC` | 0.1474s | 0.1275s | +0.0199s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.80 MB | 11.34 MB | 0.0% | 154.7% |
| `f1ap_rel18.6_specs` | 10.30 MB | 13.49 MB | 174.2% | 118.7% |
| `ngap_rel18.6_specs` | 9.48 MB | 9.41 MB | 144.4% | 149.7% |
| `lteNRRCC` | 8.87 MB | 99.63 MB | 151.1% | 127.7% |
<!-- BENCH_RESULTS_END -->
