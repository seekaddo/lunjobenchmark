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
Generated: 2026-06-06T23:10:13.645825+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0356s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1125s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0766s | +0.0023s | worse |
| `lteNRRCC` | 0.1213s | 0.1221s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 7.5% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 116.0% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 105.1% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0336s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.0917s | 0.0912s | +0.0005s | worse |
| `ngap_rel18.6_specs` | 0.0643s | 0.0637s | +0.0006s | worse |
| `lteNRRCC` | 0.1243s | 0.1228s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.58 MB | 85.7% | 110.3% |
| `f1ap_rel18.6_specs` | 22.03 MB | 103.35 MB | 109.1% | 103.4% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.07 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.37 MB | 66.11 MB | 106.5% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0356s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0962s | 0.0935s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0668s | 0.0670s | -0.0002s | improved |
| `lteNRRCC` | 0.1292s | 0.1280s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 55.84 MB | 96.7% | 109.4% |
| `f1ap_rel18.6_specs` | 34.42 MB | 164.66 MB | 108.8% | 105.0% |
| `ngap_rel18.6_specs` | 24.23 MB | 117.89 MB | 111.1% | 106.5% |
| `lteNRRCC` | 74.93 MB | 102.80 MB | 104.7% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0326s | +0.0097s | worse |
| `f1ap_rel18.6_specs` | 0.0707s | 0.0692s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0491s | 0.0468s | +0.0023s | worse |
| `lteNRRCC` | 0.0954s | 0.0779s | +0.0175s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.42 MB | 7.98 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.67 MB | 8.23 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.81 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 7.39 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0397s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1133s | 0.1079s | +0.0054s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0756s | +0.0011s | worse |
| `lteNRRCC` | 0.1404s | 0.1381s | +0.0023s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.35 MB | 7.36 MB | 161.9% | 80.5% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.67 MB | 159.8% | 223.6% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.99 MB | 80.9% | 97.1% |
| `lteNRRCC` | 51.08 MB | 51.39 MB | 160.2% | 159.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0430s | 0.0400s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.1248s | 0.1130s | +0.0118s | worse |
| `ngap_rel18.6_specs` | 0.0876s | 0.0761s | +0.0115s | worse |
| `lteNRRCC` | 0.1404s | 0.1265s | +0.0139s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.00 MB | 8.93 MB | 97.0% | 169.0% |
| `f1ap_rel18.6_specs` | 10.11 MB | 157.79 MB | 159.7% | 168.6% |
| `ngap_rel18.6_specs` | 9.01 MB | 9.20 MB | 83.4% | 83.8% |
| `lteNRRCC` | 67.23 MB | 101.70 MB | 164.2% | 106.9% |
<!-- BENCH_RESULTS_END -->
