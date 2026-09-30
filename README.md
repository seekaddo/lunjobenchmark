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
Generated: 2026-09-30T16:21:37.612915+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0366s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1151s | 0.1121s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0784s | 0.0768s | +0.0016s | worse |
| `lteNRRCC` | 0.1243s | 0.1198s | +0.0045s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 60.6% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.32 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0235s | 0.0364s | -0.0129s | improved |
| `f1ap_rel18.6_specs` | 0.0675s | 0.0925s | -0.0250s | improved |
| `ngap_rel18.6_specs` | 0.0422s | 0.0665s | -0.0243s | improved |
| `lteNRRCC` | 0.0865s | 0.1242s | -0.0377s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 36.38 MB | 11.8% | 105.3% |
| `f1ap_rel18.6_specs` | 22.03 MB | 102.89 MB | 100.0% | 102.6% |
| `ngap_rel18.6_specs` | 18.14 MB | 74.64 MB | 105.6% | 103.0% |
| `lteNRRCC` | 47.60 MB | 66.43 MB | 102.5% | 102.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0384s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1043s | 0.0979s | +0.0064s | worse |
| `ngap_rel18.6_specs` | 0.0693s | 0.0704s | -0.0011s | improved |
| `lteNRRCC` | 0.1230s | 0.1302s | -0.0072s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.72 MB | 14.3% | 107.1% |
| `f1ap_rel18.6_specs` | 35.11 MB | 164.70 MB | 103.4% | 101.7% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.72 MB | 108.0% | 102.2% |
| `lteNRRCC` | 74.39 MB | 102.53 MB | 101.7% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0494s | 0.0430s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.1318s | 0.1204s | +0.0114s | worse |
| `ngap_rel18.6_specs` | 0.0783s | 0.0750s | +0.0033s | worse |
| `lteNRRCC` | 0.1050s | 0.1239s | -0.0189s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.67 MB | 3.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.56 MB | 9.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.75 MB | 5.05 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.03 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0274s | +0.0137s | worse |
| `f1ap_rel18.6_specs` | 0.1140s | 0.0765s | +0.0375s | worse |
| `ngap_rel18.6_specs` | 0.0805s | 0.0538s | +0.0267s | worse |
| `lteNRRCC` | 0.1394s | 0.0994s | +0.0400s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.79 MB | 0.0% | 90.9% |
| `f1ap_rel18.6_specs` | 8.71 MB | 106.61 MB | 110.8% | 102.7% |
| `ngap_rel18.6_specs` | 8.09 MB | 8.15 MB | 161.0% | 163.3% |
| `lteNRRCC` | 48.87 MB | 69.58 MB | 159.0% | 159.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0446s | -0.0059s | improved |
| `f1ap_rel18.6_specs` | 0.1079s | 0.1204s | -0.0125s | improved |
| `ngap_rel18.6_specs` | 0.0746s | 0.0833s | -0.0087s | improved |
| `lteNRRCC` | 0.1255s | 0.1320s | -0.0065s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.45 MB | 8.63 MB | 0.0% | 78.8% |
| `f1ap_rel18.6_specs` | 11.37 MB | 9.12 MB | 111.6% | 94.1% |
| `ngap_rel18.6_specs` | 10.55 MB | 11.11 MB | 113.2% | 226.7% |
| `lteNRRCC` | 8.41 MB | 77.56 MB | 162.3% | 170.7% |
<!-- BENCH_RESULTS_END -->
