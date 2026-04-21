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
Generated: 2026-04-21T22:47:26.495503+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0371s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1168s | 0.1167s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0820s | 0.0786s | +0.0034s | worse |
| `lteNRRCC` | 0.1251s | 0.1217s | +0.0034s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 8.0% | 109.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0338s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0925s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0661s | 0.0654s | +0.0007s | worse |
| `lteNRRCC` | 0.1291s | 0.1271s | +0.0020s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.68 MB | 85.7% | 114.3% |
| `f1ap_rel18.6_specs` | 22.41 MB | 102.73 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.59 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.12 MB | 66.51 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0324s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.0948s | 0.0962s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0662s | -0.0004s | improved |
| `lteNRRCC` | 0.1287s | 0.1139s | +0.0148s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.26 MB | 55.83 MB | 92.6% | 110.0% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.61 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.16 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.90 MB | 102.82 MB | 104.7% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0245s | 0.0277s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.0646s | 0.0845s | -0.0199s | improved |
| `ngap_rel18.6_specs` | 0.0493s | 0.0606s | -0.0113s | improved |
| `lteNRRCC` | 0.0758s | 0.0955s | -0.0197s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.69 MB | 1.02 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.19 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.84 MB | 2.02 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.55 MB | 8.05 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0398s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1099s | +0.0001s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0759s | +0.0008s | worse |
| `lteNRRCC` | 0.1402s | 0.1309s | +0.0093s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.80 MB | 79.2% | 222.9% |
| `f1ap_rel18.6_specs` | 8.38 MB | 8.42 MB | 158.8% | 157.8% |
| `ngap_rel18.6_specs` | 8.11 MB | 7.88 MB | 99.6% | 154.9% |
| `lteNRRCC` | 48.38 MB | 48.80 MB | 156.6% | 105.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0370s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1102s | +0.0044s | worse |
| `ngap_rel18.6_specs` | 0.0781s | 0.0773s | +0.0008s | worse |
| `lteNRRCC` | 0.1276s | 0.1302s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.54 MB | 9.00 MB | 148.3% | 153.0% |
| `f1ap_rel18.6_specs` | 12.01 MB | 10.45 MB | 106.8% | 89.1% |
| `ngap_rel18.6_specs` | 11.18 MB | 9.41 MB | 211.4% | 152.3% |
| `lteNRRCC` | 8.80 MB | 79.01 MB | 73.7% | 150.8% |
<!-- BENCH_RESULTS_END -->
