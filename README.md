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
Generated: 2026-10-29T01:40:58.774993+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0400s | 0.0419s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1222s | 0.1251s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0844s | 0.0830s | +0.0014s | worse |
| `lteNRRCC` | 0.1273s | 0.1291s | -0.0018s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.93 MB | 53.55 MB | 62.5% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 103.8% |
| `lteNRRCC` | 72.32 MB | 100.18 MB | 103.3% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0484s | 0.0458s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1469s | 0.1419s | +0.0050s | worse |
| `ngap_rel18.6_specs` | 0.1002s | 0.0991s | +0.0011s | worse |
| `lteNRRCC` | 0.1563s | 0.1576s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.69 MB | 34.65 MB | 78.6% | 105.9% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 102.8% | 101.2% |
| `ngap_rel18.6_specs` | 17.97 MB | 72.65 MB | 107.1% | 101.7% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 102.7% | 101.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0493s | 0.0600s | -0.0107s | improved |
| `f1ap_rel18.6_specs` | 0.1512s | 0.1860s | -0.0348s | improved |
| `ngap_rel18.6_specs` | 0.1036s | 0.1299s | -0.0263s | improved |
| `lteNRRCC` | 0.1479s | 0.1829s | -0.0350s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.70 MB | 53.73 MB | 70.0% | 103.0% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 103.2% | 102.4% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 104.2% | 103.3% |
| `lteNRRCC` | 72.59 MB | 100.36 MB | 100.0% | 101.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0356s | 0.0233s | +0.0123s | worse |
| `f1ap_rel18.6_specs` | 0.0823s | 0.0813s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0668s | 0.0564s | +0.0104s | worse |
| `lteNRRCC` | 0.0893s | 0.0858s | +0.0035s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.41 MB | 5.86 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.09 MB | 8.50 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.75 MB | 5.28 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.38 MB | 2.03 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0408s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1150s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0805s | -0.0042s | improved |
| `lteNRRCC` | 0.1397s | 0.1416s | -0.0019s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.36 MB | 7.57 MB | 0.0% | 106.3% |
| `f1ap_rel18.6_specs` | 8.75 MB | 8.68 MB | 111.4% | 109.9% |
| `ngap_rel18.6_specs` | 8.00 MB | 7.93 MB | 155.4% | 155.2% |
| `lteNRRCC` | 48.59 MB | 59.39 MB | 158.4% | 104.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0298s | +0.0092s | worse |
| `f1ap_rel18.6_specs` | 0.1150s | 0.0842s | +0.0308s | worse |
| `ngap_rel18.6_specs` | 0.0794s | 0.0575s | +0.0219s | worse |
| `lteNRRCC` | 0.1443s | 0.0864s | +0.0579s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.93 MB | 0.0% | 161.6% |
| `f1ap_rel18.6_specs` | 9.82 MB | 164.20 MB | 107.2% | 102.7% |
| `ngap_rel18.6_specs` | 9.57 MB | 10.05 MB | 99.0% | 175.2% |
| `lteNRRCC` | 8.76 MB | 99.04 MB | 153.3% | 111.0% |
<!-- BENCH_RESULTS_END -->
