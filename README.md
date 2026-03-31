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
Generated: 2026-03-31T11:03:30.463887+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0374s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1167s | 0.1143s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0807s | 0.0787s | +0.0020s | worse |
| `lteNRRCC` | 0.1241s | 0.1238s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 7.8% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.4% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.7% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 104.9% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0353s | 0.0367s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0966s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0653s | 0.0699s | -0.0046s | improved |
| `lteNRRCC` | 0.1286s | 0.1281s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.15 MB | 36.72 MB | 17.0% | 107.1% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.04 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.73 MB | 74.15 MB | 111.5% | 104.5% |
| `lteNRRCC` | 48.82 MB | 66.21 MB | 103.1% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0360s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0956s | -0.0054s | improved |
| `ngap_rel18.6_specs` | 0.0636s | 0.0668s | -0.0032s | improved |
| `lteNRRCC` | 0.1172s | 0.1293s | -0.0121s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 55.43 MB | 88.9% | 111.1% |
| `f1ap_rel18.6_specs` | 34.01 MB | 163.35 MB | 106.7% | 105.3% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.67 MB | 112.0% | 104.7% |
| `lteNRRCC` | 74.07 MB | 102.61 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0192s | +0.0034s | worse |
| `f1ap_rel18.6_specs` | 0.0682s | 0.0675s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0383s | 0.0457s | -0.0074s | improved |
| `lteNRRCC` | 0.0703s | 0.0853s | -0.0150s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.73 MB | 5.27 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.12 MB | 4.25 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 4.16 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.97 MB | 4.03 MB | 0.0% | 0.0% |
<!-- BENCH_RESULTS_END -->
