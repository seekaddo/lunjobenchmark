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
Generated: 2026-03-14T06:35:51.949742+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0383s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1287s | 0.1217s | +0.0070s | worse |
| `ngap_rel18.6_specs` | 0.0872s | 0.0863s | +0.0009s | worse |
| `lteNRRCC` | 0.1299s | 0.1256s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.41 MB | 55.79 MB | 105.3% | 106.7% |
| `f1ap_rel18.6_specs` | 32.29 MB | 176.91 MB | 110.0% | 104.1% |
| `ngap_rel18.6_specs` | 22.29 MB | 125.79 MB | 112.0% | 105.4% |
| `lteNRRCC` | 72.35 MB | 99.96 MB | 103.2% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0381s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.1018s | 0.1022s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0707s | 0.0736s | -0.0029s | improved |
| `lteNRRCC` | 0.1223s | 0.1366s | -0.0143s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.80 MB | 37.14 MB | 87.0% | 107.4% |
| `f1ap_rel18.6_specs` | 22.34 MB | 111.89 MB | 106.7% | 103.3% |
| `ngap_rel18.6_specs` | 16.77 MB | 80.05 MB | 112.5% | 104.4% |
| `lteNRRCC` | 48.69 MB | 65.43 MB | 105.1% | 104.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0347s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0958s | 0.0928s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0688s | 0.0658s | +0.0030s | worse |
| `lteNRRCC` | 0.1193s | 0.1175s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.75 MB | 57.71 MB | 33.8% | 113.3% |
| `f1ap_rel18.6_specs` | 33.90 MB | 179.04 MB | 109.4% | 105.0% |
| `ngap_rel18.6_specs` | 24.41 MB | 128.04 MB | 114.8% | 106.4% |
| `lteNRRCC` | 74.93 MB | 102.70 MB | 104.9% | 104.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0199s | 0.0201s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0621s | 0.0652s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0444s | 0.0429s | +0.0015s | worse |
| `lteNRRCC` | 0.0686s | 0.0690s | -0.0004s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.80 MB | 3.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.05 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.00 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.12 MB | 3.75 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0408s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1131s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0766s | 0.0792s | -0.0026s | improved |
| `lteNRRCC` | 0.1400s | 0.1405s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.21 MB | 6.95 MB | 93.7% | 168.9% |
| `f1ap_rel18.6_specs` | 8.18 MB | 112.35 MB | 119.8% | 97.6% |
| `ngap_rel18.6_specs` | 7.87 MB | 7.34 MB | 120.7% | 166.2% |
| `lteNRRCC` | 47.43 MB | 48.20 MB | 164.6% | 239.5% |
<!-- BENCH_RESULTS_END -->
