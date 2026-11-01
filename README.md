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
Generated: 2026-11-01T16:42:37.281685+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0397s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1275s | 0.1220s | +0.0055s | worse |
| `ngap_rel18.6_specs` | 0.0871s | 0.0842s | +0.0029s | worse |
| `lteNRRCC` | 0.1306s | 0.1271s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.92 MB | 53.55 MB | 74.1% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.1% | 102.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 101.8% |
| `lteNRRCC` | 72.35 MB | 100.18 MB | 101.6% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0297s | 0.0301s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0977s | -0.0024s | improved |
| `ngap_rel18.6_specs` | 0.0659s | 0.0662s | -0.0003s | improved |
| `lteNRRCC` | 0.0957s | 0.1113s | -0.0156s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.69 MB | 34.65 MB | 69.6% | 104.3% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 104.3% | 101.7% |
| `ngap_rel18.6_specs` | 18.09 MB | 72.65 MB | 105.3% | 105.1% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 100.0% | 101.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0476s | 0.0557s | -0.0081s | improved |
| `f1ap_rel18.6_specs` | 0.1465s | 0.1709s | -0.0244s | improved |
| `ngap_rel18.6_specs` | 0.1023s | 0.1173s | -0.0150s | improved |
| `lteNRRCC` | 0.1470s | 0.1665s | -0.0195s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.69 MB | 53.73 MB | 72.0% | 103.0% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 106.7% | 102.4% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 104.3% | 103.4% |
| `lteNRRCC` | 72.64 MB | 100.36 MB | 101.6% | 101.2% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0457s | -0.0057s | improved |
| `f1ap_rel18.6_specs` | 0.1226s | 0.1224s | +0.0002s | worse |
| `ngap_rel18.6_specs` | 0.0825s | 0.0881s | -0.0056s | improved |
| `lteNRRCC` | 0.1444s | 0.1395s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.23 MB | 7.99 MB | 0.0% | 109.3% |
| `f1ap_rel18.6_specs` | 8.20 MB | 8.82 MB | 96.6% | 113.8% |
| `ngap_rel18.6_specs` | 7.06 MB | 7.06 MB | 101.7% | 112.7% |
| `lteNRRCC` | 46.90 MB | 69.50 MB | 105.9% | 195.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0450s | 0.0452s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1257s | 0.1356s | -0.0099s | improved |
| `ngap_rel18.6_specs` | 0.0869s | 0.0942s | -0.0073s | improved |
| `lteNRRCC` | 0.1362s | 0.1384s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.73 MB | 0.0% | 94.9% |
| `f1ap_rel18.6_specs` | 11.77 MB | 10.06 MB | 99.3% | 160.5% |
| `ngap_rel18.6_specs` | 9.09 MB | 10.32 MB | 155.5% | 218.5% |
| `lteNRRCC` | 8.81 MB | 98.59 MB | 162.4% | 107.1% |
<!-- BENCH_RESULTS_END -->
