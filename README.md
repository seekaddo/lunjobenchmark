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
Generated: 2026-07-04T23:03:51.553996+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0354s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1068s | 0.1096s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0740s | 0.0758s | -0.0018s | improved |
| `lteNRRCC` | 0.1179s | 0.1196s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 18.4% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0342s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0992s | 0.0970s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0692s | 0.0661s | +0.0031s | worse |
| `lteNRRCC` | 0.1319s | 0.1305s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.65 MB | 85.2% | 114.3% |
| `f1ap_rel18.6_specs` | 22.40 MB | 102.69 MB | 108.8% | 105.0% |
| `ngap_rel18.6_specs` | 17.57 MB | 74.65 MB | 110.7% | 108.9% |
| `lteNRRCC` | 48.70 MB | 66.15 MB | 102.9% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0362s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0900s | 0.0901s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0614s | 0.0629s | -0.0015s | improved |
| `lteNRRCC` | 0.1143s | 0.1216s | -0.0073s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 54.91 MB | 87.5% | 111.5% |
| `f1ap_rel18.6_specs` | 34.75 MB | 164.52 MB | 106.9% | 105.6% |
| `ngap_rel18.6_specs` | 23.79 MB | 117.89 MB | 112.5% | 104.9% |
| `lteNRRCC` | 74.57 MB | 102.70 MB | 103.4% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0221s | 0.0228s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0674s | 0.0705s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0457s | 0.0603s | -0.0146s | improved |
| `lteNRRCC` | 0.0787s | 0.1022s | -0.0235s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.22 MB | 4.48 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.97 MB | 4.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.09 MB | 4.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.84 MB | 4.20 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0420s | 0.0416s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1188s | 0.1128s | +0.0060s | worse |
| `ngap_rel18.6_specs` | 0.0827s | 0.0794s | +0.0033s | worse |
| `lteNRRCC` | 0.1443s | 0.1301s | +0.0142s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.05 MB | 8.03 MB | 95.6% | 77.8% |
| `f1ap_rel18.6_specs` | 8.73 MB | 104.99 MB | 193.8% | 154.5% |
| `ngap_rel18.6_specs` | 8.30 MB | 8.42 MB | 155.5% | 155.8% |
| `lteNRRCC` | 50.73 MB | 57.42 MB | 111.9% | 108.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0448s | 0.0484s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.1317s | 0.1303s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0922s | 0.0924s | -0.0002s | improved |
| `lteNRRCC` | 0.1425s | 0.1348s | +0.0077s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.53 MB | 10.30 MB | 211.9% | 85.0% |
| `f1ap_rel18.6_specs` | 10.07 MB | 139.55 MB | 159.9% | 215.4% |
| `ngap_rel18.6_specs` | 10.09 MB | 9.41 MB | 110.2% | 160.1% |
| `lteNRRCC` | 69.30 MB | 79.90 MB | 158.8% | 109.7% |
<!-- BENCH_RESULTS_END -->
