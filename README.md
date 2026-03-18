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
Generated: 2026-03-18T11:00:03.525627+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0406s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.1223s | 0.1305s | -0.0082s | improved |
| `ngap_rel18.6_specs` | 0.0836s | 0.0894s | -0.0058s | improved |
| `lteNRRCC` | 0.1224s | 0.1296s | -0.0072s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.53 MB | 55.78 MB | 95.0% | 110.0% |
| `f1ap_rel18.6_specs` | 32.53 MB | 176.91 MB | 106.9% | 102.8% |
| `ngap_rel18.6_specs` | 22.41 MB | 125.78 MB | 108.7% | 103.8% |
| `lteNRRCC` | 72.32 MB | 100.09 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0368s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0967s | 0.0989s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0694s | 0.0695s | -0.0001s | improved |
| `lteNRRCC` | 0.1297s | 0.1309s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.32 MB | 37.20 MB | 27.2% | 110.0% |
| `f1ap_rel18.6_specs` | 22.48 MB | 111.48 MB | 108.8% | 106.7% |
| `ngap_rel18.6_specs` | 16.82 MB | 80.47 MB | 114.3% | 106.5% |
| `lteNRRCC` | 48.46 MB | 65.85 MB | 104.5% | 105.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0349s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0919s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0677s | 0.0653s | +0.0024s | worse |
| `lteNRRCC` | 0.1204s | 0.1150s | +0.0054s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.37 MB | 57.84 MB | 19.0% | 110.3% |
| `f1ap_rel18.6_specs` | 34.22 MB | 179.17 MB | 109.7% | 105.2% |
| `ngap_rel18.6_specs` | 24.11 MB | 127.91 MB | 111.5% | 108.9% |
| `lteNRRCC` | 74.31 MB | 102.62 MB | 105.1% | 105.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0262s | 0.0243s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0890s | 0.0907s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0570s | 0.0540s | +0.0030s | worse |
| `lteNRRCC` | 0.0880s | 0.0913s | -0.0033s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.59 MB | 4.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.42 MB | 2.92 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.05 MB | 3.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.92 MB | 1.53 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0399s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1124s | 0.1106s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0780s | +0.0013s | worse |
| `lteNRRCC` | 0.1352s | 0.1348s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.43 MB | 7.30 MB | 167.8% | 167.6% |
| `f1ap_rel18.6_specs` | 7.60 MB | 115.11 MB | 102.3% | 109.7% |
| `ngap_rel18.6_specs` | 7.60 MB | 7.54 MB | 167.2% | 82.9% |
| `lteNRRCC` | 51.59 MB | 48.48 MB | 166.6% | 109.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0386s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1162s | 0.1107s | +0.0055s | worse |
| `ngap_rel18.6_specs` | 0.0831s | 0.0818s | +0.0013s | worse |
| `lteNRRCC` | 0.1250s | 0.1238s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.69 MB | 10.33 MB | 118.7% | 233.9% |
| `f1ap_rel18.6_specs` | 9.59 MB | 179.18 MB | 82.4% | 187.7% |
| `ngap_rel18.6_specs` | 9.09 MB | 10.26 MB | 97.4% | 117.3% |
| `lteNRRCC` | 9.42 MB | 99.55 MB | 231.7% | 236.7% |
<!-- BENCH_RESULTS_END -->
