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
Generated: 2026-10-23T14:50:26.367962+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0377s | -0.0038s | improved |
| `f1ap_rel18.6_specs` | 0.1088s | 0.1165s | -0.0077s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0800s | -0.0062s | improved |
| `lteNRRCC` | 0.1188s | 0.1232s | -0.0044s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 73.9% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 100.0% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0266s | +0.0095s | worse |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0728s | +0.0210s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0513s | +0.0150s | worse |
| `lteNRRCC` | 0.1302s | 0.0967s | +0.0335s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 36.50 MB | 80.0% | 107.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.47 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 18.04 MB | 73.66 MB | 104.0% | 104.8% |
| `lteNRRCC` | 48.48 MB | 66.50 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0283s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.0924s | 0.0745s | +0.0179s | worse |
| `ngap_rel18.6_specs` | 0.0640s | 0.0518s | +0.0122s | worse |
| `lteNRRCC` | 0.1188s | 0.1016s | +0.0172s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 55.86 MB | 76.9% | 107.4% |
| `f1ap_rel18.6_specs` | 34.10 MB | 163.59 MB | 103.6% | 103.6% |
| `ngap_rel18.6_specs` | 24.16 MB | 117.88 MB | 104.3% | 102.4% |
| `lteNRRCC` | 74.67 MB | 102.62 MB | 101.8% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0292s | 0.0142s | +0.0150s | worse |
| `f1ap_rel18.6_specs` | 0.0769s | 0.0683s | +0.0086s | worse |
| `ngap_rel18.6_specs` | 0.0506s | 0.0603s | -0.0097s | improved |
| `lteNRRCC` | 0.0857s | 0.0859s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.91 MB | 5.09 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.56 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.20 MB | 4.55 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.97 MB | 4.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0268s | 0.0340s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.0760s | 0.0872s | -0.0112s | improved |
| `ngap_rel18.6_specs` | 0.0525s | 0.0610s | -0.0085s | improved |
| `lteNRRCC` | 0.0884s | 0.0965s | -0.0081s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 8.58 MB | 0.0% | 158.6% |
| `f1ap_rel18.6_specs` | 8.93 MB | 8.88 MB | 158.3% | 156.2% |
| `ngap_rel18.6_specs` | 8.85 MB | 8.88 MB | 156.9% | 119.2% |
| `lteNRRCC` | 8.81 MB | 68.36 MB | 153.4% | 151.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0409s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1214s | 0.1189s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0814s | 0.0847s | -0.0033s | improved |
| `lteNRRCC` | 0.1373s | 0.1354s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 9.54 MB | 0.0% | 162.3% |
| `f1ap_rel18.6_specs` | 10.90 MB | 163.27 MB | 200.3% | 161.0% |
| `ngap_rel18.6_specs` | 9.26 MB | 11.05 MB | 81.1% | 92.6% |
| `lteNRRCC` | 8.73 MB | 101.69 MB | 80.5% | 108.0% |
<!-- BENCH_RESULTS_END -->
