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
Generated: 2026-05-21T12:49:52.193919+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0358s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1139s | 0.1116s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0786s | 0.0766s | +0.0020s | worse |
| `lteNRRCC` | 0.1219s | 0.1198s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.89 MB | 53.55 MB | 30.3% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0335s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0926s | 0.0906s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0651s | 0.0637s | +0.0014s | worse |
| `lteNRRCC` | 0.1268s | 0.1229s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.80 MB | 36.67 MB | 84.6% | 110.7% |
| `f1ap_rel18.6_specs` | 21.76 MB | 103.34 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.46 MB | 74.61 MB | 115.4% | 107.0% |
| `lteNRRCC` | 48.84 MB | 66.24 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0370s | -0.0035s | improved |
| `f1ap_rel18.6_specs` | 0.0888s | 0.0983s | -0.0095s | improved |
| `ngap_rel18.6_specs` | 0.0625s | 0.0663s | -0.0038s | improved |
| `lteNRRCC` | 0.1154s | 0.1294s | -0.0140s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 55.57 MB | 79.3% | 111.1% |
| `f1ap_rel18.6_specs` | 34.18 MB | 163.51 MB | 112.9% | 105.5% |
| `ngap_rel18.6_specs` | 24.40 MB | 117.23 MB | 108.0% | 107.1% |
| `lteNRRCC` | 74.65 MB | 102.79 MB | 103.3% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0269s | 0.0291s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0810s | 0.0881s | -0.0071s | improved |
| `ngap_rel18.6_specs` | 0.0507s | 0.0738s | -0.0231s | improved |
| `lteNRRCC` | 0.0839s | 0.0810s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.72 MB | 8.42 MB | 0.0% | 0.7% |
| `f1ap_rel18.6_specs` | 9.11 MB | 4.31 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.61 MB | 5.30 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.69 MB | 3.83 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0329s | 0.0318s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0909s | 0.0886s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0636s | 0.0614s | +0.0022s | worse |
| `lteNRRCC` | 0.1110s | 0.1093s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.62 MB | 8.12 MB | 215.9% | 134.5% |
| `f1ap_rel18.6_specs` | 8.24 MB | 106.64 MB | 214.9% | 138.8% |
| `ngap_rel18.6_specs` | 8.21 MB | 8.31 MB | 0.0% | 139.9% |
| `lteNRRCC` | 51.84 MB | 65.80 MB | 209.6% | 111.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0423s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.1091s | 0.1217s | -0.0126s | improved |
| `ngap_rel18.6_specs` | 0.0764s | 0.0854s | -0.0090s | improved |
| `lteNRRCC` | 0.1292s | 0.1385s | -0.0093s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.89 MB | 8.71 MB | 101.4% | 78.4% |
| `f1ap_rel18.6_specs` | 11.33 MB | 153.59 MB | 224.9% | 157.1% |
| `ngap_rel18.6_specs` | 11.06 MB | 9.01 MB | 108.4% | 156.5% |
| `lteNRRCC` | 73.73 MB | 98.58 MB | 155.3% | 111.0% |
<!-- BENCH_RESULTS_END -->
