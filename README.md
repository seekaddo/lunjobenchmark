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
Generated: 2026-04-30T22:58:49.590436+00:00

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0347s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0920s | 0.0926s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0644s | 0.0649s | -0.0005s | improved |
| `lteNRRCC` | 0.1274s | 0.1248s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.25 MB | 36.67 MB | 92.3% | 107.1% |
| `f1ap_rel18.6_specs` | 21.96 MB | 103.20 MB | 109.4% | 105.2% |
| `ngap_rel18.6_specs` | 16.66 MB | 74.38 MB | 111.1% | 109.3% |
| `lteNRRCC` | 47.97 MB | 66.36 MB | 104.6% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0333s | +0.0046s | worse |
| `f1ap_rel18.6_specs` | 0.0978s | 0.0881s | +0.0097s | worse |
| `ngap_rel18.6_specs` | 0.0687s | 0.0612s | +0.0075s | worse |
| `lteNRRCC` | 0.1311s | 0.1150s | +0.0161s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.80 MB | 89.7% | 110.0% |
| `f1ap_rel18.6_specs` | 34.62 MB | 164.75 MB | 109.1% | 104.9% |
| `ngap_rel18.6_specs` | 24.26 MB | 117.58 MB | 110.7% | 108.3% |
| `lteNRRCC` | 74.93 MB | 102.77 MB | 104.6% | 103.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0196s | 0.0259s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0580s | 0.0680s | -0.0100s | improved |
| `ngap_rel18.6_specs` | 0.0403s | 0.0493s | -0.0090s | improved |
| `lteNRRCC` | 0.0701s | 0.0825s | -0.0124s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.22 MB | 3.78 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.33 MB | 4.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.61 MB | 3.69 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0389s | 0.0433s | -0.0044s | improved |
| `f1ap_rel18.6_specs` | 0.1119s | 0.1210s | -0.0091s | improved |
| `ngap_rel18.6_specs` | 0.0751s | 0.0857s | -0.0106s | improved |
| `lteNRRCC` | 0.1369s | 0.1474s | -0.0105s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.59 MB | 7.53 MB | 81.4% | 77.9% |
| `f1ap_rel18.6_specs` | 8.60 MB | 106.64 MB | 111.0% | 109.4% |
| `ngap_rel18.6_specs` | 8.42 MB | 7.98 MB | 217.7% | 154.4% |
| `lteNRRCC` | 8.34 MB | 70.55 MB | 153.5% | 150.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0403s | 0.0379s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1198s | 0.1054s | +0.0144s | worse |
| `ngap_rel18.6_specs` | 0.0804s | 0.0725s | +0.0079s | worse |
| `lteNRRCC` | 0.1317s | 0.1266s | +0.0051s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.65 MB | 10.90 MB | 154.6% | 201.5% |
| `f1ap_rel18.6_specs` | 1.22 MB | 11.38 MB | 0.0% | 191.3% |
| `ngap_rel18.6_specs` | 9.26 MB | 9.26 MB | 156.8% | 154.2% |
| `lteNRRCC` | 8.68 MB | 98.99 MB | 154.9% | 205.7% |
<!-- BENCH_RESULTS_END -->
