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
Generated: 2026-08-13T22:50:41.446571+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0359s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.1132s | 0.1105s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0759s | +0.0016s | worse |
| `lteNRRCC` | 0.1206s | 0.1195s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 75.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0263s | 0.0347s | -0.0084s | improved |
| `f1ap_rel18.6_specs` | 0.0727s | 0.0949s | -0.0222s | improved |
| `ngap_rel18.6_specs` | 0.0509s | 0.0663s | -0.0154s | improved |
| `lteNRRCC` | 0.0961s | 0.1259s | -0.0298s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.11 MB | 36.30 MB | 86.4% | 104.8% |
| `f1ap_rel18.6_specs` | 21.79 MB | 103.05 MB | 100.0% | 102.3% |
| `ngap_rel18.6_specs` | 19.11 MB | 74.49 MB | 109.5% | 103.0% |
| `lteNRRCC` | 48.01 MB | 66.04 MB | 102.1% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0334s | 0.0343s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.0896s | 0.0904s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0636s | 0.0629s | +0.0007s | worse |
| `lteNRRCC` | 0.1171s | 0.1166s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.79 MB | 76.9% | 103.8% |
| `f1ap_rel18.6_specs` | 35.19 MB | 164.48 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 22.59 MB | 117.75 MB | 104.2% | 105.0% |
| `lteNRRCC` | 74.75 MB | 102.95 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0283s | 0.0251s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0824s | 0.0865s | -0.0041s | improved |
| `ngap_rel18.6_specs` | 0.0566s | 0.0592s | -0.0026s | improved |
| `lteNRRCC` | 0.1003s | 0.0970s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.91 MB | 4.06 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.33 MB | 2.72 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 6.70 MB | 9.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.05 MB | 6.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0395s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1097s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.0777s | 0.0771s | +0.0006s | worse |
| `lteNRRCC` | 0.1375s | 0.1401s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 7.36 MB | 0.0% | 160.2% |
| `f1ap_rel18.6_specs` | 8.02 MB | 8.12 MB | 96.3% | 164.3% |
| `ngap_rel18.6_specs` | 8.13 MB | 8.31 MB | 100.8% | 98.5% |
| `lteNRRCC` | 8.24 MB | 60.50 MB | 79.9% | 106.5% |
<!-- BENCH_RESULTS_END -->
