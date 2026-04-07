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
Generated: 2026-04-07T11:05:41.788678+00:00

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0352s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0940s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0669s | 0.0660s | +0.0009s | worse |
| `lteNRRCC` | 0.1289s | 0.1276s | +0.0013s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 36.58 MB | 92.3% | 110.7% |
| `f1ap_rel18.6_specs` | 22.18 MB | 103.14 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 16.82 MB | 73.86 MB | 111.1% | 106.8% |
| `lteNRRCC` | 47.62 MB | 66.54 MB | 104.6% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0371s | 0.0339s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0972s | 0.0919s | +0.0053s | worse |
| `ngap_rel18.6_specs` | 0.0678s | 0.0634s | +0.0044s | worse |
| `lteNRRCC` | 0.1296s | 0.1149s | +0.0147s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.36 MB | 92.9% | 113.3% |
| `f1ap_rel18.6_specs` | 35.11 MB | 164.52 MB | 109.1% | 104.9% |
| `ngap_rel18.6_specs` | 24.20 MB | 117.66 MB | 107.1% | 106.4% |
| `lteNRRCC` | 74.18 MB | 102.16 MB | 106.2% | 105.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0203s | 0.0220s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.0608s | 0.0641s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0417s | 0.0478s | -0.0061s | improved |
| `lteNRRCC` | 0.0711s | 0.0759s | -0.0048s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.38 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.77 MB | 5.64 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.70 MB | 4.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0410s | 0.0400s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1149s | 0.1079s | +0.0070s | worse |
| `ngap_rel18.6_specs` | 0.0801s | 0.0758s | +0.0043s | worse |
| `lteNRRCC` | 0.1424s | 0.1373s | +0.0051s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.68 MB | 8.43 MB | 151.3% | 217.8% |
| `f1ap_rel18.6_specs` | 8.41 MB | 8.54 MB | 75.5% | 150.9% |
| `ngap_rel18.6_specs` | 7.46 MB | 8.45 MB | 99.1% | 210.2% |
| `lteNRRCC` | 50.80 MB | 52.25 MB | 146.7% | 108.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0431s | -0.0073s | improved |
| `f1ap_rel18.6_specs` | 0.1058s | 0.1234s | -0.0176s | improved |
| `ngap_rel18.6_specs` | 0.0736s | 0.0876s | -0.0140s | improved |
| `lteNRRCC` | 0.1142s | 0.1329s | -0.0187s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.07 MB | 9.64 MB | 102.3% | 100.8% |
| `f1ap_rel18.6_specs` | 11.69 MB | 154.50 MB | 89.4% | 101.7% |
| `ngap_rel18.6_specs` | 10.43 MB | 11.64 MB | 198.6% | 113.6% |
| `lteNRRCC` | 9.23 MB | 74.13 MB | 98.0% | 116.1% |
<!-- BENCH_RESULTS_END -->
