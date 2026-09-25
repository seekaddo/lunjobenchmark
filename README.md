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
Generated: 2026-09-25T15:06:16.942992+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0342s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.1169s | 0.1079s | +0.0090s | worse |
| `ngap_rel18.6_specs` | 0.0791s | 0.0734s | +0.0057s | worse |
| `lteNRRCC` | 0.1231s | 0.1174s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 80.0% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0353s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0955s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0651s | 0.0663s | -0.0012s | improved |
| `lteNRRCC` | 0.1234s | 0.1293s | -0.0059s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.42 MB | 36.69 MB | 84.0% | 103.7% |
| `f1ap_rel18.6_specs` | 22.39 MB | 103.40 MB | 106.5% | 103.6% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.48 MB | 104.0% | 102.3% |
| `lteNRRCC` | 48.75 MB | 66.32 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0233s | 0.0280s | -0.0047s | improved |
| `f1ap_rel18.6_specs` | 0.0617s | 0.0767s | -0.0150s | improved |
| `ngap_rel18.6_specs` | 0.0424s | 0.0526s | -0.0102s | improved |
| `lteNRRCC` | 0.0773s | 0.1040s | -0.0267s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.55 MB | 55.54 MB | 66.7% | 105.6% |
| `f1ap_rel18.6_specs` | 34.61 MB | 164.16 MB | 105.6% | 104.8% |
| `ngap_rel18.6_specs` | 23.80 MB | 117.84 MB | 106.7% | 103.6% |
| `lteNRRCC` | 74.45 MB | 102.95 MB | 102.7% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0252s | 0.0366s | -0.0114s | improved |
| `f1ap_rel18.6_specs` | 0.0960s | 0.0856s | +0.0104s | worse |
| `ngap_rel18.6_specs` | 0.0709s | 0.0654s | +0.0055s | worse |
| `lteNRRCC` | 0.1018s | 0.1034s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 3.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.03 MB | 7.89 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.95 MB | 5.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.88 MB | 5.34 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0412s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1183s | 0.1127s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0776s | +0.0010s | worse |
| `lteNRRCC` | 0.1435s | 0.1395s | +0.0040s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.40 MB | 7.86 MB | 203.3% | 97.1% |
| `f1ap_rel18.6_specs` | 8.89 MB | 106.59 MB | 104.8% | 163.0% |
| `ngap_rel18.6_specs` | 8.20 MB | 8.20 MB | 158.8% | 82.7% |
| `lteNRRCC` | 51.80 MB | 55.91 MB | 162.2% | 105.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0296s | 0.0342s | -0.0046s | improved |
| `f1ap_rel18.6_specs` | 0.0810s | 0.1008s | -0.0198s | improved |
| `ngap_rel18.6_specs` | 0.0563s | 0.0719s | -0.0156s | improved |
| `lteNRRCC` | 0.0879s | 0.1119s | -0.0240s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.01 MB | 23.97 MB | 124.5% | 186.9% |
| `f1ap_rel18.6_specs` | 30.21 MB | 21.11 MB | 125.8% | 91.0% |
| `ngap_rel18.6_specs` | 17.98 MB | 82.49 MB | 100.4% | 111.4% |
| `lteNRRCC` | 10.53 MB | 18.53 MB | 134.4% | 93.4% |
<!-- BENCH_RESULTS_END -->
