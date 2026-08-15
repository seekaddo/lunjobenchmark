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
Generated: 2026-08-15T10:28:50.604451+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0346s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1134s | 0.1089s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0761s | 0.0745s | +0.0016s | worse |
| `lteNRRCC` | 0.1207s | 0.1181s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 75.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0344s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.0975s | 0.0930s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0691s | 0.0660s | +0.0031s | worse |
| `lteNRRCC` | 0.1337s | 0.1332s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.38 MB | 75.0% | 103.6% |
| `f1ap_rel18.6_specs` | 22.28 MB | 103.31 MB | 103.1% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.65 MB | 103.7% | 104.4% |
| `lteNRRCC` | 48.67 MB | 66.34 MB | 101.5% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0316s | +0.0056s | worse |
| `f1ap_rel18.6_specs` | 0.0907s | 0.0953s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.0645s | 0.0608s | +0.0037s | worse |
| `lteNRRCC` | 0.1171s | 0.0891s | +0.0280s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.51 MB | 74.1% | 107.7% |
| `f1ap_rel18.6_specs` | 34.71 MB | 164.74 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.40 MB | 117.54 MB | 108.7% | 104.9% |
| `lteNRRCC` | 74.24 MB | 102.78 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0312s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.1043s | 0.0860s | +0.0183s | worse |
| `ngap_rel18.6_specs` | 0.0670s | 0.0769s | -0.0099s | improved |
| `lteNRRCC` | 0.1078s | 0.1137s | -0.0059s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.97 MB | 11.06 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 8.50 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.28 MB | 8.48 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.59 MB | 4.50 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0408s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1146s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0773s | 0.0796s | -0.0023s | improved |
| `lteNRRCC` | 0.1410s | 0.1412s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.76 MB | 0.0% | 111.8% |
| `f1ap_rel18.6_specs` | 8.25 MB | 8.38 MB | 112.3% | 161.1% |
| `ngap_rel18.6_specs` | 7.56 MB | 7.56 MB | 80.0% | 173.2% |
| `lteNRRCC` | 51.79 MB | 50.83 MB | 223.1% | 109.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0389s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1268s | 0.1125s | +0.0143s | worse |
| `ngap_rel18.6_specs` | 0.0864s | 0.0753s | +0.0111s | worse |
| `lteNRRCC` | 0.1264s | 0.1273s | -0.0009s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 10.09 MB | 113.8% | 108.0% |
| `f1ap_rel18.6_specs` | 11.02 MB | 122.27 MB | 180.2% | 126.1% |
| `ngap_rel18.6_specs` | 10.26 MB | 10.51 MB | 98.1% | 118.0% |
| `lteNRRCC` | 72.11 MB | 75.95 MB | 253.8% | 127.5% |
<!-- BENCH_RESULTS_END -->
