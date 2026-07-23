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
Generated: 2026-07-23T11:55:01.500130+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0361s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1100s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0753s | +0.0020s | worse |
| `lteNRRCC` | 0.1207s | 0.1200s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 19.3% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 106.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0269s | 0.0346s | -0.0077s | improved |
| `f1ap_rel18.6_specs` | 0.0738s | 0.0927s | -0.0189s | improved |
| `ngap_rel18.6_specs` | 0.0516s | 0.0652s | -0.0136s | improved |
| `lteNRRCC` | 0.0970s | 0.1285s | -0.0315s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.25 MB | 36.14 MB | 33.9% | 109.1% |
| `f1ap_rel18.6_specs` | 22.17 MB | 103.15 MB | 108.3% | 104.3% |
| `ngap_rel18.6_specs` | 19.11 MB | 74.44 MB | 104.8% | 105.9% |
| `lteNRRCC` | 48.74 MB | 66.48 MB | 106.2% | 103.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0329s | +0.0068s | worse |
| `f1ap_rel18.6_specs` | 0.0978s | 0.0883s | +0.0095s | worse |
| `ngap_rel18.6_specs` | 0.0632s | 0.0620s | +0.0012s | worse |
| `lteNRRCC` | 0.1208s | 0.1160s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.28 MB | 55.67 MB | 77.8% | 103.4% |
| `f1ap_rel18.6_specs` | 34.01 MB | 164.78 MB | 103.3% | 103.6% |
| `ngap_rel18.6_specs` | 24.06 MB | 117.32 MB | 108.3% | 102.4% |
| `lteNRRCC` | 74.52 MB | 102.90 MB | 101.8% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0226s | 0.0450s | -0.0224s | improved |
| `f1ap_rel18.6_specs` | 0.0715s | 0.0733s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0502s | 0.0538s | -0.0036s | improved |
| `lteNRRCC` | 0.0772s | 0.0836s | -0.0064s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.14 MB | 4.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.33 MB | 3.36 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.08 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.42 MB | 3.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0396s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1097s | 0.1080s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0757s | 0.0750s | +0.0007s | worse |
| `lteNRRCC` | 0.1392s | 0.1399s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.47 MB | 80.0% | 158.6% |
| `f1ap_rel18.6_specs` | 8.11 MB | 8.18 MB | 98.4% | 161.9% |
| `ngap_rel18.6_specs` | 7.68 MB | 7.68 MB | 86.0% | 79.5% |
| `lteNRRCC` | 49.20 MB | 70.55 MB | 106.6% | 112.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0365s | +0.0027s | worse |
| `f1ap_rel18.6_specs` | 0.1159s | 0.1021s | +0.0138s | worse |
| `ngap_rel18.6_specs` | 0.0828s | 0.0722s | +0.0106s | worse |
| `lteNRRCC` | 0.1266s | 0.1130s | +0.0136s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.59 MB | 9.08 MB | 162.0% | 92.7% |
| `f1ap_rel18.6_specs` | 9.69 MB | 164.19 MB | 158.8% | 158.8% |
| `ngap_rel18.6_specs` | 8.65 MB | 9.02 MB | 161.5% | 79.2% |
| `lteNRRCC` | 73.77 MB | 73.88 MB | 223.7% | 107.6% |
<!-- BENCH_RESULTS_END -->
