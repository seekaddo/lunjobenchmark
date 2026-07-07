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
Generated: 2026-07-07T12:30:47.420592+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0362s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1102s | 0.1195s | -0.0093s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0768s | -0.0013s | improved |
| `lteNRRCC` | 0.1180s | 0.1206s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.60 MB | 53.55 MB | 20.4% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0277s | 0.0347s | -0.0070s | improved |
| `f1ap_rel18.6_specs` | 0.0752s | 0.0926s | -0.0174s | improved |
| `ngap_rel18.6_specs` | 0.0538s | 0.0720s | -0.0182s | improved |
| `lteNRRCC` | 0.0984s | 0.1292s | -0.0308s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.23 MB | 36.25 MB | 12.8% | 108.7% |
| `f1ap_rel18.6_specs` | 22.37 MB | 103.15 MB | 107.1% | 104.3% |
| `ngap_rel18.6_specs` | 19.20 MB | 73.84 MB | 109.5% | 105.7% |
| `lteNRRCC` | 48.71 MB | 66.17 MB | 106.1% | 105.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0346s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1043s | 0.0938s | +0.0105s | worse |
| `ngap_rel18.6_specs` | 0.0721s | 0.0646s | +0.0075s | worse |
| `lteNRRCC` | 0.1204s | 0.1257s | -0.0053s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 55.10 MB | 76.0% | 107.4% |
| `f1ap_rel18.6_specs` | 35.17 MB | 164.21 MB | 107.1% | 103.2% |
| `ngap_rel18.6_specs` | 23.80 MB | 117.49 MB | 108.7% | 104.3% |
| `lteNRRCC` | 74.41 MB | 101.99 MB | 105.3% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0240s | 0.0206s | +0.0034s | worse |
| `f1ap_rel18.6_specs` | 0.0730s | 0.0704s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0614s | 0.0485s | +0.0129s | worse |
| `lteNRRCC` | 0.0817s | 0.0774s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.42 MB | 8.30 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.30 MB | 12.64 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.52 MB | 8.48 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.48 MB | 7.58 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0410s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1158s | 0.1118s | +0.0040s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0770s | +0.0033s | worse |
| `lteNRRCC` | 0.1413s | 0.1414s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.62 MB | 7.56 MB | 169.8% | 167.7% |
| `f1ap_rel18.6_specs` | 8.45 MB | 8.44 MB | 106.0% | 84.6% |
| `ngap_rel18.6_specs` | 7.88 MB | 8.07 MB | 166.9% | 166.7% |
| `lteNRRCC` | 48.70 MB | 69.98 MB | 165.0% | 167.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0407s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1124s | 0.1206s | -0.0082s | improved |
| `ngap_rel18.6_specs` | 0.0779s | 0.0839s | -0.0060s | improved |
| `lteNRRCC` | 0.1283s | 0.1389s | -0.0106s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.59 MB | 8.33 MB | 158.6% | 81.6% |
| `f1ap_rel18.6_specs` | 9.68 MB | 164.19 MB | 157.6% | 159.3% |
| `ngap_rel18.6_specs` | 10.38 MB | 9.02 MB | 110.2% | 159.1% |
| `lteNRRCC` | 68.86 MB | 78.39 MB | 108.2% | 108.2% |
<!-- BENCH_RESULTS_END -->
