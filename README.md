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
Generated: 2026-07-14T23:02:07.683529+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0359s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1122s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0770s | +0.0007s | worse |
| `lteNRRCC` | 0.1215s | 0.1204s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.79 MB | 53.55 MB | 22.1% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0279s | +0.0061s | worse |
| `f1ap_rel18.6_specs` | 0.0923s | 0.0744s | +0.0179s | worse |
| `ngap_rel18.6_specs` | 0.0659s | 0.0525s | +0.0134s | worse |
| `lteNRRCC` | 0.1276s | 0.0983s | +0.0293s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.16 MB | 36.00 MB | 85.2% | 111.1% |
| `f1ap_rel18.6_specs` | 21.87 MB | 103.22 MB | 109.4% | 105.4% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.59 MB | 111.1% | 104.3% |
| `lteNRRCC` | 48.62 MB | 66.36 MB | 103.1% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0329s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0898s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0666s | 0.0629s | +0.0037s | worse |
| `lteNRRCC` | 0.1204s | 0.1171s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 55.64 MB | 85.7% | 110.3% |
| `f1ap_rel18.6_specs` | 35.25 MB | 163.75 MB | 110.0% | 103.4% |
| `ngap_rel18.6_specs` | 24.03 MB | 117.07 MB | 112.5% | 106.8% |
| `lteNRRCC` | 74.79 MB | 102.61 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0235s | 0.0249s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0854s | 0.0749s | +0.0105s | worse |
| `ngap_rel18.6_specs` | 0.0563s | 0.0502s | +0.0061s | worse |
| `lteNRRCC` | 0.1242s | 0.0764s | +0.0478s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 896 KB | 7.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.36 MB | 2.50 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.36 MB | 5.62 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.41 MB | 28.23 MB | 0.0% | 37.6% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0401s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1068s | 0.1074s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0736s | 0.0771s | -0.0035s | improved |
| `lteNRRCC` | 0.1403s | 0.1389s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.88 MB | 7.50 MB | 230.4% | 162.5% |
| `f1ap_rel18.6_specs` | 8.04 MB | 106.65 MB | 164.3% | 105.4% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.55 MB | 164.2% | 92.5% |
| `lteNRRCC` | 47.94 MB | 59.92 MB | 108.2% | 109.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0395s | -0.0041s | improved |
| `f1ap_rel18.6_specs` | 0.1055s | 0.1105s | -0.0050s | improved |
| `ngap_rel18.6_specs` | 0.0701s | 0.0758s | -0.0057s | improved |
| `lteNRRCC` | 0.1129s | 0.1307s | -0.0178s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.78 MB | 10.28 MB | 196.8% | 264.3% |
| `f1ap_rel18.6_specs` | 11.04 MB | 164.20 MB | 189.0% | 101.1% |
| `ngap_rel18.6_specs` | 9.35 MB | 9.62 MB | 198.8% | 205.1% |
| `lteNRRCC` | 73.78 MB | 76.21 MB | 182.2% | 114.3% |
<!-- BENCH_RESULTS_END -->
