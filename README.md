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
Generated: 2026-09-21T16:22:10.839425+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0335s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1115s | 0.1085s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0755s | 0.0748s | +0.0007s | worse |
| `lteNRRCC` | 0.1221s | 0.1174s | +0.0047s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.86 MB | 53.55 MB | 72.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0243s | +0.0129s | worse |
| `f1ap_rel18.6_specs` | 0.0998s | 0.0737s | +0.0261s | worse |
| `ngap_rel18.6_specs` | 0.0698s | 0.0508s | +0.0190s | worse |
| `lteNRRCC` | 0.1336s | 0.0877s | +0.0459s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.56 MB | 36.64 MB | 14.3% | 107.1% |
| `f1ap_rel18.6_specs` | 22.21 MB | 103.33 MB | 106.2% | 101.7% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.62 MB | 107.7% | 104.4% |
| `lteNRRCC` | 48.80 MB | 66.42 MB | 103.1% | 102.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0270s | 0.0346s | -0.0076s | improved |
| `f1ap_rel18.6_specs` | 0.0875s | 0.0957s | -0.0082s | improved |
| `ngap_rel18.6_specs` | 0.0614s | 0.0643s | -0.0029s | improved |
| `lteNRRCC` | 0.1056s | 0.1192s | -0.0136s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.86 MB | 55.57 MB | 71.4% | 104.8% |
| `f1ap_rel18.6_specs` | 35.21 MB | 164.77 MB | 104.2% | 101.9% |
| `ngap_rel18.6_specs` | 24.39 MB | 117.68 MB | 105.0% | 100.0% |
| `lteNRRCC` | 74.87 MB | 102.80 MB | 101.9% | 100.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0225s | +0.0120s | worse |
| `f1ap_rel18.6_specs` | 0.1225s | 0.0692s | +0.0533s | worse |
| `ngap_rel18.6_specs` | 0.1042s | 0.0483s | +0.0559s | worse |
| `lteNRRCC` | 0.1231s | 0.0759s | +0.0472s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.95 MB | 6.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.33 MB | 4.34 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.92 MB | 8.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.45 MB | 6.20 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0260s | +0.0152s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.0727s | +0.0391s | worse |
| `ngap_rel18.6_specs` | 0.0785s | 0.0512s | +0.0273s | worse |
| `lteNRRCC` | 0.1410s | 0.0849s | +0.0561s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.90 MB | 8.66 MB | 199.1% | 185.2% |
| `f1ap_rel18.6_specs` | 9.02 MB | 8.82 MB | 214.9% | 89.2% |
| `ngap_rel18.6_specs` | 8.04 MB | 8.14 MB | 150.2% | 93.9% |
| `lteNRRCC` | 48.77 MB | 69.20 MB | 164.9% | 160.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0382s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1139s | 0.1207s | -0.0068s | improved |
| `ngap_rel18.6_specs` | 0.0777s | 0.0733s | +0.0044s | worse |
| `lteNRRCC` | 0.1292s | 0.1105s | +0.0187s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.58 MB | 0.0% | 179.3% |
| `f1ap_rel18.6_specs` | 9.65 MB | 9.58 MB | 77.9% | 160.7% |
| `ngap_rel18.6_specs` | 8.96 MB | 10.15 MB | 159.6% | 105.5% |
| `lteNRRCC` | 73.78 MB | 91.64 MB | 157.7% | 156.9% |
<!-- BENCH_RESULTS_END -->
