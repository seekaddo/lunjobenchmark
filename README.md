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
Generated: 2026-10-03T14:38:28.358322+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0344s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1095s | 0.1069s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0754s | 0.0729s | +0.0025s | worse |
| `lteNRRCC` | 0.1179s | 0.1185s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 18.2% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.32 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0359s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0961s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0669s | -0.0011s | improved |
| `lteNRRCC` | 0.1295s | 0.1298s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 36.50 MB | 19.3% | 107.7% |
| `f1ap_rel18.6_specs` | 21.31 MB | 103.15 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.61 MB | 108.0% | 104.8% |
| `lteNRRCC` | 48.62 MB | 65.66 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0237s | 0.0330s | -0.0093s | improved |
| `f1ap_rel18.6_specs` | 0.0683s | 0.0882s | -0.0199s | improved |
| `ngap_rel18.6_specs` | 0.0528s | 0.0613s | -0.0085s | improved |
| `lteNRRCC` | 0.0908s | 0.1173s | -0.0265s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.75 MB | 55.89 MB | 68.4% | 105.6% |
| `f1ap_rel18.6_specs` | 34.71 MB | 163.52 MB | 105.0% | 100.0% |
| `ngap_rel18.6_specs` | 24.25 MB | 117.73 MB | 100.0% | 103.1% |
| `lteNRRCC` | 74.89 MB | 102.33 MB | 102.3% | 102.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0408s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0871s | 0.0895s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0630s | 0.0511s | +0.0119s | worse |
| `lteNRRCC` | 0.1181s | 0.0921s | +0.0260s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.98 MB | 4.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.36 MB | 8.91 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.41 MB | 8.23 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.17 MB | 3.53 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0407s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1081s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0768s | 0.0748s | +0.0020s | worse |
| `lteNRRCC` | 0.1412s | 0.1379s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.36 MB | 7.85 MB | 0.0% | 109.0% |
| `f1ap_rel18.6_specs` | 8.88 MB | 8.00 MB | 222.2% | 161.3% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.58 MB | 161.1% | 79.6% |
| `lteNRRCC` | 50.83 MB | 61.38 MB | 154.1% | 108.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0342s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1115s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0708s | +0.0067s | worse |
| `lteNRRCC` | 0.1289s | 0.1115s | +0.0174s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.07 MB | 8.63 MB | 0.0% | 159.6% |
| `f1ap_rel18.6_specs` | 11.24 MB | 9.78 MB | 112.2% | 156.7% |
| `ngap_rel18.6_specs` | 8.99 MB | 8.93 MB | 90.6% | 158.8% |
| `lteNRRCC` | 8.66 MB | 90.61 MB | 155.3% | 156.4% |
<!-- BENCH_RESULTS_END -->
