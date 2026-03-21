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
Generated: 2026-03-21T22:33:29.871160+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0404s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.1137s | 0.1214s | -0.0077s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0832s | -0.0056s | improved |
| `lteNRRCC` | 0.1220s | 0.1273s | -0.0053s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 100.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0361s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0955s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0668s | 0.0674s | -0.0006s | improved |
| `lteNRRCC` | 0.1295s | 0.1302s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 36.66 MB | 92.3% | 110.3% |
| `f1ap_rel18.6_specs` | 21.85 MB | 103.25 MB | 108.8% | 105.1% |
| `ngap_rel18.6_specs` | 16.81 MB | 74.51 MB | 110.7% | 106.7% |
| `lteNRRCC` | 48.50 MB | 66.46 MB | 106.1% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0378s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0917s | 0.0947s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0666s | -0.0026s | improved |
| `lteNRRCC` | 0.1190s | 0.1203s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.44 MB | 55.44 MB | 71.4% | 113.3% |
| `f1ap_rel18.6_specs` | 34.52 MB | 164.59 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 24.33 MB | 116.98 MB | 111.5% | 106.8% |
| `lteNRRCC` | 74.73 MB | 102.84 MB | 105.0% | 105.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0206s | 0.0393s | -0.0187s | improved |
| `f1ap_rel18.6_specs` | 0.0658s | 0.0992s | -0.0334s | improved |
| `ngap_rel18.6_specs` | 0.0407s | 0.0605s | -0.0198s | improved |
| `lteNRRCC` | 0.0682s | 0.0953s | -0.0271s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.42 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.94 MB | 4.02 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.84 MB | 3.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.12 MB | 3.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0381s | 0.0384s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1043s | 0.1129s | -0.0086s | improved |
| `ngap_rel18.6_specs` | 0.0725s | 0.0736s | -0.0011s | improved |
| `lteNRRCC` | 0.1389s | 0.1375s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.57 MB | 7.31 MB | 162.6% | 165.6% |
| `f1ap_rel18.6_specs` | 8.55 MB | 106.65 MB | 228.6% | 105.8% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.55 MB | 81.8% | 165.2% |
| `lteNRRCC` | 50.73 MB | 51.09 MB | 117.5% | 105.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0393s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1080s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0742s | 0.0746s | -0.0004s | improved |
| `lteNRRCC` | 0.1243s | 0.1259s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.79 MB | 10.91 MB | 161.7% | 226.2% |
| `f1ap_rel18.6_specs` | 9.72 MB | 10.06 MB | 158.9% | 158.9% |
| `ngap_rel18.6_specs` | 9.02 MB | 10.11 MB | 157.5% | 100.1% |
| `lteNRRCC` | 9.16 MB | 90.20 MB | 111.4% | 105.8% |
<!-- BENCH_RESULTS_END -->
