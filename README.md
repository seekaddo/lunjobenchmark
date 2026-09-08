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
Generated: 2026-09-08T00:07:42.290553+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0362s | 0.0358s | +0.0004s | worse |
| `f1ap_rel18.6_specs` | 0.1106s | 0.1120s | -0.0014s | improved |
| `ngap_rel18.6_specs` | 0.0764s | 0.0757s | +0.0007s | worse |
| `lteNRRCC` | 0.1200s | 0.1203s | -0.0003s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 73.1% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0355s | 0.0326s | +0.0029s | worse |
| `f1ap_rel18.6_specs` | 0.0957s | 0.0936s | +0.0021s | worse |
| `ngap_rel18.6_specs` | 0.0675s | 0.0652s | +0.0023s | worse |
| `lteNRRCC` | 0.1300s | 0.1153s | +0.0147s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.60 MB | 35.91 MB | 71.0% | 103.6% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.31 MB | 106.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.93 MB | 74.08 MB | 103.8% | 102.3% |
| `lteNRRCC` | 48.62 MB | 66.10 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0286s | +0.0071s | worse |
| `f1ap_rel18.6_specs` | 0.0958s | 0.0753s | +0.0205s | worse |
| `ngap_rel18.6_specs` | 0.0674s | 0.0528s | +0.0146s | worse |
| `lteNRRCC` | 0.1298s | 0.1018s | +0.0280s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.65 MB | 55.34 MB | 17.7% | 103.6% |
| `f1ap_rel18.6_specs` | 35.23 MB | 164.73 MB | 103.2% | 101.7% |
| `ngap_rel18.6_specs` | 23.79 MB | 116.97 MB | 107.7% | 104.5% |
| `lteNRRCC` | 74.80 MB | 102.51 MB | 101.6% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0601s | 0.0217s | +0.0384s | worse |
| `f1ap_rel18.6_specs` | 0.1066s | 0.0638s | +0.0428s | worse |
| `ngap_rel18.6_specs` | 0.0730s | 0.0513s | +0.0217s | worse |
| `lteNRRCC` | 0.0875s | 0.0782s | +0.0093s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 6.72 MB | 8.41 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.16 MB | 8.89 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 3.94 MB | 8.28 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.02 MB | 4.81 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0345s | +0.0051s | worse |
| `f1ap_rel18.6_specs` | 0.1066s | 0.0955s | +0.0111s | worse |
| `ngap_rel18.6_specs` | 0.0729s | 0.0676s | +0.0053s | worse |
| `lteNRRCC` | 0.1374s | 0.1133s | +0.0241s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.71 MB | 7.83 MB | 93.5% | 222.8% |
| `f1ap_rel18.6_specs` | 8.62 MB | 8.00 MB | 170.9% | 180.2% |
| `ngap_rel18.6_specs` | 7.69 MB | 7.52 MB | 86.8% | 82.0% |
| `lteNRRCC` | 8.30 MB | 70.57 MB | 103.8% | 163.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0396s | 0.0408s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1146s | 0.1201s | -0.0055s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0831s | -0.0061s | improved |
| `lteNRRCC` | 0.1269s | 0.1376s | -0.0107s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.67 MB | 8.80 MB | 0.0% | 155.9% |
| `f1ap_rel18.6_specs` | 9.69 MB | 11.27 MB | 160.2% | 228.4% |
| `ngap_rel18.6_specs` | 10.38 MB | 10.89 MB | 108.2% | 114.0% |
| `lteNRRCC` | 8.56 MB | 95.56 MB | 158.5% | 106.2% |
<!-- BENCH_RESULTS_END -->
