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
Generated: 2026-06-28T11:51:08.474385+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0342s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1114s | 0.1086s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0765s | 0.0754s | +0.0011s | worse |
| `lteNRRCC` | 0.1202s | 0.1184s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 21.9% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0349s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0894s | 0.0947s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0631s | 0.0659s | -0.0028s | improved |
| `lteNRRCC` | 0.1214s | 0.1301s | -0.0087s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 36.07 MB | 18.0% | 111.1% |
| `f1ap_rel18.6_specs` | 21.72 MB | 103.44 MB | 109.7% | 103.6% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.71 MB | 107.7% | 109.5% |
| `lteNRRCC` | 48.55 MB | 66.04 MB | 103.2% | 104.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0374s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.0910s | 0.0904s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0623s | 0.0618s | +0.0005s | worse |
| `lteNRRCC` | 0.1164s | 0.1169s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 55.90 MB | 81.5% | 111.1% |
| `f1ap_rel18.6_specs` | 34.35 MB | 163.61 MB | 110.3% | 103.6% |
| `ngap_rel18.6_specs` | 24.57 MB | 117.35 MB | 112.5% | 104.7% |
| `lteNRRCC` | 74.81 MB | 102.48 MB | 105.3% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0545s | 0.0242s | +0.0303s | worse |
| `f1ap_rel18.6_specs` | 0.0789s | 0.0661s | +0.0128s | worse |
| `ngap_rel18.6_specs` | 0.0513s | 0.0518s | -0.0005s | improved |
| `lteNRRCC` | 0.0746s | 0.0778s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.28 MB | 4.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.08 MB | 8.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.58 MB | 5.42 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.95 MB | 4.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0401s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1065s | 0.1107s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0770s | -0.0001s | improved |
| `lteNRRCC` | 0.1365s | 0.1401s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.34 MB | 7.50 MB | 167.0% | 100.9% |
| `f1ap_rel18.6_specs` | 8.61 MB | 106.64 MB | 114.5% | 109.9% |
| `ngap_rel18.6_specs` | 7.55 MB | 8.18 MB | 160.5% | 117.2% |
| `lteNRRCC` | 51.73 MB | 56.57 MB | 233.7% | 117.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0430s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1195s | -0.0115s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0842s | -0.0080s | improved |
| `lteNRRCC` | 0.1275s | 0.1379s | -0.0104s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.21 MB | 9.07 MB | 106.7% | 94.7% |
| `f1ap_rel18.6_specs` | 11.26 MB | 11.14 MB | 220.0% | 104.3% |
| `ngap_rel18.6_specs` | 10.88 MB | 10.94 MB | 108.9% | 111.2% |
| `lteNRRCC` | 73.09 MB | 84.49 MB | 154.0% | 156.6% |
<!-- BENCH_RESULTS_END -->
