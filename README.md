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
Generated: 2026-07-25T11:17:13.316917+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0358s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1149s | 0.1157s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0787s | -0.0016s | improved |
| `lteNRRCC` | 0.1213s | 0.1239s | -0.0026s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 14.5% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.3% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0336s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.0971s | 0.0913s | +0.0058s | worse |
| `ngap_rel18.6_specs` | 0.0682s | 0.0637s | +0.0045s | worse |
| `lteNRRCC` | 0.1312s | 0.1230s | +0.0082s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 36.50 MB | 10.4% | 107.1% |
| `f1ap_rel18.6_specs` | 22.27 MB | 102.70 MB | 106.2% | 103.4% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.63 MB | 107.7% | 104.5% |
| `lteNRRCC` | 48.54 MB | 66.28 MB | 101.4% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0337s | 0.0352s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.0896s | 0.0911s | -0.0015s | improved |
| `ngap_rel18.6_specs` | 0.0628s | 0.0647s | -0.0019s | improved |
| `lteNRRCC` | 0.1187s | 0.1185s | +0.0002s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.77 MB | 52.8% | 107.7% |
| `f1ap_rel18.6_specs` | 34.73 MB | 163.78 MB | 107.1% | 103.7% |
| `ngap_rel18.6_specs` | 24.52 MB | 117.08 MB | 108.7% | 105.0% |
| `lteNRRCC` | 74.84 MB | 102.50 MB | 101.7% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0201s | 0.0206s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.0660s | 0.0682s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0451s | 0.0471s | -0.0020s | improved |
| `lteNRRCC` | 0.0700s | 0.1034s | -0.0334s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.17 MB | 3.98 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.50 MB | 4.03 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.44 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.81 MB | 4.02 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0401s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.0928s | 0.1081s | -0.0153s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0769s | -0.0130s | improved |
| `lteNRRCC` | 0.1122s | 0.1390s | -0.0268s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.75 MB | 7.91 MB | 0.0% | 102.6% |
| `f1ap_rel18.6_specs` | 8.55 MB | 106.66 MB | 102.7% | 135.3% |
| `ngap_rel18.6_specs` | 8.06 MB | 8.25 MB | 102.4% | 138.7% |
| `lteNRRCC` | 8.61 MB | 68.19 MB | 197.8% | 134.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0381s | +0.0025s | worse |
| `f1ap_rel18.6_specs` | 0.1155s | 0.1095s | +0.0060s | worse |
| `ngap_rel18.6_specs` | 0.0799s | 0.0789s | +0.0010s | worse |
| `lteNRRCC` | 0.1313s | 0.1276s | +0.0037s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.11 MB | 8.93 MB | 219.4% | 154.3% |
| `f1ap_rel18.6_specs` | 10.91 MB | 164.19 MB | 221.2% | 108.3% |
| `ngap_rel18.6_specs` | 9.08 MB | 9.20 MB | 157.3% | 153.7% |
| `lteNRRCC` | 8.68 MB | 75.64 MB | 152.7% | 153.5% |
<!-- BENCH_RESULTS_END -->
