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
Generated: 2026-10-17T00:15:20.111167+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0362s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1120s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0768s | -0.0017s | improved |
| `lteNRRCC` | 0.1182s | 0.1198s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 14.4% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 100.0% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0291s | 0.0351s | -0.0060s | improved |
| `f1ap_rel18.6_specs` | 0.0765s | 0.0931s | -0.0166s | improved |
| `ngap_rel18.6_specs` | 0.0530s | 0.0658s | -0.0128s | improved |
| `lteNRRCC` | 0.0999s | 0.1286s | -0.0287s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.76 MB | 36.10 MB | 84.2% | 100.0% |
| `f1ap_rel18.6_specs` | 22.30 MB | 102.30 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 18.18 MB | 73.99 MB | 105.0% | 102.9% |
| `lteNRRCC` | 48.43 MB | 66.19 MB | 102.1% | 103.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0346s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0891s | 0.0906s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0619s | 0.0636s | -0.0017s | improved |
| `lteNRRCC` | 0.1150s | 0.1173s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.31 MB | 79.2% | 108.0% |
| `f1ap_rel18.6_specs` | 35.18 MB | 164.16 MB | 107.4% | 103.8% |
| `ngap_rel18.6_specs` | 24.11 MB | 117.37 MB | 109.1% | 105.0% |
| `lteNRRCC` | 75.01 MB | 102.76 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0421s | 0.0266s | +0.0155s | worse |
| `f1ap_rel18.6_specs` | 0.0729s | 0.0775s | -0.0046s | improved |
| `ngap_rel18.6_specs` | 0.0563s | 0.0520s | +0.0043s | worse |
| `lteNRRCC` | 0.0986s | 0.0961s | +0.0025s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.03 MB | 8.27 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.17 MB | 6.69 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.59 MB | 8.33 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.86 MB | 5.17 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0396s | -0.0054s | improved |
| `f1ap_rel18.6_specs` | 0.0986s | 0.1099s | -0.0113s | improved |
| `ngap_rel18.6_specs` | 0.0728s | 0.0764s | -0.0036s | improved |
| `lteNRRCC` | 0.1173s | 0.1387s | -0.0214s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.30 MB | 7.78 MB | 0.0% | 205.3% |
| `f1ap_rel18.6_specs` | 8.63 MB | 8.75 MB | 142.2% | 96.7% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.20 MB | 202.7% | 138.7% |
| `lteNRRCC` | 8.57 MB | 56.16 MB | 138.4% | 206.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0418s | 0.0394s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1140s | 0.1129s | +0.0011s | worse |
| `ngap_rel18.6_specs` | 0.0823s | 0.0790s | +0.0033s | worse |
| `lteNRRCC` | 0.1286s | 0.1283s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 8.92 MB | 0.0% | 152.6% |
| `f1ap_rel18.6_specs` | 11.62 MB | 10.04 MB | 218.0% | 150.3% |
| `ngap_rel18.6_specs` | 9.32 MB | 11.27 MB | 148.2% | 106.6% |
| `lteNRRCC` | 8.79 MB | 80.62 MB | 151.8% | 106.5% |
<!-- BENCH_RESULTS_END -->
