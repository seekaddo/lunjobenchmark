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
Generated: 2026-09-08T14:19:06.393098+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0362s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1106s | +0.0022s | worse |
| `ngap_rel18.6_specs` | 0.0771s | 0.0764s | +0.0007s | worse |
| `lteNRRCC` | 0.1211s | 0.1200s | +0.0011s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.74 MB | 53.55 MB | 82.6% | 103.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.0% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.0% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0355s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0950s | 0.0957s | -0.0007s | improved |
| `ngap_rel18.6_specs` | 0.0669s | 0.0675s | -0.0006s | improved |
| `lteNRRCC` | 0.1280s | 0.1300s | -0.0020s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.62 MB | 36.67 MB | 17.5% | 103.6% |
| `f1ap_rel18.6_specs` | 22.22 MB | 103.39 MB | 106.5% | 103.5% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.51 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.41 MB | 66.38 MB | 101.6% | 101.3% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0357s | -0.0010s | improved |
| `f1ap_rel18.6_specs` | 0.0907s | 0.0958s | -0.0051s | improved |
| `ngap_rel18.6_specs` | 0.0639s | 0.0674s | -0.0035s | improved |
| `lteNRRCC` | 0.1175s | 0.1298s | -0.0123s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.43 MB | 55.25 MB | 65.6% | 103.7% |
| `f1ap_rel18.6_specs` | 35.25 MB | 164.36 MB | 107.1% | 101.8% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.23 MB | 108.7% | 102.4% |
| `lteNRRCC` | 74.76 MB | 102.80 MB | 101.7% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0208s | 0.0601s | -0.0393s | improved |
| `f1ap_rel18.6_specs` | 0.0839s | 0.1066s | -0.0227s | improved |
| `ngap_rel18.6_specs` | 0.0696s | 0.0730s | -0.0034s | improved |
| `lteNRRCC` | 0.0923s | 0.0875s | +0.0048s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.81 MB | 7.23 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.59 MB | 3.09 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.80 MB | 7.14 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.36 MB | 7.17 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0393s | 0.0396s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1066s | +0.0052s | worse |
| `ngap_rel18.6_specs` | 0.0814s | 0.0729s | +0.0085s | worse |
| `lteNRRCC` | 0.1434s | 0.1374s | +0.0060s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.39 MB | 7.44 MB | 172.1% | 158.6% |
| `f1ap_rel18.6_specs` | 8.61 MB | 106.65 MB | 103.4% | 110.2% |
| `ngap_rel18.6_specs` | 8.18 MB | 7.92 MB | 113.6% | 158.1% |
| `lteNRRCC` | 49.52 MB | 51.65 MB | 109.2% | 195.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0414s | 0.0396s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.1166s | 0.1146s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0844s | 0.0770s | +0.0074s | worse |
| `lteNRRCC` | 0.1261s | 0.1269s | -0.0008s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.29 MB | 10.09 MB | 122.9% | 110.0% |
| `f1ap_rel18.6_specs` | 10.25 MB | 140.11 MB | 125.5% | 128.7% |
| `ngap_rel18.6_specs` | 10.07 MB | 10.38 MB | 255.6% | 104.3% |
| `lteNRRCC` | 8.69 MB | 88.39 MB | 96.1% | 108.9% |
<!-- BENCH_RESULTS_END -->
