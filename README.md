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
Generated: 2026-10-08T17:19:32.230082+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0354s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1135s | 0.1125s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0767s | 0.0764s | +0.0003s | worse |
| `lteNRRCC` | 0.1201s | 0.1209s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 90.5% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0328s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0934s | 0.0954s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0635s | 0.0665s | -0.0030s | improved |
| `lteNRRCC` | 0.1132s | 0.1181s | -0.0049s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.56 MB | 36.66 MB | 9.9% | 104.0% |
| `f1ap_rel18.6_specs` | 22.22 MB | 102.84 MB | 103.7% | 103.6% |
| `ngap_rel18.6_specs` | 18.07 MB | 74.71 MB | 100.0% | 102.4% |
| `lteNRRCC` | 48.58 MB | 66.10 MB | 101.8% | 101.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0353s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0956s | 0.0934s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0709s | 0.0647s | +0.0062s | worse |
| `lteNRRCC` | 0.1193s | 0.1185s | +0.0008s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.66 MB | 76.9% | 103.7% |
| `f1ap_rel18.6_specs` | 34.48 MB | 164.41 MB | 103.4% | 103.6% |
| `ngap_rel18.6_specs` | 24.32 MB | 117.37 MB | 108.3% | 102.3% |
| `lteNRRCC` | 74.25 MB | 102.63 MB | 101.7% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0458s | 0.0416s | +0.0042s | worse |
| `f1ap_rel18.6_specs` | 0.0736s | 0.0762s | -0.0026s | improved |
| `ngap_rel18.6_specs` | 0.0440s | 0.0572s | -0.0132s | improved |
| `lteNRRCC` | 0.0755s | 0.0979s | -0.0224s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.17 MB | 4.72 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.19 MB | 9.23 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.47 MB | 8.48 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.52 MB | 7.48 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0443s | 0.0364s | +0.0079s | worse |
| `f1ap_rel18.6_specs` | 0.1124s | 0.0962s | +0.0162s | worse |
| `ngap_rel18.6_specs` | 0.0759s | 0.0679s | +0.0080s | worse |
| `lteNRRCC` | 0.1401s | 0.1101s | +0.0300s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.39 MB | 7.30 MB | 0.0% | 82.0% |
| `f1ap_rel18.6_specs` | 8.34 MB | 7.60 MB | 94.9% | 155.6% |
| `ngap_rel18.6_specs` | 7.63 MB | 7.84 MB | 80.4% | 100.8% |
| `lteNRRCC` | 7.81 MB | 59.75 MB | 79.6% | 156.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0395s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1144s | 0.1111s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0802s | 0.0761s | +0.0041s | worse |
| `lteNRRCC` | 0.1288s | 0.1287s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.80 MB | 0.0% | 221.8% |
| `f1ap_rel18.6_specs` | 11.56 MB | 164.17 MB | 113.9% | 110.2% |
| `ngap_rel18.6_specs` | 11.00 MB | 9.19 MB | 108.6% | 152.5% |
| `lteNRRCC` | 9.91 MB | 93.14 MB | 108.3% | 158.2% |
<!-- BENCH_RESULTS_END -->
