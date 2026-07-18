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
Generated: 2026-07-18T22:56:39.768538+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0361s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1125s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0765s | 0.0767s | -0.0002s | improved |
| `lteNRRCC` | 0.1211s | 0.1206s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 21.6% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0279s | 0.0371s | -0.0092s | improved |
| `f1ap_rel18.6_specs` | 0.0761s | 0.0946s | -0.0185s | improved |
| `ngap_rel18.6_specs` | 0.0545s | 0.0664s | -0.0119s | improved |
| `lteNRRCC` | 0.0989s | 0.1296s | -0.0307s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.28 MB | 35.91 MB | 57.1% | 108.7% |
| `f1ap_rel18.6_specs` | 22.14 MB | 103.14 MB | 112.0% | 104.3% |
| `ngap_rel18.6_specs` | 19.21 MB | 74.58 MB | 109.1% | 105.6% |
| `lteNRRCC` | 48.77 MB | 66.23 MB | 104.1% | 101.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0346s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0914s | 0.0927s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0652s | +0.0000s | flat |
| `lteNRRCC` | 0.1177s | 0.1191s | -0.0014s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 55.87 MB | 75.9% | 111.1% |
| `f1ap_rel18.6_specs` | 35.27 MB | 163.63 MB | 110.3% | 103.6% |
| `ngap_rel18.6_specs` | 23.95 MB | 117.55 MB | 108.3% | 104.8% |
| `lteNRRCC` | 74.77 MB | 101.97 MB | 105.1% | 104.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0234s | +0.0125s | worse |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0670s | +0.0268s | worse |
| `ngap_rel18.6_specs` | 0.0566s | 0.0466s | +0.0100s | worse |
| `lteNRRCC` | 0.1235s | 0.0800s | +0.0435s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.00 MB | 4.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 1.92 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.80 MB | 1.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.56 MB | 7.39 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0417s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1060s | 0.1138s | -0.0078s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0800s | -0.0049s | improved |
| `lteNRRCC` | 0.1401s | 0.1475s | -0.0074s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.76 MB | 7.50 MB | 159.8% | 159.2% |
| `f1ap_rel18.6_specs` | 8.08 MB | 106.65 MB | 161.1% | 165.6% |
| `ngap_rel18.6_specs` | 7.67 MB | 7.56 MB | 153.0% | 165.5% |
| `lteNRRCC` | 50.80 MB | 53.51 MB | 155.9% | 109.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0400s | -0.0064s | improved |
| `f1ap_rel18.6_specs` | 0.1006s | 0.1205s | -0.0199s | improved |
| `ngap_rel18.6_specs` | 0.0773s | 0.0766s | +0.0007s | worse |
| `lteNRRCC` | 0.1115s | 0.1009s | +0.0106s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.00 MB | 10.27 MB | 103.4% | 138.3% |
| `f1ap_rel18.6_specs` | 10.35 MB | 152.10 MB | 109.6% | 138.1% |
| `ngap_rel18.6_specs` | 10.25 MB | 10.50 MB | 139.1% | 139.6% |
| `lteNRRCC` | 72.96 MB | 77.51 MB | 139.1% | 139.2% |
<!-- BENCH_RESULTS_END -->
