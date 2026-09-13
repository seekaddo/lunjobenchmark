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
Generated: 2026-09-13T14:13:09.693445+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0346s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1114s | 0.1092s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0783s | 0.0755s | +0.0028s | worse |
| `lteNRRCC` | 0.1231s | 0.1187s | +0.0044s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 17.8% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0342s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0975s | 0.0923s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0657s | +0.0006s | worse |
| `lteNRRCC` | 0.1303s | 0.1251s | +0.0052s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.61 MB | 80.8% | 107.4% |
| `f1ap_rel18.6_specs` | 22.12 MB | 103.33 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 18.02 MB | 74.56 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.35 MB | 65.50 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0324s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0896s | 0.0890s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0647s | 0.0617s | +0.0030s | worse |
| `lteNRRCC` | 0.1173s | 0.1164s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 55.18 MB | 73.1% | 107.7% |
| `f1ap_rel18.6_specs` | 34.75 MB | 164.63 MB | 103.4% | 103.7% |
| `ngap_rel18.6_specs` | 23.98 MB | 117.88 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.89 MB | 102.44 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0285s | 0.0514s | -0.0229s | improved |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0704s | +0.0221s | worse |
| `ngap_rel18.6_specs` | 0.0535s | 0.0487s | +0.0048s | worse |
| `lteNRRCC` | 0.0926s | 0.0790s | +0.0136s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.19 MB | 4.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.19 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.25 MB | 8.25 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.89 MB | 5.16 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0403s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.0901s | 0.1126s | -0.0225s | improved |
| `ngap_rel18.6_specs` | 0.0626s | 0.0786s | -0.0160s | improved |
| `lteNRRCC` | 0.1111s | 0.1410s | -0.0299s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.07 MB | 7.97 MB | 131.2% | 139.2% |
| `f1ap_rel18.6_specs` | 8.55 MB | 106.64 MB | 111.0% | 139.4% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.33 MB | 140.2% | 137.5% |
| `lteNRRCC` | 8.54 MB | 61.72 MB | 99.3% | 139.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0394s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1141s | 0.1135s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0782s | -0.0011s | improved |
| `lteNRRCC` | 0.1276s | 0.1310s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.54 MB | 8.66 MB | 106.6% | 158.8% |
| `f1ap_rel18.6_specs` | 9.72 MB | 164.16 MB | 158.8% | 159.1% |
| `ngap_rel18.6_specs` | 10.95 MB | 9.21 MB | 224.8% | 154.0% |
| `lteNRRCC` | 8.69 MB | 84.21 MB | 153.8% | 156.7% |
<!-- BENCH_RESULTS_END -->
