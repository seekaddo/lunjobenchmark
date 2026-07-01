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
Generated: 2026-07-01T12:39:04.599286+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0347s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1121s | 0.1089s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0750s | +0.0019s | worse |
| `lteNRRCC` | 0.1204s | 0.1186s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.69 MB | 53.55 MB | 21.1% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.0% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0347s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0925s | +0.0038s | worse |
| `ngap_rel18.6_specs` | 0.0671s | 0.0653s | +0.0018s | worse |
| `lteNRRCC` | 0.1293s | 0.1272s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 36.59 MB | 79.3% | 110.7% |
| `f1ap_rel18.6_specs` | 22.38 MB | 103.36 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 17.77 MB | 74.52 MB | 111.5% | 106.8% |
| `lteNRRCC` | 48.38 MB | 65.87 MB | 104.5% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0324s | 0.0348s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.0882s | 0.0999s | -0.0117s | improved |
| `ngap_rel18.6_specs` | 0.0615s | 0.0689s | -0.0074s | improved |
| `lteNRRCC` | 0.1144s | 0.1163s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.51 MB | 55.21 MB | 84.0% | 111.5% |
| `f1ap_rel18.6_specs` | 34.68 MB | 164.68 MB | 110.7% | 105.6% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.59 MB | 113.0% | 104.9% |
| `lteNRRCC` | 74.27 MB | 101.93 MB | 105.2% | 102.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0238s | 0.0239s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0712s | 0.0665s | +0.0047s | worse |
| `ngap_rel18.6_specs` | 0.0475s | 0.0470s | +0.0005s | worse |
| `lteNRRCC` | 0.0785s | 0.0765s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.34 MB | 4.61 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.69 MB | 6.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.33 MB | 4.45 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.33 MB | 3.44 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0381s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1053s | +0.0039s | worse |
| `ngap_rel18.6_specs` | 0.0762s | 0.0736s | +0.0026s | worse |
| `lteNRRCC` | 0.1390s | 0.1355s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.55 MB | 7.49 MB | 93.5% | 156.6% |
| `f1ap_rel18.6_specs` | 8.10 MB | 106.64 MB | 160.6% | 109.1% |
| `ngap_rel18.6_specs` | 8.23 MB | 7.84 MB | 111.8% | 84.5% |
| `lteNRRCC` | 50.73 MB | 49.63 MB | 224.1% | 108.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0389s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1071s | 0.1084s | -0.0013s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0765s | +0.0006s | worse |
| `lteNRRCC` | 0.1272s | 0.1251s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.45 MB | 8.72 MB | 79.1% | 159.4% |
| `f1ap_rel18.6_specs` | 9.55 MB | 155.10 MB | 158.2% | 108.1% |
| `ngap_rel18.6_specs` | 8.89 MB | 8.95 MB | 156.9% | 157.1% |
| `lteNRRCC` | 8.43 MB | 74.14 MB | 77.1% | 108.2% |
<!-- BENCH_RESULTS_END -->
