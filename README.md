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
Generated: 2026-09-11T14:12:32.595452+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0337s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1092s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0754s | 0.0744s | +0.0010s | worse |
| `lteNRRCC` | 0.1204s | 0.1178s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 81.8% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0358s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0901s | 0.0966s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0679s | -0.0040s | improved |
| `lteNRRCC` | 0.1236s | 0.1298s | -0.0062s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 36.56 MB | 16.8% | 103.7% |
| `f1ap_rel18.6_specs` | 21.94 MB | 103.44 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.61 MB | 108.0% | 104.8% |
| `lteNRRCC` | 48.39 MB | 66.33 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0323s | 0.0349s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0893s | 0.0927s | -0.0034s | improved |
| `ngap_rel18.6_specs` | 0.0617s | 0.0651s | -0.0034s | improved |
| `lteNRRCC` | 0.1146s | 0.1262s | -0.0116s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.36 MB | 55.77 MB | 67.9% | 108.0% |
| `f1ap_rel18.6_specs` | 35.19 MB | 164.52 MB | 103.6% | 103.7% |
| `ngap_rel18.6_specs` | 24.44 MB | 117.56 MB | 108.7% | 102.5% |
| `lteNRRCC` | 74.58 MB | 102.92 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0309s | 0.0170s | +0.0139s | worse |
| `f1ap_rel18.6_specs` | 0.0813s | 0.0657s | +0.0156s | worse |
| `ngap_rel18.6_specs` | 0.0516s | 0.0485s | +0.0031s | worse |
| `lteNRRCC` | 0.0934s | 0.0798s | +0.0136s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.98 MB | 5.66 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.66 MB | 5.56 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.20 MB | 2.89 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.80 MB | 1.11 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0393s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1130s | -0.0045s | improved |
| `ngap_rel18.6_specs` | 0.0780s | 0.0762s | +0.0018s | worse |
| `lteNRRCC` | 0.1376s | 0.1377s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.51 MB | 7.75 MB | 97.2% | 116.8% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.38 MB | 162.8% | 109.3% |
| `ngap_rel18.6_specs` | 7.62 MB | 7.45 MB | 168.9% | 165.4% |
| `lteNRRCC` | 8.48 MB | 68.92 MB | 113.6% | 159.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0346s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.1077s | 0.1025s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0743s | 0.0700s | +0.0043s | worse |
| `lteNRRCC` | 0.1244s | 0.1118s | +0.0126s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.61 MB | 8.93 MB | 102.7% | 96.6% |
| `f1ap_rel18.6_specs` | 9.75 MB | 164.20 MB | 161.8% | 161.5% |
| `ngap_rel18.6_specs` | 9.15 MB | 9.15 MB | 95.9% | 161.5% |
| `lteNRRCC` | 9.24 MB | 79.70 MB | 105.0% | 160.9% |
<!-- BENCH_RESULTS_END -->
