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
Generated: 2026-08-18T10:35:15.232436+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0354s | 0.0357s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.1128s | 0.1122s | +0.0006s | worse |
| `ngap_rel18.6_specs` | 0.0760s | 0.0777s | -0.0017s | improved |
| `lteNRRCC` | 0.1199s | 0.1206s | -0.0007s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 16.4% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 103.1% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0347s | 0.0364s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.0952s | 0.0949s | +0.0003s | worse |
| `ngap_rel18.6_specs` | 0.0672s | 0.0667s | +0.0005s | worse |
| `lteNRRCC` | 0.1281s | 0.1296s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.60 MB | 36.41 MB | 16.9% | 103.8% |
| `f1ap_rel18.6_specs` | 21.32 MB | 103.27 MB | 103.2% | 101.8% |
| `ngap_rel18.6_specs` | 17.88 MB | 74.22 MB | 108.0% | 102.4% |
| `lteNRRCC` | 48.18 MB | 65.68 MB | 100.0% | 102.7% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0365s | 0.0379s | -0.0014s | improved |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0916s | +0.0045s | worse |
| `ngap_rel18.6_specs` | 0.0684s | 0.0649s | +0.0035s | worse |
| `lteNRRCC` | 0.1300s | 0.1177s | +0.0123s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 55.88 MB | 78.6% | 107.1% |
| `f1ap_rel18.6_specs` | 34.53 MB | 164.36 MB | 103.2% | 103.4% |
| `ngap_rel18.6_specs` | 24.46 MB | 117.53 MB | 103.8% | 102.3% |
| `lteNRRCC` | 74.60 MB | 102.34 MB | 101.6% | 101.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0238s | 0.0223s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.0956s | 0.0670s | +0.0286s | worse |
| `ngap_rel18.6_specs` | 0.0745s | 0.0455s | +0.0290s | worse |
| `lteNRRCC` | 0.0914s | 0.0762s | +0.0152s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.12 MB | 7.91 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 8.89 MB | 9.00 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 5.12 MB | 8.72 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.75 MB | 7.72 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0390s | 0.0549s | -0.0159s | improved |
| `f1ap_rel18.6_specs` | 0.1087s | 0.1196s | -0.0109s | improved |
| `ngap_rel18.6_specs` | 0.0752s | 0.0848s | -0.0096s | improved |
| `lteNRRCC` | 0.1391s | 0.1461s | -0.0070s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.81 MB | 0.0% | 104.1% |
| `f1ap_rel18.6_specs` | 8.86 MB | 8.43 MB | 215.7% | 233.6% |
| `ngap_rel18.6_specs` | 7.68 MB | 7.61 MB | 157.3% | 82.4% |
| `lteNRRCC` | 51.84 MB | 51.55 MB | 108.2% | 116.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0391s | 0.0454s | -0.0063s | improved |
| `f1ap_rel18.6_specs` | 0.1170s | 0.1245s | -0.0075s | improved |
| `ngap_rel18.6_specs` | 0.0771s | 0.0867s | -0.0096s | improved |
| `lteNRRCC` | 0.1281s | 0.1346s | -0.0065s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.79 MB | 0.0% | 75.7% |
| `f1ap_rel18.6_specs` | 10.06 MB | 9.94 MB | 152.4% | 148.1% |
| `ngap_rel18.6_specs` | 10.70 MB | 9.15 MB | 110.0% | 154.2% |
| `lteNRRCC` | 73.78 MB | 92.80 MB | 147.1% | 148.3% |
<!-- BENCH_RESULTS_END -->
