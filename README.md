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
Generated: 2026-04-25T22:46:42.740709+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0367s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1113s | 0.1142s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0754s | 0.0800s | -0.0046s | improved |
| `lteNRRCC` | 0.1199s | 0.1238s | -0.0039s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 28.8% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 106.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0323s | 0.0351s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0947s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0646s | 0.0668s | -0.0022s | improved |
| `lteNRRCC` | 0.1244s | 0.1303s | -0.0059s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.36 MB | 36.57 MB | 95.2% | 108.0% |
| `f1ap_rel18.6_specs` | 22.25 MB | 102.61 MB | 103.6% | 103.6% |
| `ngap_rel18.6_specs` | 16.84 MB | 74.71 MB | 109.1% | 104.9% |
| `lteNRRCC` | 48.15 MB | 65.90 MB | 103.6% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0327s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.1046s | 0.0878s | +0.0168s | worse |
| `ngap_rel18.6_specs` | 0.0734s | 0.0618s | +0.0116s | worse |
| `lteNRRCC` | 0.1195s | 0.1142s | +0.0053s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.36 MB | 55.32 MB | 25.3% | 107.4% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.58 MB | 110.7% | 104.9% |
| `ngap_rel18.6_specs` | 24.02 MB | 117.24 MB | 113.6% | 104.4% |
| `lteNRRCC` | 74.89 MB | 102.50 MB | 103.5% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0198s | 0.0252s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.0668s | 0.0632s | +0.0036s | worse |
| `ngap_rel18.6_specs` | 0.0428s | 0.0473s | -0.0045s | improved |
| `lteNRRCC` | 0.0708s | 0.0742s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.36 MB | 4.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.55 MB | 3.81 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.94 MB | 4.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.78 MB | 3.55 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0323s | 0.0448s | -0.0125s | improved |
| `f1ap_rel18.6_specs` | 0.0901s | 0.1213s | -0.0312s | improved |
| `ngap_rel18.6_specs` | 0.0623s | 0.0858s | -0.0235s | improved |
| `lteNRRCC` | 0.1113s | 0.1353s | -0.0240s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.75 MB | 7.56 MB | 142.8% | 214.1% |
| `f1ap_rel18.6_specs` | 8.61 MB | 106.64 MB | 142.4% | 141.7% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.11 MB | 144.6% | 144.0% |
| `lteNRRCC` | 48.00 MB | 48.23 MB | 140.3% | 141.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0401s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.1105s | 0.1137s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0784s | 0.0817s | -0.0033s | improved |
| `lteNRRCC` | 0.1270s | 0.1296s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.65 MB | 8.58 MB | 162.6% | 161.8% |
| `f1ap_rel18.6_specs` | 10.00 MB | 10.58 MB | 79.3% | 113.3% |
| `ngap_rel18.6_specs` | 9.08 MB | 9.02 MB | 79.6% | 159.3% |
| `lteNRRCC` | 8.91 MB | 75.70 MB | 95.7% | 107.5% |
<!-- BENCH_RESULTS_END -->
