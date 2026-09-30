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
Generated: 2026-09-30T01:11:20.219923+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0361s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1121s | 0.1100s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0768s | 0.0759s | +0.0009s | worse |
| `lteNRRCC` | 0.1198s | 0.1206s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 67.9% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0312s | +0.0052s | worse |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0826s | +0.0099s | worse |
| `ngap_rel18.6_specs` | 0.0665s | 0.0586s | +0.0079s | worse |
| `lteNRRCC` | 0.1242s | 0.1035s | +0.0207s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.41 MB | 84.0% | 107.4% |
| `f1ap_rel18.6_specs` | 22.27 MB | 103.11 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.62 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.00 MB | 66.36 MB | 103.3% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0266s | +0.0118s | worse |
| `f1ap_rel18.6_specs` | 0.0979s | 0.0845s | +0.0134s | worse |
| `ngap_rel18.6_specs` | 0.0704s | 0.0571s | +0.0133s | worse |
| `lteNRRCC` | 0.1302s | 0.0868s | +0.0434s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.55 MB | 55.48 MB | 92.0% | 106.9% |
| `f1ap_rel18.6_specs` | 35.18 MB | 164.73 MB | 106.2% | 103.3% |
| `ngap_rel18.6_specs` | 24.30 MB | 117.63 MB | 107.7% | 102.2% |
| `lteNRRCC` | 74.23 MB | 102.62 MB | 103.1% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0430s | 0.0339s | +0.0091s | worse |
| `f1ap_rel18.6_specs` | 0.1204s | 0.0946s | +0.0258s | worse |
| `ngap_rel18.6_specs` | 0.0750s | 0.0721s | +0.0029s | worse |
| `lteNRRCC` | 0.1239s | 0.1095s | +0.0144s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.22 MB | 8.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.59 MB | 1.58 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.81 MB | 6.53 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.44 MB | 1.17 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0274s | 0.0502s | -0.0228s | improved |
| `f1ap_rel18.6_specs` | 0.0765s | 0.1157s | -0.0392s | improved |
| `ngap_rel18.6_specs` | 0.0538s | 0.0811s | -0.0273s | improved |
| `lteNRRCC` | 0.0994s | 0.1445s | -0.0451s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.31 MB | 38.39 MB | 0.0% | 110.4% |
| `f1ap_rel18.6_specs` | 13.03 MB | 13.09 MB | 99.7% | 81.1% |
| `ngap_rel18.6_specs` | 11.66 MB | 17.07 MB | 91.9% | 107.7% |
| `lteNRRCC` | 15.12 MB | 70.52 MB | 78.3% | 104.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0446s | 0.0372s | +0.0074s | worse |
| `f1ap_rel18.6_specs` | 0.1204s | 0.1072s | +0.0132s | worse |
| `ngap_rel18.6_specs` | 0.0833s | 0.0737s | +0.0096s | worse |
| `lteNRRCC` | 0.1320s | 0.1267s | +0.0053s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.26 MB | 9.89 MB | 212.6% | 78.7% |
| `f1ap_rel18.6_specs` | 11.02 MB | 10.23 MB | 171.4% | 166.0% |
| `ngap_rel18.6_specs` | 9.46 MB | 10.49 MB | 158.0% | 106.8% |
| `lteNRRCC` | 8.73 MB | 101.70 MB | 78.3% | 102.8% |
<!-- BENCH_RESULTS_END -->
