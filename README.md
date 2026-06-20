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
Generated: 2026-06-20T23:16:18.886677+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0338s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1096s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0748s | 0.0734s | +0.0014s | worse |
| `lteNRRCC` | 0.1192s | 0.1174s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.91 MB | 53.55 MB | 22.2% | 110.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0334s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0938s | 0.0968s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0656s | 0.0683s | -0.0027s | improved |
| `lteNRRCC` | 0.1306s | 0.1182s | +0.0124s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 36.19 MB | 85.2% | 111.1% |
| `f1ap_rel18.6_specs` | 22.43 MB | 103.13 MB | 106.2% | 105.3% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.66 MB | 111.5% | 104.5% |
| `lteNRRCC` | 48.41 MB | 66.48 MB | 103.1% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0346s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.1003s | -0.0056s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0689s | -0.0032s | improved |
| `lteNRRCC` | 0.1280s | 0.1148s | +0.0132s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.40 MB | 55.75 MB | 100.0% | 110.3% |
| `f1ap_rel18.6_specs` | 34.66 MB | 164.67 MB | 109.7% | 105.2% |
| `ngap_rel18.6_specs` | 23.78 MB | 117.34 MB | 111.5% | 106.8% |
| `lteNRRCC` | 74.14 MB | 102.80 MB | 104.7% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0252s | 0.0177s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.0680s | 0.0709s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0479s | 0.0477s | +0.0002s | worse |
| `lteNRRCC` | 0.0816s | 0.0761s | +0.0055s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.67 MB | 4.47 MB | 0.0% | 0.6% |
| `f1ap_rel18.6_specs` | 4.94 MB | 4.55 MB | 0.1% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 5.45 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.92 MB | 4.44 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0298s | +0.0102s | worse |
| `f1ap_rel18.6_specs` | 0.1100s | 0.0826s | +0.0274s | worse |
| `ngap_rel18.6_specs` | 0.0779s | 0.0577s | +0.0202s | worse |
| `lteNRRCC` | 0.1471s | 0.0940s | +0.0531s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.75 MB | 7.82 MB | 102.8% | 127.4% |
| `f1ap_rel18.6_specs` | 8.18 MB | 8.87 MB | 176.2% | 107.0% |
| `ngap_rel18.6_specs` | 7.65 MB | 7.68 MB | 169.8% | 159.5% |
| `lteNRRCC` | 47.83 MB | 51.77 MB | 110.0% | 107.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0428s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.1271s | 0.1244s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0814s | 0.0871s | -0.0057s | improved |
| `lteNRRCC` | 0.1445s | 0.1404s | +0.0041s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.50 MB | 8.94 MB | 219.0% | 166.9% |
| `f1ap_rel18.6_specs` | 10.07 MB | 136.17 MB | 82.6% | 161.3% |
| `ngap_rel18.6_specs` | 9.49 MB | 9.28 MB | 80.4% | 165.3% |
| `lteNRRCC` | 72.54 MB | 101.72 MB | 162.5% | 165.7% |
<!-- BENCH_RESULTS_END -->
