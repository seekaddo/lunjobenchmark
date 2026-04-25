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
Generated: 2026-04-25T10:52:09.925729+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0379s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1142s | 0.1172s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0800s | 0.0796s | +0.0004s | worse |
| `lteNRRCC` | 0.1238s | 0.1242s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.91 MB | 53.55 MB | 10.5% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0357s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0947s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0668s | 0.0662s | +0.0006s | worse |
| `lteNRRCC` | 0.1303s | 0.1265s | +0.0038s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.12 MB | 36.48 MB | 29.6% | 110.7% |
| `f1ap_rel18.6_specs` | 21.89 MB | 103.45 MB | 106.1% | 103.2% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.47 MB | 107.4% | 106.7% |
| `lteNRRCC` | 48.39 MB | 65.76 MB | 104.5% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0286s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.0878s | 0.0760s | +0.0118s | worse |
| `ngap_rel18.6_specs` | 0.0618s | 0.0525s | +0.0093s | worse |
| `lteNRRCC` | 0.1142s | 0.1013s | +0.0129s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.82 MB | 88.5% | 111.1% |
| `f1ap_rel18.6_specs` | 34.55 MB | 164.17 MB | 110.3% | 103.6% |
| `ngap_rel18.6_specs` | 24.38 MB | 117.29 MB | 108.0% | 107.3% |
| `lteNRRCC` | 74.83 MB | 102.17 MB | 103.4% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0252s | 0.0246s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0632s | 0.0631s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0473s | 0.0659s | -0.0186s | improved |
| `lteNRRCC` | 0.0742s | 0.1107s | -0.0365s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.70 MB | 7.61 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.62 MB | 4.19 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.64 MB | 9.97 MB | 0.9% | 0.0% |
| `lteNRRCC` | 3.95 MB | 3.80 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0448s | 0.0327s | +0.0121s | worse |
| `f1ap_rel18.6_specs` | 0.1213s | 0.0915s | +0.0298s | worse |
| `ngap_rel18.6_specs` | 0.0858s | 0.0632s | +0.0226s | worse |
| `lteNRRCC` | 0.1353s | 0.1137s | +0.0216s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.04 MB | 7.80 MB | 77.1% | 152.8% |
| `f1ap_rel18.6_specs` | 8.54 MB | 8.73 MB | 156.9% | 102.5% |
| `ngap_rel18.6_specs` | 7.98 MB | 8.17 MB | 77.7% | 157.7% |
| `lteNRRCC` | 8.16 MB | 69.98 MB | 148.8% | 101.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0339s | +0.0062s | worse |
| `f1ap_rel18.6_specs` | 0.1137s | 0.0971s | +0.0166s | worse |
| `ngap_rel18.6_specs` | 0.0817s | 0.0695s | +0.0122s | worse |
| `lteNRRCC` | 0.1296s | 0.1109s | +0.0187s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.89 MB | 8.85 MB | 108.8% | 153.6% |
| `f1ap_rel18.6_specs` | 11.26 MB | 164.19 MB | 113.8% | 159.2% |
| `ngap_rel18.6_specs` | 10.75 MB | 10.43 MB | 230.4% | 229.5% |
| `lteNRRCC` | 70.11 MB | 84.54 MB | 157.7% | 159.3% |
<!-- BENCH_RESULTS_END -->
