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
Generated: 2026-06-10T13:37:46.248331+00:00

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0334s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.0958s | 0.0912s | +0.0046s | worse |
| `ngap_rel18.6_specs` | 0.0666s | 0.0647s | +0.0019s | worse |
| `lteNRRCC` | 0.1172s | 0.1239s | -0.0067s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.57 MB | 21.3% | 111.5% |
| `f1ap_rel18.6_specs` | 22.20 MB | 103.20 MB | 110.7% | 105.4% |
| `ngap_rel18.6_specs` | 17.77 MB | 73.82 MB | 108.7% | 104.8% |
| `lteNRRCC` | 48.58 MB | 66.04 MB | 101.8% | 104.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0349s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.0995s | 0.0932s | +0.0063s | worse |
| `ngap_rel18.6_specs` | 0.0687s | 0.0640s | +0.0047s | worse |
| `lteNRRCC` | 0.1313s | 0.1264s | +0.0049s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.41 MB | 55.88 MB | 92.6% | 109.7% |
| `f1ap_rel18.6_specs` | 34.74 MB | 164.45 MB | 112.5% | 104.9% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.67 MB | 107.1% | 106.4% |
| `lteNRRCC` | 75.02 MB | 102.86 MB | 103.1% | 103.8% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0279s | 0.0304s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0906s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0819s | 0.0570s | +0.0249s | worse |
| `lteNRRCC` | 0.1106s | 0.0834s | +0.0272s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.75 MB | 6.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 7.83 MB | 1.92 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.53 MB | 8.50 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.83 MB | 5.14 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0407s | -0.0024s | improved |
| `f1ap_rel18.6_specs` | 0.1042s | 0.1113s | -0.0071s | improved |
| `ngap_rel18.6_specs` | 0.0731s | 0.0763s | -0.0032s | improved |
| `lteNRRCC` | 0.1365s | 0.1392s | -0.0027s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.35 MB | 7.50 MB | 82.5% | 98.3% |
| `f1ap_rel18.6_specs` | 7.97 MB | 8.11 MB | 164.1% | 165.1% |
| `ngap_rel18.6_specs` | 7.61 MB | 8.05 MB | 164.5% | 112.4% |
| `lteNRRCC` | 46.95 MB | 69.23 MB | 166.0% | 111.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0440s | 0.0352s | +0.0088s | worse |
| `f1ap_rel18.6_specs` | 0.1282s | 0.1035s | +0.0247s | worse |
| `ngap_rel18.6_specs` | 0.0896s | 0.0716s | +0.0180s | worse |
| `lteNRRCC` | 0.1420s | 0.1123s | +0.0297s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.93 MB | 10.52 MB | 160.2% | 108.8% |
| `f1ap_rel18.6_specs` | 10.03 MB | 155.93 MB | 81.7% | 163.3% |
| `ngap_rel18.6_specs` | 9.38 MB | 9.41 MB | 80.8% | 81.8% |
| `lteNRRCC` | 8.87 MB | 99.76 MB | 79.4% | 112.0% |
<!-- BENCH_RESULTS_END -->
