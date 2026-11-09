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
Generated: 2026-11-09T01:34:06.724486+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0398s | 0.0410s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1226s | 0.1265s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0851s | 0.0863s | -0.0012s | improved |
| `lteNRRCC` | 0.1275s | 0.1288s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.81 MB | 53.55 MB | 76.9% | 106.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 105.7% |
| `lteNRRCC` | 72.37 MB | 100.18 MB | 101.6% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0468s | -0.0090s | improved |
| `f1ap_rel18.6_specs` | 0.1112s | 0.1422s | -0.0310s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0988s | -0.0230s | improved |
| `lteNRRCC` | 0.1212s | 0.1556s | -0.0344s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.85 MB | 34.65 MB | 35.3% | 103.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 103.6% | 103.1% |
| `ngap_rel18.6_specs` | 18.09 MB | 72.65 MB | 100.0% | 102.2% |
| `lteNRRCC` | 46.66 MB | 64.21 MB | 101.8% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0516s | 0.0497s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1553s | 0.1514s | +0.0039s | worse |
| `ngap_rel18.6_specs` | 0.1092s | 0.1054s | +0.0038s | worse |
| `lteNRRCC` | 0.1566s | 0.1476s | +0.0090s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 53.73 MB | 77.8% | 105.9% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 103.0% | 102.3% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 103.7% | 103.0% |
| `lteNRRCC` | 72.66 MB | 100.36 MB | 101.4% | 102.3% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0343s | +0.0064s | worse |
| `f1ap_rel18.6_specs` | 0.1111s | 0.0968s | +0.0143s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0699s | +0.0071s | worse |
| `lteNRRCC` | 0.1244s | 0.1140s | +0.0104s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 8.05 MB | 0.0% | 161.6% |
| `f1ap_rel18.6_specs` | 8.80 MB | 100.00 MB | 157.9% | 110.4% |
| `ngap_rel18.6_specs` | 8.37 MB | 8.50 MB | 159.5% | 81.3% |
| `lteNRRCC` | 50.87 MB | 60.68 MB | 111.8% | 159.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0401s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1110s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0756s | 0.0755s | +0.0001s | worse |
| `lteNRRCC` | 0.1154s | 0.1268s | -0.0114s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.10 MB | 0.0% | 92.4% |
| `f1ap_rel18.6_specs` | 10.59 MB | 164.20 MB | 196.8% | 101.6% |
| `ngap_rel18.6_specs` | 10.45 MB | 10.57 MB | 94.4% | 187.3% |
| `lteNRRCC` | 9.43 MB | 84.71 MB | 184.9% | 256.5% |
<!-- BENCH_RESULTS_END -->
