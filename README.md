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
Generated: 2026-09-21T00:03:14.750408+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0340s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1103s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0748s | 0.0750s | -0.0002s | improved |
| `lteNRRCC` | 0.1174s | 0.1202s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 15.7% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 100.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 104.3% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0243s | 0.0376s | -0.0133s | improved |
| `f1ap_rel18.6_specs` | 0.0737s | 0.1017s | -0.0280s | improved |
| `ngap_rel18.6_specs` | 0.0508s | 0.0710s | -0.0202s | improved |
| `lteNRRCC` | 0.0877s | 0.1367s | -0.0490s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.48 MB | 48.3% | 100.0% |
| `f1ap_rel18.6_specs` | 22.38 MB | 103.41 MB | 100.0% | 100.0% |
| `ngap_rel18.6_specs` | 18.05 MB | 74.38 MB | 106.2% | 100.0% |
| `lteNRRCC` | 48.66 MB | 66.36 MB | 100.0% | 100.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0307s | +0.0039s | worse |
| `f1ap_rel18.6_specs` | 0.0957s | 0.0880s | +0.0077s | worse |
| `ngap_rel18.6_specs` | 0.0643s | 0.0583s | +0.0060s | worse |
| `lteNRRCC` | 0.1192s | 0.0978s | +0.0214s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 55.43 MB | 74.1% | 103.7% |
| `f1ap_rel18.6_specs` | 34.03 MB | 164.39 MB | 106.9% | 101.8% |
| `ngap_rel18.6_specs` | 24.45 MB | 117.03 MB | 108.3% | 102.4% |
| `lteNRRCC` | 74.88 MB | 102.25 MB | 103.5% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0225s | 0.0216s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0692s | 0.0847s | -0.0155s | improved |
| `ngap_rel18.6_specs` | 0.0483s | 0.0486s | -0.0003s | improved |
| `lteNRRCC` | 0.0759s | 0.0770s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.06 MB | 5.17 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.02 MB | 4.66 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.48 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.38 MB | 7.39 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0260s | 0.0412s | -0.0152s | improved |
| `f1ap_rel18.6_specs` | 0.0727s | 0.1101s | -0.0374s | improved |
| `ngap_rel18.6_specs` | 0.0512s | 0.0774s | -0.0262s | improved |
| `lteNRRCC` | 0.0849s | 0.1379s | -0.0530s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.21 MB | 0.0% | 146.5% |
| `f1ap_rel18.6_specs` | 18.05 MB | 11.30 MB | 145.3% | 121.9% |
| `ngap_rel18.6_specs` | 11.61 MB | 11.70 MB | 115.7% | 118.3% |
| `lteNRRCC` | 10.66 MB | 10.08 MB | 120.8% | 136.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0393s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1207s | 0.1164s | +0.0043s | worse |
| `ngap_rel18.6_specs` | 0.0733s | 0.0807s | -0.0074s | improved |
| `lteNRRCC` | 0.1105s | 0.1328s | -0.0223s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.25 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 10.56 MB | 126.77 MB | 151.5% | 127.5% |
| `ngap_rel18.6_specs` | 9.98 MB | 7.78 MB | 148.4% | 148.4% |
| `lteNRRCC` | 8.73 MB | 86.00 MB | 146.2% | 136.6% |
<!-- BENCH_RESULTS_END -->
