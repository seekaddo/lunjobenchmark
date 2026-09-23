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
Generated: 2026-09-23T14:50:35.779507+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0361s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1133s | 0.1104s | +0.0029s | worse |
| `ngap_rel18.6_specs` | 0.0778s | 0.0755s | +0.0023s | worse |
| `lteNRRCC` | 0.1214s | 0.1196s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 10.0% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0329s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0979s | 0.0958s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0684s | 0.0655s | +0.0029s | worse |
| `lteNRRCC` | 0.1323s | 0.1179s | +0.0144s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.00 MB | 22.2% | 103.6% |
| `f1ap_rel18.6_specs` | 22.25 MB | 102.55 MB | 106.2% | 103.4% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.66 MB | 107.7% | 102.2% |
| `lteNRRCC` | 48.83 MB | 65.45 MB | 101.5% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0311s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.0913s | 0.0941s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0643s | +0.0006s | worse |
| `lteNRRCC` | 0.1183s | 0.0958s | +0.0225s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.48 MB | 80.0% | 103.7% |
| `f1ap_rel18.6_specs` | 34.70 MB | 164.49 MB | 103.6% | 103.6% |
| `ngap_rel18.6_specs` | 24.01 MB | 117.82 MB | 104.2% | 102.4% |
| `lteNRRCC` | 74.95 MB | 102.52 MB | 103.5% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0275s | 0.0362s | -0.0087s | improved |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0950s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0657s | 0.0640s | +0.0017s | worse |
| `lteNRRCC` | 0.0995s | 0.1141s | -0.0146s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.66 MB | 4.31 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 10.75 MB | 9.14 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.17 MB | 1.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.27 MB | 4.89 MB | 1.3% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0426s | 0.0390s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1066s | +0.0049s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0743s | +0.0050s | worse |
| `lteNRRCC` | 0.1277s | 0.1363s | -0.0086s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.29 MB | 8.25 MB | 0.0% | 155.0% |
| `f1ap_rel18.6_specs` | 8.81 MB | 106.59 MB | 152.7% | 110.8% |
| `ngap_rel18.6_specs` | 8.50 MB | 8.34 MB | 99.2% | 149.3% |
| `lteNRRCC` | 51.78 MB | 59.75 MB | 110.2% | 155.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0430s | 0.0423s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1229s | 0.1157s | +0.0072s | worse |
| `ngap_rel18.6_specs` | 0.0840s | 0.0828s | +0.0012s | worse |
| `lteNRRCC` | 0.1348s | 0.1321s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.99 MB | 0.0% | 146.8% |
| `f1ap_rel18.6_specs` | 10.10 MB | 10.56 MB | 146.2% | 88.2% |
| `ngap_rel18.6_specs` | 9.25 MB | 11.11 MB | 145.9% | 204.9% |
| `lteNRRCC` | 8.85 MB | 101.69 MB | 149.3% | 144.8% |
<!-- BENCH_RESULTS_END -->
