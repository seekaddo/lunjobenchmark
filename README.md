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
Generated: 2026-06-08T23:17:12.863998+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0337s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1078s | -0.0003s | improved |
| `ngap_rel18.6_specs` | 0.0734s | 0.0721s | +0.0013s | worse |
| `lteNRRCC` | 0.1186s | 0.1174s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 22.6% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0354s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0949s | 0.0937s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0672s | 0.0664s | +0.0008s | worse |
| `lteNRRCC` | 0.1295s | 0.1293s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.67 MB | 85.7% | 106.9% |
| `f1ap_rel18.6_specs` | 21.89 MB | 103.41 MB | 109.1% | 106.9% |
| `ngap_rel18.6_specs` | 17.70 MB | 73.71 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.41 MB | 66.29 MB | 104.5% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0336s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.0928s | 0.0912s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0657s | 0.0634s | +0.0023s | worse |
| `lteNRRCC` | 0.1278s | 0.1185s | +0.0093s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.30 MB | 28.1% | 106.7% |
| `f1ap_rel18.6_specs` | 35.19 MB | 163.52 MB | 109.4% | 103.4% |
| `ngap_rel18.6_specs` | 24.50 MB | 116.93 MB | 110.7% | 106.7% |
| `lteNRRCC` | 73.90 MB | 102.50 MB | 104.7% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0319s | 0.0246s | +0.0073s | worse |
| `f1ap_rel18.6_specs` | 0.0830s | 0.0915s | -0.0085s | improved |
| `ngap_rel18.6_specs` | 0.0641s | 0.0650s | -0.0009s | improved |
| `lteNRRCC` | 0.1061s | 0.1135s | -0.0074s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.72 MB | 4.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.03 MB | 8.08 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.84 MB | 1.66 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.69 MB | 1.50 MB | 0.0% | 0.9% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0444s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.1074s | 0.1118s | -0.0044s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0796s | -0.0041s | improved |
| `lteNRRCC` | 0.1377s | 0.1395s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.91 MB | 7.36 MB | 226.9% | 172.7% |
| `f1ap_rel18.6_specs` | 8.68 MB | 8.49 MB | 204.1% | 230.4% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.55 MB | 168.7% | 162.8% |
| `lteNRRCC` | 50.96 MB | 48.80 MB | 163.9% | 97.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0388s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1180s | 0.1107s | +0.0073s | worse |
| `ngap_rel18.6_specs` | 0.0837s | 0.0804s | +0.0033s | worse |
| `lteNRRCC` | 0.1362s | 0.1272s | +0.0090s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.00 MB | 9.01 MB | 83.2% | 166.1% |
| `f1ap_rel18.6_specs` | 10.08 MB | 164.16 MB | 164.7% | 110.1% |
| `ngap_rel18.6_specs` | 9.27 MB | 9.20 MB | 163.9% | 82.4% |
| `lteNRRCC` | 73.52 MB | 87.32 MB | 162.7% | 99.6% |
<!-- BENCH_RESULTS_END -->
