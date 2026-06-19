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
Generated: 2026-06-19T13:39:19.638100+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0350s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1094s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0756s | +0.0019s | worse |
| `lteNRRCC` | 0.1207s | 0.1193s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 13.1% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.2% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0203s | 0.0356s | -0.0153s | improved |
| `f1ap_rel18.6_specs` | 0.0558s | 0.0948s | -0.0390s | improved |
| `ngap_rel18.6_specs` | 0.0392s | 0.0669s | -0.0277s | improved |
| `lteNRRCC` | 0.0705s | 0.1257s | -0.0552s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.31 MB | 36.10 MB | 88.9% | 105.6% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.40 MB | 110.5% | 102.9% |
| `ngap_rel18.6_specs` | 19.28 MB | 74.44 MB | 106.2% | 107.7% |
| `lteNRRCC` | 48.52 MB | 66.25 MB | 102.8% | 104.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0359s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0900s | 0.0953s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0668s | -0.0029s | improved |
| `lteNRRCC` | 0.1187s | 0.1290s | -0.0103s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.89 MB | 17.3% | 111.1% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.47 MB | 110.7% | 103.6% |
| `ngap_rel18.6_specs` | 24.39 MB | 117.70 MB | 108.3% | 104.9% |
| `lteNRRCC` | 74.90 MB | 102.47 MB | 103.4% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0244s | 0.0226s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.0712s | 0.0684s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0490s | 0.0479s | +0.0011s | worse |
| `lteNRRCC` | 0.0794s | 0.0782s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.62 MB | 4.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.14 MB | 6.80 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.75 MB | 4.81 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.42 MB | 4.28 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0405s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1093s | 0.1105s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0804s | 0.0800s | +0.0004s | worse |
| `lteNRRCC` | 0.1396s | 0.1492s | -0.0096s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.45 MB | 7.37 MB | 160.5% | 159.3% |
| `f1ap_rel18.6_specs` | 8.12 MB | 8.75 MB | 161.1% | 230.7% |
| `ngap_rel18.6_specs` | 8.25 MB | 7.65 MB | 224.0% | 79.5% |
| `lteNRRCC` | 48.23 MB | 69.24 MB | 158.3% | 105.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0599s | 0.0394s | +0.0205s | worse |
| `f1ap_rel18.6_specs` | 0.1367s | 0.1132s | +0.0235s | worse |
| `ngap_rel18.6_specs` | 0.0952s | 0.0779s | +0.0173s | worse |
| `lteNRRCC` | 0.1340s | 0.1298s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.78 MB | 10.52 MB | 0.0% | 153.7% |
| `f1ap_rel18.6_specs` | 11.20 MB | 136.03 MB | 99.1% | 108.8% |
| `ngap_rel18.6_specs` | 10.37 MB | 10.50 MB | 160.6% | 218.5% |
| `lteNRRCC` | 73.02 MB | 74.14 MB | 127.8% | 203.2% |
<!-- BENCH_RESULTS_END -->
