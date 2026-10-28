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
Generated: 2026-10-28T16:36:46.426339+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0353s | +0.0066s | worse |
| `f1ap_rel18.6_specs` | 0.1251s | 0.1101s | +0.0150s | worse |
| `ngap_rel18.6_specs` | 0.0830s | 0.0755s | +0.0075s | worse |
| `lteNRRCC` | 0.1291s | 0.1196s | +0.0095s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.75 MB | 53.55 MB | 61.8% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 103.7% |
| `lteNRRCC` | 72.41 MB | 100.18 MB | 101.6% | 102.6% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0458s | 0.0368s | +0.0090s | worse |
| `f1ap_rel18.6_specs` | 0.1419s | 0.0951s | +0.0468s | worse |
| `ngap_rel18.6_specs` | 0.0991s | 0.0661s | +0.0330s | worse |
| `lteNRRCC` | 0.1576s | 0.1306s | +0.0270s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 34.65 MB | 84.6% | 106.1% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.7% | 102.5% |
| `ngap_rel18.6_specs` | 17.93 MB | 72.65 MB | 103.6% | 101.7% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.7% | 102.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0600s | 0.0349s | +0.0251s | worse |
| `f1ap_rel18.6_specs` | 0.1860s | 0.0926s | +0.0934s | worse |
| `ngap_rel18.6_specs` | 0.1299s | 0.0641s | +0.0658s | worse |
| `lteNRRCC` | 0.1829s | 0.1262s | +0.0567s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.67 MB | 53.73 MB | 19.5% | 104.8% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.1% | 101.9% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 103.3% | 102.7% |
| `lteNRRCC` | 72.66 MB | 100.36 MB | 102.4% | 101.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0233s | 0.0226s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.0813s | 0.0788s | +0.0025s | worse |
| `ngap_rel18.6_specs` | 0.0564s | 0.0489s | +0.0075s | worse |
| `lteNRRCC` | 0.0858s | 0.0763s | +0.0095s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.39 MB | 2.22 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.88 MB | 9.34 MB | 0.0% | 1.8% |
| `ngap_rel18.6_specs` | 5.28 MB | 3.66 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.08 MB | 6.28 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0408s | 0.0407s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.1150s | 0.1140s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0805s | 0.0784s | +0.0021s | worse |
| `lteNRRCC` | 0.1416s | 0.1404s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.52 MB | 7.85 MB | 100.9% | 164.3% |
| `f1ap_rel18.6_specs` | 8.69 MB | 8.69 MB | 161.9% | 201.0% |
| `ngap_rel18.6_specs` | 8.44 MB | 8.32 MB | 98.7% | 159.0% |
| `lteNRRCC` | 51.85 MB | 69.24 MB | 220.4% | 111.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0298s | 0.0379s | -0.0081s | improved |
| `f1ap_rel18.6_specs` | 0.0842s | 0.1110s | -0.0268s | improved |
| `ngap_rel18.6_specs` | 0.0575s | 0.0755s | -0.0180s | improved |
| `lteNRRCC` | 0.0864s | 0.1306s | -0.0442s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 29.84 MB | 0.0% | 83.7% |
| `f1ap_rel18.6_specs` | 34.38 MB | 22.64 MB | 53.6% | 84.6% |
| `ngap_rel18.6_specs` | 15.34 MB | 24.19 MB | 112.3% | 148.7% |
| `lteNRRCC` | 15.52 MB | 17.52 MB | 93.2% | 73.2% |
<!-- BENCH_RESULTS_END -->
