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
Generated: 2026-08-07T01:31:30.472711+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0356s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1110s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0760s | +0.0006s | worse |
| `lteNRRCC` | 0.1210s | 0.1202s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 78.3% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0279s | +0.0066s | worse |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0733s | +0.0220s | worse |
| `ngap_rel18.6_specs` | 0.0665s | 0.0510s | +0.0155s | worse |
| `lteNRRCC` | 0.1287s | 0.0974s | +0.0313s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.34 MB | 36.45 MB | 77.8% | 103.7% |
| `f1ap_rel18.6_specs` | 22.07 MB | 103.30 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.34 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.72 MB | 66.48 MB | 101.6% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0362s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.0899s | 0.0964s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0634s | 0.0677s | -0.0043s | improved |
| `lteNRRCC` | 0.1176s | 0.1314s | -0.0138s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.76 MB | 20.2% | 107.4% |
| `f1ap_rel18.6_specs` | 34.55 MB | 163.39 MB | 107.1% | 103.7% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.33 MB | 104.3% | 104.9% |
| `lteNRRCC` | 74.89 MB | 102.18 MB | 103.4% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0323s | 0.0306s | +0.0017s | worse |
| `f1ap_rel18.6_specs` | 0.1017s | 0.0939s | +0.0078s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0587s | +0.0170s | worse |
| `lteNRRCC` | 0.1108s | 0.1193s | -0.0085s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.23 MB | 7.20 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.61 MB | 9.75 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.34 MB | 5.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.62 MB | 4.30 MB | 1.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0393s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1050s | 0.1086s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0735s | 0.0764s | -0.0029s | improved |
| `lteNRRCC` | 0.1369s | 0.1379s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.44 MB | 0.0% | 175.4% |
| `f1ap_rel18.6_specs` | 8.03 MB | 8.11 MB | 81.1% | 165.1% |
| `ngap_rel18.6_specs` | 8.36 MB | 8.30 MB | 186.6% | 186.7% |
| `lteNRRCC` | 45.14 MB | 50.88 MB | 164.2% | 159.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0414s | -0.0037s | improved |
| `f1ap_rel18.6_specs` | 0.1121s | 0.1212s | -0.0091s | improved |
| `ngap_rel18.6_specs` | 0.0774s | 0.0816s | -0.0042s | improved |
| `lteNRRCC` | 0.1288s | 0.1372s | -0.0084s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 8.53 MB | 0.0% | 161.3% |
| `f1ap_rel18.6_specs` | 9.63 MB | 157.12 MB | 164.4% | 162.0% |
| `ngap_rel18.6_specs` | 8.91 MB | 10.52 MB | 81.0% | 233.2% |
| `lteNRRCC` | 9.62 MB | 73.23 MB | 115.2% | 155.2% |
<!-- BENCH_RESULTS_END -->
