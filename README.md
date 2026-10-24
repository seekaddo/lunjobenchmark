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
Generated: 2026-10-24T13:55:06.091394+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0357s | -0.0015s | improved |
| `f1ap_rel18.6_specs` | 0.1096s | 0.1129s | -0.0033s | improved |
| `ngap_rel18.6_specs` | 0.0755s | 0.0770s | -0.0015s | improved |
| `lteNRRCC` | 0.1193s | 0.1204s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 62.1% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 102.2% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.6% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0258s | 0.0373s | -0.0115s | improved |
| `f1ap_rel18.6_specs` | 0.0668s | 0.1035s | -0.0367s | improved |
| `ngap_rel18.6_specs` | 0.0462s | 0.0718s | -0.0256s | improved |
| `lteNRRCC` | 0.0819s | 0.1349s | -0.0530s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.77 MB | 36.58 MB | 14.2% | 105.3% |
| `f1ap_rel18.6_specs` | 22.42 MB | 102.42 MB | 100.0% | 104.9% |
| `ngap_rel18.6_specs` | 18.03 MB | 74.34 MB | 105.6% | 103.2% |
| `lteNRRCC` | 48.74 MB | 66.28 MB | 105.1% | 102.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0227s | +0.0120s | worse |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0614s | +0.0319s | worse |
| `ngap_rel18.6_specs` | 0.0648s | 0.0416s | +0.0232s | worse |
| `lteNRRCC` | 0.1222s | 0.0763s | +0.0459s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.80 MB | 83.3% | 103.8% |
| `f1ap_rel18.6_specs` | 33.86 MB | 164.41 MB | 103.4% | 103.6% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.18 MB | 104.2% | 104.8% |
| `lteNRRCC` | 74.96 MB | 102.94 MB | 103.4% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0476s | 0.0225s | +0.0251s | worse |
| `f1ap_rel18.6_specs` | 0.1321s | 0.0783s | +0.0538s | worse |
| `ngap_rel18.6_specs` | 0.0637s | 0.0698s | -0.0061s | improved |
| `lteNRRCC` | 0.0863s | 0.0758s | +0.0105s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.75 MB | 1.95 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.95 MB | 6.78 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.33 MB | 3.64 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.27 MB | 1.95 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0414s | -0.0040s | improved |
| `f1ap_rel18.6_specs` | 0.1033s | 0.1114s | -0.0081s | improved |
| `ngap_rel18.6_specs` | 0.0736s | 0.0768s | -0.0032s | improved |
| `lteNRRCC` | 0.1381s | 0.1383s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.45 MB | 7.36 MB | 215.9% | 91.2% |
| `f1ap_rel18.6_specs` | 8.05 MB | 8.62 MB | 164.5% | 227.6% |
| `ngap_rel18.6_specs` | 8.19 MB | 7.62 MB | 116.6% | 160.1% |
| `lteNRRCC` | 50.88 MB | 59.55 MB | 229.6% | 117.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0473s | -0.0082s | improved |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1395s | -0.0259s | improved |
| `ngap_rel18.6_specs` | 0.0890s | 0.0958s | -0.0068s | improved |
| `lteNRRCC` | 0.1373s | 0.1388s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.13 MB | 8.90 MB | 0.0% | 155.3% |
| `f1ap_rel18.6_specs` | 10.04 MB | 13.14 MB | 154.3% | 177.4% |
| `ngap_rel18.6_specs` | 9.05 MB | 9.20 MB | 154.9% | 163.0% |
| `lteNRRCC` | 8.59 MB | 99.74 MB | 153.2% | 105.8% |
<!-- BENCH_RESULTS_END -->
