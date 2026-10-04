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
Generated: 2026-10-04T00:26:55.609142+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0344s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1082s | 0.1095s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0760s | 0.0754s | +0.0006s | worse |
| `lteNRRCC` | 0.1186s | 0.1179s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 78.3% | 107.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0346s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0964s | 0.0947s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0676s | 0.0658s | +0.0018s | worse |
| `lteNRRCC` | 0.1291s | 0.1295s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 36.39 MB | 76.9% | 107.7% |
| `f1ap_rel18.6_specs` | 22.02 MB | 103.29 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.91 MB | 74.61 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.58 MB | 66.12 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0237s | +0.0104s | worse |
| `f1ap_rel18.6_specs` | 0.0914s | 0.0683s | +0.0231s | worse |
| `ngap_rel18.6_specs` | 0.0629s | 0.0528s | +0.0101s | worse |
| `lteNRRCC` | 0.1182s | 0.0908s | +0.0274s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.13 MB | 80.0% | 103.8% |
| `f1ap_rel18.6_specs` | 34.57 MB | 164.64 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.54 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.96 MB | 102.63 MB | 101.7% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0195s | 0.0401s | -0.0206s | improved |
| `f1ap_rel18.6_specs` | 0.0666s | 0.0871s | -0.0205s | improved |
| `ngap_rel18.6_specs` | 0.0516s | 0.0630s | -0.0114s | improved |
| `lteNRRCC` | 0.0783s | 0.1181s | -0.0398s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.61 MB | 7.83 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.67 MB | 9.28 MB | 0.0% | 1.2% |
| `ngap_rel18.6_specs` | 8.38 MB | 8.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.45 MB | 7.44 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0390s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1033s | 0.1100s | -0.0067s | improved |
| `ngap_rel18.6_specs` | 0.0694s | 0.0768s | -0.0074s | improved |
| `lteNRRCC` | 0.1118s | 0.1412s | -0.0294s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.09 MB | 8.36 MB | 0.0% | 132.7% |
| `f1ap_rel18.6_specs` | 8.37 MB | 8.70 MB | 201.0% | 135.5% |
| `ngap_rel18.6_specs` | 8.08 MB | 8.32 MB | 131.6% | 126.6% |
| `lteNRRCC` | 8.01 MB | 68.63 MB | 133.8% | 122.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0383s | -0.0051s | improved |
| `f1ap_rel18.6_specs` | 0.0978s | 0.1136s | -0.0158s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0775s | -0.0117s | improved |
| `lteNRRCC` | 0.1095s | 0.1289s | -0.0194s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.08 MB | 10.20 MB | 137.5% | 142.5% |
| `f1ap_rel18.6_specs` | 10.56 MB | 164.18 MB | 140.9% | 139.2% |
| `ngap_rel18.6_specs` | 10.36 MB | 10.30 MB | 139.4% | 139.7% |
| `lteNRRCC` | 8.79 MB | 99.13 MB | 104.4% | 132.0% |
<!-- BENCH_RESULTS_END -->
