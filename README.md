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
Generated: 2026-11-13T17:36:42.135245+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0420s | 0.0409s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1290s | 0.1257s | +0.0033s | worse |
| `ngap_rel18.6_specs` | 0.0898s | 0.0863s | +0.0035s | worse |
| `lteNRRCC` | 0.1323s | 0.1304s | +0.0019s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 81.0% | 109.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.0% | 103.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 106.1% |
| `lteNRRCC` | 72.41 MB | 100.11 MB | 104.2% | 104.5% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0357s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.1207s | 0.1095s | +0.0112s | worse |
| `ngap_rel18.6_specs` | 0.0851s | 0.0757s | +0.0094s | worse |
| `lteNRRCC` | 0.1323s | 0.1190s | +0.0133s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.03 MB | 34.65 MB | 75.0% | 105.1% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 107.9% | 102.5% |
| `ngap_rel18.6_specs` | 18.03 MB | 72.65 MB | 109.1% | 103.3% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.8% | 103.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0312s | 0.0441s | -0.0129s | improved |
| `f1ap_rel18.6_specs` | 0.1046s | 0.1328s | -0.0282s | improved |
| `ngap_rel18.6_specs` | 0.0705s | 0.0928s | -0.0223s | improved |
| `lteNRRCC` | 0.1014s | 0.1380s | -0.0366s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.09 MB | 53.73 MB | 6.9% | 103.4% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 108.7% | 102.1% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 103.9% | 103.2% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0397s | 0.0276s | +0.0121s | worse |
| `f1ap_rel18.6_specs` | 0.1129s | 0.0784s | +0.0345s | worse |
| `ngap_rel18.6_specs` | 0.0769s | 0.0536s | +0.0233s | worse |
| `lteNRRCC` | 0.1374s | 0.0884s | +0.0490s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 7.70 MB | 0.0% | 223.9% |
| `f1ap_rel18.6_specs` | 7.99 MB | 8.05 MB | 80.3% | 159.8% |
| `ngap_rel18.6_specs` | 7.61 MB | 7.55 MB | 162.5% | 165.5% |
| `lteNRRCC` | 50.75 MB | 57.41 MB | 113.5% | 159.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0466s | -0.0130s | improved |
| `f1ap_rel18.6_specs` | 0.0990s | 0.1303s | -0.0313s | improved |
| `ngap_rel18.6_specs` | 0.0661s | 0.0945s | -0.0284s | improved |
| `lteNRRCC` | 0.1088s | 0.1347s | -0.0259s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.17 MB | 0.0% | 139.7% |
| `f1ap_rel18.6_specs` | 11.16 MB | 164.20 MB | 140.4% | 140.2% |
| `ngap_rel18.6_specs` | 10.21 MB | 10.21 MB | 140.3% | 141.1% |
| `lteNRRCC` | 9.27 MB | 81.96 MB | 142.3% | 140.4% |
<!-- BENCH_RESULTS_END -->
