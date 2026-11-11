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
Generated: 2026-11-11T17:49:07.132141+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0409s | 0.0401s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1258s | 0.1282s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0873s | 0.0882s | -0.0009s | improved |
| `lteNRRCC` | 0.1296s | 0.1294s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 15.4% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 103.6% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.2% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0285s | 0.0356s | -0.0071s | improved |
| `f1ap_rel18.6_specs` | 0.0934s | 0.1100s | -0.0166s | improved |
| `ngap_rel18.6_specs` | 0.0641s | 0.0750s | -0.0109s | improved |
| `lteNRRCC` | 0.1040s | 0.1191s | -0.0151s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 34.65 MB | 68.2% | 104.5% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 104.2% | 101.8% |
| `ngap_rel18.6_specs` | 18.06 MB | 72.65 MB | 105.3% | 100.0% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.0% | 101.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0530s | 0.0472s | +0.0058s | worse |
| `f1ap_rel18.6_specs` | 0.1655s | 0.1468s | +0.0187s | worse |
| `ngap_rel18.6_specs` | 0.1136s | 0.1025s | +0.0111s | worse |
| `lteNRRCC` | 0.1616s | 0.1439s | +0.0177s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 53.73 MB | 81.5% | 105.4% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.7% | 102.2% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.4% | 102.9% |
| `lteNRRCC` | 72.62 MB | 100.36 MB | 102.7% | 102.2% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0326s | 0.0341s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0923s | 0.0950s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0643s | 0.0662s | -0.0019s | improved |
| `lteNRRCC` | 0.1108s | 0.1129s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.82 MB | 0.0% | 213.5% |
| `f1ap_rel18.6_specs` | 8.56 MB | 106.66 MB | 141.0% | 135.9% |
| `ngap_rel18.6_specs` | 8.19 MB | 8.25 MB | 139.8% | 142.2% |
| `lteNRRCC` | 8.43 MB | 57.40 MB | 136.4% | 139.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0410s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1135s | 0.1127s | +0.0008s | worse |
| `ngap_rel18.6_specs` | 0.0797s | 0.0804s | -0.0007s | improved |
| `lteNRRCC` | 0.1148s | 0.1309s | -0.0161s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.23 MB | 0.0% | 133.7% |
| `f1ap_rel18.6_specs` | 10.78 MB | 148.43 MB | 269.6% | 133.1% |
| `ngap_rel18.6_specs` | 10.32 MB | 10.27 MB | 135.4% | 132.8% |
| `lteNRRCC` | 73.79 MB | 86.53 MB | 135.8% | 133.1% |
<!-- BENCH_RESULTS_END -->
