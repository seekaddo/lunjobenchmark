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
Generated: 2026-03-27T10:56:26.302164+00:00

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0351s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0979s | 0.0922s | +0.0057s | worse |
| `ngap_rel18.6_specs` | 0.0698s | 0.0654s | +0.0044s | worse |
| `lteNRRCC` | 0.1312s | 0.1272s | +0.0040s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.62 MB | 25.3% | 110.3% |
| `f1ap_rel18.6_specs` | 22.29 MB | 103.41 MB | 109.1% | 105.0% |
| `ngap_rel18.6_specs` | 16.66 MB | 74.00 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.70 MB | 66.40 MB | 103.0% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0352s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0887s | 0.1017s | -0.0130s | improved |
| `ngap_rel18.6_specs` | 0.0615s | 0.0711s | -0.0096s | improved |
| `lteNRRCC` | 0.1149s | 0.1229s | -0.0080s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.86 MB | 25.0% | 111.1% |
| `f1ap_rel18.6_specs` | 34.50 MB | 164.43 MB | 106.7% | 105.5% |
| `ngap_rel18.6_specs` | 24.37 MB | 117.29 MB | 116.7% | 107.1% |
| `lteNRRCC` | 74.18 MB | 102.88 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0315s | 0.0203s | +0.0112s | worse |
| `f1ap_rel18.6_specs` | 0.0976s | 0.0687s | +0.0289s | worse |
| `ngap_rel18.6_specs` | 0.0558s | 0.0453s | +0.0105s | worse |
| `lteNRRCC` | 0.1347s | 0.0728s | +0.0619s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 5.97 MB | 7.86 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.77 MB | 8.94 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 9.86 MB | 8.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.19 MB | 5.23 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0429s | -0.0049s | improved |
| `f1ap_rel18.6_specs` | 0.1046s | 0.1117s | -0.0071s | improved |
| `ngap_rel18.6_specs` | 0.0728s | 0.0790s | -0.0062s | improved |
| `lteNRRCC` | 0.1355s | 0.1401s | -0.0046s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.01 MB | 7.75 MB | 83.5% | 117.7% |
| `f1ap_rel18.6_specs` | 8.54 MB | 106.64 MB | 226.8% | 164.5% |
| `ngap_rel18.6_specs` | 7.61 MB | 8.11 MB | 172.0% | 108.9% |
| `lteNRRCC` | 47.81 MB | 70.55 MB | 159.0% | 173.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0372s | +0.0023s | worse |
| `f1ap_rel18.6_specs` | 0.1075s | 0.1092s | -0.0017s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0755s | -0.0012s | improved |
| `lteNRRCC` | 0.1244s | 0.1256s | -0.0012s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.40 MB | 8.58 MB | 108.2% | 159.1% |
| `f1ap_rel18.6_specs` | 11.34 MB | 164.14 MB | 222.0% | 229.0% |
| `ngap_rel18.6_specs` | 10.78 MB | 10.07 MB | 231.9% | 104.2% |
| `lteNRRCC` | 9.73 MB | 91.95 MB | 231.7% | 112.8% |
<!-- BENCH_RESULTS_END -->
