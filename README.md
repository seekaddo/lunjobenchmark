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
Generated: 2026-07-28T23:06:31.852379+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0338s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1096s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0742s | +0.0027s | worse |
| `lteNRRCC` | 0.1201s | 0.1186s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 75.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0272s | +0.0078s | worse |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0735s | +0.0204s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0515s | +0.0152s | worse |
| `lteNRRCC` | 0.1301s | 0.0979s | +0.0322s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.53 MB | 36.14 MB | 21.6% | 103.7% |
| `f1ap_rel18.6_specs` | 21.62 MB | 103.22 MB | 103.2% | 100.0% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.71 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.56 MB | 66.22 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0293s | 0.0282s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0774s | 0.0761s | +0.0013s | worse |
| `ngap_rel18.6_specs` | 0.0547s | 0.0524s | +0.0023s | worse |
| `lteNRRCC` | 0.1025s | 0.1012s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.26 MB | 55.35 MB | 13.2% | 104.3% |
| `f1ap_rel18.6_specs` | 34.57 MB | 164.32 MB | 104.2% | 102.1% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.09 MB | 105.0% | 102.9% |
| `lteNRRCC` | 74.95 MB | 102.48 MB | 100.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0562s | 0.0365s | +0.0197s | worse |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0824s | +0.0109s | worse |
| `ngap_rel18.6_specs` | 0.0560s | 0.0524s | +0.0036s | worse |
| `lteNRRCC` | 0.1002s | 0.0675s | +0.0327s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.19 MB | 4.31 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 560 KB | 5.16 MB | 0.0% | 0.6% |
| `ngap_rel18.6_specs` | 6.23 MB | 5.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 2.41 MB | 5.50 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0390s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1189s | 0.1069s | +0.0120s | worse |
| `ngap_rel18.6_specs` | 0.0811s | 0.0762s | +0.0049s | worse |
| `lteNRRCC` | 0.1452s | 0.1413s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.62 MB | 7.82 MB | 0.0% | 166.4% |
| `f1ap_rel18.6_specs` | 8.44 MB | 8.55 MB | 162.5% | 83.3% |
| `ngap_rel18.6_specs` | 7.99 MB | 8.05 MB | 165.1% | 82.9% |
| `lteNRRCC` | 8.29 MB | 70.55 MB | 81.0% | 164.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0466s | 0.0401s | +0.0065s | worse |
| `f1ap_rel18.6_specs` | 0.1192s | 0.1155s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0853s | 0.0832s | +0.0021s | worse |
| `lteNRRCC` | 0.1178s | 0.1302s | -0.0124s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.21 MB | 9.90 MB | 195.9% | 126.2% |
| `f1ap_rel18.6_specs` | 10.44 MB | 118.39 MB | 129.9% | 135.8% |
| `ngap_rel18.6_specs` | 9.68 MB | 10.25 MB | 132.6% | 194.7% |
| `lteNRRCC` | 8.81 MB | 73.25 MB | 133.5% | 134.3% |
<!-- BENCH_RESULTS_END -->
