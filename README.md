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
Generated: 2026-04-13T22:53:39.974591+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0379s | -0.0020s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1177s | -0.0069s | improved |
| `ngap_rel18.6_specs` | 0.0783s | 0.0813s | -0.0030s | improved |
| `lteNRRCC` | 0.1200s | 0.1246s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 24.7% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0362s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0926s | 0.0937s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0657s | -0.0008s | improved |
| `lteNRRCC` | 0.1286s | 0.1287s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.26 MB | 36.56 MB | 96.6% | 110.7% |
| `f1ap_rel18.6_specs` | 22.43 MB | 102.71 MB | 109.1% | 105.3% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.46 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.30 MB | 66.19 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0353s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0908s | 0.0928s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0652s | 0.0646s | +0.0006s | worse |
| `lteNRRCC` | 0.1174s | 0.1262s | -0.0088s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.90 MB | 21.2% | 114.3% |
| `f1ap_rel18.6_specs` | 34.43 MB | 164.46 MB | 110.0% | 105.3% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.31 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.89 MB | 102.79 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0238s | 0.0323s | -0.0085s | improved |
| `f1ap_rel18.6_specs` | 0.0674s | 0.0565s | +0.0109s | worse |
| `ngap_rel18.6_specs` | 0.0523s | 0.0411s | +0.0112s | worse |
| `lteNRRCC` | 0.0778s | 0.0684s | +0.0094s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.41 MB | 3.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.03 MB | 2.20 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.38 MB | 7.52 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.12 MB | 2.62 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0413s | 0.0448s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.1171s | 0.1141s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0815s | 0.0824s | -0.0009s | improved |
| `lteNRRCC` | 0.1423s | 0.1289s | +0.0134s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.82 MB | 7.85 MB | 167.3% | 100.7% |
| `f1ap_rel18.6_specs` | 8.75 MB | 106.64 MB | 157.1% | 105.7% |
| `ngap_rel18.6_specs` | 8.31 MB | 8.37 MB | 78.2% | 79.0% |
| `lteNRRCC` | 48.70 MB | 52.00 MB | 104.8% | 107.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0387s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1203s | 0.1137s | +0.0066s | worse |
| `ngap_rel18.6_specs` | 0.0864s | 0.0787s | +0.0077s | worse |
| `lteNRRCC` | 0.1258s | 0.1287s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.33 MB | 8.58 MB | 81.0% | 80.4% |
| `f1ap_rel18.6_specs` | 9.49 MB | 164.20 MB | 81.1% | 163.9% |
| `ngap_rel18.6_specs` | 8.89 MB | 8.96 MB | 162.9% | 151.6% |
| `lteNRRCC` | 70.10 MB | 76.14 MB | 105.9% | 161.6% |
<!-- BENCH_RESULTS_END -->
