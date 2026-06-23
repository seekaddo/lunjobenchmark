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
Generated: 2026-06-23T23:13:26.026977+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0353s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1102s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0764s | 0.0757s | +0.0007s | worse |
| `lteNRRCC` | 0.1210s | 0.1188s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 6.3% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 110.0% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.5% | 104.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.2% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0354s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0946s | 0.0956s | -0.0010s | improved |
| `ngap_rel18.6_specs` | 0.0673s | 0.0695s | -0.0022s | improved |
| `lteNRRCC` | 0.1302s | 0.1272s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 36.57 MB | 22.3% | 110.7% |
| `f1ap_rel18.6_specs` | 22.18 MB | 103.46 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 17.70 MB | 74.52 MB | 111.5% | 106.8% |
| `lteNRRCC` | 48.78 MB | 65.68 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0283s | 0.0336s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.0755s | 0.0883s | -0.0128s | improved |
| `ngap_rel18.6_specs` | 0.0523s | 0.0616s | -0.0093s | improved |
| `lteNRRCC` | 0.1005s | 0.1154s | -0.0149s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.28 MB | 55.54 MB | 27.9% | 113.6% |
| `f1ap_rel18.6_specs` | 34.56 MB | 164.41 MB | 108.3% | 104.3% |
| `ngap_rel18.6_specs` | 24.24 MB | 117.56 MB | 110.0% | 105.7% |
| `lteNRRCC` | 74.98 MB | 102.41 MB | 104.1% | 105.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0291s | 0.0206s | +0.0085s | worse |
| `f1ap_rel18.6_specs` | 0.0865s | 0.0620s | +0.0245s | worse |
| `ngap_rel18.6_specs` | 0.0610s | 0.0476s | +0.0134s | worse |
| `lteNRRCC` | 0.0961s | 0.0755s | +0.0206s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.61 MB | 5.41 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.95 MB | 4.36 MB | 0.0% | 1.2% |
| `ngap_rel18.6_specs` | 7.56 MB | 8.50 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.66 MB | 7.38 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0392s | +0.0024s | worse |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1095s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0787s | 0.0770s | +0.0017s | worse |
| `lteNRRCC` | 0.1321s | 0.1399s | -0.0078s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.56 MB | 7.50 MB | 83.0% | 100.0% |
| `f1ap_rel18.6_specs` | 8.17 MB | 8.45 MB | 80.9% | 118.6% |
| `ngap_rel18.6_specs` | 8.05 MB | 8.05 MB | 99.5% | 161.9% |
| `lteNRRCC` | 7.48 MB | 70.55 MB | 119.4% | 163.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0386s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.1071s | 0.1110s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0779s | -0.0041s | improved |
| `lteNRRCC` | 0.1140s | 0.1242s | -0.0102s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.83 MB | 10.02 MB | 139.8% | 140.7% |
| `f1ap_rel18.6_specs` | 10.45 MB | 149.41 MB | 140.4% | 125.7% |
| `ngap_rel18.6_specs` | 10.17 MB | 10.43 MB | 140.7% | 140.1% |
| `lteNRRCC` | 8.95 MB | 98.55 MB | 141.7% | 116.2% |
<!-- BENCH_RESULTS_END -->
