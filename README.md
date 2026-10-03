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
Generated: 2026-10-03T01:01:50.549021+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0372s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1069s | 0.1118s | -0.0049s | improved |
| `ngap_rel18.6_specs` | 0.0729s | 0.0771s | -0.0042s | improved |
| `lteNRRCC` | 0.1185s | 0.1208s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 81.0% | 107.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0375s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0972s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0669s | 0.0701s | -0.0032s | improved |
| `lteNRRCC` | 0.1298s | 0.1328s | -0.0030s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 36.22 MB | 14.1% | 103.7% |
| `f1ap_rel18.6_specs` | 21.81 MB | 103.43 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 18.01 MB | 74.50 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.30 MB | 66.04 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0361s | -0.0031s | improved |
| `f1ap_rel18.6_specs` | 0.0882s | 0.0953s | -0.0071s | improved |
| `ngap_rel18.6_specs` | 0.0613s | 0.0672s | -0.0059s | improved |
| `lteNRRCC` | 0.1173s | 0.1298s | -0.0125s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.49 MB | 76.0% | 108.0% |
| `f1ap_rel18.6_specs` | 34.55 MB | 163.75 MB | 103.6% | 103.8% |
| `ngap_rel18.6_specs` | 23.96 MB | 117.49 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.54 MB | 102.82 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0398s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.0895s | 0.0849s | +0.0046s | worse |
| `ngap_rel18.6_specs` | 0.0511s | 0.0699s | -0.0188s | improved |
| `lteNRRCC` | 0.0921s | 0.0938s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.56 MB | 3.66 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.67 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.66 MB | 6.72 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.61 MB | 8.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0405s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1081s | 0.1148s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0748s | 0.0789s | -0.0041s | improved |
| `lteNRRCC` | 0.1379s | 0.1406s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.52 MB | 7.53 MB | 0.0% | 79.4% |
| `f1ap_rel18.6_specs` | 8.58 MB | 8.41 MB | 105.8% | 159.2% |
| `ngap_rel18.6_specs` | 7.95 MB | 7.89 MB | 154.2% | 157.3% |
| `lteNRRCC` | 8.38 MB | 51.86 MB | 155.8% | 155.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0392s | -0.0050s | improved |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1163s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0708s | 0.0817s | -0.0109s | improved |
| `lteNRRCC` | 0.1115s | 0.1270s | -0.0155s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.07 MB | 0.0% | 138.4% |
| `f1ap_rel18.6_specs` | 11.01 MB | 164.17 MB | 141.9% | 106.9% |
| `ngap_rel18.6_specs` | 10.43 MB | 10.36 MB | 140.3% | 140.2% |
| `lteNRRCC` | 8.79 MB | 80.50 MB | 208.9% | 140.5% |
<!-- BENCH_RESULTS_END -->
