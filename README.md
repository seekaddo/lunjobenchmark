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
Generated: 2026-10-27T15:48:37.765409+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0355s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1104s | 0.1120s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0766s | -0.0016s | improved |
| `lteNRRCC` | 0.1214s | 0.1210s | +0.0004s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 81.8% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0248s | 0.0352s | -0.0104s | improved |
| `f1ap_rel18.6_specs` | 0.0673s | 0.0945s | -0.0272s | improved |
| `ngap_rel18.6_specs` | 0.0466s | 0.0673s | -0.0207s | improved |
| `lteNRRCC` | 0.0808s | 0.1307s | -0.0499s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 36.03 MB | 71.4% | 104.5% |
| `f1ap_rel18.6_specs` | 22.24 MB | 103.31 MB | 104.8% | 102.4% |
| `ngap_rel18.6_specs` | 18.20 MB | 74.30 MB | 105.9% | 103.2% |
| `lteNRRCC` | 48.59 MB | 65.85 MB | 102.6% | 102.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0326s | 0.0362s | -0.0036s | improved |
| `f1ap_rel18.6_specs` | 0.0893s | 0.0961s | -0.0068s | improved |
| `ngap_rel18.6_specs` | 0.0629s | 0.0659s | -0.0030s | improved |
| `lteNRRCC` | 0.1160s | 0.1283s | -0.0123s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.61 MB | 55.77 MB | 81.8% | 103.8% |
| `f1ap_rel18.6_specs` | 35.12 MB | 164.48 MB | 103.6% | 103.8% |
| `ngap_rel18.6_specs` | 23.91 MB | 117.46 MB | 109.1% | 102.5% |
| `lteNRRCC` | 74.38 MB | 102.73 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0212s | +0.0145s | worse |
| `f1ap_rel18.6_specs` | 0.1213s | 0.0699s | +0.0514s | worse |
| `ngap_rel18.6_specs` | 0.0936s | 0.0534s | +0.0402s | worse |
| `lteNRRCC` | 0.1267s | 0.0755s | +0.0512s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.23 MB | 7.70 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.88 MB | 163.62 MB | 0.0% | 34.7% |
| `ngap_rel18.6_specs` | 7.34 MB | 4.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.05 MB | 6.94 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0434s | -0.0104s | improved |
| `f1ap_rel18.6_specs` | 0.0928s | 0.1126s | -0.0198s | improved |
| `ngap_rel18.6_specs` | 0.0669s | 0.0796s | -0.0127s | improved |
| `lteNRRCC` | 0.1120s | 0.1416s | -0.0296s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.77 MB | 7.91 MB | 131.9% | 134.2% |
| `f1ap_rel18.6_specs` | 9.06 MB | 106.66 MB | 136.3% | 276.0% |
| `ngap_rel18.6_specs` | 8.32 MB | 8.32 MB | 100.1% | 200.8% |
| `lteNRRCC` | 8.49 MB | 68.88 MB | 99.2% | 128.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0318s | 0.0381s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.0857s | 0.1092s | -0.0235s | improved |
| `ngap_rel18.6_specs` | 0.0604s | 0.0746s | -0.0142s | improved |
| `lteNRRCC` | 0.0905s | 0.1290s | -0.0385s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.55 MB | 55.63 MB | 0.0% | 107.3% |
| `f1ap_rel18.6_specs` | 19.58 MB | 18.58 MB | 94.9% | 158.5% |
| `ngap_rel18.6_specs` | 20.97 MB | 11.15 MB | 168.5% | 148.9% |
| `lteNRRCC` | 11.83 MB | 101.73 MB | 96.0% | 123.8% |
<!-- BENCH_RESULTS_END -->
