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
Generated: 2026-06-13T23:12:52.700595+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0366s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1140s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0780s | 0.0778s | +0.0002s | worse |
| `lteNRRCC` | 0.1203s | 0.1220s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 20.9% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 106.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0334s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0904s | 0.0918s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0633s | 0.0636s | -0.0003s | improved |
| `lteNRRCC` | 0.1223s | 0.1232s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.21 MB | 92.0% | 111.1% |
| `f1ap_rel18.6_specs` | 22.38 MB | 103.16 MB | 109.7% | 105.4% |
| `ngap_rel18.6_specs` | 17.64 MB | 74.39 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.60 MB | 66.03 MB | 104.9% | 104.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0354s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.0884s | 0.0952s | -0.0068s | improved |
| `ngap_rel18.6_specs` | 0.0656s | 0.0650s | +0.0006s | worse |
| `lteNRRCC` | 0.1176s | 0.1268s | -0.0092s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.38 MB | 55.66 MB | 75.0% | 111.1% |
| `f1ap_rel18.6_specs` | 33.88 MB | 164.21 MB | 110.3% | 105.6% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.37 MB | 112.5% | 104.9% |
| `lteNRRCC` | 74.36 MB | 102.11 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0216s | 0.0223s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0805s | 0.0679s | +0.0126s | worse |
| `ngap_rel18.6_specs` | 0.0465s | 0.0465s | +0.0000s | flat |
| `lteNRRCC` | 0.0784s | 0.0816s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.34 MB | 4.48 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.91 MB | 4.98 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.84 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.95 MB | 3.98 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0396s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1081s | 0.1070s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0747s | +0.0020s | worse |
| `lteNRRCC` | 0.1400s | 0.1383s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.44 MB | 7.44 MB | 80.8% | 162.7% |
| `f1ap_rel18.6_specs` | 8.45 MB | 8.19 MB | 101.9% | 103.4% |
| `ngap_rel18.6_specs` | 8.18 MB | 7.62 MB | 226.1% | 90.4% |
| `lteNRRCC` | 51.21 MB | 70.56 MB | 106.5% | 150.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0405s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.1169s | 0.1115s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0802s | 0.0787s | +0.0015s | worse |
| `lteNRRCC` | 0.1347s | 0.1302s | +0.0045s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.00 MB | 8.91 MB | 169.0% | 167.4% |
| `f1ap_rel18.6_specs` | 10.06 MB | 163.56 MB | 83.4% | 107.6% |
| `ngap_rel18.6_specs` | 9.26 MB | 9.26 MB | 165.7% | 83.4% |
| `lteNRRCC` | 65.79 MB | 101.70 MB | 165.3% | 106.7% |
<!-- BENCH_RESULTS_END -->
