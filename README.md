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
Generated: 2026-10-04T15:13:31.571326+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0347s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1082s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0772s | 0.0760s | +0.0012s | worse |
| `lteNRRCC` | 0.1192s | 0.1186s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 75.0% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0351s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0964s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0676s | -0.0024s | improved |
| `lteNRRCC` | 0.1284s | 0.1291s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.63 MB | 36.68 MB | 74.1% | 103.8% |
| `f1ap_rel18.6_specs` | 22.41 MB | 103.49 MB | 106.2% | 103.5% |
| `ngap_rel18.6_specs` | 17.91 MB | 73.92 MB | 108.0% | 104.8% |
| `lteNRRCC` | 48.52 MB | 66.23 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0341s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0899s | 0.0914s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0629s | -0.0011s | improved |
| `lteNRRCC` | 0.1189s | 0.1182s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.71 MB | 76.0% | 108.0% |
| `f1ap_rel18.6_specs` | 34.45 MB | 164.74 MB | 107.4% | 101.9% |
| `ngap_rel18.6_specs` | 24.07 MB | 117.59 MB | 104.3% | 105.0% |
| `lteNRRCC` | 74.91 MB | 102.23 MB | 101.8% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0306s | 0.0195s | +0.0111s | worse |
| `f1ap_rel18.6_specs` | 0.1277s | 0.0666s | +0.0611s | worse |
| `ngap_rel18.6_specs` | 0.0732s | 0.0516s | +0.0216s | worse |
| `lteNRRCC` | 0.0985s | 0.0783s | +0.0202s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.34 MB | 3.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.09 MB | 7.11 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 11.19 MB | 7.69 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.00 MB | 9.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0362s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.1081s | 0.1033s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0762s | 0.0694s | +0.0068s | worse |
| `lteNRRCC` | 0.1395s | 0.1118s | +0.0277s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.29 MB | 7.41 MB | 149.9% | 164.2% |
| `f1ap_rel18.6_specs` | 8.08 MB | 8.14 MB | 158.3% | 94.3% |
| `ngap_rel18.6_specs` | 8.02 MB | 7.59 MB | 100.1% | 160.3% |
| `lteNRRCC` | 8.14 MB | 49.55 MB | 159.5% | 156.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0426s | 0.0332s | +0.0094s | worse |
| `f1ap_rel18.6_specs` | 0.1167s | 0.0978s | +0.0189s | worse |
| `ngap_rel18.6_specs` | 0.0807s | 0.0658s | +0.0149s | worse |
| `lteNRRCC` | 0.1361s | 0.1095s | +0.0266s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.45 MB | 9.05 MB | 0.0% | 148.7% |
| `f1ap_rel18.6_specs` | 10.05 MB | 10.41 MB | 151.6% | 94.4% |
| `ngap_rel18.6_specs` | 10.17 MB | 9.46 MB | 95.0% | 87.4% |
| `lteNRRCC` | 9.03 MB | 75.90 MB | 89.9% | 110.3% |
<!-- BENCH_RESULTS_END -->
