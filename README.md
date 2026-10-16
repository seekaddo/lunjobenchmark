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
Generated: 2026-10-16T00:12:01.036057+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0354s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1101s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0747s | 0.0756s | -0.0009s | improved |
| `lteNRRCC` | 0.1193s | 0.1194s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 85.0% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0262s | 0.0347s | -0.0085s | improved |
| `f1ap_rel18.6_specs` | 0.0729s | 0.0933s | -0.0204s | improved |
| `ngap_rel18.6_specs` | 0.0509s | 0.0657s | -0.0148s | improved |
| `lteNRRCC` | 0.0968s | 0.1300s | -0.0332s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 36.41 MB | 61.5% | 100.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.09 MB | 104.2% | 102.3% |
| `ngap_rel18.6_specs` | 18.18 MB | 74.50 MB | 105.3% | 103.0% |
| `lteNRRCC` | 48.48 MB | 66.37 MB | 102.1% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0285s | 0.0344s | -0.0059s | improved |
| `f1ap_rel18.6_specs` | 0.0758s | 0.0931s | -0.0173s | improved |
| `ngap_rel18.6_specs` | 0.0528s | 0.0639s | -0.0111s | improved |
| `lteNRRCC` | 0.1016s | 0.1201s | -0.0185s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 55.76 MB | 43.2% | 104.5% |
| `f1ap_rel18.6_specs` | 34.27 MB | 164.55 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 24.09 MB | 117.55 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.50 MB | 102.71 MB | 104.2% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0206s | 0.0320s | -0.0114s | improved |
| `f1ap_rel18.6_specs` | 0.0862s | 0.0702s | +0.0160s | worse |
| `ngap_rel18.6_specs` | 0.0905s | 0.0565s | +0.0340s | worse |
| `lteNRRCC` | 0.0884s | 0.1081s | -0.0197s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.78 MB | 4.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.16 MB | 4.20 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.64 MB | 8.31 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.38 MB | 7.48 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0368s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1045s | +0.0099s | worse |
| `ngap_rel18.6_specs` | 0.0811s | 0.0722s | +0.0089s | worse |
| `lteNRRCC` | 0.1441s | 0.1109s | +0.0332s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.27 MB | 7.78 MB | 203.3% | 99.0% |
| `f1ap_rel18.6_specs` | 8.51 MB | 106.61 MB | 153.7% | 150.1% |
| `ngap_rel18.6_specs` | 7.95 MB | 7.84 MB | 152.1% | 158.0% |
| `lteNRRCC` | 8.05 MB | 56.72 MB | 150.1% | 109.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0441s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1177s | 0.1234s | -0.0057s | improved |
| `ngap_rel18.6_specs` | 0.0837s | 0.0869s | -0.0032s | improved |
| `lteNRRCC` | 0.1368s | 0.1357s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.12 MB | 9.04 MB | 0.0% | 144.2% |
| `f1ap_rel18.6_specs` | 9.46 MB | 10.40 MB | 158.4% | 73.7% |
| `ngap_rel18.6_specs` | 10.53 MB | 9.45 MB | 201.0% | 145.5% |
| `lteNRRCC` | 9.52 MB | 98.65 MB | 99.4% | 175.9% |
<!-- BENCH_RESULTS_END -->
