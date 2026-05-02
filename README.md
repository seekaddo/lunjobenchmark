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
Generated: 2026-05-02T22:52:52.276375+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0355s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1118s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0757s | +0.0010s | worse |
| `lteNRRCC` | 0.1210s | 0.1204s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 30.3% | 113.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0347s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0924s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0656s | 0.0639s | +0.0017s | worse |
| `lteNRRCC` | 0.1296s | 0.1236s | +0.0060s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.24 MB | 36.72 MB | 100.0% | 110.7% |
| `f1ap_rel18.6_specs` | 22.42 MB | 103.32 MB | 106.1% | 103.4% |
| `ngap_rel18.6_specs` | 16.76 MB | 74.61 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.60 MB | 66.36 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0338s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0884s | 0.0908s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0616s | 0.0625s | -0.0009s | improved |
| `lteNRRCC` | 0.1163s | 0.1160s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.70 MB | 92.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.19 MB | 164.19 MB | 113.8% | 105.5% |
| `ngap_rel18.6_specs` | 23.86 MB | 117.50 MB | 112.0% | 104.7% |
| `lteNRRCC` | 74.85 MB | 102.79 MB | 103.4% | 105.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0129s | 0.0228s | -0.0099s | improved |
| `f1ap_rel18.6_specs` | 0.0660s | 0.0808s | -0.0148s | improved |
| `ngap_rel18.6_specs` | 0.0447s | 0.0446s | +0.0001s | worse |
| `lteNRRCC` | 0.0772s | 0.0734s | +0.0038s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.78 MB | 4.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.11 MB | 4.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.19 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.00 MB | 4.36 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0395s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1061s | 0.1093s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0767s | -0.0015s | improved |
| `lteNRRCC` | 0.1370s | 0.1438s | -0.0068s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.34 MB | 7.29 MB | 164.5% | 156.2% |
| `f1ap_rel18.6_specs` | 7.73 MB | 106.65 MB | 164.9% | 111.1% |
| `ngap_rel18.6_specs` | 8.24 MB | 7.92 MB | 222.4% | 77.1% |
| `lteNRRCC` | 50.91 MB | 54.14 MB | 159.3% | 115.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0399s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1107s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0860s | -0.0115s | improved |
| `lteNRRCC` | 0.1251s | 0.1319s | -0.0068s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.65 MB | 8.58 MB | 81.0% | 160.2% |
| `f1ap_rel18.6_specs` | 9.99 MB | 162.41 MB | 157.2% | 161.8% |
| `ngap_rel18.6_specs` | 8.89 MB | 9.02 MB | 80.6% | 163.3% |
| `lteNRRCC` | 73.77 MB | 75.83 MB | 229.8% | 108.4% |
<!-- BENCH_RESULTS_END -->
