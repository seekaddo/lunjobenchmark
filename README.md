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
Generated: 2026-06-26T23:14:57.388456+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0348s | +0.0009s | worse |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1127s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0748s | 0.0769s | -0.0021s | improved |
| `lteNRRCC` | 0.1193s | 0.1230s | -0.0037s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.87 MB | 53.55 MB | 19.4% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 106.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0338s | 0.0363s | -0.0025s | improved |
| `f1ap_rel18.6_specs` | 0.0912s | 0.0951s | -0.0039s | improved |
| `ngap_rel18.6_specs` | 0.0632s | 0.0667s | -0.0035s | improved |
| `lteNRRCC` | 0.1225s | 0.1324s | -0.0099s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.32 MB | 36.67 MB | 24.7% | 107.1% |
| `f1ap_rel18.6_specs` | 21.73 MB | 103.06 MB | 109.7% | 105.4% |
| `ngap_rel18.6_specs` | 17.76 MB | 74.59 MB | 107.7% | 107.0% |
| `lteNRRCC` | 48.04 MB | 66.36 MB | 103.2% | 104.2% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0350s | 0.0332s | +0.0018s | worse |
| `f1ap_rel18.6_specs` | 0.0930s | 0.0902s | +0.0028s | worse |
| `ngap_rel18.6_specs` | 0.0648s | 0.0631s | +0.0017s | worse |
| `lteNRRCC` | 0.1292s | 0.1183s | +0.0109s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.47 MB | 55.83 MB | 85.2% | 106.9% |
| `f1ap_rel18.6_specs` | 35.26 MB | 164.39 MB | 109.4% | 103.4% |
| `ngap_rel18.6_specs` | 24.27 MB | 117.70 MB | 111.5% | 104.7% |
| `lteNRRCC` | 74.90 MB | 102.06 MB | 103.1% | 102.7% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0323s | 0.0245s | +0.0078s | worse |
| `f1ap_rel18.6_specs` | 0.0896s | 0.0683s | +0.0213s | worse |
| `ngap_rel18.6_specs` | 0.0615s | 0.0519s | +0.0096s | worse |
| `lteNRRCC` | 0.1047s | 0.0772s | +0.0275s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.50 MB | 8.33 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 5.48 MB | 9.02 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 7.84 MB | 8.27 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.95 MB | 7.69 MB | 0.0% | 0.1% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0412s | 0.0400s | +0.0012s | worse |
| `f1ap_rel18.6_specs` | 0.1098s | 0.1117s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0776s | 0.0766s | +0.0010s | worse |
| `lteNRRCC` | 0.1385s | 0.1385s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.32 MB | 7.30 MB | 161.9% | 165.0% |
| `f1ap_rel18.6_specs` | 7.84 MB | 106.63 MB | 166.4% | 106.2% |
| `ngap_rel18.6_specs` | 7.55 MB | 7.61 MB | 81.4% | 159.8% |
| `lteNRRCC` | 51.84 MB | 50.95 MB | 116.9% | 108.2% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0440s | 0.0407s | +0.0033s | worse |
| `f1ap_rel18.6_specs` | 0.1288s | 0.1147s | +0.0141s | worse |
| `ngap_rel18.6_specs` | 0.0893s | 0.0795s | +0.0098s | worse |
| `lteNRRCC` | 0.1362s | 0.1310s | +0.0052s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.26 MB | 9.64 MB | 161.7% | 159.9% |
| `f1ap_rel18.6_specs` | 10.43 MB | 10.43 MB | 161.9% | 95.7% |
| `ngap_rel18.6_specs` | 10.19 MB | 9.48 MB | 158.7% | 160.3% |
| `lteNRRCC` | 9.30 MB | 98.78 MB | 115.6% | 157.4% |
<!-- BENCH_RESULTS_END -->
