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
Generated: 2026-07-17T22:55:27.067872+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0358s | 0.0348s | +0.0010s | worse |
| `f1ap_rel18.6_specs` | 0.1109s | 0.1102s | +0.0007s | worse |
| `ngap_rel18.6_specs` | 0.0760s | 0.0759s | +0.0001s | worse |
| `lteNRRCC` | 0.1201s | 0.1194s | +0.0007s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 22.0% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.7% | 104.6% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 104.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0264s | +0.0099s | worse |
| `f1ap_rel18.6_specs` | 0.0971s | 0.0725s | +0.0246s | worse |
| `ngap_rel18.6_specs` | 0.0709s | 0.0515s | +0.0194s | worse |
| `lteNRRCC` | 0.1326s | 0.0971s | +0.0355s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 35.66 MB | 75.0% | 110.3% |
| `f1ap_rel18.6_specs` | 22.24 MB | 103.28 MB | 109.1% | 103.3% |
| `ngap_rel18.6_specs` | 17.59 MB | 74.16 MB | 111.1% | 104.4% |
| `lteNRRCC` | 48.34 MB | 66.16 MB | 104.6% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0337s | +0.0014s | worse |
| `f1ap_rel18.6_specs` | 0.0936s | 0.0906s | +0.0030s | worse |
| `ngap_rel18.6_specs` | 0.0647s | 0.0635s | +0.0012s | worse |
| `lteNRRCC` | 0.1272s | 0.1182s | +0.0090s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.52 MB | 55.56 MB | 22.4% | 106.9% |
| `f1ap_rel18.6_specs` | 34.47 MB | 164.65 MB | 106.2% | 103.4% |
| `ngap_rel18.6_specs` | 24.12 MB | 117.34 MB | 111.1% | 107.0% |
| `lteNRRCC` | 74.55 MB | 102.84 MB | 104.8% | 104.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0434s | 0.0415s | +0.0019s | worse |
| `f1ap_rel18.6_specs` | 0.1008s | 0.1121s | -0.0113s | improved |
| `ngap_rel18.6_specs` | 0.0681s | 0.0812s | -0.0131s | improved |
| `lteNRRCC` | 0.1155s | 0.1230s | -0.0075s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.61 MB | 7.12 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 9.16 MB | 6.67 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.41 MB | 10.80 MB | 0.0% | 0.0% |
| `lteNRRCC` | 8.73 MB | 8.47 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0330s | 0.0400s | -0.0070s | improved |
| `f1ap_rel18.6_specs` | 0.0925s | 0.1098s | -0.0173s | improved |
| `ngap_rel18.6_specs` | 0.0667s | 0.0775s | -0.0108s | improved |
| `lteNRRCC` | 0.1234s | 0.1405s | -0.0171s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.40 MB | 8.39 MB | 107.8% | 111.2% |
| `f1ap_rel18.6_specs` | 8.98 MB | 8.73 MB | 130.7% | 199.6% |
| `ngap_rel18.6_specs` | 8.18 MB | 8.88 MB | 0.0% | 118.8% |
| `lteNRRCC` | 8.60 MB | 61.17 MB | 195.7% | 133.9% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0407s | 0.0446s | -0.0039s | improved |
| `f1ap_rel18.6_specs` | 0.1154s | 0.1290s | -0.0136s | improved |
| `ngap_rel18.6_specs` | 0.0864s | 0.0873s | -0.0009s | improved |
| `lteNRRCC` | 0.1059s | 0.1439s | -0.0380s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.55 MB | 10.39 MB | 141.6% | 126.9% |
| `f1ap_rel18.6_specs` | 11.05 MB | 130.29 MB | 95.4% | 104.7% |
| `ngap_rel18.6_specs` | 10.63 MB | 10.63 MB | 265.5% | 94.8% |
| `lteNRRCC` | 9.61 MB | 90.93 MB | 187.2% | 142.5% |
<!-- BENCH_RESULTS_END -->
