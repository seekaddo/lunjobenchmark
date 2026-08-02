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
Generated: 2026-08-02T11:20:50.745743+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0357s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1145s | 0.1128s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0801s | 0.0776s | +0.0025s | worse |
| `lteNRRCC` | 0.1219s | 0.1207s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 17.7% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 100.0% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.7% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0280s | +0.0067s | worse |
| `f1ap_rel18.6_specs` | 0.0947s | 0.0749s | +0.0198s | worse |
| `ngap_rel18.6_specs` | 0.0661s | 0.0514s | +0.0147s | worse |
| `lteNRRCC` | 0.1308s | 0.0983s | +0.0325s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.36 MB | 36.48 MB | 17.8% | 107.7% |
| `f1ap_rel18.6_specs` | 22.11 MB | 103.43 MB | 106.5% | 101.8% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.38 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.39 MB | 66.41 MB | 103.2% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0341s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0919s | 0.0916s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0640s | 0.0689s | -0.0049s | improved |
| `lteNRRCC` | 0.1179s | 0.1149s | +0.0030s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 55.85 MB | 14.2% | 107.7% |
| `f1ap_rel18.6_specs` | 35.18 MB | 164.76 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.64 MB | 108.3% | 102.4% |
| `lteNRRCC` | 74.84 MB | 102.84 MB | 101.7% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0217s | 0.0243s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0662s | 0.0872s | -0.0210s | improved |
| `ngap_rel18.6_specs` | 0.0479s | 0.0584s | -0.0105s | improved |
| `lteNRRCC` | 0.0753s | 0.0959s | -0.0206s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.78 MB | 4.33 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.64 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.88 MB | 4.19 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.73 MB | 4.05 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0406s | 0.0380s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1099s | 0.1041s | +0.0058s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0727s | +0.0046s | worse |
| `lteNRRCC` | 0.1417s | 0.1362s | +0.0055s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.63 MB | 0.0% | 75.7% |
| `f1ap_rel18.6_specs` | 8.48 MB | 106.64 MB | 87.7% | 157.1% |
| `ngap_rel18.6_specs` | 8.06 MB | 8.00 MB | 73.9% | 152.9% |
| `lteNRRCC` | 49.52 MB | 69.30 MB | 106.8% | 149.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0376s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1110s | 0.1084s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0733s | +0.0040s | worse |
| `lteNRRCC` | 0.1281s | 0.1240s | +0.0041s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 8.59 MB | 0.0% | 78.8% |
| `f1ap_rel18.6_specs` | 9.62 MB | 164.19 MB | 161.3% | 157.2% |
| `ngap_rel18.6_specs` | 8.77 MB | 10.25 MB | 80.5% | 100.2% |
| `lteNRRCC` | 8.50 MB | 83.23 MB | 177.9% | 154.3% |
<!-- BENCH_RESULTS_END -->
