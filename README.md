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
Generated: 2026-08-20T22:33:52.436958+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0358s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1116s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0764s | -0.0008s | improved |
| `lteNRRCC` | 0.1197s | 0.1205s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 63.3% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0353s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0960s | 0.0956s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0675s | 0.0660s | +0.0015s | worse |
| `lteNRRCC` | 0.1295s | 0.1295s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.55 MB | 18.4% | 107.4% |
| `f1ap_rel18.6_specs` | 21.70 MB | 102.64 MB | 103.2% | 103.5% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.23 MB | 103.8% | 104.7% |
| `lteNRRCC` | 48.69 MB | 66.45 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0370s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.0884s | 0.0971s | -0.0087s | improved |
| `ngap_rel18.6_specs` | 0.0620s | 0.0688s | -0.0068s | improved |
| `lteNRRCC` | 0.1153s | 0.1307s | -0.0154s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.50 MB | 67.9% | 107.7% |
| `f1ap_rel18.6_specs` | 34.60 MB | 164.25 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.82 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.94 MB | 102.58 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0168s | 0.0243s | -0.0075s | improved |
| `f1ap_rel18.6_specs` | 0.0651s | 0.0683s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0439s | 0.0474s | -0.0035s | improved |
| `lteNRRCC` | 0.0758s | 0.0776s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.56 MB | 1.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.42 MB | 3.08 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.38 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.73 MB | 3.77 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0393s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1133s | 0.1091s | +0.0042s | worse |
| `ngap_rel18.6_specs` | 0.0844s | 0.0766s | +0.0078s | worse |
| `lteNRRCC` | 0.1389s | 0.1390s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.64 MB | 7.91 MB | 108.2% | 108.2% |
| `f1ap_rel18.6_specs` | 8.51 MB | 8.32 MB | 83.4% | 83.5% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.05 MB | 99.9% | 164.8% |
| `lteNRRCC` | 51.21 MB | 69.68 MB | 111.2% | 164.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0387s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1152s | 0.1096s | +0.0056s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0763s | +0.0008s | worse |
| `lteNRRCC` | 0.1287s | 0.1269s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.48 MB | 8.95 MB | 0.0% | 149.6% |
| `f1ap_rel18.6_specs` | 11.34 MB | 164.20 MB | 112.4% | 154.7% |
| `ngap_rel18.6_specs` | 9.22 MB | 9.03 MB | 149.5% | 154.2% |
| `lteNRRCC` | 8.76 MB | 74.16 MB | 150.5% | 153.4% |
<!-- BENCH_RESULTS_END -->
