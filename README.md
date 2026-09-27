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
Generated: 2026-09-27T15:03:45.741499+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0350s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1093s | 0.1112s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0748s | 0.0760s | -0.0012s | improved |
| `lteNRRCC` | 0.1189s | 0.1207s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 79.2% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.6% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0338s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.1000s | 0.0977s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0723s | 0.0676s | +0.0047s | worse |
| `lteNRRCC` | 0.1328s | 0.1198s | +0.0130s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.61 MB | 69.7% | 107.1% |
| `f1ap_rel18.6_specs` | 22.15 MB | 102.74 MB | 106.2% | 103.4% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.35 MB | 103.8% | 104.5% |
| `lteNRRCC` | 48.50 MB | 66.01 MB | 103.1% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0292s | 0.0353s | -0.0061s | improved |
| `f1ap_rel18.6_specs` | 0.0769s | 0.0919s | -0.0150s | improved |
| `ngap_rel18.6_specs` | 0.0533s | 0.0651s | -0.0118s | improved |
| `lteNRRCC` | 0.1018s | 0.1262s | -0.0244s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 55.78 MB | 23.6% | 109.1% |
| `f1ap_rel18.6_specs` | 35.13 MB | 163.72 MB | 104.2% | 102.1% |
| `ngap_rel18.6_specs` | 24.21 MB | 117.09 MB | 110.0% | 102.9% |
| `lteNRRCC` | 74.34 MB | 102.24 MB | 102.0% | 101.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0460s | 0.0239s | +0.0221s | worse |
| `f1ap_rel18.6_specs` | 0.0663s | 0.0987s | -0.0324s | improved |
| `ngap_rel18.6_specs` | 0.0510s | 0.0436s | +0.0074s | worse |
| `lteNRRCC` | 0.0810s | 0.0858s | -0.0048s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.42 MB | 8.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.12 MB | 9.39 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.45 MB | 8.48 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.44 MB | 7.42 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0396s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1056s | 0.1086s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0733s | 0.0760s | -0.0027s | improved |
| `lteNRRCC` | 0.1379s | 0.1396s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.49 MB | 7.34 MB | 88.3% | 175.9% |
| `f1ap_rel18.6_specs` | 8.09 MB | 8.02 MB | 160.2% | 93.6% |
| `ngap_rel18.6_specs` | 7.53 MB | 8.35 MB | 162.5% | 103.9% |
| `lteNRRCC` | 48.75 MB | 51.72 MB | 108.3% | 107.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0390s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1167s | 0.1105s | +0.0062s | worse |
| `ngap_rel18.6_specs` | 0.0795s | 0.0752s | +0.0043s | worse |
| `lteNRRCC` | 0.1294s | 0.1279s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.54 MB | 8.73 MB | 0.0% | 99.5% |
| `f1ap_rel18.6_specs` | 9.65 MB | 164.16 MB | 80.2% | 104.8% |
| `ngap_rel18.6_specs` | 10.79 MB | 9.05 MB | 107.1% | 157.1% |
| `lteNRRCC` | 9.33 MB | 98.66 MB | 99.1% | 156.4% |
<!-- BENCH_RESULTS_END -->
