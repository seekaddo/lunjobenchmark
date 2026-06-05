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
Generated: 2026-06-05T12:43:13.063041+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0347s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1093s | +0.0051s | worse |
| `ngap_rel18.6_specs` | 0.0787s | 0.0746s | +0.0041s | worse |
| `lteNRRCC` | 0.1224s | 0.1182s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 22.9% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0337s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.0944s | 0.0915s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0670s | 0.0635s | +0.0035s | worse |
| `lteNRRCC` | 0.1279s | 0.1230s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.67 MB | 82.8% | 109.7% |
| `f1ap_rel18.6_specs` | 22.44 MB | 103.40 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.36 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.42 MB | 65.77 MB | 106.2% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0366s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1020s | 0.0966s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0719s | 0.0666s | +0.0053s | worse |
| `lteNRRCC` | 0.1339s | 0.1304s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.86 MB | 90.3% | 109.4% |
| `f1ap_rel18.6_specs` | 34.33 MB | 164.48 MB | 108.8% | 104.7% |
| `ngap_rel18.6_specs` | 24.18 MB | 117.51 MB | 116.7% | 108.3% |
| `lteNRRCC` | 74.77 MB | 102.61 MB | 105.8% | 103.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0215s | 0.0212s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1108s | 0.0679s | +0.0429s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0494s | +0.0164s | worse |
| `lteNRRCC` | 0.1046s | 0.0803s | +0.0243s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.66 MB | 8.53 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.78 MB | 2.50 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.83 MB | 4.84 MB | 0.0% | 0.0% |
| `lteNRRCC` | 1.95 MB | 1.56 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0322s | +0.0078s | worse |
| `f1ap_rel18.6_specs` | 0.1099s | 0.0933s | +0.0166s | worse |
| `ngap_rel18.6_specs` | 0.0774s | 0.0639s | +0.0135s | worse |
| `lteNRRCC` | 0.1384s | 0.1115s | +0.0269s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.36 MB | 109.6% | 111.1% |
| `f1ap_rel18.6_specs` | 8.67 MB | 8.42 MB | 223.3% | 158.2% |
| `ngap_rel18.6_specs` | 7.68 MB | 8.25 MB | 158.1% | 224.6% |
| `lteNRRCC` | 51.83 MB | 51.87 MB | 108.1% | 154.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0414s | -0.0048s | improved |
| `f1ap_rel18.6_specs` | 0.1002s | 0.1239s | -0.0237s | improved |
| `ngap_rel18.6_specs` | 0.0704s | 0.0918s | -0.0214s | improved |
| `lteNRRCC` | 0.1135s | 0.1385s | -0.0250s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.16 MB | 9.97 MB | 142.2% | 139.3% |
| `f1ap_rel18.6_specs` | 10.90 MB | 164.20 MB | 141.4% | 137.7% |
| `ngap_rel18.6_specs` | 10.39 MB | 10.20 MB | 140.1% | 141.5% |
| `lteNRRCC` | 9.37 MB | 77.46 MB | 136.3% | 137.4% |
<!-- BENCH_RESULTS_END -->
