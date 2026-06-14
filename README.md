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
Generated: 2026-06-14T23:16:01.974847+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0353s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1103s | 0.1111s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0757s | 0.0758s | -0.0001s | improved |
| `lteNRRCC` | 0.1187s | 0.1208s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 5.3% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0340s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0935s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0657s | +0.0006s | worse |
| `lteNRRCC` | 0.1245s | 0.1269s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.38 MB | 36.73 MB | 82.1% | 107.1% |
| `f1ap_rel18.6_specs` | 22.40 MB | 103.20 MB | 106.2% | 105.3% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.58 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.80 MB | 66.32 MB | 104.8% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0357s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0973s | 0.0962s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0665s | 0.0726s | -0.0061s | improved |
| `lteNRRCC` | 0.1290s | 0.1282s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.80 MB | 85.2% | 106.9% |
| `f1ap_rel18.6_specs` | 34.77 MB | 164.66 MB | 106.2% | 105.0% |
| `ngap_rel18.6_specs` | 24.21 MB | 117.34 MB | 111.5% | 106.7% |
| `lteNRRCC` | 74.91 MB | 102.48 MB | 104.8% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0176s | 0.0244s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.0713s | 0.0823s | -0.0110s | improved |
| `ngap_rel18.6_specs` | 0.0460s | 0.0470s | -0.0010s | improved |
| `lteNRRCC` | 0.0761s | 0.0801s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.94 MB | 4.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.03 MB | 8.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.38 MB | 8.55 MB | 1.2% | 0.0% |
| `lteNRRCC` | 7.50 MB | 7.52 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0395s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1077s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0783s | 0.0747s | +0.0036s | worse |
| `lteNRRCC` | 0.1367s | 0.1274s | +0.0093s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.30 MB | 7.32 MB | 92.9% | 164.4% |
| `f1ap_rel18.6_specs` | 7.98 MB | 106.66 MB | 103.5% | 109.0% |
| `ngap_rel18.6_specs` | 7.48 MB | 8.06 MB | 163.7% | 108.1% |
| `lteNRRCC` | 50.96 MB | 70.56 MB | 228.7% | 109.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0449s | 0.0376s | +0.0073s | worse |
| `f1ap_rel18.6_specs` | 0.1276s | 0.1148s | +0.0128s | worse |
| `ngap_rel18.6_specs` | 0.0906s | 0.0770s | +0.0136s | worse |
| `lteNRRCC` | 0.1477s | 0.1262s | +0.0215s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.77 MB | 9.77 MB | 77.7% | 78.1% |
| `f1ap_rel18.6_specs` | 11.38 MB | 159.22 MB | 98.2% | 153.5% |
| `ngap_rel18.6_specs` | 10.25 MB | 10.68 MB | 154.6% | 94.3% |
| `lteNRRCC` | 73.77 MB | 87.81 MB | 107.0% | 152.2% |
<!-- BENCH_RESULTS_END -->
