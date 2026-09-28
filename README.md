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
Generated: 2026-09-28T18:08:08.610939+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0364s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1115s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0774s | 0.0767s | +0.0007s | worse |
| `lteNRRCC` | 0.1199s | 0.1197s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 82.6% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.33 MB | 100.11 MB | 101.8% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0369s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.0964s | 0.0994s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0706s | 0.0677s | +0.0029s | worse |
| `lteNRRCC` | 0.1301s | 0.1325s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.50 MB | 13.8% | 103.6% |
| `f1ap_rel18.6_specs` | 22.29 MB | 103.38 MB | 106.2% | 103.4% |
| `ngap_rel18.6_specs` | 17.89 MB | 74.48 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.77 MB | 65.73 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0305s | 0.0382s | -0.0077s | improved |
| `f1ap_rel18.6_specs` | 0.0811s | 0.0990s | -0.0179s | improved |
| `ngap_rel18.6_specs` | 0.0589s | 0.0692s | -0.0103s | improved |
| `lteNRRCC` | 0.1044s | 0.1334s | -0.0290s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 55.52 MB | 5.3% | 104.0% |
| `f1ap_rel18.6_specs` | 34.29 MB | 164.59 MB | 103.7% | 102.0% |
| `ngap_rel18.6_specs` | 24.31 MB | 117.70 MB | 104.8% | 102.7% |
| `lteNRRCC` | 74.68 MB | 102.95 MB | 102.0% | 101.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0253s | +0.0135s | worse |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0792s | +0.0169s | worse |
| `ngap_rel18.6_specs` | 0.0550s | 0.0489s | +0.0061s | worse |
| `lteNRRCC` | 0.0926s | 0.0802s | +0.0124s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.52 MB | 8.62 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 9.98 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.00 MB | 8.45 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.03 MB | 6.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0353s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.1112s | 0.0983s | +0.0129s | worse |
| `ngap_rel18.6_specs` | 0.0782s | 0.0688s | +0.0094s | worse |
| `lteNRRCC` | 0.1508s | 0.1186s | +0.0322s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.36 MB | 7.95 MB | 93.8% | 88.9% |
| `f1ap_rel18.6_specs` | 8.96 MB | 8.71 MB | 214.4% | 155.7% |
| `ngap_rel18.6_specs` | 8.40 MB | 8.34 MB | 96.0% | 98.5% |
| `lteNRRCC` | 8.64 MB | 70.52 MB | 156.5% | 170.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0461s | -0.0052s | improved |
| `f1ap_rel18.6_specs` | 0.1212s | 0.1292s | -0.0080s | improved |
| `ngap_rel18.6_specs` | 0.0813s | 0.0919s | -0.0106s | improved |
| `lteNRRCC` | 0.1360s | 0.1391s | -0.0031s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.94 MB | 8.91 MB | 108.0% | 167.5% |
| `f1ap_rel18.6_specs` | 11.23 MB | 164.16 MB | 218.8% | 166.0% |
| `ngap_rel18.6_specs` | 10.09 MB | 9.45 MB | 151.9% | 80.4% |
| `lteNRRCC` | 73.63 MB | 91.79 MB | 160.3% | 106.5% |
<!-- BENCH_RESULTS_END -->
