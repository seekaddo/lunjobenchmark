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
Generated: 2026-10-24T00:25:38.496039+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0339s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1129s | 0.1088s | +0.0041s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0738s | +0.0032s | worse |
| `lteNRRCC` | 0.1204s | 0.1188s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 59.4% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 100.0% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 100.0% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0361s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1035s | 0.0938s | +0.0097s | worse |
| `ngap_rel18.6_specs` | 0.0718s | 0.0663s | +0.0055s | worse |
| `lteNRRCC` | 0.1349s | 0.1302s | +0.0047s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 36.49 MB | 84.0% | 107.1% |
| `f1ap_rel18.6_specs` | 22.14 MB | 103.44 MB | 103.0% | 101.7% |
| `ngap_rel18.6_specs` | 18.06 MB | 74.57 MB | 104.0% | 104.7% |
| `lteNRRCC` | 48.78 MB | 66.28 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0227s | 0.0347s | -0.0120s | improved |
| `f1ap_rel18.6_specs` | 0.0614s | 0.0924s | -0.0310s | improved |
| `ngap_rel18.6_specs` | 0.0416s | 0.0640s | -0.0224s | improved |
| `lteNRRCC` | 0.0763s | 0.1188s | -0.0425s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.70 MB | 55.71 MB | 15.1% | 105.6% |
| `f1ap_rel18.6_specs` | 35.24 MB | 163.39 MB | 105.3% | 102.7% |
| `ngap_rel18.6_specs` | 24.50 MB | 117.05 MB | 100.0% | 102.9% |
| `lteNRRCC` | 74.94 MB | 102.95 MB | 102.7% | 102.2% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0225s | 0.0292s | -0.0067s | improved |
| `f1ap_rel18.6_specs` | 0.0783s | 0.0769s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0698s | 0.0506s | +0.0192s | worse |
| `lteNRRCC` | 0.0758s | 0.0857s | -0.0099s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.36 MB | 5.47 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.23 MB | 4.08 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.62 MB | 8.25 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.27 MB | 7.50 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0268s | +0.0146s | worse |
| `f1ap_rel18.6_specs` | 0.1114s | 0.0760s | +0.0354s | worse |
| `ngap_rel18.6_specs` | 0.0768s | 0.0525s | +0.0243s | worse |
| `lteNRRCC` | 0.1383s | 0.0884s | +0.0499s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.22 MB | 7.66 MB | 0.0% | 154.7% |
| `f1ap_rel18.6_specs` | 8.89 MB | 8.58 MB | 96.4% | 149.2% |
| `ngap_rel18.6_specs` | 8.15 MB | 8.09 MB | 156.7% | 148.5% |
| `lteNRRCC` | 8.45 MB | 68.15 MB | 162.0% | 204.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0473s | 0.0408s | +0.0065s | worse |
| `f1ap_rel18.6_specs` | 0.1395s | 0.1214s | +0.0181s | worse |
| `ngap_rel18.6_specs` | 0.0958s | 0.0814s | +0.0144s | worse |
| `lteNRRCC` | 0.1388s | 0.1373s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.14 MB | 0.0% | 158.8% |
| `f1ap_rel18.6_specs` | 10.42 MB | 133.90 MB | 90.4% | 159.7% |
| `ngap_rel18.6_specs` | 10.80 MB | 11.18 MB | 107.1% | 193.7% |
| `lteNRRCC` | 73.76 MB | 88.18 MB | 112.5% | 215.0% |
<!-- BENCH_RESULTS_END -->
