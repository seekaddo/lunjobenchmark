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
Generated: 2026-09-25T00:24:24.447911+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0345s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1079s | 0.1075s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0734s | 0.0752s | -0.0018s | improved |
| `lteNRRCC` | 0.1174s | 0.1173s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.63 MB | 53.55 MB | 90.0% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 101.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0344s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0955s | 0.0921s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0654s | +0.0009s | worse |
| `lteNRRCC` | 0.1293s | 0.1274s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.66 MB | 15.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.49 MB | 100.0% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.31 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.50 MB | 65.70 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0280s | 0.0295s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0767s | 0.0795s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0526s | 0.0529s | -0.0003s | improved |
| `lteNRRCC` | 0.1040s | 0.1028s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 55.60 MB | 61.5% | 104.3% |
| `f1ap_rel18.6_specs` | 34.56 MB | 164.77 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 24.47 MB | 117.38 MB | 105.0% | 105.9% |
| `lteNRRCC` | 74.60 MB | 102.88 MB | 104.1% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0429s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0856s | 0.1167s | -0.0311s | improved |
| `ngap_rel18.6_specs` | 0.0654s | 0.0699s | -0.0045s | improved |
| `lteNRRCC` | 0.1034s | 0.1046s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.95 MB | 4.19 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.64 MB | 10.52 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.84 MB | 7.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.50 MB | 5.25 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0341s | +0.0071s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.0916s | +0.0211s | worse |
| `ngap_rel18.6_specs` | 0.0776s | 0.0633s | +0.0143s | worse |
| `lteNRRCC` | 0.1395s | 0.1163s | +0.0232s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.21 MB | 7.60 MB | 221.1% | 96.8% |
| `f1ap_rel18.6_specs` | 8.31 MB | 8.14 MB | 100.0% | 100.0% |
| `ngap_rel18.6_specs` | 7.58 MB | 8.14 MB | 164.4% | 108.5% |
| `lteNRRCC` | 51.36 MB | 51.52 MB | 110.8% | 159.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0448s | -0.0106s | improved |
| `f1ap_rel18.6_specs` | 0.1008s | 0.1222s | -0.0214s | improved |
| `ngap_rel18.6_specs` | 0.0719s | 0.0865s | -0.0146s | improved |
| `lteNRRCC` | 0.1119s | 0.1308s | -0.0189s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.02 MB | 0.0% | 280.3% |
| `f1ap_rel18.6_specs` | 11.24 MB | 164.18 MB | 134.1% | 136.3% |
| `ngap_rel18.6_specs` | 10.62 MB | 9.55 MB | 138.8% | 207.3% |
| `lteNRRCC` | 9.54 MB | 98.69 MB | 138.4% | 138.4% |
<!-- BENCH_RESULTS_END -->
