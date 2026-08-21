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
Generated: 2026-08-21T22:30:51.230810+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0330s | +0.0038s | worse |
| `f1ap_rel18.6_specs` | 0.1154s | 0.1071s | +0.0083s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0734s | +0.0059s | worse |
| `lteNRRCC` | 0.1244s | 0.1173s | +0.0071s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.85 MB | 53.55 MB | 82.6% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0274s | +0.0091s | worse |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0789s | +0.0129s | worse |
| `ngap_rel18.6_specs` | 0.0651s | 0.0520s | +0.0131s | worse |
| `lteNRRCC` | 0.1284s | 0.1022s | +0.0262s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 36.21 MB | 17.4% | 103.8% |
| `f1ap_rel18.6_specs` | 22.39 MB | 103.32 MB | 106.5% | 103.6% |
| `ngap_rel18.6_specs` | 17.93 MB | 73.68 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.71 MB | 65.69 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0238s | +0.0125s | worse |
| `f1ap_rel18.6_specs` | 0.0987s | 0.0744s | +0.0243s | worse |
| `ngap_rel18.6_specs` | 0.0663s | 0.0511s | +0.0152s | worse |
| `lteNRRCC` | 0.1207s | 0.0970s | +0.0237s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.55 MB | 55.58 MB | 71.4% | 107.4% |
| `f1ap_rel18.6_specs` | 34.69 MB | 164.69 MB | 103.4% | 101.8% |
| `ngap_rel18.6_specs` | 24.26 MB | 117.79 MB | 108.3% | 104.7% |
| `lteNRRCC` | 74.95 MB | 102.86 MB | 101.7% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0231s | 0.0222s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0672s | 0.0668s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0454s | 0.0452s | +0.0002s | worse |
| `lteNRRCC` | 0.0772s | 0.0753s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.58 MB | 3.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.41 MB | 4.88 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.80 MB | 4.66 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0393s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1065s | 0.1097s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0742s | 0.0758s | -0.0016s | improved |
| `lteNRRCC` | 0.1381s | 0.1371s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.69 MB | 7.50 MB | 111.9% | 159.7% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.11 MB | 161.6% | 161.9% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.68 MB | 160.2% | 81.8% |
| `lteNRRCC` | 51.84 MB | 69.23 MB | 108.1% | 106.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0336s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.1133s | 0.0854s | +0.0279s | worse |
| `ngap_rel18.6_specs` | 0.0800s | 0.0602s | +0.0198s | worse |
| `lteNRRCC` | 0.1313s | 0.0902s | +0.0411s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.60 MB | 8.65 MB | 0.0% | 160.2% |
| `f1ap_rel18.6_specs` | 9.56 MB | 148.18 MB | 158.9% | 162.3% |
| `ngap_rel18.6_specs` | 10.39 MB | 10.06 MB | 220.4% | 108.9% |
| `lteNRRCC` | 72.25 MB | 89.95 MB | 105.4% | 108.8% |
<!-- BENCH_RESULTS_END -->
