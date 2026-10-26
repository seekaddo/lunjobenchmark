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
Generated: 2026-10-26T16:41:27.146128+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0347s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1097s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0747s | +0.0030s | worse |
| `lteNRRCC` | 0.1211s | 0.1188s | +0.0023s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 78.3% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0253s | 0.0218s | +0.0035s | worse |
| `f1ap_rel18.6_specs` | 0.0691s | 0.0597s | +0.0094s | worse |
| `ngap_rel18.6_specs` | 0.0489s | 0.0434s | +0.0055s | worse |
| `lteNRRCC` | 0.0853s | 0.0773s | +0.0080s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.53 MB | 36.68 MB | 71.4% | 104.8% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.00 MB | 104.8% | 104.8% |
| `ngap_rel18.6_specs` | 18.15 MB | 74.54 MB | 105.6% | 100.0% |
| `lteNRRCC` | 48.76 MB | 65.20 MB | 100.0% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0329s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.0899s | 0.0890s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0632s | 0.0630s | +0.0002s | worse |
| `lteNRRCC` | 0.1175s | 0.1172s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.59 MB | 55.52 MB | 63.3% | 108.0% |
| `f1ap_rel18.6_specs` | 34.43 MB | 164.13 MB | 103.6% | 103.8% |
| `ngap_rel18.6_specs` | 23.58 MB | 117.59 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.70 MB | 102.63 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0217s | +0.0173s | worse |
| `f1ap_rel18.6_specs` | 0.0870s | 0.0772s | +0.0098s | worse |
| `ngap_rel18.6_specs` | 0.0578s | 0.0487s | +0.0091s | worse |
| `lteNRRCC` | 0.0893s | 0.0774s | +0.0119s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.31 MB | 6.03 MB | 0.0% | 0.4% |
| `f1ap_rel18.6_specs` | 4.05 MB | 5.53 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 6.11 MB | 0.0% | 0.0% |
| `lteNRRCC` | 1.88 MB | 7.67 MB | 0.0% | 1.3% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0324s | 0.0406s | -0.0082s | improved |
| `f1ap_rel18.6_specs` | 0.0905s | 0.1095s | -0.0190s | improved |
| `ngap_rel18.6_specs` | 0.0684s | 0.0784s | -0.0100s | improved |
| `lteNRRCC` | 0.1106s | 0.1397s | -0.0291s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.83 MB | 0.0% | 119.1% |
| `f1ap_rel18.6_specs` | 8.75 MB | 8.75 MB | 140.9% | 143.1% |
| `ngap_rel18.6_specs` | 8.19 MB | 8.19 MB | 139.9% | 138.1% |
| `lteNRRCC` | 51.85 MB | 51.53 MB | 136.7% | 137.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0405s | -0.0052s | improved |
| `f1ap_rel18.6_specs` | 0.1005s | 0.1188s | -0.0183s | improved |
| `ngap_rel18.6_specs` | 0.0723s | 0.0838s | -0.0115s | improved |
| `lteNRRCC` | 0.1120s | 0.1324s | -0.0204s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.54 MB | 9.97 MB | 133.0% | 127.0% |
| `f1ap_rel18.6_specs` | 11.08 MB | 161.23 MB | 135.4% | 137.6% |
| `ngap_rel18.6_specs` | 10.12 MB | 10.11 MB | 97.5% | 97.5% |
| `lteNRRCC` | 9.24 MB | 94.52 MB | 190.9% | 137.1% |
<!-- BENCH_RESULTS_END -->
