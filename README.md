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
Generated: 2026-08-17T22:30:41.622021+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0365s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1122s | 0.1130s | -0.0008s | improved |
| `ngap_rel18.6_specs` | 0.0777s | 0.0804s | -0.0027s | improved |
| `lteNRRCC` | 0.1206s | 0.1219s | -0.0013s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.68 MB | 53.55 MB | 75.0% | 103.6% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.6% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 102.1% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.8% | 102.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0364s | 0.0258s | +0.0106s | worse |
| `f1ap_rel18.6_specs` | 0.0949s | 0.0780s | +0.0169s | worse |
| `ngap_rel18.6_specs` | 0.0667s | 0.0525s | +0.0142s | worse |
| `lteNRRCC` | 0.1296s | 0.0944s | +0.0352s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.60 MB | 36.74 MB | 77.8% | 103.7% |
| `f1ap_rel18.6_specs` | 21.76 MB | 103.41 MB | 103.1% | 101.8% |
| `ngap_rel18.6_specs` | 17.90 MB | 74.33 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.26 MB | 66.21 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0379s | 0.0357s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.0916s | 0.0938s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0649s | 0.0649s | +0.0000s | flat |
| `lteNRRCC` | 0.1177s | 0.1280s | -0.0103s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 55.82 MB | 75.0% | 103.7% |
| `f1ap_rel18.6_specs` | 34.79 MB | 164.69 MB | 103.4% | 103.6% |
| `ngap_rel18.6_specs` | 24.01 MB | 117.73 MB | 104.3% | 104.9% |
| `lteNRRCC` | 74.64 MB | 102.13 MB | 103.3% | 102.9% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0223s | 0.0218s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.0670s | 0.0817s | -0.0147s | improved |
| `ngap_rel18.6_specs` | 0.0455s | 0.0574s | -0.0119s | improved |
| `lteNRRCC` | 0.0762s | 0.0826s | -0.0064s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.19 MB | 4.59 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.59 MB | 4.97 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.81 MB | 4.00 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.03 MB | 3.95 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0549s | 0.0394s | +0.0155s | worse |
| `f1ap_rel18.6_specs` | 0.1196s | 0.1080s | +0.0116s | worse |
| `ngap_rel18.6_specs` | 0.0848s | 0.0782s | +0.0066s | worse |
| `lteNRRCC` | 0.1461s | 0.1275s | +0.0186s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.81 MB | 0.0% | 144.6% |
| `f1ap_rel18.6_specs` | 8.04 MB | 8.98 MB | 85.5% | 107.4% |
| `ngap_rel18.6_specs` | 8.11 MB | 8.24 MB | 80.9% | 181.3% |
| `lteNRRCC` | 8.41 MB | 51.99 MB | 141.8% | 148.1% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0454s | 0.0432s | +0.0022s | worse |
| `f1ap_rel18.6_specs` | 0.1245s | 0.1309s | -0.0064s | improved |
| `ngap_rel18.6_specs` | 0.0867s | 0.0891s | -0.0024s | improved |
| `lteNRRCC` | 0.1346s | 0.1331s | +0.0015s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.14 MB | 10.08 MB | 0.0% | 153.2% |
| `f1ap_rel18.6_specs` | 10.50 MB | 10.50 MB | 156.7% | 169.8% |
| `ngap_rel18.6_specs` | 10.80 MB | 10.30 MB | 230.3% | 91.1% |
| `lteNRRCC` | 8.80 MB | 101.70 MB | 154.7% | 159.2% |
<!-- BENCH_RESULTS_END -->
