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
Generated: 2026-11-12T02:47:32.130779+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0424s | 0.0409s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1306s | 0.1258s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0894s | 0.0873s | +0.0021s | worse |
| `lteNRRCC` | 0.1326s | 0.1296s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 61.1% | 106.2% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 101.8% |
| `lteNRRCC` | 72.41 MB | 100.11 MB | 103.2% | 102.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0285s | +0.0081s | worse |
| `f1ap_rel18.6_specs` | 0.1104s | 0.0934s | +0.0170s | worse |
| `ngap_rel18.6_specs` | 0.0758s | 0.0641s | +0.0117s | worse |
| `lteNRRCC` | 0.1193s | 0.1040s | +0.0153s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.81 MB | 34.65 MB | 44.7% | 107.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 103.7% | 101.6% |
| `ngap_rel18.6_specs` | 18.06 MB | 72.65 MB | 104.8% | 102.2% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 101.8% | 102.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0452s | 0.0530s | -0.0078s | improved |
| `f1ap_rel18.6_specs` | 0.1413s | 0.1655s | -0.0242s | improved |
| `ngap_rel18.6_specs` | 0.0988s | 0.1136s | -0.0148s | improved |
| `lteNRRCC` | 0.1369s | 0.1616s | -0.0247s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 53.73 MB | 82.6% | 106.5% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 106.7% | 102.6% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 104.3% | 101.8% |
| `lteNRRCC` | 72.66 MB | 100.36 MB | 101.6% | 101.3% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0326s | 0.0326s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0935s | 0.0923s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0636s | 0.0643s | -0.0007s | improved |
| `lteNRRCC` | 0.1114s | 0.1108s | +0.0006s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.91 MB | 0.0% | 138.9% |
| `f1ap_rel18.6_specs` | 8.80 MB | 8.40 MB | 117.0% | 105.6% |
| `ngap_rel18.6_specs` | 8.31 MB | 8.25 MB | 271.8% | 97.7% |
| `lteNRRCC` | 8.73 MB | 68.49 MB | 116.8% | 140.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0388s | -0.0044s | improved |
| `f1ap_rel18.6_specs` | 0.1005s | 0.1135s | -0.0130s | improved |
| `ngap_rel18.6_specs` | 0.0682s | 0.0797s | -0.0115s | improved |
| `lteNRRCC` | 0.1112s | 0.1148s | -0.0036s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 9.84 MB | 0.0% | 98.5% |
| `f1ap_rel18.6_specs` | 11.21 MB | 164.20 MB | 136.3% | 135.8% |
| `ngap_rel18.6_specs` | 10.11 MB | 10.51 MB | 190.5% | 119.0% |
| `lteNRRCC` | 8.81 MB | 98.96 MB | 101.2% | 106.1% |
<!-- BENCH_RESULTS_END -->
