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
Generated: 2026-11-01T00:52:53.717994+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0383s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1220s | 0.1170s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0842s | 0.0822s | +0.0020s | worse |
| `lteNRRCC` | 0.1271s | 0.1228s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.75 MB | 53.55 MB | 83.3% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 101.9% |
| `lteNRRCC` | 72.35 MB | 100.18 MB | 101.6% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0301s | 0.0308s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0977s | 0.0930s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0662s | 0.0735s | -0.0073s | improved |
| `lteNRRCC` | 0.1113s | 0.1027s | +0.0086s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.58 MB | 34.65 MB | 13.9% | 104.3% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 108.7% | 101.8% |
| `ngap_rel18.6_specs` | 18.04 MB | 72.65 MB | 105.3% | 104.9% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 104.2% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0557s | 0.0532s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.1709s | 0.1653s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.1173s | 0.1194s | -0.0021s | improved |
| `lteNRRCC` | 0.1665s | 0.1631s | +0.0034s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 53.73 MB | 76.7% | 105.0% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.6% | 102.1% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 106.9% | 102.8% |
| `lteNRRCC` | 72.64 MB | 100.36 MB | 102.7% | 102.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0280s | 0.0251s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.1104s | 0.0836s | +0.0268s | worse |
| `ngap_rel18.6_specs` | 0.0774s | 0.0505s | +0.0269s | worse |
| `lteNRRCC` | 0.1146s | 0.0854s | +0.0292s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.97 MB | 8.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.67 MB | 7.25 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.27 MB | 5.00 MB | 1.3% | 0.0% |
| `lteNRRCC` | 2.44 MB | 7.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0457s | 0.0416s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1224s | 0.1111s | +0.0113s | worse |
| `ngap_rel18.6_specs` | 0.0881s | 0.0780s | +0.0101s | worse |
| `lteNRRCC` | 0.1395s | 0.1279s | +0.0116s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 8.05 MB | 0.0% | 86.1% |
| `f1ap_rel18.6_specs` | 9.05 MB | 9.00 MB | 176.0% | 136.7% |
| `ngap_rel18.6_specs` | 8.44 MB | 8.38 MB | 91.7% | 92.0% |
| `lteNRRCC` | 8.55 MB | 8.65 MB | 89.0% | 144.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0452s | 0.0371s | +0.0081s | worse |
| `f1ap_rel18.6_specs` | 0.1356s | 0.1049s | +0.0307s | worse |
| `ngap_rel18.6_specs` | 0.0942s | 0.0724s | +0.0218s | worse |
| `lteNRRCC` | 0.1384s | 0.1167s | +0.0217s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 10.55 MB | 0.0% | 109.0% |
| `f1ap_rel18.6_specs` | 11.21 MB | 133.54 MB | 98.9% | 171.7% |
| `ngap_rel18.6_specs` | 10.55 MB | 10.39 MB | 113.2% | 77.5% |
| `lteNRRCC` | 9.31 MB | 84.63 MB | 167.7% | 208.4% |
<!-- BENCH_RESULTS_END -->
