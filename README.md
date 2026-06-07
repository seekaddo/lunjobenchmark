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
Generated: 2026-06-07T11:54:33.489994+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0373s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1132s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0761s | 0.0789s | -0.0028s | improved |
| `lteNRRCC` | 0.1196s | 0.1213s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 7.4% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0346s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0991s | 0.0917s | +0.0074s | worse |
| `ngap_rel18.6_specs` | 0.0695s | 0.0643s | +0.0052s | worse |
| `lteNRRCC` | 0.1327s | 0.1243s | +0.0084s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 36.42 MB | 80.6% | 110.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.96 MB | 108.8% | 104.9% |
| `ngap_rel18.6_specs` | 17.66 MB | 74.68 MB | 110.7% | 106.5% |
| `lteNRRCC` | 48.78 MB | 66.35 MB | 104.5% | 105.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0363s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0962s | -0.0031s | improved |
| `ngap_rel18.6_specs` | 0.0648s | 0.0668s | -0.0020s | improved |
| `lteNRRCC` | 0.1273s | 0.1292s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 55.14 MB | 96.2% | 110.3% |
| `f1ap_rel18.6_specs` | 34.72 MB | 164.66 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 23.96 MB | 116.67 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.64 MB | 101.99 MB | 104.7% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0423s | -0.0087s | improved |
| `f1ap_rel18.6_specs` | 0.0684s | 0.0707s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0498s | 0.0491s | +0.0007s | worse |
| `lteNRRCC` | 0.0772s | 0.0954s | -0.0182s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.62 MB | 5.11 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.69 MB | 9.09 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.36 MB | 4.77 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.19 MB | 4.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0322s | 0.0397s | -0.0075s | improved |
| `f1ap_rel18.6_specs` | 0.0944s | 0.1133s | -0.0189s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0767s | -0.0114s | improved |
| `lteNRRCC` | 0.1127s | 0.1404s | -0.0277s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.82 MB | 7.81 MB | 139.3% | 143.2% |
| `f1ap_rel18.6_specs` | 8.46 MB | 8.54 MB | 102.5% | 212.3% |
| `ngap_rel18.6_specs` | 8.24 MB | 7.99 MB | 139.3% | 109.4% |
| `lteNRRCC` | 8.29 MB | 51.84 MB | 209.6% | 104.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0430s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.1072s | 0.1248s | -0.0176s | improved |
| `ngap_rel18.6_specs` | 0.0736s | 0.0876s | -0.0140s | improved |
| `lteNRRCC` | 0.1290s | 0.1404s | -0.0114s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.64 MB | 10.28 MB | 80.7% | 118.6% |
| `f1ap_rel18.6_specs` | 11.16 MB | 163.25 MB | 114.6% | 107.4% |
| `ngap_rel18.6_specs` | 8.89 MB | 9.43 MB | 80.1% | 107.2% |
| `lteNRRCC` | 73.20 MB | 101.68 MB | 157.2% | 108.7% |
<!-- BENCH_RESULTS_END -->
