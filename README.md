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
Generated: 2026-09-04T14:08:28.660089+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0336s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1073s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0729s | 0.0735s | -0.0006s | improved |
| `lteNRRCC` | 0.1161s | 0.1172s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 81.8% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.6% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0351s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0944s | 0.0951s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0667s | 0.0673s | -0.0006s | improved |
| `lteNRRCC` | 0.1292s | 0.1297s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.70 MB | 14.9% | 103.7% |
| `f1ap_rel18.6_specs` | 21.80 MB | 102.98 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.01 MB | 104.0% | 102.3% |
| `lteNRRCC` | 48.77 MB | 66.34 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0361s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0895s | 0.0943s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0637s | 0.0672s | -0.0035s | improved |
| `lteNRRCC` | 0.1168s | 0.1320s | -0.0152s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.66 MB | 83.3% | 103.8% |
| `f1ap_rel18.6_specs` | 34.74 MB | 163.85 MB | 103.6% | 101.8% |
| `ngap_rel18.6_specs` | 24.47 MB | 117.76 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.95 MB | 102.82 MB | 103.5% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0261s | 0.0226s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.0817s | 0.1022s | -0.0205s | improved |
| `ngap_rel18.6_specs` | 0.0485s | 0.0997s | -0.0512s | improved |
| `lteNRRCC` | 0.0944s | 0.1019s | -0.0075s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.41 MB | 7.09 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.22 MB | 9.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.16 MB | 8.20 MB | 0.0% | 1.2% |
| `lteNRRCC` | 7.08 MB | 7.38 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0423s | -0.0046s | improved |
| `f1ap_rel18.6_specs` | 0.1017s | 0.1153s | -0.0136s | improved |
| `ngap_rel18.6_specs` | 0.0724s | 0.0771s | -0.0047s | improved |
| `lteNRRCC` | 0.1124s | 0.1395s | -0.0271s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.12 MB | 8.41 MB | 122.2% | 125.7% |
| `f1ap_rel18.6_specs` | 8.55 MB | 105.81 MB | 130.0% | 124.4% |
| `ngap_rel18.6_specs` | 8.43 MB | 8.37 MB | 127.2% | 124.3% |
| `lteNRRCC` | 8.48 MB | 53.33 MB | 129.0% | 126.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0418s | -0.0039s | improved |
| `f1ap_rel18.6_specs` | 0.1090s | 0.1186s | -0.0096s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0836s | -0.0060s | improved |
| `lteNRRCC` | 0.1248s | 0.1366s | -0.0118s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.23 MB | 10.48 MB | 114.0% | 240.3% |
| `f1ap_rel18.6_specs` | 9.41 MB | 164.20 MB | 182.6% | 182.0% |
| `ngap_rel18.6_specs` | 8.72 MB | 9.34 MB | 176.7% | 172.8% |
| `lteNRRCC` | 9.38 MB | 98.59 MB | 232.5% | 118.4% |
<!-- BENCH_RESULTS_END -->
