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
Generated: 2026-08-07T10:58:37.938415+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0357s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1140s | 0.1118s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0775s | 0.0766s | +0.0009s | worse |
| `lteNRRCC` | 0.1208s | 0.1210s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 16.5% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0346s | 0.0345s | +0.0001s | worse |
| `f1ap_rel18.6_specs` | 0.0921s | 0.0953s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0650s | 0.0665s | -0.0015s | improved |
| `lteNRRCC` | 0.1267s | 0.1287s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 36.46 MB | 80.0% | 107.7% |
| `f1ap_rel18.6_specs` | 21.72 MB | 102.75 MB | 103.2% | 103.6% |
| `ngap_rel18.6_specs` | 17.62 MB | 74.27 MB | 104.0% | 104.9% |
| `lteNRRCC` | 48.07 MB | 66.42 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0337s | +0.0008s | worse |
| `f1ap_rel18.6_specs` | 0.0918s | 0.0899s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0641s | 0.0634s | +0.0007s | worse |
| `lteNRRCC` | 0.1187s | 0.1176s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.37 MB | 55.87 MB | 58.8% | 103.7% |
| `f1ap_rel18.6_specs` | 35.26 MB | 164.55 MB | 106.9% | 103.6% |
| `ngap_rel18.6_specs` | 24.57 MB | 117.77 MB | 104.2% | 104.7% |
| `lteNRRCC` | 74.61 MB | 102.48 MB | 103.4% | 101.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0323s | +0.0013s | worse |
| `f1ap_rel18.6_specs` | 0.0613s | 0.1017s | -0.0404s | improved |
| `ngap_rel18.6_specs` | 0.0429s | 0.0757s | -0.0328s | improved |
| `lteNRRCC` | 0.0752s | 0.1108s | -0.0356s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.31 MB | 4.97 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.03 MB | 4.56 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.81 MB | 4.81 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.77 MB | 4.25 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0402s | 0.0382s | +0.0020s | worse |
| `f1ap_rel18.6_specs` | 0.1102s | 0.1050s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0770s | 0.0735s | +0.0035s | worse |
| `lteNRRCC` | 0.1398s | 0.1369s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.33 MB | 7.98 MB | 0.0% | 219.8% |
| `f1ap_rel18.6_specs` | 8.54 MB | 106.65 MB | 83.4% | 106.5% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.24 MB | 81.0% | 82.0% |
| `lteNRRCC` | 51.64 MB | 62.48 MB | 104.2% | 170.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0377s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1213s | 0.1121s | +0.0092s | worse |
| `ngap_rel18.6_specs` | 0.0839s | 0.0774s | +0.0065s | worse |
| `lteNRRCC` | 0.1396s | 0.1288s | +0.0108s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.16 MB | 9.01 MB | 0.0% | 81.6% |
| `f1ap_rel18.6_specs` | 10.21 MB | 164.19 MB | 81.2% | 158.8% |
| `ngap_rel18.6_specs` | 9.41 MB | 9.41 MB | 162.1% | 160.5% |
| `lteNRRCC` | 73.03 MB | 101.69 MB | 106.7% | 158.7% |
<!-- BENCH_RESULTS_END -->
