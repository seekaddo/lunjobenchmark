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
Generated: 2026-10-30T01:46:53.263269+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0392s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1209s | 0.1234s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0817s | 0.0845s | -0.0028s | improved |
| `lteNRRCC` | 0.1266s | 0.1282s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 18.9% | 103.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 101.9% |
| `lteNRRCC` | 72.41 MB | 100.18 MB | 101.6% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0455s | 0.0491s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.1379s | 0.1478s | -0.0099s | improved |
| `ngap_rel18.6_specs` | 0.0966s | 0.1005s | -0.0039s | improved |
| `lteNRRCC` | 0.1546s | 0.1589s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.57 MB | 34.65 MB | 78.6% | 106.1% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.7% | 102.5% |
| `ngap_rel18.6_specs` | 17.97 MB | 72.65 MB | 103.6% | 101.7% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 102.7% | 101.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0602s | 0.0533s | +0.0069s | worse |
| `f1ap_rel18.6_specs` | 0.1848s | 0.1657s | +0.0191s | worse |
| `ngap_rel18.6_specs` | 0.1277s | 0.1129s | +0.0148s | worse |
| `lteNRRCC` | 0.1819s | 0.1610s | +0.0209s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 53.73 MB | 85.7% | 105.0% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.3% | 101.9% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 106.7% | 101.3% |
| `lteNRRCC` | 72.61 MB | 100.36 MB | 102.4% | 102.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0200s | 0.0305s | -0.0105s | improved |
| `f1ap_rel18.6_specs` | 0.0739s | 0.0721s | +0.0018s | worse |
| `ngap_rel18.6_specs` | 0.0559s | 0.0508s | +0.0051s | worse |
| `lteNRRCC` | 0.0813s | 0.0809s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.25 MB | 4.56 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.52 MB | 5.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.17 MB | 7.86 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.05 MB | 3.95 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0325s | 0.0411s | -0.0086s | improved |
| `f1ap_rel18.6_specs` | 0.0914s | 0.1139s | -0.0225s | improved |
| `ngap_rel18.6_specs` | 0.0674s | 0.0793s | -0.0119s | improved |
| `lteNRRCC` | 0.1119s | 0.1304s | -0.0185s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.19 MB | 7.98 MB | 134.4% | 141.4% |
| `f1ap_rel18.6_specs` | 8.99 MB | 8.87 MB | 106.1% | 206.3% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.56 MB | 124.5% | 249.4% |
| `lteNRRCC` | 8.48 MB | 55.83 MB | 140.3% | 139.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0401s | 0.0423s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1157s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0798s | 0.0844s | -0.0046s | improved |
| `lteNRRCC` | 0.1300s | 0.1518s | -0.0218s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.15 MB | 9.05 MB | 0.0% | 148.3% |
| `f1ap_rel18.6_specs` | 12.23 MB | 164.21 MB | 88.0% | 149.3% |
| `ngap_rel18.6_specs` | 11.47 MB | 9.37 MB | 213.2% | 152.1% |
| `lteNRRCC` | 8.83 MB | 98.76 MB | 146.8% | 151.9% |
<!-- BENCH_RESULTS_END -->
