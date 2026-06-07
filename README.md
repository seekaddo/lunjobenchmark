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
Generated: 2026-06-07T23:12:23.447317+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0354s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1120s | 0.1100s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0761s | +0.0006s | worse |
| `lteNRRCC` | 0.1206s | 0.1196s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.91 MB | 53.55 MB | 27.5% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.1% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0362s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0991s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0695s | -0.0034s | improved |
| `lteNRRCC` | 0.1267s | 0.1327s | -0.0060s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.35 MB | 36.57 MB | 22.7% | 113.8% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.30 MB | 109.1% | 106.8% |
| `ngap_rel18.6_specs` | 17.66 MB | 73.67 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.73 MB | 66.53 MB | 104.8% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0357s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.0995s | 0.0931s | +0.0064s | worse |
| `ngap_rel18.6_specs` | 0.0712s | 0.0648s | +0.0064s | worse |
| `lteNRRCC` | 0.1323s | 0.1273s | +0.0050s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.07 MB | 55.64 MB | 92.9% | 109.7% |
| `f1ap_rel18.6_specs` | 34.80 MB | 164.64 MB | 112.1% | 104.8% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.24 MB | 110.7% | 106.4% |
| `lteNRRCC` | 74.54 MB | 102.71 MB | 106.2% | 102.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0336s | +0.0055s | worse |
| `f1ap_rel18.6_specs` | 0.0690s | 0.0684s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0508s | 0.0498s | +0.0010s | worse |
| `lteNRRCC` | 0.0829s | 0.0772s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.97 MB | 4.42 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.16 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.41 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.28 MB | 4.19 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0322s | +0.0072s | worse |
| `f1ap_rel18.6_specs` | 0.1097s | 0.0944s | +0.0153s | worse |
| `ngap_rel18.6_specs` | 0.0750s | 0.0653s | +0.0097s | worse |
| `lteNRRCC` | 0.1370s | 0.1127s | +0.0243s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.88 MB | 7.35 MB | 234.0% | 171.5% |
| `f1ap_rel18.6_specs` | 8.55 MB | 8.38 MB | 231.5% | 201.8% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.61 MB | 163.0% | 94.2% |
| `lteNRRCC` | 46.07 MB | 70.56 MB | 110.0% | 166.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0377s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1140s | 0.1072s | +0.0068s | worse |
| `ngap_rel18.6_specs` | 0.0768s | 0.0736s | +0.0032s | worse |
| `lteNRRCC` | 0.1277s | 0.1290s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.51 MB | 8.44 MB | 158.1% | 80.7% |
| `f1ap_rel18.6_specs` | 9.93 MB | 164.18 MB | 174.0% | 157.9% |
| `ngap_rel18.6_specs` | 10.50 MB | 8.76 MB | 114.3% | 159.3% |
| `lteNRRCC` | 8.55 MB | 101.71 MB | 77.1% | 153.0% |
<!-- BENCH_RESULTS_END -->
