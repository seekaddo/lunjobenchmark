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
Generated: 2026-03-14T14:15:52.690878+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0382s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1174s | 0.1214s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0820s | 0.0825s | -0.0005s | improved |
| `lteNRRCC` | 0.1245s | 0.1250s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.42 MB | 55.80 MB | 105.9% | 103.6% |
| `f1ap_rel18.6_specs` | 32.30 MB | 176.92 MB | 107.1% | 102.9% |
| `ngap_rel18.6_specs` | 22.30 MB | 125.80 MB | 109.1% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.06 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0365s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0990s | 0.1008s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0701s | 0.0707s | -0.0006s | improved |
| `lteNRRCC` | 0.1337s | 0.1336s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.75 MB | 37.71 MB | 83.3% | 110.0% |
| `f1ap_rel18.6_specs` | 22.35 MB | 111.42 MB | 111.4% | 104.9% |
| `ngap_rel18.6_specs` | 16.59 MB | 79.91 MB | 110.3% | 104.3% |
| `lteNRRCC` | 48.89 MB | 66.41 MB | 104.3% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0369s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0932s | 0.0939s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0665s | 0.0666s | -0.0001s | improved |
| `lteNRRCC` | 0.1169s | 0.1165s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 56.88 MB | 27.8% | 110.3% |
| `f1ap_rel18.6_specs` | 35.12 MB | 179.28 MB | 109.7% | 105.1% |
| `ngap_rel18.6_specs` | 24.51 MB | 127.94 MB | 115.4% | 106.7% |
| `lteNRRCC` | 74.71 MB | 102.33 MB | 103.3% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0220s | 0.0248s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.0680s | 0.0717s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0472s | 0.0443s | +0.0029s | worse |
| `lteNRRCC` | 0.0746s | 0.0770s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.55 MB | 4.31 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.84 MB | 5.22 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.84 MB | 3.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0417s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1224s | -0.0114s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0806s | -0.0030s | improved |
| `lteNRRCC` | 0.1409s | 0.1440s | -0.0031s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.31 MB | 7.30 MB | 160.0% | 96.0% |
| `f1ap_rel18.6_specs` | 7.93 MB | 113.34 MB | 161.4% | 107.0% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.55 MB | 79.0% | 78.6% |
| `lteNRRCC` | 49.57 MB | 70.62 MB | 156.9% | 108.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0418s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1154s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0762s | 0.0816s | -0.0054s | improved |
| `lteNRRCC` | 0.1249s | 0.1308s | -0.0059s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.05 MB | 8.56 MB | 168.1% | 156.8% |
| `f1ap_rel18.6_specs` | 9.65 MB | 179.21 MB | 161.7% | 105.0% |
| `ngap_rel18.6_specs` | 9.34 MB | 8.90 MB | 95.1% | 159.6% |
| `lteNRRCC` | 73.85 MB | 101.73 MB | 108.2% | 105.5% |
<!-- BENCH_RESULTS_END -->
