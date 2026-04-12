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
Generated: 2026-04-12T10:49:22.481019+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0371s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1164s | 0.1137s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0791s | 0.0776s | +0.0015s | worse |
| `lteNRRCC` | 0.1236s | 0.1234s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 26.7% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0373s | -0.0029s | improved |
| `f1ap_rel18.6_specs` | 0.0941s | 0.0929s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0653s | 0.0661s | -0.0008s | improved |
| `lteNRRCC` | 0.1280s | 0.1251s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.70 MB | 92.3% | 110.7% |
| `f1ap_rel18.6_specs` | 22.38 MB | 102.66 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.41 MB | 111.5% | 106.8% |
| `lteNRRCC` | 48.30 MB | 65.50 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0355s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0904s | 0.0948s | -0.0044s | improved |
| `ngap_rel18.6_specs` | 0.0625s | 0.0650s | -0.0025s | improved |
| `lteNRRCC` | 0.1160s | 0.1259s | -0.0099s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.89 MB | 96.0% | 107.1% |
| `f1ap_rel18.6_specs` | 34.70 MB | 164.77 MB | 113.8% | 105.5% |
| `ngap_rel18.6_specs` | 24.30 MB | 116.89 MB | 108.0% | 107.1% |
| `lteNRRCC` | 74.79 MB | 102.11 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0294s | 0.0192s | +0.0102s | worse |
| `f1ap_rel18.6_specs` | 0.0836s | 0.0598s | +0.0238s | worse |
| `ngap_rel18.6_specs` | 0.0465s | 0.0408s | +0.0057s | worse |
| `lteNRRCC` | 0.0743s | 0.0751s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.42 MB | 4.39 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 3.88 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.09 MB | 4.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.52 MB | 4.25 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0396s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1065s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0754s | 0.0768s | -0.0014s | improved |
| `lteNRRCC` | 0.1379s | 0.1409s | -0.0030s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.30 MB | 7.28 MB | 185.6% | 165.6% |
| `f1ap_rel18.6_specs` | 8.16 MB | 8.03 MB | 118.3% | 170.1% |
| `ngap_rel18.6_specs` | 7.46 MB | 8.16 MB | 82.8% | 117.6% |
| `lteNRRCC` | 51.32 MB | 51.26 MB | 106.9% | 117.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0427s | 0.0395s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.1268s | 0.1083s | +0.0185s | worse |
| `ngap_rel18.6_specs` | 0.0867s | 0.0768s | +0.0099s | worse |
| `lteNRRCC` | 0.1318s | 0.1278s | +0.0040s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.55 MB | 10.08 MB | 159.1% | 95.1% |
| `f1ap_rel18.6_specs` | 10.50 MB | 10.29 MB | 160.6% | 92.6% |
| `ngap_rel18.6_specs` | 10.55 MB | 9.40 MB | 102.9% | 164.1% |
| `lteNRRCC` | 8.86 MB | 99.68 MB | 81.9% | 105.1% |
<!-- BENCH_RESULTS_END -->
