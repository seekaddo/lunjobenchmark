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
Generated: 2026-10-29T16:48:58.185201+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0400s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1234s | 0.1222s | +0.0012s | worse |
| `ngap_rel18.6_specs` | 0.0845s | 0.0844s | +0.0001s | worse |
| `lteNRRCC` | 0.1282s | 0.1273s | +0.0009s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 90.9% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.1% | 101.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 103.6% |
| `lteNRRCC` | 72.38 MB | 100.11 MB | 101.6% | 101.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0491s | 0.0484s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1478s | 0.1469s | +0.0009s | worse |
| `ngap_rel18.6_specs` | 0.1005s | 0.1002s | +0.0003s | worse |
| `lteNRRCC` | 0.1589s | 0.1563s | +0.0026s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.72 MB | 34.65 MB | 79.3% | 105.7% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 105.6% | 102.4% |
| `ngap_rel18.6_specs` | 17.97 MB | 72.65 MB | 106.9% | 103.1% |
| `lteNRRCC` | 46.70 MB | 64.21 MB | 102.7% | 102.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0533s | 0.0493s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.1657s | 0.1512s | +0.0145s | worse |
| `ngap_rel18.6_specs` | 0.1129s | 0.1036s | +0.0093s | worse |
| `lteNRRCC` | 0.1610s | 0.1479s | +0.0131s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.50 MB | 53.73 MB | 81.5% | 108.1% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 105.7% | 102.2% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 107.1% | 103.0% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 102.7% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0305s | 0.0356s | -0.0051s | improved |
| `f1ap_rel18.6_specs` | 0.0721s | 0.0823s | -0.0102s | improved |
| `ngap_rel18.6_specs` | 0.0508s | 0.0668s | -0.0160s | improved |
| `lteNRRCC` | 0.0809s | 0.0893s | -0.0084s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.22 MB | 4.33 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.48 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.50 MB | 4.83 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.56 MB | 4.41 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0392s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1139s | 0.1108s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0763s | +0.0030s | worse |
| `lteNRRCC` | 0.1304s | 0.1397s | -0.0093s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.87 MB | 7.88 MB | 0.0% | 160.2% |
| `f1ap_rel18.6_specs` | 8.67 MB | 8.61 MB | 162.0% | 110.3% |
| `ngap_rel18.6_specs` | 8.30 MB | 8.12 MB | 160.6% | 159.3% |
| `lteNRRCC` | 8.54 MB | 8.20 MB | 108.8% | 157.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0423s | 0.0390s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.1157s | 0.1150s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0844s | 0.0794s | +0.0050s | worse |
| `lteNRRCC` | 0.1518s | 0.1443s | +0.0075s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.93 MB | 11.35 MB | 0.0% | 163.7% |
| `f1ap_rel18.6_specs` | 11.22 MB | 10.19 MB | 141.0% | 166.6% |
| `ngap_rel18.6_specs` | 8.72 MB | 11.55 MB | 97.1% | 171.2% |
| `lteNRRCC` | 73.79 MB | 101.73 MB | 180.0% | 218.7% |
<!-- BENCH_RESULTS_END -->
