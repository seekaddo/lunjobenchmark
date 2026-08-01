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
Generated: 2026-08-01T11:22:51.195383+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0366s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1126s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0772s | 0.0778s | -0.0006s | improved |
| `lteNRRCC` | 0.1197s | 0.1217s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 18.6% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.7% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0259s | +0.0092s | worse |
| `f1ap_rel18.6_specs` | 0.0962s | 0.0729s | +0.0233s | worse |
| `ngap_rel18.6_specs` | 0.0668s | 0.0557s | +0.0111s | worse |
| `lteNRRCC` | 0.1300s | 0.0971s | +0.0329s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.34 MB | 36.57 MB | 19.6% | 107.4% |
| `f1ap_rel18.6_specs` | 21.84 MB | 103.35 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.58 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.07 MB | 66.52 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0366s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.0916s | 0.0942s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0632s | 0.0656s | -0.0024s | improved |
| `lteNRRCC` | 0.1173s | 0.1284s | -0.0111s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 55.50 MB | 71.4% | 103.7% |
| `f1ap_rel18.6_specs` | 34.17 MB | 164.33 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.45 MB | 117.62 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.87 MB | 102.59 MB | 101.8% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0190s | 0.0327s | -0.0137s | improved |
| `f1ap_rel18.6_specs` | 0.0669s | 0.0785s | -0.0116s | improved |
| `ngap_rel18.6_specs` | 0.0415s | 0.0565s | -0.0150s | improved |
| `lteNRRCC` | 0.0717s | 0.1010s | -0.0293s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.28 MB | 3.41 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.80 MB | 3.92 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.83 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.97 MB | 3.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0405s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1098s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0798s | 0.0786s | +0.0012s | worse |
| `lteNRRCC` | 0.1555s | 0.1405s | +0.0150s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.43 MB | 7.86 MB | 0.0% | 111.0% |
| `f1ap_rel18.6_specs` | 8.05 MB | 8.62 MB | 90.0% | 106.5% |
| `ngap_rel18.6_specs` | 7.90 MB | 7.56 MB | 80.3% | 162.0% |
| `lteNRRCC` | 51.85 MB | 62.93 MB | 105.2% | 161.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0391s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1181s | 0.1153s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0805s | 0.0778s | +0.0027s | worse |
| `lteNRRCC` | 0.1318s | 0.1300s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 8.73 MB | 0.0% | 77.6% |
| `f1ap_rel18.6_specs` | 10.04 MB | 155.17 MB | 78.2% | 152.2% |
| `ngap_rel18.6_specs` | 9.13 MB | 10.26 MB | 153.9% | 99.5% |
| `lteNRRCC` | 73.67 MB | 81.34 MB | 151.3% | 110.6% |
<!-- BENCH_RESULTS_END -->
