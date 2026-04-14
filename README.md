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
Generated: 2026-04-14T22:53:28.641071+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0403s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.1163s | 0.1239s | -0.0076s | improved |
| `ngap_rel18.6_specs` | 0.0810s | 0.0865s | -0.0055s | improved |
| `lteNRRCC` | 0.1234s | 0.1287s | -0.0053s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.86 MB | 53.55 MB | 26.7% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0369s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0959s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0685s | -0.0036s | improved |
| `lteNRRCC` | 0.1275s | 0.1316s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.09 MB | 92.6% | 110.3% |
| `f1ap_rel18.6_specs` | 22.53 MB | 103.27 MB | 109.1% | 106.8% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.05 MB | 110.7% | 106.7% |
| `lteNRRCC` | 48.79 MB | 65.98 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0318s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.0992s | 0.0864s | +0.0128s | worse |
| `ngap_rel18.6_specs` | 0.0696s | 0.0596s | +0.0100s | worse |
| `lteNRRCC` | 0.1157s | 0.1142s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.33 MB | 55.56 MB | 100.0% | 107.7% |
| `f1ap_rel18.6_specs` | 34.71 MB | 164.78 MB | 111.5% | 103.4% |
| `ngap_rel18.6_specs` | 24.58 MB | 117.59 MB | 114.3% | 104.7% |
| `lteNRRCC` | 74.56 MB | 102.77 MB | 103.6% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0274s | 0.0202s | +0.0072s | worse |
| `f1ap_rel18.6_specs` | 0.0635s | 0.0641s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0603s | 0.0505s | +0.0098s | worse |
| `lteNRRCC` | 0.0880s | 0.0792s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.77 MB | 7.98 MB | 0.0% | 1.2% |
| `f1ap_rel18.6_specs` | 9.03 MB | 8.69 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.42 MB | 6.58 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.09 MB | 8.06 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0396s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0907s | 0.1106s | -0.0199s | improved |
| `ngap_rel18.6_specs` | 0.0644s | 0.0774s | -0.0130s | improved |
| `lteNRRCC` | 0.1116s | 0.1403s | -0.0287s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.82 MB | 7.80 MB | 141.9% | 102.8% |
| `f1ap_rel18.6_specs` | 8.25 MB | 106.63 MB | 104.2% | 142.6% |
| `ngap_rel18.6_specs` | 8.23 MB | 7.95 MB | 137.1% | 106.0% |
| `lteNRRCC` | 8.41 MB | 51.72 MB | 140.5% | 143.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0425s | -0.0046s | improved |
| `f1ap_rel18.6_specs` | 0.1051s | 0.1191s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0735s | 0.0836s | -0.0101s | improved |
| `lteNRRCC` | 0.1236s | 0.1347s | -0.0111s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.52 MB | 8.71 MB | 79.0% | 178.0% |
| `f1ap_rel18.6_specs` | 9.86 MB | 163.10 MB | 81.4% | 160.2% |
| `ngap_rel18.6_specs` | 8.95 MB | 8.89 MB | 161.9% | 162.0% |
| `lteNRRCC` | 8.61 MB | 80.95 MB | 159.4% | 107.2% |
<!-- BENCH_RESULTS_END -->
