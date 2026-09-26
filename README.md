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
Generated: 2026-09-26T14:17:54.132956+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0405s | -0.0043s | improved |
| `f1ap_rel18.6_specs` | 0.1120s | 0.1229s | -0.0109s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0861s | -0.0090s | improved |
| `lteNRRCC` | 0.1219s | 0.1288s | -0.0069s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 40.8% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0344s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.0970s | 0.0938s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0684s | 0.0665s | +0.0019s | worse |
| `lteNRRCC` | 0.1308s | 0.1278s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 35.85 MB | 77.8% | 107.1% |
| `f1ap_rel18.6_specs` | 21.79 MB | 103.38 MB | 103.1% | 101.8% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.26 MB | 103.8% | 104.7% |
| `lteNRRCC` | 47.87 MB | 65.64 MB | 103.1% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0337s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1023s | 0.0906s | +0.0117s | worse |
| `ngap_rel18.6_specs` | 0.0716s | 0.0639s | +0.0077s | worse |
| `lteNRRCC` | 0.1187s | 0.1166s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.71 MB | 55.83 MB | 77.3% | 103.8% |
| `f1ap_rel18.6_specs` | 35.13 MB | 164.54 MB | 103.7% | 101.7% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.89 MB | 109.5% | 102.3% |
| `lteNRRCC` | 74.11 MB | 102.89 MB | 101.8% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0289s | 0.0349s | -0.0060s | improved |
| `f1ap_rel18.6_specs` | 0.0708s | 0.1089s | -0.0381s | improved |
| `ngap_rel18.6_specs` | 0.0439s | 0.0748s | -0.0309s | improved |
| `lteNRRCC` | 0.0990s | 0.1009s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.33 MB | 4.92 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.72 MB | 10.06 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.80 MB | 7.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.19 MB | 7.34 MB | 0.0% | 0.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0432s | 0.0392s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.1286s | 0.1106s | +0.0180s | worse |
| `ngap_rel18.6_specs` | 0.0880s | 0.0783s | +0.0097s | worse |
| `lteNRRCC` | 0.1343s | 0.1276s | +0.0067s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.01 MB | 10.25 MB | 110.8% | 115.7% |
| `f1ap_rel18.6_specs` | 10.55 MB | 11.23 MB | 113.7% | 222.9% |
| `ngap_rel18.6_specs` | 12.07 MB | 10.60 MB | 181.3% | 115.5% |
| `lteNRRCC` | 8.93 MB | 99.03 MB | 162.7% | 156.7% |
<!-- BENCH_RESULTS_END -->
