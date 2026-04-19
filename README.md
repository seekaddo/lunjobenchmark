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
Generated: 2026-04-19T22:43:40.516771+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0357s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1121s | 0.1111s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0775s | -0.0002s | improved |
| `lteNRRCC` | 0.1214s | 0.1220s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.93 MB | 53.55 MB | 10.0% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.3% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0312s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0925s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0641s | +0.0026s | worse |
| `lteNRRCC` | 0.1310s | 0.1151s | +0.0159s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.63 MB | 92.3% | 114.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.61 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 16.78 MB | 74.47 MB | 111.1% | 107.0% |
| `lteNRRCC` | 48.31 MB | 66.36 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0352s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1021s | 0.0941s | +0.0080s | worse |
| `ngap_rel18.6_specs` | 0.0713s | 0.0651s | +0.0062s | worse |
| `lteNRRCC` | 0.1199s | 0.1287s | -0.0088s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.31 MB | 55.52 MB | 45.5% | 111.1% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.54 MB | 107.1% | 103.3% |
| `ngap_rel18.6_specs` | 24.58 MB | 117.05 MB | 109.1% | 106.8% |
| `lteNRRCC` | 73.96 MB | 102.59 MB | 103.6% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0309s | 0.0240s | +0.0069s | worse |
| `f1ap_rel18.6_specs` | 0.0717s | 0.0626s | +0.0091s | worse |
| `ngap_rel18.6_specs` | 0.0488s | 0.0444s | +0.0044s | worse |
| `lteNRRCC` | 0.0845s | 0.0685s | +0.0160s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.20 MB | 5.98 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.44 MB | 5.55 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.39 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.81 MB | 4.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0334s | +0.0061s | worse |
| `f1ap_rel18.6_specs` | 0.1055s | 0.0937s | +0.0118s | worse |
| `ngap_rel18.6_specs` | 0.0749s | 0.0671s | +0.0078s | worse |
| `lteNRRCC` | 0.1366s | 0.1111s | +0.0255s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.35 MB | 98.1% | 163.1% |
| `f1ap_rel18.6_specs` | 7.96 MB | 106.64 MB | 160.5% | 163.7% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.54 MB | 172.4% | 162.1% |
| `lteNRRCC` | 49.89 MB | 69.04 MB | 118.4% | 161.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0378s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1082s | 0.1083s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0763s | +0.0015s | worse |
| `lteNRRCC` | 0.1251s | 0.1243s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.59 MB | 10.09 MB | 162.4% | 238.4% |
| `f1ap_rel18.6_specs` | 11.20 MB | 164.20 MB | 231.7% | 106.0% |
| `ngap_rel18.6_specs` | 8.77 MB | 10.94 MB | 160.5% | 104.8% |
| `lteNRRCC` | 71.19 MB | 97.45 MB | 160.8% | 240.3% |
<!-- BENCH_RESULTS_END -->
