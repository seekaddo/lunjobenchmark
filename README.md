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
Generated: 2026-04-04T10:42:11.635484+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0375s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1178s | 0.1158s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0797s | 0.0801s | -0.0004s | improved |
| `lteNRRCC` | 0.1253s | 0.1240s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.92 MB | 53.55 MB | 7.9% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.6% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 104.9% | 103.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0341s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0938s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0664s | -0.0007s | improved |
| `lteNRRCC` | 0.1279s | 0.1276s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.52 MB | 27.9% | 107.1% |
| `f1ap_rel18.6_specs` | 21.78 MB | 103.33 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 16.51 MB | 74.68 MB | 111.5% | 106.8% |
| `lteNRRCC` | 48.52 MB | 65.90 MB | 104.7% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0346s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0891s | 0.0990s | -0.0099s | improved |
| `ngap_rel18.6_specs` | 0.0621s | 0.0687s | -0.0066s | improved |
| `lteNRRCC` | 0.1150s | 0.1153s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.55 MB | 96.0% | 111.1% |
| `f1ap_rel18.6_specs` | 35.14 MB | 164.43 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.36 MB | 117.47 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.98 MB | 102.81 MB | 105.2% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0205s | 0.0297s | -0.0092s | improved |
| `f1ap_rel18.6_specs` | 0.0587s | 0.0696s | -0.0109s | improved |
| `ngap_rel18.6_specs` | 0.0403s | 0.0580s | -0.0177s | improved |
| `lteNRRCC` | 0.0676s | 0.0768s | -0.0092s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.77 MB | 4.22 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.19 MB | 4.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.19 MB | 5.50 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.53 MB | 3.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0391s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1046s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0772s | 0.0734s | +0.0038s | worse |
| `lteNRRCC` | 0.1302s | 0.1354s | -0.0052s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.85 MB | 7.89 MB | 78.5% | 159.4% |
| `f1ap_rel18.6_specs` | 8.79 MB | 8.78 MB | 157.1% | 220.8% |
| `ngap_rel18.6_specs` | 8.54 MB | 8.36 MB | 117.1% | 115.2% |
| `lteNRRCC` | 8.53 MB | 8.40 MB | 116.9% | 215.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0400s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1065s | 0.1106s | -0.0041s | improved |
| `ngap_rel18.6_specs` | 0.0741s | 0.0761s | -0.0020s | improved |
| `lteNRRCC` | 0.1278s | 0.1251s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.55 MB | 8.71 MB | 0.0% | 80.7% |
| `f1ap_rel18.6_specs` | 9.55 MB | 11.38 MB | 160.0% | 229.0% |
| `ngap_rel18.6_specs` | 8.88 MB | 9.07 MB | 159.1% | 79.8% |
| `lteNRRCC` | 8.61 MB | 98.56 MB | 158.2% | 111.2% |
<!-- BENCH_RESULTS_END -->
