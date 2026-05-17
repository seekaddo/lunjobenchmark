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
Generated: 2026-05-17T22:58:38.301056+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0367s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1160s | 0.1126s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0809s | 0.0765s | +0.0044s | worse |
| `lteNRRCC` | 0.1242s | 0.1203s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 11.0% | 109.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 104.2% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.6% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 104.9% | 105.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0316s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.0953s | 0.0919s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0680s | 0.0642s | +0.0038s | worse |
| `lteNRRCC` | 0.1298s | 0.1150s | +0.0148s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.84 MB | 36.38 MB | 88.9% | 110.7% |
| `f1ap_rel18.6_specs` | 22.32 MB | 103.47 MB | 109.1% | 105.1% |
| `ngap_rel18.6_specs` | 16.54 MB | 74.61 MB | 111.1% | 106.7% |
| `lteNRRCC` | 48.68 MB | 66.28 MB | 104.5% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0328s | 0.0344s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.0895s | 0.1012s | -0.0117s | improved |
| `ngap_rel18.6_specs` | 0.0618s | 0.0700s | -0.0082s | improved |
| `lteNRRCC` | 0.1156s | 0.1179s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.80 MB | 55.50 MB | 24.7% | 111.1% |
| `f1ap_rel18.6_specs` | 34.67 MB | 164.65 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 23.54 MB | 117.82 MB | 112.5% | 107.1% |
| `lteNRRCC` | 74.65 MB | 102.51 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0442s | 0.0255s | +0.0187s | worse |
| `f1ap_rel18.6_specs` | 0.0684s | 0.0717s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0512s | 0.0483s | +0.0029s | worse |
| `lteNRRCC` | 0.0781s | 0.0764s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.16 MB | 4.58 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.02 MB | 4.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.12 MB | 4.00 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.70 MB | 3.98 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0400s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.0957s | 0.1072s | -0.0115s | improved |
| `ngap_rel18.6_specs` | 0.0651s | 0.0758s | -0.0107s | improved |
| `lteNRRCC` | 0.1128s | 0.1391s | -0.0263s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.97 MB | 7.81 MB | 100.3% | 130.8% |
| `f1ap_rel18.6_specs` | 8.41 MB | 8.80 MB | 103.2% | 269.9% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.18 MB | 109.5% | 119.7% |
| `lteNRRCC` | 8.54 MB | 51.99 MB | 101.2% | 137.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0432s | 0.0393s | +0.0039s | worse |
| `f1ap_rel18.6_specs` | 0.1256s | 0.1041s | +0.0215s | worse |
| `ngap_rel18.6_specs` | 0.0878s | 0.0737s | +0.0141s | worse |
| `lteNRRCC` | 0.1447s | 0.1134s | +0.0313s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.56 MB | 9.71 MB | 78.7% | 157.2% |
| `f1ap_rel18.6_specs` | 10.77 MB | 161.66 MB | 154.6% | 106.6% |
| `ngap_rel18.6_specs` | 9.87 MB | 10.19 MB | 157.7% | 155.1% |
| `lteNRRCC` | 9.24 MB | 74.15 MB | 150.8% | 107.3% |
<!-- BENCH_RESULTS_END -->
