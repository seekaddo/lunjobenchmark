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
Generated: 2026-10-20T01:00:41.483555+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0370s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1207s | 0.1125s | +0.0082s | worse |
| `ngap_rel18.6_specs` | 0.0818s | 0.0772s | +0.0046s | worse |
| `lteNRRCC` | 0.1261s | 0.1217s | +0.0044s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 4.8% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.2% | 103.8% |
| `lteNRRCC` | 72.38 MB | 100.11 MB | 101.7% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0462s | 0.0219s | +0.0243s | worse |
| `f1ap_rel18.6_specs` | 0.1413s | 0.0605s | +0.0808s | worse |
| `ngap_rel18.6_specs` | 0.0977s | 0.0417s | +0.0560s | worse |
| `lteNRRCC` | 0.1558s | 0.0766s | +0.0792s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.58 MB | 34.65 MB | 59.0% | 105.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.6% | 101.2% |
| `ngap_rel18.6_specs` | 18.02 MB | 72.65 MB | 107.1% | 103.3% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.7% | 102.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0220s | 0.0284s | -0.0064s | improved |
| `f1ap_rel18.6_specs` | 0.0621s | 0.0771s | -0.0150s | improved |
| `ngap_rel18.6_specs` | 0.0438s | 0.0534s | -0.0096s | improved |
| `lteNRRCC` | 0.0781s | 0.1025s | -0.0244s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.80 MB | 55.72 MB | 63.6% | 100.0% |
| `f1ap_rel18.6_specs` | 34.69 MB | 164.59 MB | 105.3% | 102.6% |
| `ngap_rel18.6_specs` | 24.33 MB | 117.51 MB | 100.0% | 103.6% |
| `lteNRRCC` | 74.82 MB | 102.95 MB | 102.8% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0250s | 0.0262s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.0651s | 0.0932s | -0.0281s | improved |
| `ngap_rel18.6_specs` | 0.0493s | 0.0645s | -0.0152s | improved |
| `lteNRRCC` | 0.0837s | 0.1040s | -0.0203s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.70 MB | 3.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.55 MB | 9.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.03 MB | 8.50 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.05 MB | 7.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0419s | 0.0282s | +0.0137s | worse |
| `f1ap_rel18.6_specs` | 0.1126s | 0.0781s | +0.0345s | worse |
| `ngap_rel18.6_specs` | 0.0789s | 0.0599s | +0.0190s | worse |
| `lteNRRCC` | 0.1390s | 0.0919s | +0.0471s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.38 MB | 7.78 MB | 0.0% | 100.0% |
| `f1ap_rel18.6_specs` | 8.43 MB | 8.07 MB | 152.9% | 160.0% |
| `ngap_rel18.6_specs` | 8.33 MB | 7.95 MB | 220.1% | 153.5% |
| `lteNRRCC` | 49.47 MB | 67.07 MB | 152.1% | 153.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0389s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1199s | 0.1140s | +0.0059s | worse |
| `ngap_rel18.6_specs` | 0.0839s | 0.0774s | +0.0065s | worse |
| `lteNRRCC` | 0.1341s | 0.1308s | +0.0033s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.15 MB | 9.07 MB | 0.0% | 148.1% |
| `f1ap_rel18.6_specs` | 10.05 MB | 164.18 MB | 146.1% | 152.6% |
| `ngap_rel18.6_specs` | 10.24 MB | 9.26 MB | 98.7% | 150.0% |
| `lteNRRCC` | 8.55 MB | 99.01 MB | 152.2% | 161.5% |
<!-- BENCH_RESULTS_END -->
