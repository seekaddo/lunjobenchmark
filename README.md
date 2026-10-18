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
Generated: 2026-10-18T13:53:11.840061+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0339s | +0.0048s | worse |
| `f1ap_rel18.6_specs` | 0.1188s | 0.1062s | +0.0126s | worse |
| `ngap_rel18.6_specs` | 0.0815s | 0.0727s | +0.0088s | worse |
| `lteNRRCC` | 0.1257s | 0.1169s | +0.0088s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 74.1% | 103.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 103.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0361s | -0.0027s | improved |
| `f1ap_rel18.6_specs` | 0.0965s | 0.0959s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0657s | 0.0680s | -0.0023s | improved |
| `lteNRRCC` | 0.1178s | 0.1300s | -0.0122s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 36.14 MB | 80.0% | 104.2% |
| `f1ap_rel18.6_specs` | 22.20 MB | 102.63 MB | 103.8% | 101.8% |
| `ngap_rel18.6_specs` | 17.97 MB | 74.57 MB | 109.5% | 102.5% |
| `lteNRRCC` | 47.88 MB | 65.39 MB | 101.8% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0385s | -0.0058s | improved |
| `f1ap_rel18.6_specs` | 0.0885s | 0.0943s | -0.0058s | improved |
| `ngap_rel18.6_specs` | 0.0617s | 0.0636s | -0.0019s | improved |
| `lteNRRCC` | 0.1157s | 0.1181s | -0.0024s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.69 MB | 76.9% | 108.0% |
| `f1ap_rel18.6_specs` | 34.18 MB | 163.81 MB | 103.6% | 103.8% |
| `ngap_rel18.6_specs` | 24.42 MB | 117.49 MB | 104.5% | 100.0% |
| `lteNRRCC` | 74.57 MB | 102.58 MB | 103.6% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0291s | 0.0263s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.0764s | 0.1172s | -0.0408s | improved |
| `ngap_rel18.6_specs` | 0.0534s | 0.0631s | -0.0097s | improved |
| `lteNRRCC` | 0.0960s | 0.1324s | -0.0364s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.75 MB | 4.16 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.36 MB | 4.95 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.28 MB | 5.59 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.19 MB | 4.91 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0405s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1148s | 0.1146s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0808s | -0.0042s | improved |
| `lteNRRCC` | 0.1405s | 0.1413s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.52 MB | 7.46 MB | 0.0% | 157.8% |
| `f1ap_rel18.6_specs` | 8.34 MB | 8.13 MB | 155.8% | 162.6% |
| `ngap_rel18.6_specs` | 7.85 MB | 7.95 MB | 154.7% | 170.8% |
| `lteNRRCC` | 51.80 MB | 56.41 MB | 167.1% | 103.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0374s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1059s | +0.0073s | worse |
| `ngap_rel18.6_specs` | 0.0790s | 0.0739s | +0.0051s | worse |
| `lteNRRCC` | 0.1300s | 0.1146s | +0.0154s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.13 MB | 10.19 MB | 0.0% | 113.8% |
| `f1ap_rel18.6_specs` | 10.34 MB | 10.91 MB | 102.2% | 230.3% |
| `ngap_rel18.6_specs` | 9.05 MB | 10.21 MB | 158.4% | 110.2% |
| `lteNRRCC` | 9.46 MB | 99.05 MB | 223.6% | 228.6% |
<!-- BENCH_RESULTS_END -->
