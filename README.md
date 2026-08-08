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
Generated: 2026-08-08T10:39:57.252896+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0340s | 0.0351s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1087s | 0.1077s | +0.0010s | worse |
| `ngap_rel18.6_specs` | 0.0743s | 0.0741s | +0.0002s | worse |
| `lteNRRCC` | 0.1174s | 0.1179s | -0.0005s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 78.3% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0373s | 0.0342s | +0.0031s | worse |
| `f1ap_rel18.6_specs` | 0.0951s | 0.0928s | +0.0023s | worse |
| `ngap_rel18.6_specs` | 0.0664s | 0.0647s | +0.0017s | worse |
| `lteNRRCC` | 0.1269s | 0.1251s | +0.0018s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.42 MB | 70.0% | 103.6% |
| `f1ap_rel18.6_specs` | 22.15 MB | 103.31 MB | 103.0% | 101.7% |
| `ngap_rel18.6_specs` | 17.57 MB | 74.30 MB | 107.7% | 104.5% |
| `lteNRRCC` | 48.66 MB | 66.38 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0342s | 0.0355s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0903s | 0.1002s | -0.0099s | improved |
| `ngap_rel18.6_specs` | 0.0614s | 0.0682s | -0.0068s | improved |
| `lteNRRCC` | 0.1248s | 0.1138s | +0.0110s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.25 MB | 55.82 MB | 74.1% | 103.8% |
| `f1ap_rel18.6_specs` | 34.05 MB | 164.50 MB | 100.0% | 101.9% |
| `ngap_rel18.6_specs` | 24.53 MB | 117.21 MB | 104.3% | 102.5% |
| `lteNRRCC` | 74.62 MB | 101.90 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0218s | 0.0363s | -0.0145s | improved |
| `f1ap_rel18.6_specs` | 0.0718s | 0.1026s | -0.0308s | improved |
| `ngap_rel18.6_specs` | 0.0498s | 0.0640s | -0.0142s | improved |
| `lteNRRCC` | 0.0793s | 0.1170s | -0.0377s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.97 MB | 5.48 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 2.95 MB | 4.38 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.83 MB | 4.44 MB | 0.4% | 0.0% |
| `lteNRRCC` | 3.83 MB | 3.84 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0383s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1085s | 0.1050s | +0.0035s | worse |
| `ngap_rel18.6_specs` | 0.0761s | 0.0735s | +0.0026s | worse |
| `lteNRRCC` | 0.1409s | 0.1366s | +0.0043s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.51 MB | 0.0% | 160.7% |
| `f1ap_rel18.6_specs` | 8.12 MB | 8.10 MB | 160.9% | 81.1% |
| `ngap_rel18.6_specs` | 8.00 MB | 7.62 MB | 78.3% | 160.9% |
| `lteNRRCC` | 47.44 MB | 52.27 MB | 160.7% | 159.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0476s | -0.0090s | improved |
| `f1ap_rel18.6_specs` | 0.1162s | 0.1416s | -0.0254s | improved |
| `ngap_rel18.6_specs` | 0.0796s | 0.0963s | -0.0167s | improved |
| `lteNRRCC` | 0.1320s | 0.1384s | -0.0064s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.93 MB | 0.0% | 89.5% |
| `f1ap_rel18.6_specs` | 9.81 MB | 11.03 MB | 153.6% | 111.2% |
| `ngap_rel18.6_specs` | 9.02 MB | 9.27 MB | 155.7% | 151.1% |
| `lteNRRCC` | 8.68 MB | 74.15 MB | 151.9% | 103.7% |
<!-- BENCH_RESULTS_END -->
