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
Generated: 2026-05-18T13:53:09.361922+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0379s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.1125s | 0.1160s | -0.0035s | improved |
| `ngap_rel18.6_specs` | 0.0780s | 0.0809s | -0.0029s | improved |
| `lteNRRCC` | 0.1199s | 0.1242s | -0.0043s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.95 MB | 53.55 MB | 28.2% | 110.3% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 104.0% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.1% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0339s | 0.0357s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0917s | 0.0953s | -0.0036s | improved |
| `ngap_rel18.6_specs` | 0.0640s | 0.0680s | -0.0040s | improved |
| `lteNRRCC` | 0.1238s | 0.1298s | -0.0060s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.85 MB | 36.03 MB | 19.5% | 110.3% |
| `f1ap_rel18.6_specs` | 22.18 MB | 102.94 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 16.81 MB | 74.30 MB | 111.1% | 106.8% |
| `lteNRRCC` | 48.34 MB | 66.34 MB | 104.8% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0327s | 0.0328s | -0.0001s | improved |
| `f1ap_rel18.6_specs` | 0.0890s | 0.0895s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0619s | 0.0618s | +0.0001s | worse |
| `lteNRRCC` | 0.1156s | 0.1156s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.74 MB | 55.66 MB | 95.7% | 111.1% |
| `f1ap_rel18.6_specs` | 35.11 MB | 164.55 MB | 110.3% | 105.5% |
| `ngap_rel18.6_specs` | 24.48 MB | 117.56 MB | 112.5% | 107.3% |
| `lteNRRCC` | 74.89 MB | 102.75 MB | 105.2% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0442s | -0.0106s | improved |
| `f1ap_rel18.6_specs` | 0.0732s | 0.0684s | +0.0048s | worse |
| `ngap_rel18.6_specs` | 0.0475s | 0.0512s | -0.0037s | improved |
| `lteNRRCC` | 0.0981s | 0.0781s | +0.0200s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 1.53 MB | 4.00 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.61 MB | 1.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 2.30 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.66 MB | 3.92 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0441s | 0.0347s | +0.0094s | worse |
| `f1ap_rel18.6_specs` | 0.1192s | 0.0957s | +0.0235s | worse |
| `ngap_rel18.6_specs` | 0.0799s | 0.0651s | +0.0148s | worse |
| `lteNRRCC` | 0.1418s | 0.1128s | +0.0290s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.00 MB | 7.85 MB | 83.4% | 165.9% |
| `f1ap_rel18.6_specs` | 10.11 MB | 106.57 MB | 174.6% | 106.1% |
| `ngap_rel18.6_specs` | 8.13 MB | 9.37 MB | 209.8% | 196.5% |
| `lteNRRCC` | 9.73 MB | 68.61 MB | 86.7% | 106.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0388s | 0.0432s | -0.0044s | improved |
| `f1ap_rel18.6_specs` | 0.1130s | 0.1256s | -0.0126s | improved |
| `ngap_rel18.6_specs` | 0.0784s | 0.0878s | -0.0094s | improved |
| `lteNRRCC` | 0.1281s | 0.1447s | -0.0166s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.48 MB | 8.61 MB | 110.9% | 159.6% |
| `f1ap_rel18.6_specs` | 11.22 MB | 164.21 MB | 112.6% | 151.8% |
| `ngap_rel18.6_specs` | 8.97 MB | 9.46 MB | 158.9% | 96.8% |
| `lteNRRCC` | 8.91 MB | 88.89 MB | 93.7% | 165.1% |
<!-- BENCH_RESULTS_END -->
