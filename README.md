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
Generated: 2026-06-22T23:25:55.002959+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0343s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1123s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0768s | -0.0017s | improved |
| `lteNRRCC` | 0.1190s | 0.1190s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 23.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0357s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0950s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0684s | -0.0023s | improved |
| `lteNRRCC` | 0.1239s | 0.1264s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.65 MB | 88.5% | 110.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.32 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.71 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.32 MB | 66.54 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0343s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.0944s | 0.0936s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0670s | 0.0656s | +0.0014s | worse |
| `lteNRRCC` | 0.1280s | 0.1222s | +0.0058s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.44 MB | 55.23 MB | 92.3% | 113.8% |
| `f1ap_rel18.6_specs` | 33.95 MB | 164.20 MB | 109.4% | 106.9% |
| `ngap_rel18.6_specs` | 24.60 MB | 117.83 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.83 MB | 102.86 MB | 104.8% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0188s | +0.0202s | worse |
| `f1ap_rel18.6_specs` | 0.1262s | 0.0662s | +0.0600s | worse |
| `ngap_rel18.6_specs` | 0.0847s | 0.0402s | +0.0445s | worse |
| `lteNRRCC` | 0.1282s | 0.0737s | +0.0545s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.06 MB | 10.03 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.92 MB | 9.80 MB | 0.0% | 3.3% |
| `ngap_rel18.6_specs` | 6.16 MB | 5.59 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.70 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0364s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.1133s | 0.0998s | +0.0135s | worse |
| `ngap_rel18.6_specs` | 0.0798s | 0.0699s | +0.0099s | worse |
| `lteNRRCC` | 0.1321s | 0.1283s | +0.0038s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.40 MB | 7.81 MB | 103.5% | 81.2% |
| `f1ap_rel18.6_specs` | 8.61 MB | 8.38 MB | 167.9% | 168.8% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.26 MB | 117.5% | 116.2% |
| `lteNRRCC` | 8.34 MB | 69.10 MB | 161.5% | 107.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0429s | -0.0051s | improved |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1220s | -0.0094s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0856s | -0.0080s | improved |
| `lteNRRCC` | 0.1295s | 0.1403s | -0.0108s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.57 MB | 8.51 MB | 80.9% | 163.0% |
| `f1ap_rel18.6_specs` | 9.48 MB | 163.38 MB | 161.3% | 163.4% |
| `ngap_rel18.6_specs` | 8.77 MB | 9.02 MB | 81.3% | 161.7% |
| `lteNRRCC` | 8.43 MB | 84.47 MB | 78.5% | 160.1% |
<!-- BENCH_RESULTS_END -->
