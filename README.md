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
Generated: 2026-05-15T23:02:18.872628+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0375s | 0.0368s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1173s | 0.1139s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0784s | +0.0019s | worse |
| `lteNRRCC` | 0.1241s | 0.1236s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.80 MB | 53.55 MB | 7.5% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 107.5% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.8% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0350s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0949s | 0.0962s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0675s | 0.0665s | +0.0010s | worse |
| `lteNRRCC` | 0.1258s | 0.1179s | +0.0079s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.81 MB | 36.11 MB | 92.6% | 110.0% |
| `f1ap_rel18.6_specs` | 21.96 MB | 103.21 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.71 MB | 74.57 MB | 114.8% | 106.7% |
| `lteNRRCC` | 48.61 MB | 66.04 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0340s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0914s | 0.0989s | -0.0075s | improved |
| `ngap_rel18.6_specs` | 0.0650s | 0.0682s | -0.0032s | improved |
| `lteNRRCC` | 0.1181s | 0.1163s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 55.71 MB | 85.2% | 110.7% |
| `f1ap_rel18.6_specs` | 35.24 MB | 163.86 MB | 110.0% | 103.5% |
| `ngap_rel18.6_specs` | 23.88 MB | 117.41 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.75 MB | 102.75 MB | 105.1% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0199s | 0.0131s | +0.0068s | worse |
| `f1ap_rel18.6_specs` | 0.0666s | 0.0679s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0501s | 0.0457s | +0.0044s | worse |
| `lteNRRCC` | 0.0708s | 0.0850s | -0.0142s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.95 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 8.09 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.39 MB | 8.52 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.81 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0394s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1092s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0762s | 0.0762s | +0.0000s | flat |
| `lteNRRCC` | 0.1291s | 0.1423s | -0.0132s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.04 MB | 7.84 MB | 235.5% | 81.2% |
| `f1ap_rel18.6_specs` | 8.72 MB | 8.53 MB | 160.9% | 156.5% |
| `ngap_rel18.6_specs` | 8.16 MB | 8.35 MB | 101.5% | 114.5% |
| `lteNRRCC` | 8.53 MB | 70.04 MB | 92.5% | 103.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0453s | -0.0044s | improved |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1216s | -0.0080s | improved |
| `ngap_rel18.6_specs` | 0.0794s | 0.0848s | -0.0054s | improved |
| `lteNRRCC` | 0.1280s | 0.1410s | -0.0130s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.52 MB | 8.58 MB | 159.9% | 157.4% |
| `f1ap_rel18.6_specs` | 9.68 MB | 164.16 MB | 159.8% | 113.8% |
| `ngap_rel18.6_specs` | 10.38 MB | 8.96 MB | 109.9% | 80.3% |
| `lteNRRCC` | 8.43 MB | 81.71 MB | 158.1% | 106.8% |
<!-- BENCH_RESULTS_END -->
