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
Generated: 2026-09-14T00:01:34.540574+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0357s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1102s | 0.1114s | -0.0012s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0783s | -0.0025s | improved |
| `lteNRRCC` | 0.1197s | 0.1231s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 72.0% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0363s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0975s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0675s | 0.0663s | +0.0012s | worse |
| `lteNRRCC` | 0.1307s | 0.1303s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.67 MB | 80.0% | 107.4% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.47 MB | 103.1% | 103.5% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.46 MB | 103.8% | 104.7% |
| `lteNRRCC` | 48.73 MB | 66.49 MB | 103.1% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0291s | 0.0340s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.0882s | 0.0896s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0623s | 0.0647s | -0.0024s | improved |
| `lteNRRCC` | 0.1023s | 0.1173s | -0.0150s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 55.54 MB | 37.2% | 104.3% |
| `f1ap_rel18.6_specs` | 35.20 MB | 164.26 MB | 104.2% | 103.8% |
| `ngap_rel18.6_specs` | 23.49 MB | 117.79 MB | 105.0% | 102.5% |
| `lteNRRCC` | 74.98 MB | 102.29 MB | 101.9% | 101.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0202s | 0.0285s | -0.0083s | improved |
| `f1ap_rel18.6_specs` | 0.0696s | 0.0925s | -0.0229s | improved |
| `ngap_rel18.6_specs` | 0.0453s | 0.0535s | -0.0082s | improved |
| `lteNRRCC` | 0.0772s | 0.0926s | -0.0154s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.11 MB | 8.25 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.97 MB | 9.22 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.41 MB | 8.62 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.56 MB | 4.16 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0331s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0901s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0653s | 0.0626s | +0.0027s | worse |
| `lteNRRCC` | 0.1126s | 0.1111s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 8.39 MB | 123.6% | 198.3% |
| `f1ap_rel18.6_specs` | 8.81 MB | 106.65 MB | 136.4% | 133.0% |
| `ngap_rel18.6_specs` | 8.31 MB | 8.31 MB | 111.4% | 191.7% |
| `lteNRRCC` | 8.55 MB | 50.75 MB | 99.6% | 110.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0372s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1086s | 0.1141s | -0.0055s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0771s | -0.0013s | improved |
| `lteNRRCC` | 0.1271s | 0.1276s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.73 MB | 8.80 MB | 90.0% | 94.4% |
| `f1ap_rel18.6_specs` | 9.57 MB | 10.25 MB | 160.9% | 102.0% |
| `ngap_rel18.6_specs` | 8.78 MB | 8.97 MB | 159.6% | 81.6% |
| `lteNRRCC` | 72.38 MB | 99.03 MB | 159.0% | 159.4% |
<!-- BENCH_RESULTS_END -->
