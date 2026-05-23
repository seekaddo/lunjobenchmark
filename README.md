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
Generated: 2026-05-23T22:58:18.581651+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0360s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1123s | 0.1114s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0772s | -0.0003s | improved |
| `lteNRRCC` | 0.1213s | 0.1213s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 31.9% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0360s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.0973s | 0.0930s | +0.0043s | worse |
| `ngap_rel18.6_specs` | 0.0648s | 0.0661s | -0.0013s | improved |
| `lteNRRCC` | 0.1163s | 0.1349s | -0.0186s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.27 MB | 36.35 MB | 70.4% | 107.7% |
| `f1ap_rel18.6_specs` | 21.84 MB | 103.39 MB | 110.7% | 103.6% |
| `ngap_rel18.6_specs` | 17.71 MB | 74.06 MB | 108.7% | 107.1% |
| `lteNRRCC` | 48.62 MB | 66.34 MB | 103.5% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0282s | 0.0332s | -0.0050s | improved |
| `f1ap_rel18.6_specs` | 0.0759s | 0.0901s | -0.0142s | improved |
| `ngap_rel18.6_specs` | 0.0522s | 0.0627s | -0.0105s | improved |
| `lteNRRCC` | 0.1047s | 0.1163s | -0.0116s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.40 MB | 55.89 MB | 67.7% | 108.3% |
| `f1ap_rel18.6_specs` | 35.14 MB | 164.39 MB | 108.0% | 104.2% |
| `ngap_rel18.6_specs` | 24.25 MB | 117.66 MB | 109.5% | 108.3% |
| `lteNRRCC` | 74.55 MB | 102.74 MB | 106.0% | 103.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0493s | 0.0310s | +0.0183s | worse |
| `f1ap_rel18.6_specs` | 0.0656s | 0.0734s | -0.0078s | improved |
| `ngap_rel18.6_specs` | 0.0525s | 0.0415s | +0.0110s | worse |
| `lteNRRCC` | 0.0968s | 0.0717s | +0.0251s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.72 MB | 4.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.02 MB | 4.92 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.42 MB | 5.55 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.42 MB | 7.56 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0418s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1175s | 0.1158s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0824s | 0.0806s | +0.0018s | worse |
| `lteNRRCC` | 0.1513s | 0.1417s | +0.0096s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.44 MB | 7.98 MB | 102.7% | 95.5% |
| `f1ap_rel18.6_specs` | 8.55 MB | 8.45 MB | 162.5% | 84.5% |
| `ngap_rel18.6_specs` | 7.99 MB | 8.25 MB | 83.4% | 157.0% |
| `lteNRRCC` | 49.52 MB | 52.27 MB | 149.8% | 163.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0415s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.1086s | 0.1210s | -0.0124s | improved |
| `ngap_rel18.6_specs` | 0.0691s | 0.0857s | -0.0166s | improved |
| `lteNRRCC` | 0.1108s | 0.1412s | -0.0304s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.39 MB | 10.08 MB | 0.0% | 144.6% |
| `f1ap_rel18.6_specs` | 10.57 MB | 164.12 MB | 141.9% | 111.1% |
| `ngap_rel18.6_specs` | 9.07 MB | 9.14 MB | 105.0% | 209.5% |
| `lteNRRCC` | 73.77 MB | 98.58 MB | 110.4% | 108.2% |
<!-- BENCH_RESULTS_END -->
