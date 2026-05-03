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
Generated: 2026-05-03T10:59:18.473691+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0364s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1111s | 0.1125s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0767s | +0.0011s | worse |
| `lteNRRCC` | 0.1229s | 0.1210s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 14.4% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0353s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0938s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0656s | 0.0656s | +0.0000s | flat |
| `lteNRRCC` | 0.1258s | 0.1296s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.23 MB | 36.51 MB | 21.7% | 110.3% |
| `f1ap_rel18.6_specs` | 22.04 MB | 103.05 MB | 106.1% | 106.9% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.59 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.59 MB | 65.80 MB | 104.8% | 105.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0328s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0901s | 0.0884s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0622s | 0.0616s | +0.0006s | worse |
| `lteNRRCC` | 0.1153s | 0.1163s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.62 MB | 21.9% | 111.1% |
| `f1ap_rel18.6_specs` | 34.41 MB | 164.75 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.62 MB | 112.0% | 104.8% |
| `lteNRRCC` | 74.92 MB | 102.39 MB | 103.4% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0196s | 0.0129s | +0.0067s | worse |
| `f1ap_rel18.6_specs` | 0.0625s | 0.0660s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0474s | 0.0447s | +0.0027s | worse |
| `lteNRRCC` | 0.0770s | 0.0772s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.62 MB | 4.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.28 MB | 3.84 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 896 KB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.34 MB | 4.83 MB | 0.0% | 1.3% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0397s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1059s | 0.1061s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0752s | -0.0007s | improved |
| `lteNRRCC` | 0.1381s | 0.1370s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.81 MB | 117.3% | 233.0% |
| `f1ap_rel18.6_specs` | 8.55 MB | 8.23 MB | 108.5% | 162.6% |
| `ngap_rel18.6_specs` | 7.47 MB | 7.54 MB | 82.8% | 165.7% |
| `lteNRRCC` | 51.20 MB | 69.23 MB | 163.7% | 163.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0385s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1078s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0735s | 0.0745s | -0.0010s | improved |
| `lteNRRCC` | 0.1226s | 0.1251s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 10.66 MB | 160.8% | 228.6% |
| `f1ap_rel18.6_specs` | 11.66 MB | 164.16 MB | 107.8% | 162.1% |
| `ngap_rel18.6_specs` | 10.39 MB | 8.93 MB | 116.6% | 80.6% |
| `lteNRRCC` | 9.55 MB | 99.02 MB | 117.8% | 232.6% |
<!-- BENCH_RESULTS_END -->
