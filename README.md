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
Generated: 2026-04-01T11:05:52.683745+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0375s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1237s | 0.1146s | +0.0091s | worse |
| `ngap_rel18.6_specs` | 0.0845s | 0.0814s | +0.0031s | worse |
| `lteNRRCC` | 0.1290s | 0.1225s | +0.0065s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 30.4% | 106.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.4% | 105.5% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.8% | 105.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0338s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0919s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0653s | +0.0005s | worse |
| `lteNRRCC` | 0.1259s | 0.1271s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.24 MB | 36.57 MB | 96.3% | 110.0% |
| `f1ap_rel18.6_specs` | 21.69 MB | 103.40 MB | 112.5% | 103.4% |
| `ngap_rel18.6_specs` | 16.53 MB | 74.60 MB | 110.7% | 106.5% |
| `lteNRRCC` | 48.53 MB | 66.50 MB | 104.8% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0337s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1014s | 0.0914s | +0.0100s | worse |
| `ngap_rel18.6_specs` | 0.0698s | 0.0627s | +0.0071s | worse |
| `lteNRRCC` | 0.1165s | 0.1177s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.21 MB | 55.72 MB | 95.2% | 107.4% |
| `f1ap_rel18.6_specs` | 34.58 MB | 164.71 MB | 110.7% | 105.1% |
| `ngap_rel18.6_specs` | 23.75 MB | 116.60 MB | 108.7% | 104.5% |
| `lteNRRCC` | 74.90 MB | 102.51 MB | 103.6% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0236s | 0.0191s | +0.0045s | worse |
| `f1ap_rel18.6_specs` | 0.0589s | 0.0589s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0403s | 0.0401s | +0.0002s | worse |
| `lteNRRCC` | 0.0680s | 0.0687s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.66 MB | 4.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.05 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 4.42 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.84 MB | 3.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0378s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1090s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0752s | -0.0001s | improved |
| `lteNRRCC` | 0.1370s | 0.1374s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.37 MB | 165.6% | 94.3% |
| `f1ap_rel18.6_specs` | 8.55 MB | 8.44 MB | 101.7% | 108.7% |
| `ngap_rel18.6_specs` | 8.11 MB | 7.47 MB | 107.5% | 83.0% |
| `lteNRRCC` | 51.14 MB | 48.89 MB | 163.0% | 107.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0496s | 0.0379s | +0.0117s | worse |
| `f1ap_rel18.6_specs` | 0.1393s | 0.1132s | +0.0261s | worse |
| `ngap_rel18.6_specs` | 0.1013s | 0.0782s | +0.0231s | worse |
| `lteNRRCC` | 0.1506s | 0.1279s | +0.0227s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.93 MB | 13.59 MB | 110.6% | 177.3% |
| `f1ap_rel18.6_specs` | 11.13 MB | 9.92 MB | 101.7% | 153.2% |
| `ngap_rel18.6_specs` | 9.47 MB | 9.37 MB | 79.1% | 97.4% |
| `lteNRRCC` | 8.55 MB | 101.67 MB | 154.6% | 132.8% |
<!-- BENCH_RESULTS_END -->
