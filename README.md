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
Generated: 2026-09-02T23:57:41.520470+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0372s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1101s | 0.1126s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0757s | 0.0784s | -0.0027s | improved |
| `lteNRRCC` | 0.1192s | 0.1213s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 19.0% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0354s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.0952s | 0.0932s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0652s | 0.0664s | -0.0012s | improved |
| `lteNRRCC` | 0.1259s | 0.1299s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.54 MB | 72.4% | 106.9% |
| `f1ap_rel18.6_specs` | 22.43 MB | 103.49 MB | 106.5% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.53 MB | 108.0% | 104.8% |
| `lteNRRCC` | 48.70 MB | 65.85 MB | 103.3% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0347s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0904s | +0.0057s | worse |
| `ngap_rel18.6_specs` | 0.0678s | 0.0622s | +0.0056s | worse |
| `lteNRRCC` | 0.1292s | 0.1149s | +0.0143s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.55 MB | 88.0% | 103.4% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.61 MB | 103.2% | 101.7% |
| `ngap_rel18.6_specs` | 24.12 MB | 117.89 MB | 103.8% | 102.3% |
| `lteNRRCC` | 74.47 MB | 102.67 MB | 101.6% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0231s | 0.0355s | -0.0124s | improved |
| `f1ap_rel18.6_specs` | 0.0676s | 0.0992s | -0.0316s | improved |
| `ngap_rel18.6_specs` | 0.0467s | 0.0859s | -0.0392s | improved |
| `lteNRRCC` | 0.0772s | 0.0962s | -0.0190s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.73 MB | 4.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.94 MB | 4.95 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.80 MB | 4.84 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.83 MB | 3.80 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0394s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1065s | 0.1108s | -0.0043s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0751s | -0.0006s | improved |
| `lteNRRCC` | 0.1384s | 0.1385s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.99 MB | 7.33 MB | 110.0% | 92.8% |
| `f1ap_rel18.6_specs` | 8.41 MB | 7.97 MB | 103.2% | 93.9% |
| `ngap_rel18.6_specs` | 8.23 MB | 8.17 MB | 115.0% | 116.2% |
| `lteNRRCC` | 51.83 MB | 60.98 MB | 170.4% | 163.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0432s | 0.0385s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.1162s | 0.1107s | +0.0055s | worse |
| `ngap_rel18.6_specs` | 0.0812s | 0.0771s | +0.0041s | worse |
| `lteNRRCC` | 0.1383s | 0.1240s | +0.0143s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.45 MB | 10.16 MB | 0.0% | 224.0% |
| `f1ap_rel18.6_specs` | 10.10 MB | 164.20 MB | 169.9% | 111.3% |
| `ngap_rel18.6_specs` | 9.41 MB | 9.34 MB | 162.1% | 163.8% |
| `lteNRRCC` | 8.75 MB | 89.71 MB | 163.3% | 163.7% |
<!-- BENCH_RESULTS_END -->
