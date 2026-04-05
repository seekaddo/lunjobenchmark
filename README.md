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
Generated: 2026-04-05T22:39:53.599028+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0360s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1159s | 0.1129s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0776s | +0.0014s | worse |
| `lteNRRCC` | 0.1231s | 0.1215s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 34.3% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0340s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0924s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0662s | 0.0657s | +0.0005s | worse |
| `lteNRRCC` | 0.1281s | 0.1287s | -0.0006s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.20 MB | 92.6% | 113.8% |
| `f1ap_rel18.6_specs` | 21.59 MB | 102.72 MB | 106.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.28 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.69 MB | 66.36 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0347s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.0868s | 0.0911s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0603s | 0.0638s | -0.0035s | improved |
| `lteNRRCC` | 0.1141s | 0.1166s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.26 MB | 55.86 MB | 104.5% | 111.1% |
| `f1ap_rel18.6_specs` | 34.73 MB | 164.66 MB | 106.9% | 105.6% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.71 MB | 112.5% | 104.9% |
| `lteNRRCC` | 74.87 MB | 102.95 MB | 105.3% | 104.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0194s | 0.0194s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0588s | 0.0643s | -0.0055s | improved |
| `ngap_rel18.6_specs` | 0.0400s | 0.0399s | +0.0001s | worse |
| `lteNRRCC` | 0.0679s | 0.0731s | -0.0052s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.73 MB | 4.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 3.89 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.12 MB | 4.11 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 3.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0389s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1045s | 0.1061s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0731s | 0.0738s | -0.0007s | improved |
| `lteNRRCC` | 0.1357s | 0.1385s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.63 MB | 93.3% | 95.4% |
| `f1ap_rel18.6_specs` | 8.52 MB | 106.65 MB | 235.6% | 115.6% |
| `ngap_rel18.6_specs` | 8.30 MB | 8.18 MB | 116.6% | 116.8% |
| `lteNRRCC` | 8.54 MB | 50.72 MB | 235.8% | 114.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0380s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1222s | 0.1075s | +0.0147s | worse |
| `ngap_rel18.6_specs` | 0.0829s | 0.0745s | +0.0084s | worse |
| `lteNRRCC` | 0.1274s | 0.1242s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.84 MB | 8.86 MB | 110.3% | 152.4% |
| `f1ap_rel18.6_specs` | 11.38 MB | 11.82 MB | 108.9% | 218.7% |
| `ngap_rel18.6_specs` | 9.20 MB | 9.26 MB | 150.8% | 153.2% |
| `lteNRRCC` | 72.36 MB | 94.82 MB | 148.6% | 151.1% |
<!-- BENCH_RESULTS_END -->
