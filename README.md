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
Generated: 2026-03-25T10:56:53.781416+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0376s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1122s | 0.1146s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0784s | 0.0792s | -0.0008s | improved |
| `lteNRRCC` | 0.1214s | 0.1222s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 53.55 MB | 7.7% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 103.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0352s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0956s | 0.0942s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0682s | 0.0668s | +0.0014s | worse |
| `lteNRRCC` | 0.1296s | 0.1289s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 36.41 MB | 92.6% | 110.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.38 MB | 108.8% | 105.1% |
| `ngap_rel18.6_specs` | 16.65 MB | 74.62 MB | 114.3% | 106.5% |
| `lteNRRCC` | 48.54 MB | 65.79 MB | 104.5% | 105.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0357s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0918s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0639s | +0.0001s | worse |
| `lteNRRCC` | 0.1184s | 0.1183s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.30 MB | 55.87 MB | 25.8% | 110.3% |
| `f1ap_rel18.6_specs` | 35.14 MB | 164.37 MB | 113.3% | 105.3% |
| `ngap_rel18.6_specs` | 23.57 MB | 117.70 MB | 107.7% | 107.0% |
| `lteNRRCC` | 74.88 MB | 102.88 MB | 103.3% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0195s | 0.0216s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.0583s | 0.0655s | -0.0072s | improved |
| `ngap_rel18.6_specs` | 0.0457s | 0.0448s | +0.0009s | worse |
| `lteNRRCC` | 0.0743s | 0.0734s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.64 MB | 4.45 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.06 MB | 4.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.84 MB | 4.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.73 MB | 4.64 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0385s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1054s | 0.1057s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0744s | 0.0731s | +0.0013s | worse |
| `lteNRRCC` | 0.1379s | 0.1437s | -0.0058s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.34 MB | 7.88 MB | 162.8% | 114.3% |
| `f1ap_rel18.6_specs` | 8.44 MB | 106.64 MB | 113.8% | 107.5% |
| `ngap_rel18.6_specs` | 8.36 MB | 7.95 MB | 112.2% | 116.3% |
| `lteNRRCC` | 51.45 MB | 51.20 MB | 165.0% | 108.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0389s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1122s | 0.1105s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0773s | -0.0003s | improved |
| `lteNRRCC` | 0.1289s | 0.1254s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.29 MB | 8.52 MB | 235.4% | 167.2% |
| `f1ap_rel18.6_specs` | 9.74 MB | 164.19 MB | 164.4% | 239.3% |
| `ngap_rel18.6_specs` | 8.95 MB | 8.95 MB | 163.7% | 163.8% |
| `lteNRRCC` | 8.55 MB | 77.01 MB | 162.6% | 116.1% |
<!-- BENCH_RESULTS_END -->
