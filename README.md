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
Generated: 2026-06-10T23:40:45.229849+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0351s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1080s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0759s | +0.0011s | worse |
| `lteNRRCC` | 0.1204s | 0.1171s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.57 MB | 53.55 MB | 21.1% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.3% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 113.0% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0344s | 0.0330s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0928s | 0.0958s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0660s | 0.0666s | -0.0006s | improved |
| `lteNRRCC` | 0.1292s | 0.1172s | +0.0120s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 35.95 MB | 73.3% | 111.1% |
| `f1ap_rel18.6_specs` | 22.02 MB | 102.91 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.60 MB | 107.7% | 107.0% |
| `lteNRRCC` | 48.23 MB | 65.91 MB | 104.7% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0285s | 0.0378s | -0.0093s | improved |
| `f1ap_rel18.6_specs` | 0.0772s | 0.0995s | -0.0223s | improved |
| `ngap_rel18.6_specs` | 0.0533s | 0.0687s | -0.0154s | improved |
| `lteNRRCC` | 0.1020s | 0.1313s | -0.0293s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.38 MB | 55.78 MB | 65.6% | 113.0% |
| `f1ap_rel18.6_specs` | 34.81 MB | 164.32 MB | 112.0% | 105.8% |
| `ngap_rel18.6_specs` | 24.20 MB | 117.58 MB | 109.1% | 105.6% |
| `lteNRRCC` | 74.84 MB | 102.95 MB | 103.9% | 101.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0199s | 0.0279s | -0.0080s | improved |
| `f1ap_rel18.6_specs` | 0.0711s | 0.0902s | -0.0191s | improved |
| `ngap_rel18.6_specs` | 0.0498s | 0.0819s | -0.0321s | improved |
| `lteNRRCC` | 0.0892s | 0.1106s | -0.0214s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.72 MB | 3.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 13.05 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 720 KB | 3.55 MB | 0.0% | 0.0% |
| `lteNRRCC` | 5.05 MB | 5.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0425s | 0.0383s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1042s | +0.0084s | worse |
| `ngap_rel18.6_specs` | 0.0801s | 0.0731s | +0.0070s | worse |
| `lteNRRCC` | 0.1422s | 0.1365s | +0.0057s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.98 MB | 8.05 MB | 152.3% | 95.9% |
| `f1ap_rel18.6_specs` | 8.38 MB | 8.46 MB | 150.4% | 76.4% |
| `ngap_rel18.6_specs` | 8.08 MB | 7.99 MB | 152.5% | 157.7% |
| `lteNRRCC` | 8.48 MB | 51.39 MB | 89.0% | 146.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0440s | -0.0098s | improved |
| `f1ap_rel18.6_specs` | 0.1010s | 0.1282s | -0.0272s | improved |
| `ngap_rel18.6_specs` | 0.0675s | 0.0896s | -0.0221s | improved |
| `lteNRRCC` | 0.1091s | 0.1420s | -0.0329s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.94 MB | 9.08 MB | 0.0% | 213.8% |
| `f1ap_rel18.6_specs` | 10.58 MB | 163.59 MB | 130.8% | 138.2% |
| `ngap_rel18.6_specs` | 10.20 MB | 10.26 MB | 140.5% | 141.4% |
| `lteNRRCC` | 9.37 MB | 85.64 MB | 141.4% | 139.7% |
<!-- BENCH_RESULTS_END -->
