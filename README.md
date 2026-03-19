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
Generated: 2026-03-19T17:31:11.753331+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0360s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.1171s | 0.1140s | +0.0031s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0792s | +0.0024s | worse |
| `lteNRRCC` | 0.1255s | 0.1226s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 86.4% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.4% | 102.8% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0367s | 0.0358s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.0994s | 0.0970s | +0.0024s | worse |
| `ngap_rel18.6_specs` | 0.0698s | 0.0678s | +0.0020s | worse |
| `lteNRRCC` | 0.1339s | 0.1312s | +0.0027s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 36.72 MB | 96.4% | 112.9% |
| `f1ap_rel18.6_specs` | 22.37 MB | 103.48 MB | 108.6% | 106.5% |
| `ngap_rel18.6_specs` | 16.55 MB | 74.65 MB | 113.8% | 108.3% |
| `lteNRRCC` | 48.69 MB | 66.09 MB | 104.4% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0341s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0899s | 0.0896s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0630s | 0.0628s | +0.0002s | worse |
| `lteNRRCC` | 0.1165s | 0.1160s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.34 MB | 55.83 MB | 92.3% | 110.3% |
| `f1ap_rel18.6_specs` | 34.58 MB | 164.62 MB | 112.9% | 105.3% |
| `ngap_rel18.6_specs` | 24.59 MB | 117.89 MB | 115.4% | 109.3% |
| `lteNRRCC` | 74.53 MB | 102.82 MB | 106.5% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0249s | 0.0236s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0777s | 0.0670s | +0.0107s | worse |
| `ngap_rel18.6_specs` | 0.0494s | 0.0464s | +0.0030s | worse |
| `lteNRRCC` | 0.0989s | 0.0756s | +0.0233s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.56 MB | 4.22 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.95 MB | 4.61 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.00 MB | 6.06 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.30 MB | 3.78 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0399s | -0.0004s | improved |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1117s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0774s | -0.0011s | improved |
| `lteNRRCC` | 0.1381s | 0.1394s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.76 MB | 7.51 MB | 156.5% | 159.1% |
| `f1ap_rel18.6_specs` | 8.24 MB | 8.11 MB | 81.5% | 175.3% |
| `ngap_rel18.6_specs` | 8.37 MB | 8.34 MB | 222.4% | 222.8% |
| `lteNRRCC` | 51.84 MB | 70.55 MB | 155.1% | 155.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0409s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1236s | -0.0089s | improved |
| `ngap_rel18.6_specs` | 0.0794s | 0.0853s | -0.0059s | improved |
| `lteNRRCC` | 0.1281s | 0.1426s | -0.0145s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.73 MB | 8.66 MB | 111.5% | 159.2% |
| `f1ap_rel18.6_specs` | 11.39 MB | 162.10 MB | 113.1% | 168.7% |
| `ngap_rel18.6_specs` | 9.09 MB | 8.93 MB | 159.5% | 157.9% |
| `lteNRRCC` | 73.78 MB | 99.21 MB | 157.9% | 227.5% |
<!-- BENCH_RESULTS_END -->
