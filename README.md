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
Generated: 2026-05-24T23:02:59.517787+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0384s | -0.0016s | improved |
| `f1ap_rel18.6_specs` | 0.1127s | 0.1165s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0773s | 0.0802s | -0.0029s | improved |
| `lteNRRCC` | 0.1208s | 0.1246s | -0.0038s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 27.2% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 112.0% | 105.9% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 105.0% | 102.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0368s | 0.0367s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0971s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0670s | 0.0688s | -0.0018s | improved |
| `lteNRRCC` | 0.1299s | 0.1310s | -0.0011s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 36.40 MB | 82.8% | 106.9% |
| `f1ap_rel18.6_specs` | 22.01 MB | 103.04 MB | 109.1% | 105.2% |
| `ngap_rel18.6_specs` | 17.67 MB | 74.23 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.37 MB | 65.89 MB | 103.1% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0382s | 0.0346s | +0.0036s | worse |
| `f1ap_rel18.6_specs` | 0.0945s | 0.0928s | +0.0017s | worse |
| `ngap_rel18.6_specs` | 0.0659s | 0.0651s | +0.0008s | worse |
| `lteNRRCC` | 0.1290s | 0.1273s | +0.0017s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 55.81 MB | 22.7% | 110.0% |
| `f1ap_rel18.6_specs` | 34.79 MB | 164.30 MB | 109.4% | 103.4% |
| `ngap_rel18.6_specs` | 24.56 MB | 116.72 MB | 111.1% | 106.8% |
| `lteNRRCC` | 74.79 MB | 102.75 MB | 104.7% | 104.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0348s | 0.0234s | +0.0114s | worse |
| `f1ap_rel18.6_specs` | 0.0733s | 0.0783s | -0.0050s | improved |
| `ngap_rel18.6_specs` | 0.0591s | 0.0498s | +0.0093s | worse |
| `lteNRRCC` | 0.0932s | 0.0740s | +0.0192s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.28 MB | 6.08 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.22 MB | 4.80 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 1.33 MB | 4.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.56 MB | 2.53 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0413s | 0.0431s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1179s | -0.0061s | improved |
| `ngap_rel18.6_specs` | 0.0802s | 0.0833s | -0.0031s | improved |
| `lteNRRCC` | 0.1297s | 0.1458s | -0.0161s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.11 MB | 8.88 MB | 103.0% | 207.8% |
| `f1ap_rel18.6_specs` | 8.66 MB | 8.66 MB | 96.6% | 164.8% |
| `ngap_rel18.6_specs` | 8.17 MB | 8.23 MB | 158.9% | 162.9% |
| `lteNRRCC` | 8.28 MB | 8.59 MB | 79.2% | 116.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0454s | 0.0332s | +0.0122s | worse |
| `f1ap_rel18.6_specs` | 0.1309s | 0.0952s | +0.0357s | worse |
| `ngap_rel18.6_specs` | 0.0793s | 0.0667s | +0.0126s | worse |
| `lteNRRCC` | 0.1326s | 0.1132s | +0.0194s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.95 MB | 8.60 MB | 77.4% | 80.0% |
| `f1ap_rel18.6_specs` | 9.59 MB | 127.49 MB | 208.3% | 156.3% |
| `ngap_rel18.6_specs` | 9.03 MB | 9.50 MB | 77.9% | 87.4% |
| `lteNRRCC` | 9.31 MB | 98.83 MB | 94.1% | 107.3% |
<!-- BENCH_RESULTS_END -->
