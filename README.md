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
Generated: 2026-05-23T11:19:40.673888+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0374s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1114s | 0.1144s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0772s | 0.0779s | -0.0007s | improved |
| `lteNRRCC` | 0.1213s | 0.1233s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.84 MB | 53.55 MB | 17.2% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0353s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0934s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0660s | +0.0001s | worse |
| `lteNRRCC` | 0.1349s | 0.1260s | +0.0089s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.45 MB | 71.9% | 107.1% |
| `f1ap_rel18.6_specs` | 22.34 MB | 103.29 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.51 MB | 111.1% | 104.5% |
| `lteNRRCC` | 48.78 MB | 66.01 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0351s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.0901s | 0.0949s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0627s | 0.0657s | -0.0030s | improved |
| `lteNRRCC` | 0.1163s | 0.1281s | -0.0118s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.33 MB | 55.83 MB | 18.7% | 111.1% |
| `f1ap_rel18.6_specs` | 34.05 MB | 164.76 MB | 106.7% | 105.4% |
| `ngap_rel18.6_specs` | 24.19 MB | 117.80 MB | 112.5% | 107.1% |
| `lteNRRCC` | 74.44 MB | 101.81 MB | 105.2% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0310s | 0.0417s | -0.0107s | improved |
| `f1ap_rel18.6_specs` | 0.0734s | 0.0698s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0415s | 0.0508s | -0.0093s | improved |
| `lteNRRCC` | 0.0717s | 0.0735s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.16 MB | 4.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.05 MB | 4.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.17 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.81 MB | 3.31 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0418s | 0.0391s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1158s | 0.1057s | +0.0101s | worse |
| `ngap_rel18.6_specs` | 0.0806s | 0.0740s | +0.0066s | worse |
| `lteNRRCC` | 0.1417s | 0.1382s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.57 MB | 7.89 MB | 159.3% | 80.0% |
| `f1ap_rel18.6_specs` | 8.91 MB | 106.66 MB | 154.6% | 155.0% |
| `ngap_rel18.6_specs` | 8.31 MB | 8.38 MB | 78.0% | 165.9% |
| `lteNRRCC` | 8.67 MB | 70.56 MB | 92.8% | 155.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0415s | 0.0431s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1210s | 0.1197s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0857s | 0.0839s | +0.0018s | worse |
| `lteNRRCC` | 0.1412s | 0.1381s | +0.0031s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.67 MB | 10.30 MB | 159.6% | 101.8% |
| `f1ap_rel18.6_specs` | 10.36 MB | 10.30 MB | 162.2% | 163.7% |
| `ngap_rel18.6_specs` | 10.44 MB | 9.55 MB | 100.7% | 161.9% |
| `lteNRRCC` | 9.48 MB | 75.89 MB | 140.4% | 154.8% |
<!-- BENCH_RESULTS_END -->
