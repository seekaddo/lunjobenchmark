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
Generated: 2026-03-14T06:39:11.365236+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0405s | -0.0044s | improved |
| `f1ap_rel18.6_specs` | 0.1174s | 0.1287s | -0.0113s | improved |
| `ngap_rel18.6_specs` | 0.0815s | 0.0872s | -0.0057s | improved |
| `lteNRRCC` | 0.1223s | 0.1299s | -0.0076s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.41 MB | 55.79 MB | 105.9% | 107.1% |
| `f1ap_rel18.6_specs` | 32.29 MB | 176.91 MB | 107.1% | 101.5% |
| `ngap_rel18.6_specs` | 22.29 MB | 125.79 MB | 113.6% | 104.1% |
| `lteNRRCC` | 72.35 MB | 99.96 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0345s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0982s | 0.1018s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0686s | 0.0707s | -0.0021s | improved |
| `lteNRRCC` | 0.1292s | 0.1223s | +0.0069s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.46 MB | 37.40 MB | 32.5% | 109.7% |
| `f1ap_rel18.6_specs` | 22.42 MB | 111.39 MB | 111.4% | 106.5% |
| `ngap_rel18.6_specs` | 16.75 MB | 80.03 MB | 113.8% | 108.3% |
| `lteNRRCC` | 48.74 MB | 66.34 MB | 104.5% | 105.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0360s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0958s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0688s | -0.0034s | improved |
| `lteNRRCC` | 0.1167s | 0.1193s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.79 MB | 57.73 MB | 28.4% | 113.8% |
| `f1ap_rel18.6_specs` | 33.76 MB | 179.05 MB | 112.9% | 106.9% |
| `ngap_rel18.6_specs` | 24.31 MB | 127.27 MB | 111.1% | 106.7% |
| `lteNRRCC` | 74.55 MB | 102.83 MB | 103.3% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0292s | 0.0199s | +0.0093s | worse |
| `f1ap_rel18.6_specs` | 0.0693s | 0.0621s | +0.0072s | worse |
| `ngap_rel18.6_specs` | 0.0508s | 0.0444s | +0.0064s | worse |
| `lteNRRCC` | 0.0775s | 0.0686s | +0.0089s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.62 MB | 4.19 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.81 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 4.38 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.64 MB | 3.55 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0401s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1176s | 0.1097s | +0.0079s | worse |
| `ngap_rel18.6_specs` | 0.0806s | 0.0766s | +0.0040s | worse |
| `lteNRRCC` | 0.1484s | 0.1400s | +0.0084s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.22 MB | 7.09 MB | 162.1% | 161.7% |
| `f1ap_rel18.6_specs` | 7.93 MB | 7.92 MB | 165.1% | 162.9% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.38 MB | 164.2% | 163.0% |
| `lteNRRCC` | 46.23 MB | 67.95 MB | 109.8% | 106.5% |
<!-- BENCH_RESULTS_END -->
