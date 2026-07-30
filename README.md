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
Generated: 2026-07-30T23:14:12.433446+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0342s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1078s | 0.1082s | -0.0004s | improved |
| `ngap_rel18.6_specs` | 0.0749s | 0.0741s | +0.0008s | worse |
| `lteNRRCC` | 0.1190s | 0.1191s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.62 MB | 53.55 MB | 14.8% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0280s | +0.0082s | worse |
| `f1ap_rel18.6_specs` | 0.0978s | 0.0756s | +0.0222s | worse |
| `ngap_rel18.6_specs` | 0.0675s | 0.0529s | +0.0146s | worse |
| `lteNRRCC` | 0.1409s | 0.0993s | +0.0416s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.39 MB | 36.49 MB | 84.0% | 103.7% |
| `f1ap_rel18.6_specs` | 22.31 MB | 102.98 MB | 103.1% | 103.5% |
| `ngap_rel18.6_specs` | 17.58 MB | 74.44 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.21 MB | 66.24 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0349s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.0954s | 0.0927s | +0.0027s | worse |
| `ngap_rel18.6_specs` | 0.0672s | 0.0666s | +0.0006s | worse |
| `lteNRRCC` | 0.1302s | 0.1192s | +0.0110s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.31 MB | 54.94 MB | 20.8% | 106.9% |
| `f1ap_rel18.6_specs` | 34.79 MB | 163.44 MB | 106.5% | 103.4% |
| `ngap_rel18.6_specs` | 24.35 MB | 117.25 MB | 107.7% | 104.5% |
| `lteNRRCC` | 74.62 MB | 102.93 MB | 103.2% | 102.6% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0305s | 0.0239s | +0.0066s | worse |
| `f1ap_rel18.6_specs` | 0.1039s | 0.0653s | +0.0386s | worse |
| `ngap_rel18.6_specs` | 0.0756s | 0.0447s | +0.0309s | worse |
| `lteNRRCC` | 0.1141s | 0.0824s | +0.0317s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.08 MB | 4.27 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.33 MB | 8.53 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 9.66 MB | 10.77 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.88 MB | 5.94 MB | 1.2% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0403s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.1041s | 0.1117s | -0.0076s | improved |
| `ngap_rel18.6_specs` | 0.0728s | 0.0766s | -0.0038s | improved |
| `lteNRRCC` | 0.1366s | 0.1394s | -0.0028s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 7.82 MB | 0.0% | 111.3% |
| `f1ap_rel18.6_specs` | 8.55 MB | 8.71 MB | 116.6% | 233.4% |
| `ngap_rel18.6_specs` | 7.48 MB | 7.56 MB | 175.5% | 164.4% |
| `lteNRRCC` | 51.83 MB | 69.23 MB | 161.0% | 234.8% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0461s | 0.0455s | +0.0006s | worse |
| `f1ap_rel18.6_specs` | 0.1311s | 0.1232s | +0.0079s | worse |
| `ngap_rel18.6_specs` | 0.0906s | 0.0863s | +0.0043s | worse |
| `lteNRRCC` | 0.1377s | 0.1384s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.22 MB | 0.0% | 110.4% |
| `f1ap_rel18.6_specs` | 10.58 MB | 148.61 MB | 154.7% | 156.2% |
| `ngap_rel18.6_specs` | 10.12 MB | 10.26 MB | 218.1% | 88.9% |
| `lteNRRCC` | 68.23 MB | 77.52 MB | 110.2% | 153.3% |
<!-- BENCH_RESULTS_END -->
