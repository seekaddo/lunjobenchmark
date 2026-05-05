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
Generated: 2026-05-05T11:21:09.704373+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0368s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.1175s | 0.1149s | +0.0026s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0785s | +0.0031s | worse |
| `lteNRRCC` | 0.1269s | 0.1257s | +0.0012s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.84 MB | 53.55 MB | 6.8% | 110.0% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.5% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 111.5% | 105.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 105.0% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0377s | 0.0349s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.0999s | 0.0938s | +0.0061s | worse |
| `ngap_rel18.6_specs` | 0.0706s | 0.0659s | +0.0047s | worse |
| `lteNRRCC` | 0.1336s | 0.1297s | +0.0039s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.29 MB | 36.73 MB | 100.0% | 109.7% |
| `f1ap_rel18.6_specs` | 21.77 MB | 103.41 MB | 111.8% | 104.8% |
| `ngap_rel18.6_specs` | 16.56 MB | 73.89 MB | 110.7% | 106.4% |
| `lteNRRCC` | 48.01 MB | 65.83 MB | 105.9% | 103.8% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0335s | 0.0353s | -0.0018s | improved |
| `f1ap_rel18.6_specs` | 0.0887s | 0.0947s | -0.0060s | improved |
| `ngap_rel18.6_specs` | 0.0617s | 0.0652s | -0.0035s | improved |
| `lteNRRCC` | 0.1151s | 0.1280s | -0.0129s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 16.27 MB | 55.65 MB | 17.7% | 110.7% |
| `f1ap_rel18.6_specs` | 33.94 MB | 164.53 MB | 106.7% | 105.4% |
| `ngap_rel18.6_specs` | 23.86 MB | 117.43 MB | 112.5% | 107.1% |
| `lteNRRCC` | 73.86 MB | 102.86 MB | 103.4% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0200s | 0.0222s | -0.0022s | improved |
| `f1ap_rel18.6_specs` | 0.0652s | 0.0694s | -0.0042s | improved |
| `ngap_rel18.6_specs` | 0.0413s | 0.0463s | -0.0050s | improved |
| `lteNRRCC` | 0.0725s | 0.0765s | -0.0040s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.47 MB | 4.11 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.62 MB | 4.33 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.81 MB | 3.97 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.89 MB | 3.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0398s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1079s | 0.1088s | -0.0009s | improved |
| `ngap_rel18.6_specs` | 0.0745s | 0.0778s | -0.0033s | improved |
| `lteNRRCC` | 0.1387s | 0.1267s | +0.0120s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.29 MB | 7.32 MB | 81.6% | 162.1% |
| `f1ap_rel18.6_specs` | 8.03 MB | 7.85 MB | 166.8% | 155.0% |
| `ngap_rel18.6_specs` | 7.54 MB | 8.11 MB | 161.8% | 109.2% |
| `lteNRRCC` | 47.50 MB | 50.14 MB | 157.8% | 169.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0386s | 0.0349s | +0.0037s | worse |
| `f1ap_rel18.6_specs` | 0.1123s | 0.0997s | +0.0126s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0696s | +0.0075s | worse |
| `lteNRRCC` | 0.1272s | 0.1129s | +0.0143s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.59 MB | 8.86 MB | 77.9% | 77.1% |
| `f1ap_rel18.6_specs` | 9.56 MB | 164.19 MB | 159.8% | 159.7% |
| `ngap_rel18.6_specs` | 9.02 MB | 9.15 MB | 80.6% | 157.6% |
| `lteNRRCC` | 8.50 MB | 73.90 MB | 80.8% | 157.5% |
<!-- BENCH_RESULTS_END -->
