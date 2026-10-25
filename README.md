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
Generated: 2026-10-25T00:10:10.537261+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0387s | 0.0342s | +0.0045s | worse |
| `f1ap_rel18.6_specs` | 0.1195s | 0.1096s | +0.0099s | worse |
| `ngap_rel18.6_specs` | 0.0824s | 0.0755s | +0.0069s | worse |
| `lteNRRCC` | 0.1267s | 0.1193s | +0.0074s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 80.0% | 106.5% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.2% | 102.8% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.0% | 103.8% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.3% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0376s | 0.0258s | +0.0118s | worse |
| `f1ap_rel18.6_specs` | 0.0940s | 0.0668s | +0.0272s | worse |
| `ngap_rel18.6_specs` | 0.0679s | 0.0462s | +0.0217s | worse |
| `lteNRRCC` | 0.1292s | 0.0819s | +0.0473s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 36.53 MB | 80.0% | 103.7% |
| `f1ap_rel18.6_specs` | 22.30 MB | 103.34 MB | 103.2% | 103.5% |
| `ngap_rel18.6_specs` | 18.07 MB | 74.34 MB | 103.8% | 102.4% |
| `lteNRRCC` | 48.16 MB | 66.03 MB | 103.2% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0347s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0905s | 0.0933s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0614s | 0.0648s | -0.0034s | improved |
| `lteNRRCC` | 0.1162s | 0.1222s | -0.0060s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.64 MB | 54.94 MB | 82.6% | 108.0% |
| `f1ap_rel18.6_specs` | 34.48 MB | 164.26 MB | 103.6% | 103.8% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.77 MB | 108.7% | 102.5% |
| `lteNRRCC` | 74.98 MB | 101.76 MB | 101.8% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0517s | 0.0476s | +0.0041s | worse |
| `f1ap_rel18.6_specs` | 0.0932s | 0.1321s | -0.0389s | improved |
| `ngap_rel18.6_specs` | 0.0757s | 0.0637s | +0.0120s | worse |
| `lteNRRCC` | 0.1128s | 0.0863s | +0.0265s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 2.22 MB | 4.25 MB | 0.0% | 0.1% |
| `f1ap_rel18.6_specs` | 6.64 MB | 8.53 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 8.44 MB | 10.17 MB | 0.0% | 1.3% |
| `lteNRRCC` | 7.66 MB | 4.28 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0374s | +0.0030s | worse |
| `f1ap_rel18.6_specs` | 0.1116s | 0.1033s | +0.0083s | worse |
| `ngap_rel18.6_specs` | 0.0766s | 0.0736s | +0.0030s | worse |
| `lteNRRCC` | 0.1409s | 0.1381s | +0.0028s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.76 MB | 7.70 MB | 109.3% | 153.4% |
| `f1ap_rel18.6_specs` | 8.74 MB | 8.45 MB | 96.2% | 152.7% |
| `ngap_rel18.6_specs` | 8.12 MB | 8.12 MB | 169.8% | 165.7% |
| `lteNRRCC` | 48.39 MB | 51.97 MB | 106.5% | 107.3% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0391s | -0.0040s | improved |
| `f1ap_rel18.6_specs` | 0.0996s | 0.1136s | -0.0140s | improved |
| `ngap_rel18.6_specs` | 0.0707s | 0.0890s | -0.0183s | improved |
| `lteNRRCC` | 0.1108s | 0.1373s | -0.0265s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.29 MB | 9.57 MB | 133.6% | 208.3% |
| `f1ap_rel18.6_specs` | 11.41 MB | 164.19 MB | 140.6% | 140.3% |
| `ngap_rel18.6_specs` | 10.83 MB | 10.52 MB | 136.7% | 139.5% |
| `lteNRRCC` | 9.82 MB | 86.40 MB | 130.9% | 202.3% |
<!-- BENCH_RESULTS_END -->
