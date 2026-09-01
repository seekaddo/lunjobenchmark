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
Generated: 2026-09-01T14:40:42.081463+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0342s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1078s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0761s | 0.0746s | +0.0015s | worse |
| `lteNRRCC` | 0.1214s | 0.1179s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 62.1% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0311s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.0906s | 0.0912s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0616s | +0.0023s | worse |
| `lteNRRCC` | 0.1228s | 0.1106s | +0.0122s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.73 MB | 95.5% | 103.7% |
| `f1ap_rel18.6_specs` | 22.22 MB | 103.45 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.64 MB | 108.0% | 104.9% |
| `lteNRRCC` | 48.76 MB | 66.10 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0348s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0945s | 0.0908s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0625s | +0.0033s | worse |
| `lteNRRCC` | 0.1293s | 0.1166s | +0.0127s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.83 MB | 84.0% | 103.6% |
| `f1ap_rel18.6_specs` | 35.22 MB | 164.75 MB | 106.2% | 101.8% |
| `ngap_rel18.6_specs` | 24.11 MB | 117.65 MB | 103.8% | 102.3% |
| `lteNRRCC` | 74.51 MB | 102.96 MB | 103.2% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0328s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0882s | 0.1138s | -0.0256s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0634s | +0.0023s | worse |
| `lteNRRCC` | 0.1181s | 0.1098s | +0.0083s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.73 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.47 MB | 10.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.23 MB | 8.30 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.48 MB | 6.66 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0452s | -0.0100s | improved |
| `f1ap_rel18.6_specs` | 0.0965s | 0.1254s | -0.0289s | improved |
| `ngap_rel18.6_specs` | 0.0666s | 0.0870s | -0.0204s | improved |
| `lteNRRCC` | 0.1133s | 0.1584s | -0.0451s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 8.52 MB | 0.0% | 195.5% |
| `f1ap_rel18.6_specs` | 8.86 MB | 8.80 MB | 191.3% | 81.0% |
| `ngap_rel18.6_specs` | 8.37 MB | 8.46 MB | 97.9% | 99.0% |
| `lteNRRCC` | 8.67 MB | 61.43 MB | 94.6% | 108.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0372s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1084s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0776s | -0.0007s | improved |
| `lteNRRCC` | 0.1281s | 0.1228s | +0.0053s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 9.85 MB | 0.0% | 192.9% |
| `f1ap_rel18.6_specs` | 11.84 MB | 154.80 MB | 108.9% | 107.6% |
| `ngap_rel18.6_specs` | 9.50 MB | 11.34 MB | 171.4% | 105.9% |
| `lteNRRCC` | 8.88 MB | 99.02 MB | 144.2% | 146.7% |
<!-- BENCH_RESULTS_END -->
