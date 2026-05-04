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
Generated: 2026-05-04T23:01:21.519944+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0357s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1149s | 0.1117s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0785s | 0.0750s | +0.0035s | worse |
| `lteNRRCC` | 0.1257s | 0.1193s | +0.0064s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.92 MB | 53.55 MB | 11.6% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 107.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0282s | +0.0067s | worse |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0751s | +0.0187s | worse |
| `ngap_rel18.6_specs` | 0.0659s | 0.0521s | +0.0138s | worse |
| `lteNRRCC` | 0.1297s | 0.0991s | +0.0306s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.40 MB | 100.0% | 110.7% |
| `f1ap_rel18.6_specs` | 22.20 MB | 103.03 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 16.65 MB | 73.99 MB | 111.1% | 109.3% |
| `lteNRRCC` | 48.79 MB | 65.80 MB | 103.1% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0330s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0902s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0652s | 0.0624s | +0.0028s | worse |
| `lteNRRCC` | 0.1280s | 0.1184s | +0.0096s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.59 MB | 20.5% | 110.0% |
| `f1ap_rel18.6_specs` | 35.27 MB | 164.75 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 23.82 MB | 117.47 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.96 MB | 102.34 MB | 104.7% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0222s | 0.0223s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0694s | 0.0701s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0463s | 0.0530s | -0.0067s | improved |
| `lteNRRCC` | 0.0765s | 0.1043s | -0.0278s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.94 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.19 MB | 4.64 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.64 MB | 4.08 MB | 0.0% | 0.4% |
| `lteNRRCC` | 3.77 MB | 6.98 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0416s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1088s | 0.1094s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0788s | -0.0010s | improved |
| `lteNRRCC` | 0.1267s | 0.1394s | -0.0127s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.97 MB | 8.11 MB | 161.8% | 116.6% |
| `f1ap_rel18.6_specs` | 8.80 MB | 8.67 MB | 119.0% | 118.2% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.30 MB | 81.9% | 117.2% |
| `lteNRRCC` | 8.48 MB | 68.80 MB | 161.1% | 105.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0432s | -0.0083s | improved |
| `f1ap_rel18.6_specs` | 0.0997s | 0.1214s | -0.0217s | improved |
| `ngap_rel18.6_specs` | 0.0696s | 0.0841s | -0.0145s | improved |
| `lteNRRCC` | 0.1129s | 0.1413s | -0.0284s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.91 MB | 9.53 MB | 119.8% | 100.4% |
| `f1ap_rel18.6_specs` | 10.52 MB | 164.18 MB | 120.9% | 106.7% |
| `ngap_rel18.6_specs` | 9.22 MB | 9.42 MB | 103.3% | 103.9% |
| `lteNRRCC` | 68.38 MB | 92.78 MB | 141.2% | 113.7% |
<!-- BENCH_RESULTS_END -->
