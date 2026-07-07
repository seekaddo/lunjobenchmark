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
Generated: 2026-07-07T23:07:44.123328+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0350s | -0.0009s | improved |
| `f1ap_rel18.6_specs` | 0.1093s | 0.1102s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0738s | 0.0755s | -0.0017s | improved |
| `lteNRRCC` | 0.1179s | 0.1180s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 6.7% | 111.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 109.1% | 106.4% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0277s | +0.0074s | worse |
| `f1ap_rel18.6_specs` | 0.0920s | 0.0752s | +0.0168s | worse |
| `ngap_rel18.6_specs` | 0.0649s | 0.0538s | +0.0111s | worse |
| `lteNRRCC` | 0.1280s | 0.0984s | +0.0296s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.29 MB | 36.34 MB | 81.5% | 111.1% |
| `f1ap_rel18.6_specs` | 21.76 MB | 102.70 MB | 109.4% | 105.3% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.59 MB | 111.5% | 107.0% |
| `lteNRRCC` | 48.76 MB | 66.04 MB | 103.1% | 104.1% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0279s | 0.0365s | -0.0086s | improved |
| `f1ap_rel18.6_specs` | 0.0751s | 0.1043s | -0.0292s | improved |
| `ngap_rel18.6_specs` | 0.0515s | 0.0721s | -0.0206s | improved |
| `lteNRRCC` | 0.1009s | 0.1204s | -0.0195s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 19.11 MB | 55.72 MB | 87.0% | 113.6% |
| `f1ap_rel18.6_specs` | 35.24 MB | 164.74 MB | 108.0% | 104.3% |
| `ngap_rel18.6_specs` | 24.36 MB | 117.75 MB | 115.0% | 105.9% |
| `lteNRRCC` | 74.97 MB | 102.86 MB | 104.1% | 103.4% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0218s | 0.0240s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0693s | 0.0730s | -0.0037s | improved |
| `ngap_rel18.6_specs` | 0.0465s | 0.0614s | -0.0149s | improved |
| `lteNRRCC` | 0.0770s | 0.0817s | -0.0047s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 4.75 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.17 MB | 4.95 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.02 MB | 4.41 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.78 MB | 4.27 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0405s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1080s | 0.1158s | -0.0078s | improved |
| `ngap_rel18.6_specs` | 0.0763s | 0.0803s | -0.0040s | improved |
| `lteNRRCC` | 0.1391s | 0.1413s | -0.0022s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.33 MB | 7.38 MB | 161.7% | 161.3% |
| `f1ap_rel18.6_specs` | 8.05 MB | 8.71 MB | 163.4% | 223.5% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.18 MB | 116.1% | 230.7% |
| `lteNRRCC` | 51.72 MB | 49.48 MB | 112.5% | 106.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0399s | 0.0392s | +0.0007s | worse |
| `f1ap_rel18.6_specs` | 0.1092s | 0.1124s | -0.0032s | improved |
| `ngap_rel18.6_specs` | 0.0774s | 0.0779s | -0.0005s | improved |
| `lteNRRCC` | 0.1290s | 0.1283s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.66 MB | 10.30 MB | 165.7% | 230.5% |
| `f1ap_rel18.6_specs` | 9.62 MB | 162.79 MB | 80.6% | 161.8% |
| `ngap_rel18.6_specs` | 8.76 MB | 8.89 MB | 98.0% | 187.8% |
| `lteNRRCC` | 8.43 MB | 90.51 MB | 79.1% | 159.4% |
<!-- BENCH_RESULTS_END -->
