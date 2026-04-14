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
Generated: 2026-04-14T11:11:04.899370+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0359s | +0.0044s | worse |
| `f1ap_rel18.6_specs` | 0.1239s | 0.1108s | +0.0131s | worse |
| `ngap_rel18.6_specs` | 0.0865s | 0.0783s | +0.0082s | worse |
| `lteNRRCC` | 0.1287s | 0.1200s | +0.0087s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 31.6% | 108.8% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 112.1% | 103.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 110.7% | 105.3% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.8% | 103.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0348s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0959s | 0.0926s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0685s | 0.0649s | +0.0036s | worse |
| `lteNRRCC` | 0.1316s | 0.1286s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.18 MB | 36.71 MB | 92.3% | 106.9% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.44 MB | 106.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.80 MB | 74.28 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.59 MB | 66.07 MB | 106.2% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0318s | 0.0342s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.0864s | 0.0908s | -0.0044s | improved |
| `ngap_rel18.6_specs` | 0.0596s | 0.0652s | -0.0056s | improved |
| `lteNRRCC` | 0.1142s | 0.1174s | -0.0032s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.81 MB | 91.7% | 115.4% |
| `f1ap_rel18.6_specs` | 35.19 MB | 164.78 MB | 110.3% | 103.7% |
| `ngap_rel18.6_specs` | 24.53 MB | 117.76 MB | 108.3% | 107.5% |
| `lteNRRCC` | 74.93 MB | 102.86 MB | 103.5% | 104.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0202s | 0.0238s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.0641s | 0.0674s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0505s | 0.0523s | -0.0018s | improved |
| `lteNRRCC` | 0.0792s | 0.0778s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.77 MB | 2.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.70 MB | 4.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.00 MB | 5.91 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.11 MB | 4.12 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0413s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1171s | -0.0065s | improved |
| `ngap_rel18.6_specs` | 0.0774s | 0.0815s | -0.0041s | improved |
| `lteNRRCC` | 0.1403s | 0.1423s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.52 MB | 7.49 MB | 80.1% | 92.6% |
| `f1ap_rel18.6_specs` | 8.79 MB | 8.36 MB | 220.4% | 161.0% |
| `ngap_rel18.6_specs` | 7.60 MB | 7.66 MB | 160.7% | 244.3% |
| `lteNRRCC` | 51.82 MB | 70.54 MB | 159.2% | 111.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0425s | 0.0392s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.1191s | 0.1203s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0836s | 0.0864s | -0.0028s | improved |
| `lteNRRCC` | 0.1347s | 0.1258s | +0.0089s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.54 MB | 9.07 MB | 102.5% | 152.9% |
| `f1ap_rel18.6_specs` | 10.11 MB | 164.18 MB | 165.9% | 111.8% |
| `ngap_rel18.6_specs` | 12.92 MB | 9.39 MB | 86.0% | 90.4% |
| `lteNRRCC` | 8.74 MB | 97.88 MB | 152.1% | 153.0% |
<!-- BENCH_RESULTS_END -->
