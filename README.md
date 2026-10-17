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
Generated: 2026-10-17T23:54:54.783601+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0362s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1096s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0727s | 0.0745s | -0.0018s | improved |
| `lteNRRCC` | 0.1169s | 0.1179s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 89.5% | 103.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.5% | 104.3% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0367s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0959s | 0.0929s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0680s | 0.0657s | +0.0023s | worse |
| `lteNRRCC` | 0.1300s | 0.1288s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 36.34 MB | 19.3% | 107.7% |
| `f1ap_rel18.6_specs` | 22.31 MB | 102.50 MB | 106.5% | 103.4% |
| `ngap_rel18.6_specs` | 18.03 MB | 73.79 MB | 108.0% | 104.7% |
| `lteNRRCC` | 47.70 MB | 66.49 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0221s | +0.0164s | worse |
| `f1ap_rel18.6_specs` | 0.0943s | 0.0639s | +0.0304s | worse |
| `ngap_rel18.6_specs` | 0.0636s | 0.0439s | +0.0197s | worse |
| `lteNRRCC` | 0.1181s | 0.0781s | +0.0400s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 55.68 MB | 73.1% | 108.0% |
| `f1ap_rel18.6_specs` | 34.12 MB | 164.60 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 24.13 MB | 117.80 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.95 MB | 102.32 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0263s | 0.0542s | -0.0279s | improved |
| `f1ap_rel18.6_specs` | 0.1172s | 0.0642s | +0.0530s | worse |
| `ngap_rel18.6_specs` | 0.0631s | 0.0529s | +0.0102s | worse |
| `lteNRRCC` | 0.1324s | 0.1020s | +0.0304s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.55 MB | 6.69 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.66 MB | 10.80 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.83 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.25 MB | 7.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0419s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1195s | -0.0049s | improved |
| `ngap_rel18.6_specs` | 0.0808s | 0.0822s | -0.0014s | improved |
| `lteNRRCC` | 0.1413s | 0.1304s | +0.0109s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.14 MB | 7.49 MB | 109.3% | 154.6% |
| `f1ap_rel18.6_specs` | 7.99 MB | 106.60 MB | 80.9% | 218.3% |
| `ngap_rel18.6_specs` | 7.60 MB | 7.94 MB | 78.4% | 78.5% |
| `lteNRRCC` | 8.00 MB | 51.60 MB | 154.6% | 107.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0365s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1059s | 0.1044s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0739s | 0.0766s | -0.0027s | improved |
| `lteNRRCC` | 0.1146s | 0.1138s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.13 MB | 10.25 MB | 0.0% | 138.0% |
| `f1ap_rel18.6_specs` | 11.12 MB | 156.98 MB | 259.6% | 135.5% |
| `ngap_rel18.6_specs` | 9.46 MB | 10.54 MB | 204.9% | 114.6% |
| `lteNRRCC` | 73.72 MB | 87.30 MB | 136.5% | 106.1% |
<!-- BENCH_RESULTS_END -->
