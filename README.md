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
Generated: 2026-04-07T22:48:33.534942+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0344s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1091s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0747s | +0.0010s | worse |
| `lteNRRCC` | 0.1210s | 0.1171s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.88 MB | 53.55 MB | 25.6% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.1% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0347s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0929s | 0.0963s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0669s | -0.0008s | improved |
| `lteNRRCC` | 0.1277s | 0.1289s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.21 MB | 36.60 MB | 88.5% | 110.7% |
| `f1ap_rel18.6_specs` | 22.26 MB | 102.86 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.68 MB | 73.99 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.78 MB | 66.17 MB | 104.6% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0322s | 0.0371s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.0865s | 0.0972s | -0.0107s | improved |
| `ngap_rel18.6_specs` | 0.0606s | 0.0678s | -0.0072s | improved |
| `lteNRRCC` | 0.1138s | 0.1296s | -0.0158s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.73 MB | 92.0% | 107.1% |
| `f1ap_rel18.6_specs` | 34.52 MB | 164.29 MB | 106.9% | 105.6% |
| `ngap_rel18.6_specs` | 23.77 MB | 117.39 MB | 116.7% | 107.3% |
| `lteNRRCC` | 73.74 MB | 102.16 MB | 105.2% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0203s | +0.0207s | worse |
| `f1ap_rel18.6_specs` | 0.1187s | 0.0608s | +0.0579s | worse |
| `ngap_rel18.6_specs` | 0.0592s | 0.0417s | +0.0175s | worse |
| `lteNRRCC` | 0.1079s | 0.0711s | +0.0368s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.61 MB | 4.42 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.53 MB | 4.39 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.38 MB | 99.17 MB | 0.0% | 22.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0410s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1058s | 0.1149s | -0.0091s | improved |
| `ngap_rel18.6_specs` | 0.0733s | 0.0801s | -0.0068s | improved |
| `lteNRRCC` | 0.1380s | 0.1424s | -0.0044s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.49 MB | 90.8% | 163.7% |
| `f1ap_rel18.6_specs` | 8.16 MB | 8.17 MB | 78.9% | 163.7% |
| `ngap_rel18.6_specs` | 8.05 MB | 7.54 MB | 159.5% | 159.6% |
| `lteNRRCC` | 51.83 MB | 48.93 MB | 156.4% | 107.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0358s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1058s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0759s | 0.0736s | +0.0023s | worse |
| `lteNRRCC` | 0.1271s | 0.1142s | +0.0129s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.64 MB | 8.71 MB | 156.1% | 153.8% |
| `f1ap_rel18.6_specs` | 10.00 MB | 164.18 MB | 151.8% | 148.5% |
| `ngap_rel18.6_specs` | 9.13 MB | 9.13 MB | 175.4% | 156.3% |
| `lteNRRCC` | 8.61 MB | 88.82 MB | 154.9% | 169.2% |
<!-- BENCH_RESULTS_END -->
