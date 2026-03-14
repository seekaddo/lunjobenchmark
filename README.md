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
Generated: 2026-03-14T06:25:00.863881+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0373s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1217s | 0.1168s | +0.0049s | worse |
| `ngap_rel18.6_specs` | 0.0863s | 0.0819s | +0.0044s | worse |
| `lteNRRCC` | 0.1256s | 0.1234s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.41 MB | 55.79 MB | 105.6% | 106.9% |
| `f1ap_rel18.6_specs` | 32.29 MB | 176.91 MB | 103.3% | 102.8% |
| `ngap_rel18.6_specs` | 22.29 MB | 125.79 MB | 108.3% | 105.8% |
| `lteNRRCC` | 72.35 MB | 100.05 MB | 103.3% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0366s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1022s | 0.0984s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0736s | 0.0697s | +0.0039s | worse |
| `lteNRRCC` | 0.1366s | 0.1330s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.64 MB | 36.47 MB | 96.3% | 109.7% |
| `f1ap_rel18.6_specs` | 21.79 MB | 111.37 MB | 111.1% | 104.7% |
| `ngap_rel18.6_specs` | 16.77 MB | 80.01 MB | 110.0% | 106.1% |
| `lteNRRCC` | 48.29 MB | 66.42 MB | 105.8% | 105.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0353s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0928s | 0.0924s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0655s | +0.0003s | worse |
| `lteNRRCC` | 0.1175s | 0.1174s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.75 MB | 57.93 MB | 83.3% | 110.3% |
| `f1ap_rel18.6_specs` | 35.12 MB | 179.37 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 23.87 MB | 127.89 MB | 114.8% | 106.7% |
| `lteNRRCC` | 74.93 MB | 102.05 MB | 105.0% | 105.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0201s | 0.0235s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.0652s | 0.0692s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0429s | 0.0492s | -0.0063s | improved |
| `lteNRRCC` | 0.0690s | 0.0774s | -0.0084s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.30 MB | 4.05 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 4.17 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.83 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.09 MB | 4.45 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0431s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1131s | 0.1177s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.0792s | 0.0848s | -0.0056s | improved |
| `lteNRRCC` | 0.1405s | 0.1301s | +0.0104s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.70 MB | 7.31 MB | 114.2% | 91.7% |
| `f1ap_rel18.6_specs` | 8.12 MB | 115.13 MB | 115.9% | 173.9% |
| `ngap_rel18.6_specs` | 7.39 MB | 7.35 MB | 159.1% | 169.2% |
| `lteNRRCC` | 48.07 MB | 50.40 MB | 162.6% | 157.9% |
<!-- BENCH_RESULTS_END -->
