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
Generated: 2026-04-12T22:42:48.079868+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0372s | -0.0005s | improved |
| `f1ap_rel18.6_specs` | 0.1143s | 0.1164s | -0.0021s | improved |
| `ngap_rel18.6_specs` | 0.0780s | 0.0791s | -0.0011s | improved |
| `lteNRRCC` | 0.1219s | 0.1236s | -0.0017s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 7.4% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 106.7% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0344s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.0963s | 0.0941s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0675s | 0.0653s | +0.0022s | worse |
| `lteNRRCC` | 0.1280s | 0.1280s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.23 MB | 36.36 MB | 100.0% | 112.1% |
| `f1ap_rel18.6_specs` | 21.70 MB | 103.01 MB | 109.1% | 105.0% |
| `ngap_rel18.6_specs` | 16.85 MB | 74.38 MB | 110.7% | 106.7% |
| `lteNRRCC` | 48.65 MB | 65.39 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0357s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0904s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0642s | 0.0625s | +0.0017s | worse |
| `lteNRRCC` | 0.1265s | 0.1160s | +0.0105s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.68 MB | 23.6% | 110.0% |
| `f1ap_rel18.6_specs` | 34.61 MB | 164.39 MB | 112.5% | 105.1% |
| `ngap_rel18.6_specs` | 24.61 MB | 117.50 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.80 MB | 102.49 MB | 104.7% | 103.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0218s | 0.0294s | -0.0076s | improved |
| `f1ap_rel18.6_specs` | 0.0643s | 0.0836s | -0.0193s | improved |
| `ngap_rel18.6_specs` | 0.0407s | 0.0465s | -0.0058s | improved |
| `lteNRRCC` | 0.0685s | 0.0743s | -0.0058s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.55 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 4.55 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 4.77 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.12 MB | 4.88 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0379s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.1044s | 0.1062s | -0.0018s | improved |
| `ngap_rel18.6_specs` | 0.0743s | 0.0754s | -0.0011s | improved |
| `lteNRRCC` | 0.1357s | 0.1379s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.34 MB | 7.36 MB | 164.8% | 82.7% |
| `f1ap_rel18.6_specs` | 7.96 MB | 8.60 MB | 167.4% | 107.7% |
| `ngap_rel18.6_specs` | 7.54 MB | 7.54 MB | 164.0% | 81.2% |
| `lteNRRCC` | 47.56 MB | 70.54 MB | 161.0% | 107.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0427s | -0.0053s | improved |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1268s | -0.0188s | improved |
| `ngap_rel18.6_specs` | 0.0753s | 0.0867s | -0.0114s | improved |
| `lteNRRCC` | 0.1234s | 0.1318s | -0.0084s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.78 MB | 10.57 MB | 170.3% | 115.0% |
| `f1ap_rel18.6_specs` | 9.80 MB | 9.92 MB | 161.0% | 101.5% |
| `ngap_rel18.6_specs` | 8.95 MB | 8.89 MB | 158.1% | 162.1% |
| `lteNRRCC` | 8.55 MB | 81.95 MB | 78.7% | 158.5% |
<!-- BENCH_RESULTS_END -->
