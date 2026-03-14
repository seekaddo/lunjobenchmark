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
Generated: 2026-03-14T10:37:55.906409+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0390s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1214s | 0.1219s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0825s | 0.0839s | -0.0014s | improved |
| `lteNRRCC` | 0.1250s | 0.1265s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.41 MB | 55.79 MB | 95.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.29 MB | 176.91 MB | 103.4% | 102.9% |
| `ngap_rel18.6_specs` | 22.29 MB | 125.79 MB | 108.7% | 103.9% |
| `lteNRRCC` | 72.33 MB | 100.05 MB | 105.1% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0358s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1008s | 0.0963s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0707s | 0.0701s | +0.0006s | worse |
| `lteNRRCC` | 0.1336s | 0.1273s | +0.0063s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.46 MB | 37.45 MB | 92.6% | 113.3% |
| `f1ap_rel18.6_specs` | 22.38 MB | 111.88 MB | 108.6% | 104.9% |
| `ngap_rel18.6_specs` | 16.66 MB | 80.41 MB | 110.3% | 106.4% |
| `lteNRRCC` | 48.87 MB | 66.42 MB | 104.3% | 105.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0380s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0979s | -0.0040s | improved |
| `ngap_rel18.6_specs` | 0.0666s | 0.0701s | -0.0035s | improved |
| `lteNRRCC` | 0.1165s | 0.1290s | -0.0125s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.31 MB | 57.91 MB | 14.7% | 110.3% |
| `f1ap_rel18.6_specs` | 34.06 MB | 179.24 MB | 109.7% | 105.1% |
| `ngap_rel18.6_specs` | 24.33 MB | 128.00 MB | 111.5% | 106.7% |
| `lteNRRCC` | 75.09 MB | 102.76 MB | 106.8% | 105.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0248s | 0.0241s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0717s | 0.0788s | -0.0071s | improved |
| `ngap_rel18.6_specs` | 0.0443s | 0.0504s | -0.0061s | improved |
| `lteNRRCC` | 0.0770s | 0.0801s | -0.0031s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.11 MB | 3.98 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 1.75 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.69 MB | 4.45 MB | 0.0% | 0.0% |
| `lteNRRCC` | 768 KB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0417s | 0.0432s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1224s | 0.1166s | +0.0058s | worse |
| `ngap_rel18.6_specs` | 0.0806s | 0.0816s | -0.0010s | improved |
| `lteNRRCC` | 0.1440s | 0.1434s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.02 MB | 7.62 MB | 81.4% | 113.8% |
| `f1ap_rel18.6_specs` | 7.98 MB | 7.93 MB | 163.7% | 111.3% |
| `ngap_rel18.6_specs` | 7.32 MB | 7.33 MB | 178.4% | 177.2% |
| `lteNRRCC` | 46.12 MB | 68.45 MB | 105.9% | 106.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0418s | 0.0384s | +0.0034s | worse |
| `f1ap_rel18.6_specs` | 0.1154s | 0.1104s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0764s | +0.0052s | worse |
| `lteNRRCC` | 0.1308s | 0.1266s | +0.0042s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.14 MB | 10.77 MB | 97.3% | 220.9% |
| `f1ap_rel18.6_specs` | 11.43 MB | 11.05 MB | 108.8% | 105.4% |
| `ngap_rel18.6_specs` | 9.09 MB | 8.97 MB | 156.9% | 155.7% |
| `lteNRRCC` | 73.82 MB | 73.73 MB | 154.1% | 108.3% |
<!-- BENCH_RESULTS_END -->
