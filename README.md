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
Generated: 2026-11-12T18:02:33.634845+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0424s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.1237s | 0.1306s | -0.0069s | improved |
| `ngap_rel18.6_specs` | 0.0854s | 0.0894s | -0.0040s | improved |
| `lteNRRCC` | 0.1288s | 0.1326s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.75 MB | 53.55 MB | 77.8% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.0% | 103.7% |
| `lteNRRCC` | 72.37 MB | 100.18 MB | 103.2% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0292s | 0.0366s | -0.0074s | improved |
| `f1ap_rel18.6_specs` | 0.0976s | 0.1104s | -0.0128s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0758s | -0.0097s | improved |
| `lteNRRCC` | 0.1007s | 0.1193s | -0.0186s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.04 MB | 34.65 MB | 20.4% | 107.4% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 106.7% | 103.2% |
| `ngap_rel18.6_specs` | 18.18 MB | 72.65 MB | 104.0% | 104.3% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 103.8% | 103.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0611s | 0.0452s | +0.0159s | worse |
| `f1ap_rel18.6_specs` | 0.1773s | 0.1413s | +0.0360s | worse |
| `ngap_rel18.6_specs` | 0.1245s | 0.0988s | +0.0257s | worse |
| `lteNRRCC` | 0.1694s | 0.1369s | +0.0325s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 53.73 MB | 89.3% | 104.8% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 108.1% | 102.0% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 110.3% | 101.3% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 102.6% | 102.1% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0326s | +0.0076s | worse |
| `f1ap_rel18.6_specs` | 0.1168s | 0.0935s | +0.0233s | worse |
| `ngap_rel18.6_specs` | 0.0810s | 0.0636s | +0.0174s | worse |
| `lteNRRCC` | 0.1400s | 0.1114s | +0.0286s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 7.64 MB | 0.0% | 175.7% |
| `f1ap_rel18.6_specs` | 8.25 MB | 106.66 MB | 159.7% | 154.5% |
| `ngap_rel18.6_specs` | 7.63 MB | 8.12 MB | 159.6% | 90.9% |
| `lteNRRCC` | 8.06 MB | 70.56 MB | 94.5% | 106.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0344s | +0.0075s | worse |
| `f1ap_rel18.6_specs` | 0.1192s | 0.1005s | +0.0187s | worse |
| `ngap_rel18.6_specs` | 0.0822s | 0.0682s | +0.0140s | worse |
| `lteNRRCC` | 0.1368s | 0.1112s | +0.0256s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.95 MB | 0.0% | 81.9% |
| `f1ap_rel18.6_specs` | 10.06 MB | 10.19 MB | 82.3% | 163.8% |
| `ngap_rel18.6_specs` | 9.18 MB | 9.34 MB | 162.1% | 161.8% |
| `lteNRRCC` | 8.69 MB | 74.40 MB | 194.4% | 169.2% |
<!-- BENCH_RESULTS_END -->
