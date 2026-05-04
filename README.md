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
Generated: 2026-05-04T11:56:57.977961+00:00

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0282s | 0.0350s | -0.0068s | improved |
| `f1ap_rel18.6_specs` | 0.0751s | 0.0935s | -0.0184s | improved |
| `ngap_rel18.6_specs` | 0.0521s | 0.0661s | -0.0140s | improved |
| `lteNRRCC` | 0.0991s | 0.1267s | -0.0276s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.69 MB | 36.50 MB | 76.9% | 108.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.19 MB | 112.0% | 104.3% |
| `ngap_rel18.6_specs` | 16.82 MB | 74.26 MB | 109.5% | 105.7% |
| `lteNRRCC` | 48.71 MB | 66.12 MB | 104.1% | 103.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0351s | -0.0021s | improved |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0908s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0624s | 0.0633s | -0.0009s | improved |
| `lteNRRCC` | 0.1184s | 0.1162s | +0.0022s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.83 MB | 92.0% | 107.1% |
| `f1ap_rel18.6_specs` | 34.55 MB | 164.48 MB | 110.0% | 105.4% |
| `ngap_rel18.6_specs` | 24.41 MB | 117.38 MB | 112.0% | 107.1% |
| `lteNRRCC` | 74.61 MB | 102.50 MB | 105.1% | 105.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0223s | 0.0249s | -0.0026s | improved |
| `f1ap_rel18.6_specs` | 0.0701s | 0.0734s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0530s | 0.0472s | +0.0058s | worse |
| `lteNRRCC` | 0.1043s | 0.0738s | +0.0305s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.27 MB | 4.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.34 MB | 4.03 MB | 0.7% | 0.0% |
| `ngap_rel18.6_specs` | 4.16 MB | 5.30 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.97 MB | 7.98 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0416s | 0.0390s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1094s | 0.1057s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0740s | +0.0048s | worse |
| `lteNRRCC` | 0.1394s | 0.1373s | +0.0021s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.36 MB | 6.66 MB | 160.6% | 224.9% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.54 MB | 157.7% | 109.0% |
| `ngap_rel18.6_specs` | 8.11 MB | 7.61 MB | 100.8% | 78.5% |
| `lteNRRCC` | 51.14 MB | 70.55 MB | 154.0% | 158.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0432s | 0.0421s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1214s | 0.1193s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0841s | 0.0815s | +0.0026s | worse |
| `lteNRRCC` | 0.1413s | 0.1365s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.89 MB | 9.77 MB | 77.9% | 157.0% |
| `f1ap_rel18.6_specs` | 10.12 MB | 148.22 MB | 159.4% | 108.1% |
| `ngap_rel18.6_specs` | 9.48 MB | 10.18 MB | 156.6% | 156.9% |
| `lteNRRCC` | 69.11 MB | 101.23 MB | 158.2% | 210.2% |
<!-- BENCH_RESULTS_END -->
