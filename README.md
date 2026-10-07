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
Generated: 2026-10-07T01:21:52.614308+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0355s | +0.0037s | worse |
| `f1ap_rel18.6_specs` | 0.1199s | 0.1107s | +0.0092s | worse |
| `ngap_rel18.6_specs` | 0.0807s | 0.0758s | +0.0049s | worse |
| `lteNRRCC` | 0.1235s | 0.1215s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 83.3% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0332s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1013s | 0.1001s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0703s | 0.0664s | +0.0039s | worse |
| `lteNRRCC` | 0.1229s | 0.1200s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 36.71 MB | 17.3% | 103.8% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.93 MB | 107.1% | 103.4% |
| `ngap_rel18.6_specs` | 17.97 MB | 74.38 MB | 100.0% | 102.3% |
| `lteNRRCC` | 48.21 MB | 65.95 MB | 101.8% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0290s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.1003s | 0.0865s | +0.0138s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0530s | +0.0137s | worse |
| `lteNRRCC` | 0.1184s | 0.1022s | +0.0162s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.56 MB | 55.65 MB | 70.8% | 104.0% |
| `f1ap_rel18.6_specs` | 34.59 MB | 163.50 MB | 103.7% | 101.8% |
| `ngap_rel18.6_specs` | 24.36 MB | 117.55 MB | 104.8% | 102.4% |
| `lteNRRCC` | 74.79 MB | 102.89 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0188s | 0.0268s | -0.0080s | improved |
| `f1ap_rel18.6_specs` | 0.0900s | 0.0976s | -0.0076s | improved |
| `ngap_rel18.6_specs` | 0.0622s | 0.0543s | +0.0079s | worse |
| `lteNRRCC` | 0.1006s | 0.0953s | +0.0053s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.58 MB | 3.86 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.12 MB | 5.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 2.36 MB | 2.84 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.09 MB | 11.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0388s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1082s | 0.1056s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0739s | +0.0018s | worse |
| `lteNRRCC` | 0.1372s | 0.1368s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.89 MB | 7.27 MB | 0.0% | 174.2% |
| `f1ap_rel18.6_specs` | 7.86 MB | 8.00 MB | 91.7% | 93.2% |
| `ngap_rel18.6_specs` | 7.64 MB | 8.02 MB | 108.4% | 100.8% |
| `lteNRRCC` | 7.79 MB | 58.39 MB | 98.4% | 159.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0360s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1031s | 0.0988s | +0.0043s | worse |
| `ngap_rel18.6_specs` | 0.0710s | 0.0687s | +0.0023s | worse |
| `lteNRRCC` | 0.1173s | 0.1112s | +0.0061s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.45 MB | 9.79 MB | 0.0% | 111.5% |
| `f1ap_rel18.6_specs` | 11.20 MB | 155.84 MB | 128.8% | 136.8% |
| `ngap_rel18.6_specs` | 10.18 MB | 10.48 MB | 138.7% | 138.2% |
| `lteNRRCC` | 9.21 MB | 90.12 MB | 139.5% | 105.0% |
<!-- BENCH_RESULTS_END -->
