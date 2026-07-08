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
Generated: 2026-07-08T11:50:38.793566+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0341s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1093s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0750s | 0.0738s | +0.0012s | worse |
| `lteNRRCC` | 0.1202s | 0.1179s | +0.0023s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 20.0% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 104.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.4% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0279s | 0.0351s | -0.0072s | improved |
| `f1ap_rel18.6_specs` | 0.0762s | 0.0920s | -0.0158s | improved |
| `ngap_rel18.6_specs` | 0.0528s | 0.0649s | -0.0121s | improved |
| `lteNRRCC` | 0.0982s | 0.1280s | -0.0298s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.27 MB | 36.43 MB | 83.3% | 113.6% |
| `f1ap_rel18.6_specs` | 22.40 MB | 103.50 MB | 112.0% | 104.3% |
| `ngap_rel18.6_specs` | 19.25 MB | 74.30 MB | 115.0% | 105.9% |
| `lteNRRCC` | 48.68 MB | 65.81 MB | 104.2% | 103.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0279s | +0.0079s | worse |
| `f1ap_rel18.6_specs` | 0.0974s | 0.0751s | +0.0223s | worse |
| `ngap_rel18.6_specs` | 0.0679s | 0.0515s | +0.0164s | worse |
| `lteNRRCC` | 0.1236s | 0.1009s | +0.0227s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.27 MB | 80.0% | 110.3% |
| `f1ap_rel18.6_specs` | 34.73 MB | 163.00 MB | 109.7% | 105.2% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.80 MB | 112.0% | 107.0% |
| `lteNRRCC` | 74.91 MB | 102.16 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0218s | +0.0174s | worse |
| `f1ap_rel18.6_specs` | 0.1085s | 0.0693s | +0.0392s | worse |
| `ngap_rel18.6_specs` | 0.0707s | 0.0465s | +0.0242s | worse |
| `lteNRRCC` | 0.1180s | 0.0770s | +0.0410s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.73 MB | 6.69 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.67 MB | 10.59 MB | 0.7% | 0.0% |
| `ngap_rel18.6_specs` | 928 KB | 5.42 MB | 0.0% | 0.0% |
| `lteNRRCC` | 1.45 MB | 6.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0393s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1090s | 0.1080s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0763s | +0.0004s | worse |
| `lteNRRCC` | 0.1395s | 0.1391s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.68 MB | 7.62 MB | 76.9% | 156.3% |
| `f1ap_rel18.6_specs` | 8.16 MB | 8.38 MB | 155.9% | 99.8% |
| `ngap_rel18.6_specs` | 7.91 MB | 7.98 MB | 154.3% | 77.4% |
| `lteNRRCC` | 51.83 MB | 70.54 MB | 213.3% | 154.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0399s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.1100s | 0.1092s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0774s | -0.0017s | improved |
| `lteNRRCC` | 0.1299s | 0.1290s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.58 MB | 8.72 MB | 153.7% | 155.6% |
| `f1ap_rel18.6_specs` | 9.71 MB | 164.16 MB | 113.6% | 156.8% |
| `ngap_rel18.6_specs` | 9.08 MB | 9.16 MB | 171.1% | 151.0% |
| `lteNRRCC` | 8.62 MB | 92.20 MB | 76.4% | 155.0% |
<!-- BENCH_RESULTS_END -->
