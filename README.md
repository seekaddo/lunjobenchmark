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
Generated: 2026-10-06T16:38:20.210602+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0341s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.1107s | 0.1070s | +0.0037s | worse |
| `ngap_rel18.6_specs` | 0.0758s | 0.0752s | +0.0006s | worse |
| `lteNRRCC` | 0.1215s | 0.1184s | +0.0031s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 70.8% | 103.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.5% | 102.1% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0332s | 0.0369s | -0.0037s | improved |
| `f1ap_rel18.6_specs` | 0.1001s | 0.1006s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0664s | 0.0693s | -0.0029s | improved |
| `lteNRRCC` | 0.1200s | 0.1349s | -0.0149s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.74 MB | 36.57 MB | 81.0% | 104.2% |
| `f1ap_rel18.6_specs` | 22.41 MB | 103.07 MB | 103.6% | 101.8% |
| `ngap_rel18.6_specs` | 18.12 MB | 74.61 MB | 104.5% | 104.9% |
| `lteNRRCC` | 48.73 MB | 66.05 MB | 101.8% | 101.5% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0290s | 0.0350s | -0.0060s | improved |
| `f1ap_rel18.6_specs` | 0.0865s | 0.0998s | -0.0133s | improved |
| `ngap_rel18.6_specs` | 0.0530s | 0.0692s | -0.0162s | improved |
| `lteNRRCC` | 0.1022s | 0.1167s | -0.0145s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.70 MB | 55.89 MB | 64.0% | 104.5% |
| `f1ap_rel18.6_specs` | 34.59 MB | 164.66 MB | 104.3% | 102.2% |
| `ngap_rel18.6_specs` | 23.78 MB | 117.22 MB | 110.5% | 102.9% |
| `lteNRRCC` | 74.76 MB | 102.42 MB | 102.1% | 103.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0268s | 0.0368s | -0.0100s | improved |
| `f1ap_rel18.6_specs` | 0.0976s | 0.0985s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0543s | 0.0915s | -0.0372s | improved |
| `lteNRRCC` | 0.0953s | 0.0914s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.58 MB | 4.80 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.62 MB | 9.05 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.86 MB | 8.55 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.11 MB | 9.70 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0286s | +0.0102s | worse |
| `f1ap_rel18.6_specs` | 0.1056s | 0.0774s | +0.0282s | worse |
| `ngap_rel18.6_specs` | 0.0739s | 0.0554s | +0.0185s | worse |
| `lteNRRCC` | 0.1368s | 0.0919s | +0.0449s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.44 MB | 7.32 MB | 0.0% | 164.9% |
| `f1ap_rel18.6_specs` | 7.94 MB | 8.01 MB | 82.1% | 81.7% |
| `ngap_rel18.6_specs` | 7.52 MB | 7.58 MB | 164.8% | 159.4% |
| `lteNRRCC` | 51.79 MB | 55.30 MB | 106.7% | 159.6% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0360s | 0.0415s | -0.0055s | improved |
| `f1ap_rel18.6_specs` | 0.0988s | 0.1170s | -0.0182s | improved |
| `ngap_rel18.6_specs` | 0.0687s | 0.0855s | -0.0168s | improved |
| `lteNRRCC` | 0.1112s | 0.1304s | -0.0192s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.14 MB | 0.0% | 140.1% |
| `f1ap_rel18.6_specs` | 11.13 MB | 164.18 MB | 135.7% | 139.5% |
| `ngap_rel18.6_specs` | 10.24 MB | 10.77 MB | 140.5% | 138.3% |
| `lteNRRCC` | 9.16 MB | 98.81 MB | 140.3% | 140.0% |
<!-- BENCH_RESULTS_END -->
