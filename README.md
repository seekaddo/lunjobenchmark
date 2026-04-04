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
Generated: 2026-04-04T22:38:32.529942+00:00

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0363s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0925s | 0.0934s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0657s | -0.0003s | improved |
| `lteNRRCC` | 0.1283s | 0.1279s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 36.41 MB | 96.0% | 110.7% |
| `f1ap_rel18.6_specs` | 22.29 MB | 102.90 MB | 109.4% | 103.5% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.57 MB | 111.5% | 106.8% |
| `lteNRRCC` | 48.30 MB | 66.39 MB | 104.5% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0345s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.0884s | 0.0891s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0622s | 0.0621s | +0.0001s | worse |
| `lteNRRCC` | 0.1158s | 0.1150s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.39 MB | 55.60 MB | 100.0% | 110.7% |
| `f1ap_rel18.6_specs` | 35.18 MB | 164.75 MB | 113.8% | 105.5% |
| `ngap_rel18.6_specs` | 24.12 MB | 117.51 MB | 112.5% | 104.8% |
| `lteNRRCC` | 74.52 MB | 102.46 MB | 107.0% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0220s | 0.0205s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0725s | 0.0587s | +0.0138s | worse |
| `ngap_rel18.6_specs` | 0.0465s | 0.0403s | +0.0062s | worse |
| `lteNRRCC` | 0.0683s | 0.0676s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.53 MB | 4.28 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.98 MB | 3.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.78 MB | 5.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.22 MB | 5.23 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0417s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1099s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0772s | -0.0010s | improved |
| `lteNRRCC` | 0.1377s | 0.1302s | +0.0075s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.81 MB | 165.0% | 115.6% |
| `f1ap_rel18.6_specs` | 7.96 MB | 106.63 MB | 155.8% | 165.5% |
| `ngap_rel18.6_specs` | 7.47 MB | 8.04 MB | 96.4% | 108.0% |
| `lteNRRCC` | 51.78 MB | 54.62 MB | 226.6% | 116.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0422s | 0.0394s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1174s | 0.1065s | +0.0109s | worse |
| `ngap_rel18.6_specs` | 0.0819s | 0.0741s | +0.0078s | worse |
| `lteNRRCC` | 0.1288s | 0.1278s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.83 MB | 10.08 MB | 118.2% | 118.6% |
| `f1ap_rel18.6_specs` | 10.23 MB | 10.36 MB | 120.0% | 163.2% |
| `ngap_rel18.6_specs` | 9.40 MB | 10.24 MB | 167.6% | 239.3% |
| `lteNRRCC` | 9.11 MB | 98.81 MB | 121.4% | 118.6% |
<!-- BENCH_RESULTS_END -->
