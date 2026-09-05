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
Generated: 2026-09-05T23:43:09.791836+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0343s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1070s | +0.0046s | worse |
| `ngap_rel18.6_specs` | 0.0754s | 0.0739s | +0.0015s | worse |
| `lteNRRCC` | 0.1201s | 0.1174s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.73 MB | 53.55 MB | 15.2% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0347s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0937s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0682s | 0.0662s | +0.0020s | worse |
| `lteNRRCC` | 0.1301s | 0.1294s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.38 MB | 36.45 MB | 80.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.03 MB | 103.35 MB | 103.1% | 101.7% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.45 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.64 MB | 66.45 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0360s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0941s | 0.1020s | -0.0079s | improved |
| `ngap_rel18.6_specs` | 0.0689s | 0.0710s | -0.0021s | improved |
| `lteNRRCC` | 0.1286s | 0.1184s | +0.0102s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.46 MB | 55.89 MB | 91.7% | 103.6% |
| `f1ap_rel18.6_specs` | 35.15 MB | 164.72 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.62 MB | 104.0% | 102.3% |
| `lteNRRCC` | 74.75 MB | 102.52 MB | 103.2% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0314s | 0.0327s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0690s | 0.1034s | -0.0344s | improved |
| `ngap_rel18.6_specs` | 0.0507s | 0.0476s | +0.0031s | worse |
| `lteNRRCC` | 0.0862s | 0.0901s | -0.0039s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.55 MB | 4.30 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.78 MB | 5.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.78 MB | 7.12 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.64 MB | 4.23 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0404s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1011s | 0.1128s | -0.0117s | improved |
| `ngap_rel18.6_specs` | 0.0708s | 0.0792s | -0.0084s | improved |
| `lteNRRCC` | 0.1098s | 0.1452s | -0.0354s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.01 MB | 7.90 MB | 0.0% | 127.2% |
| `f1ap_rel18.6_specs` | 8.46 MB | 106.66 MB | 132.8% | 268.5% |
| `ngap_rel18.6_specs` | 8.22 MB | 8.34 MB | 133.5% | 128.4% |
| `lteNRRCC` | 8.42 MB | 52.00 MB | 127.8% | 133.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0418s | 0.0423s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1243s | 0.1199s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0846s | 0.0812s | +0.0034s | worse |
| `lteNRRCC` | 0.1383s | 0.1330s | +0.0053s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.09 MB | 9.08 MB | 218.2% | 90.8% |
| `f1ap_rel18.6_specs` | 10.58 MB | 148.73 MB | 99.3% | 228.0% |
| `ngap_rel18.6_specs` | 9.26 MB | 10.16 MB | 82.5% | 0.0% |
| `lteNRRCC` | 68.12 MB | 88.39 MB | 163.3% | 161.3% |
<!-- BENCH_RESULTS_END -->
