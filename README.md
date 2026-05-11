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
Generated: 2026-05-11T12:43:16.189810+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0361s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1135s | 0.1137s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0794s | 0.0796s | -0.0002s | improved |
| `lteNRRCC` | 0.1222s | 0.1216s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.72 MB | 53.55 MB | 7.5% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0324s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0938s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0643s | 0.0650s | -0.0007s | improved |
| `lteNRRCC` | 0.1243s | 0.1153s | +0.0090s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.71 MB | 96.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.07 MB | 102.61 MB | 109.4% | 107.0% |
| `ngap_rel18.6_specs` | 16.86 MB | 74.71 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.77 MB | 65.75 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0275s | +0.0066s | worse |
| `f1ap_rel18.6_specs` | 0.0913s | 0.0753s | +0.0160s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0520s | +0.0109s | worse |
| `lteNRRCC` | 0.1179s | 0.1015s | +0.0164s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.41 MB | 88.5% | 107.1% |
| `f1ap_rel18.6_specs` | 35.26 MB | 164.71 MB | 106.5% | 105.4% |
| `ngap_rel18.6_specs` | 23.76 MB | 117.81 MB | 112.0% | 109.5% |
| `lteNRRCC` | 74.63 MB | 102.39 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0224s | 0.0182s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.0659s | 0.0581s | +0.0078s | worse |
| `ngap_rel18.6_specs` | 0.0436s | 0.0390s | +0.0046s | worse |
| `lteNRRCC` | 0.0721s | 0.0676s | +0.0045s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.95 MB | 5.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.19 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.09 MB | 3.98 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0328s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.1090s | 0.0945s | +0.0145s | worse |
| `ngap_rel18.6_specs` | 0.0749s | 0.0657s | +0.0092s | worse |
| `lteNRRCC` | 0.1392s | 0.1123s | +0.0269s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 8.03 MB | 158.9% | 108.9% |
| `f1ap_rel18.6_specs` | 8.03 MB | 106.64 MB | 160.6% | 159.6% |
| `ngap_rel18.6_specs` | 8.18 MB | 7.67 MB | 221.4% | 158.3% |
| `lteNRRCC` | 48.56 MB | 49.12 MB | 152.0% | 104.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0428s | 0.0353s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.1241s | 0.1036s | +0.0205s | worse |
| `ngap_rel18.6_specs` | 0.0854s | 0.0708s | +0.0146s | worse |
| `lteNRRCC` | 0.1337s | 0.1128s | +0.0209s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.77 MB | 10.30 MB | 119.5% | 119.7% |
| `f1ap_rel18.6_specs` | 9.93 MB | 10.77 MB | 82.3% | 239.1% |
| `ngap_rel18.6_specs` | 10.07 MB | 10.44 MB | 119.8% | 119.6% |
| `lteNRRCC` | 8.87 MB | 101.70 MB | 241.0% | 119.6% |
<!-- BENCH_RESULTS_END -->
