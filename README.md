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
Generated: 2026-04-02T22:40:10.184232+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0360s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1127s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0775s | -0.0006s | improved |
| `lteNRRCC` | 0.1210s | 0.1206s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 28.6% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 106.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0325s | 0.0358s | -0.0033s | improved |
| `f1ap_rel18.6_specs` | 0.0955s | 0.0963s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0675s | 0.0682s | -0.0007s | improved |
| `lteNRRCC` | 0.1195s | 0.1297s | -0.0102s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.36 MB | 36.70 MB | 83.3% | 112.0% |
| `f1ap_rel18.6_specs` | 21.93 MB | 103.22 MB | 107.1% | 105.3% |
| `ngap_rel18.6_specs` | 16.73 MB | 74.59 MB | 113.0% | 104.8% |
| `lteNRRCC` | 48.60 MB | 66.25 MB | 103.5% | 103.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0326s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.0926s | 0.0874s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0655s | 0.0611s | +0.0044s | worse |
| `lteNRRCC` | 0.1177s | 0.1159s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.11 MB | 55.69 MB | 92.3% | 110.3% |
| `f1ap_rel18.6_specs` | 34.76 MB | 164.30 MB | 110.0% | 105.2% |
| `ngap_rel18.6_specs` | 24.51 MB | 117.88 MB | 112.0% | 106.8% |
| `lteNRRCC` | 74.92 MB | 102.43 MB | 105.2% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0208s | 0.0196s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.0640s | 0.0634s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0441s | 0.0427s | +0.0014s | worse |
| `lteNRRCC` | 0.0732s | 0.0769s | -0.0037s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.66 MB | 4.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.80 MB | 4.59 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.92 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.64 MB | 4.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0387s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.1188s | 0.1061s | +0.0127s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0789s | +0.0027s | worse |
| `lteNRRCC` | 0.1360s | 0.1394s | -0.0034s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.80 MB | 7.96 MB | 169.4% | 112.9% |
| `f1ap_rel18.6_specs` | 8.66 MB | 8.84 MB | 155.9% | 131.1% |
| `ngap_rel18.6_specs` | 8.29 MB | 8.35 MB | 95.7% | 97.0% |
| `lteNRRCC` | 8.59 MB | 70.54 MB | 103.1% | 157.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0393s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1112s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0765s | 0.0779s | -0.0014s | improved |
| `lteNRRCC` | 0.1259s | 0.1255s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.46 MB | 8.52 MB | 79.3% | 162.2% |
| `f1ap_rel18.6_specs` | 9.75 MB | 9.48 MB | 163.7% | 163.2% |
| `ngap_rel18.6_specs` | 10.19 MB | 10.19 MB | 212.7% | 109.8% |
| `lteNRRCC` | 8.56 MB | 74.15 MB | 161.8% | 155.6% |
<!-- BENCH_RESULTS_END -->
