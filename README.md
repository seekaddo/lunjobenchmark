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
Generated: 2026-11-09T20:35:45.286898+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0398s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1204s | 0.1226s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0835s | 0.0851s | -0.0016s | improved |
| `lteNRRCC` | 0.1272s | 0.1275s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 19.6% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 103.8% |
| `lteNRRCC` | 72.35 MB | 100.18 MB | 103.3% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0378s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1084s | 0.1112s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0758s | -0.0013s | improved |
| `lteNRRCC` | 0.1176s | 0.1212s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.85 MB | 34.65 MB | 68.0% | 103.8% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 103.7% | 101.6% |
| `ngap_rel18.6_specs` | 18.09 MB | 72.65 MB | 109.5% | 104.3% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 101.8% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0549s | 0.0516s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.1689s | 0.1553s | +0.0136s | worse |
| `ngap_rel18.6_specs` | 0.1157s | 0.1092s | +0.0065s | worse |
| `lteNRRCC` | 0.1631s | 0.1566s | +0.0065s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.60 MB | 53.73 MB | 21.7% | 105.3% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.7% | 101.0% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.1% | 102.9% |
| `lteNRRCC` | 72.61 MB | 100.36 MB | 102.7% | 102.2% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0407s | -0.0066s | improved |
| `f1ap_rel18.6_specs` | 0.0935s | 0.1111s | -0.0176s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0770s | -0.0112s | improved |
| `lteNRRCC` | 0.1127s | 0.1244s | -0.0117s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.98 MB | 0.0% | 136.6% |
| `f1ap_rel18.6_specs` | 8.93 MB | 9.13 MB | 113.2% | 97.8% |
| `ngap_rel18.6_specs` | 8.31 MB | 8.37 MB | 99.2% | 100.7% |
| `lteNRRCC` | 8.55 MB | 65.05 MB | 198.5% | 110.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0385s | -0.0028s | improved |
| `f1ap_rel18.6_specs` | 0.1017s | 0.1062s | -0.0045s | improved |
| `ngap_rel18.6_specs` | 0.0694s | 0.0756s | -0.0062s | improved |
| `lteNRRCC` | 0.1120s | 0.1154s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.95 MB | 0.0% | 97.8% |
| `f1ap_rel18.6_specs` | 10.38 MB | 164.20 MB | 200.1% | 110.8% |
| `ngap_rel18.6_specs` | 10.89 MB | 10.05 MB | 129.4% | 100.4% |
| `lteNRRCC` | 9.38 MB | 97.15 MB | 126.6% | 110.6% |
<!-- BENCH_RESULTS_END -->
