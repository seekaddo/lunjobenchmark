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
Generated: 2026-10-31T01:28:58.245827+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0412s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1227s | 0.1269s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0839s | 0.0860s | -0.0021s | improved |
| `lteNRRCC` | 0.1283s | 0.1291s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 80.0% | 103.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.2% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.0% | 103.8% |
| `lteNRRCC` | 72.35 MB | 100.18 MB | 101.6% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0475s | -0.0105s | improved |
| `f1ap_rel18.6_specs` | 0.1149s | 0.1440s | -0.0291s | improved |
| `ngap_rel18.6_specs` | 0.0804s | 0.1005s | -0.0201s | improved |
| `lteNRRCC` | 0.1253s | 0.1583s | -0.0330s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.79 MB | 34.65 MB | 78.3% | 103.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 18.03 MB | 72.65 MB | 104.5% | 102.1% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 101.7% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0534s | -0.0115s | improved |
| `f1ap_rel18.6_specs` | 0.1307s | 0.1650s | -0.0343s | improved |
| `ngap_rel18.6_specs` | 0.0908s | 0.1156s | -0.0248s | improved |
| `lteNRRCC` | 0.1344s | 0.1607s | -0.0263s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 53.73 MB | 68.0% | 100.0% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 107.1% | 101.3% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 104.5% | 101.9% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 101.6% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0251s | 0.0200s | +0.0051s | worse |
| `f1ap_rel18.6_specs` | 0.0836s | 0.0739s | +0.0097s | worse |
| `ngap_rel18.6_specs` | 0.0505s | 0.0559s | -0.0054s | improved |
| `lteNRRCC` | 0.0854s | 0.0813s | +0.0041s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.69 MB | 6.62 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.56 MB | 9.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.91 MB | 4.23 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.19 MB | 4.22 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0406s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1110s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0788s | -0.0030s | improved |
| `lteNRRCC` | 0.1386s | 0.1405s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.25 MB | 7.45 MB | 108.3% | 166.2% |
| `f1ap_rel18.6_specs` | 8.62 MB | 8.18 MB | 112.7% | 158.8% |
| `ngap_rel18.6_specs` | 8.30 MB | 8.12 MB | 111.9% | 99.8% |
| `lteNRRCC` | 50.75 MB | 51.90 MB | 159.5% | 108.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0439s | -0.0034s | improved |
| `f1ap_rel18.6_specs` | 0.1156s | 0.1286s | -0.0130s | improved |
| `ngap_rel18.6_specs` | 0.0809s | 0.0886s | -0.0077s | improved |
| `lteNRRCC` | 0.1289s | 0.1340s | -0.0051s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.69 MB | 0.0% | 219.4% |
| `f1ap_rel18.6_specs` | 9.89 MB | 11.66 MB | 155.7% | 228.1% |
| `ngap_rel18.6_specs` | 10.58 MB | 9.03 MB | 222.9% | 155.1% |
| `lteNRRCC` | 8.45 MB | 96.98 MB | 180.5% | 166.7% |
<!-- BENCH_RESULTS_END -->
