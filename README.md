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
Generated: 2026-08-23T10:30:11.253536+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0343s | 0.0364s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.1081s | 0.1136s | -0.0055s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0777s | -0.0039s | improved |
| `lteNRRCC` | 0.1182s | 0.1221s | -0.0039s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 85.7% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.6% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0319s | 0.0224s | +0.0095s | worse |
| `f1ap_rel18.6_specs` | 0.0939s | 0.0621s | +0.0318s | worse |
| `ngap_rel18.6_specs` | 0.0645s | 0.0436s | +0.0209s | worse |
| `lteNRRCC` | 0.1159s | 0.0779s | +0.0380s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.66 MB | 36.60 MB | 73.9% | 104.2% |
| `f1ap_rel18.6_specs` | 22.27 MB | 103.24 MB | 100.0% | 101.8% |
| `ngap_rel18.6_specs` | 18.00 MB | 74.21 MB | 104.8% | 102.5% |
| `lteNRRCC` | 48.80 MB | 66.49 MB | 101.8% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0366s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.0978s | 0.0925s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0695s | 0.0656s | +0.0039s | worse |
| `lteNRRCC` | 0.1296s | 0.1294s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.70 MB | 91.7% | 106.9% |
| `f1ap_rel18.6_specs` | 34.68 MB | 164.49 MB | 106.5% | 101.7% |
| `ngap_rel18.6_specs` | 24.55 MB | 117.71 MB | 107.7% | 104.4% |
| `lteNRRCC` | 74.61 MB | 102.30 MB | 103.2% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0215s | 0.0177s | +0.0038s | worse |
| `f1ap_rel18.6_specs` | 0.0842s | 0.0698s | +0.0144s | worse |
| `ngap_rel18.6_specs` | 0.0677s | 0.0477s | +0.0200s | worse |
| `lteNRRCC` | 0.0854s | 0.1309s | -0.0455s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.78 MB | 4.36 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.17 MB | 4.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.78 MB | 6.06 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.94 MB | 7.14 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0409s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1083s | 0.1136s | -0.0053s | improved |
| `ngap_rel18.6_specs` | 0.0744s | 0.0787s | -0.0043s | improved |
| `lteNRRCC` | 0.1388s | 0.1429s | -0.0041s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.57 MB | 7.63 MB | 185.3% | 94.8% |
| `f1ap_rel18.6_specs` | 7.98 MB | 8.74 MB | 163.4% | 223.8% |
| `ngap_rel18.6_specs` | 7.74 MB | 7.88 MB | 78.7% | 158.6% |
| `lteNRRCC` | 7.79 MB | 55.77 MB | 161.3% | 108.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0457s | 0.0413s | +0.0044s | worse |
| `f1ap_rel18.6_specs` | 0.1353s | 0.1186s | +0.0167s | worse |
| `ngap_rel18.6_specs` | 0.0912s | 0.0808s | +0.0104s | worse |
| `lteNRRCC` | 0.1437s | 0.1206s | +0.0231s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.54 MB | 9.85 MB | 0.0% | 164.3% |
| `f1ap_rel18.6_specs` | 10.59 MB | 164.18 MB | 148.0% | 161.6% |
| `ngap_rel18.6_specs` | 10.13 MB | 10.51 MB | 151.5% | 147.5% |
| `lteNRRCC` | 73.79 MB | 99.78 MB | 108.2% | 146.4% |
<!-- BENCH_RESULTS_END -->
