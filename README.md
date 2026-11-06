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
Generated: 2026-11-06T17:18:05.351755+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0440s | 0.0419s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1326s | 0.1272s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0919s | 0.0880s | +0.0039s | worse |
| `lteNRRCC` | 0.1335s | 0.1320s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.75 MB | 53.55 MB | 88.0% | 106.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.4% | 103.4% |
| `lteNRRCC` | 72.40 MB | 100.18 MB | 104.8% | 102.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0454s | -0.0071s | improved |
| `f1ap_rel18.6_specs` | 0.1148s | 0.1393s | -0.0245s | improved |
| `ngap_rel18.6_specs` | 0.0792s | 0.0958s | -0.0166s | improved |
| `lteNRRCC` | 0.1225s | 0.1548s | -0.0323s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 34.65 MB | 81.8% | 103.6% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 107.1% | 101.5% |
| `ngap_rel18.6_specs` | 18.09 MB | 72.65 MB | 104.5% | 104.2% |
| `lteNRRCC` | 46.71 MB | 64.21 MB | 103.6% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0379s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1204s | 0.1217s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0849s | 0.0919s | -0.0070s | improved |
| `lteNRRCC` | 0.1136s | 0.1117s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 53.73 MB | 77.3% | 103.7% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 108.0% | 101.5% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 105.0% | 103.9% |
| `lteNRRCC` | 72.64 MB | 100.36 MB | 104.0% | 101.6% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0324s | 0.0407s | -0.0083s | improved |
| `f1ap_rel18.6_specs` | 0.0914s | 0.1098s | -0.0184s | improved |
| `ngap_rel18.6_specs` | 0.0644s | 0.0744s | -0.0100s | improved |
| `lteNRRCC` | 0.1121s | 0.1392s | -0.0271s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.86 MB | 0.0% | 142.3% |
| `f1ap_rel18.6_specs` | 8.81 MB | 8.56 MB | 133.4% | 142.0% |
| `ngap_rel18.6_specs` | 8.31 MB | 8.25 MB | 140.8% | 141.1% |
| `lteNRRCC` | 51.58 MB | 52.01 MB | 142.6% | 141.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0401s | -0.0039s | improved |
| `f1ap_rel18.6_specs` | 0.1011s | 0.1159s | -0.0148s | improved |
| `ngap_rel18.6_specs` | 0.0722s | 0.0805s | -0.0083s | improved |
| `lteNRRCC` | 0.1123s | 0.1161s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.29 MB | 0.0% | 271.4% |
| `f1ap_rel18.6_specs` | 10.31 MB | 11.28 MB | 203.4% | 134.8% |
| `ngap_rel18.6_specs` | 10.45 MB | 10.58 MB | 137.0% | 139.4% |
| `lteNRRCC` | 9.37 MB | 77.14 MB | 135.6% | 108.6% |
<!-- BENCH_RESULTS_END -->
