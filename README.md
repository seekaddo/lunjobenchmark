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
Generated: 2026-06-17T13:47:22.043429+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0350s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1163s | 0.1085s | +0.0078s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0750s | +0.0027s | worse |
| `lteNRRCC` | 0.1229s | 0.1177s | +0.0052s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 7.7% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 108.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0335s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.0921s | 0.0929s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0659s | 0.0649s | +0.0010s | worse |
| `lteNRRCC` | 0.1258s | 0.1236s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.27 MB | 36.60 MB | 24.8% | 114.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.74 MB | 106.2% | 105.2% |
| `ngap_rel18.6_specs` | 17.65 MB | 74.60 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.48 MB | 66.38 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0331s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0881s | +0.0055s | worse |
| `ngap_rel18.6_specs` | 0.0641s | 0.0618s | +0.0023s | worse |
| `lteNRRCC` | 0.1183s | 0.1148s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.75 MB | 88.0% | 111.1% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.74 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.35 MB | 117.48 MB | 108.0% | 107.0% |
| `lteNRRCC` | 75.03 MB | 102.96 MB | 103.4% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0413s | 0.0228s | +0.0185s | worse |
| `f1ap_rel18.6_specs` | 0.0824s | 0.0674s | +0.0150s | worse |
| `ngap_rel18.6_specs` | 0.0791s | 0.0473s | +0.0318s | worse |
| `lteNRRCC` | 0.0945s | 0.0768s | +0.0177s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.02 MB | 4.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 1.92 MB | 2.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.06 MB | 7.00 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.66 MB | 7.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0426s | 0.0409s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1185s | 0.1192s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0827s | 0.0824s | +0.0003s | worse |
| `lteNRRCC` | 0.1428s | 0.1437s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.05 MB | 8.11 MB | 78.6% | 96.3% |
| `f1ap_rel18.6_specs` | 8.67 MB | 9.05 MB | 94.1% | 103.2% |
| `ngap_rel18.6_specs` | 8.30 MB | 8.36 MB | 162.4% | 157.8% |
| `lteNRRCC` | 51.55 MB | 51.99 MB | 156.6% | 152.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0298s | +0.0116s | worse |
| `f1ap_rel18.6_specs` | 0.1209s | 0.0841s | +0.0368s | worse |
| `ngap_rel18.6_specs` | 0.0847s | 0.0595s | +0.0252s | worse |
| `lteNRRCC` | 0.1388s | 0.0894s | +0.0494s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.46 MB | 9.71 MB | 106.8% | 96.5% |
| `f1ap_rel18.6_specs` | 9.80 MB | 164.19 MB | 83.2% | 163.8% |
| `ngap_rel18.6_specs` | 10.05 MB | 9.41 MB | 160.0% | 160.8% |
| `lteNRRCC` | 8.96 MB | 99.63 MB | 161.5% | 157.3% |
<!-- BENCH_RESULTS_END -->
