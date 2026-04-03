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
Generated: 2026-04-03T10:52:09.895526+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0359s | 0.0357s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1150s | 0.1116s | +0.0034s | worse |
| `ngap_rel18.6_specs` | 0.0803s | 0.0769s | +0.0034s | worse |
| `lteNRRCC` | 0.1213s | 0.1210s | +0.0003s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.93 MB | 53.55 MB | 6.4% | 113.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.3% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 107.7% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0325s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0928s | 0.0955s | -0.0027s | improved |
| `ngap_rel18.6_specs` | 0.0657s | 0.0675s | -0.0018s | improved |
| `lteNRRCC` | 0.1286s | 0.1195s | +0.0091s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 35.62 MB | 28.1% | 110.7% |
| `f1ap_rel18.6_specs` | 21.67 MB | 103.16 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.56 MB | 74.37 MB | 107.4% | 106.8% |
| `lteNRRCC` | 48.49 MB | 66.29 MB | 104.6% | 104.0% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0325s | 0.0347s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0878s | 0.0926s | -0.0048s | improved |
| `ngap_rel18.6_specs` | 0.0615s | 0.0655s | -0.0040s | improved |
| `lteNRRCC` | 0.1148s | 0.1177s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.30 MB | 55.49 MB | 92.0% | 107.4% |
| `f1ap_rel18.6_specs` | 34.52 MB | 164.66 MB | 113.8% | 103.6% |
| `ngap_rel18.6_specs` | 24.29 MB | 117.62 MB | 108.0% | 107.3% |
| `lteNRRCC` | 74.98 MB | 102.80 MB | 105.3% | 104.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0319s | 0.0208s | +0.0111s | worse |
| `f1ap_rel18.6_specs` | 0.0640s | 0.0640s | +0.0000s | flat |
| `ngap_rel18.6_specs` | 0.0438s | 0.0441s | -0.0003s | improved |
| `lteNRRCC` | 0.0779s | 0.0732s | +0.0047s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.53 MB | 4.14 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 6.98 MB | 4.28 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.97 MB | 4.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.88 MB | 3.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0331s | 0.0423s | -0.0092s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.1188s | -0.0246s | improved |
| `ngap_rel18.6_specs` | 0.0648s | 0.0816s | -0.0168s | improved |
| `lteNRRCC` | 0.1121s | 0.1360s | -0.0239s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.81 MB | 7.62 MB | 103.8% | 105.7% |
| `f1ap_rel18.6_specs` | 8.43 MB | 106.63 MB | 217.2% | 104.5% |
| `ngap_rel18.6_specs` | 8.23 MB | 8.36 MB | 103.0% | 131.2% |
| `lteNRRCC` | 8.53 MB | 59.37 MB | 201.8% | 103.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0449s | 0.0390s | +0.0059s | worse |
| `f1ap_rel18.6_specs` | 0.1237s | 0.1118s | +0.0119s | worse |
| `ngap_rel18.6_specs` | 0.0859s | 0.0765s | +0.0094s | worse |
| `lteNRRCC` | 0.1321s | 0.1259s | +0.0062s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.64 MB | 9.58 MB | 164.6% | 161.2% |
| `f1ap_rel18.6_specs` | 11.13 MB | 10.30 MB | 117.5% | 81.0% |
| `ngap_rel18.6_specs` | 9.34 MB | 9.65 MB | 179.4% | 82.3% |
| `lteNRRCC` | 8.61 MB | 9.36 MB | 163.4% | 114.9% |
<!-- BENCH_RESULTS_END -->
