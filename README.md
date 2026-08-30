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
Generated: 2026-08-30T14:45:49.636922+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0360s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1126s | 0.1127s | -0.0001s | improved |
| `ngap_rel18.6_specs` | 0.0768s | 0.0778s | -0.0010s | improved |
| `lteNRRCC` | 0.1209s | 0.1222s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 17.3% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 104.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0292s | 0.0289s | +0.0003s | worse |
| `f1ap_rel18.6_specs` | 0.0764s | 0.0787s | -0.0023s | improved |
| `ngap_rel18.6_specs` | 0.0536s | 0.0534s | +0.0002s | worse |
| `lteNRRCC` | 0.1006s | 0.1016s | -0.0010s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 36.39 MB | 66.7% | 104.8% |
| `f1ap_rel18.6_specs` | 22.35 MB | 103.09 MB | 104.2% | 102.2% |
| `ngap_rel18.6_specs` | 18.02 MB | 74.26 MB | 105.0% | 105.9% |
| `lteNRRCC` | 48.18 MB | 65.96 MB | 102.1% | 101.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0333s | 0.0346s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0898s | 0.0923s | -0.0025s | improved |
| `ngap_rel18.6_specs` | 0.0627s | 0.0651s | -0.0024s | improved |
| `lteNRRCC` | 0.1157s | 0.1224s | -0.0067s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.54 MB | 55.20 MB | 74.1% | 103.8% |
| `f1ap_rel18.6_specs` | 34.32 MB | 164.52 MB | 103.6% | 103.7% |
| `ngap_rel18.6_specs` | 24.25 MB | 117.84 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.82 MB | 102.78 MB | 101.7% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0438s | 0.0194s | +0.0244s | worse |
| `f1ap_rel18.6_specs` | 0.0668s | 0.0670s | -0.0002s | improved |
| `ngap_rel18.6_specs` | 0.0462s | 0.0458s | +0.0004s | worse |
| `lteNRRCC` | 0.0766s | 0.0751s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 4.70 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.02 MB | 9.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.31 MB | 8.47 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.16 MB | 7.22 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0308s | +0.0069s | worse |
| `f1ap_rel18.6_specs` | 0.1051s | 0.0853s | +0.0198s | worse |
| `ngap_rel18.6_specs` | 0.0735s | 0.0588s | +0.0147s | worse |
| `lteNRRCC` | 0.1353s | 0.0947s | +0.0406s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.38 MB | 0.0% | 165.8% |
| `f1ap_rel18.6_specs` | 8.37 MB | 8.47 MB | 163.3% | 117.4% |
| `ngap_rel18.6_specs` | 7.91 MB | 7.55 MB | 163.6% | 81.8% |
| `lteNRRCC` | 8.29 MB | 57.58 MB | 108.6% | 105.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0383s | 0.0397s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.1094s | 0.1098s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0758s | 0.0776s | -0.0018s | improved |
| `lteNRRCC` | 0.1253s | 0.1276s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.17 MB | 8.80 MB | 0.0% | 158.5% |
| `f1ap_rel18.6_specs` | 9.57 MB | 164.20 MB | 93.9% | 158.0% |
| `ngap_rel18.6_specs` | 8.96 MB | 9.15 MB | 80.9% | 78.1% |
| `lteNRRCC` | 73.68 MB | 87.41 MB | 156.1% | 106.7% |
<!-- BENCH_RESULTS_END -->
