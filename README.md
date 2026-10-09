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
Generated: 2026-10-09T16:55:16.670575+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0357s | 0.0342s | +0.0015s | worse |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1066s | +0.0051s | worse |
| `ngap_rel18.6_specs` | 0.0762s | 0.0734s | +0.0028s | worse |
| `lteNRRCC` | 0.1203s | 0.1171s | +0.0032s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.99 MB | 53.55 MB | 85.7% | 107.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 103.4% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 104.3% | 104.2% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 101.7% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0277s | 0.0290s | -0.0013s | improved |
| `f1ap_rel18.6_specs` | 0.0757s | 0.0851s | -0.0094s | improved |
| `ngap_rel18.6_specs` | 0.0526s | 0.0592s | -0.0066s | improved |
| `lteNRRCC` | 0.0976s | 0.1051s | -0.0075s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.55 MB | 35.98 MB | 14.2% | 104.8% |
| `f1ap_rel18.6_specs` | 22.34 MB | 103.43 MB | 104.2% | 104.1% |
| `ngap_rel18.6_specs` | 18.20 MB | 73.68 MB | 110.5% | 103.0% |
| `lteNRRCC` | 48.40 MB | 65.92 MB | 102.1% | 103.6% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0341s | 0.0219s | +0.0122s | worse |
| `f1ap_rel18.6_specs` | 0.0917s | 0.0820s | +0.0097s | worse |
| `ngap_rel18.6_specs` | 0.0633s | 0.0522s | +0.0111s | worse |
| `lteNRRCC` | 0.1170s | 0.0813s | +0.0357s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.68 MB | 55.59 MB | 76.9% | 103.8% |
| `f1ap_rel18.6_specs` | 34.73 MB | 164.47 MB | 103.6% | 101.9% |
| `ngap_rel18.6_specs` | 24.02 MB | 117.73 MB | 104.3% | 105.0% |
| `lteNRRCC` | 74.61 MB | 102.36 MB | 101.8% | 103.0% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0261s | 0.0357s | -0.0096s | improved |
| `f1ap_rel18.6_specs` | 0.0789s | 0.0879s | -0.0090s | improved |
| `ngap_rel18.6_specs` | 0.0832s | 0.0701s | +0.0131s | worse |
| `lteNRRCC` | 0.0833s | 0.1043s | -0.0210s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.97 MB | 9.64 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 11.41 MB | 9.98 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 9.00 MB | 8.22 MB | 0.0% | 0.0% |
| `lteNRRCC` | 7.23 MB | 7.20 MB | 0.0% | 1.2% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0336s | 0.0412s | -0.0076s | improved |
| `f1ap_rel18.6_specs` | 0.0947s | 0.1134s | -0.0187s | improved |
| `ngap_rel18.6_specs` | 0.0665s | 0.0783s | -0.0118s | improved |
| `lteNRRCC` | 0.1120s | 0.1412s | -0.0292s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.32 MB | 8.09 MB | 0.0% | 201.0% |
| `f1ap_rel18.6_specs` | 8.52 MB | 8.52 MB | 111.4% | 205.5% |
| `ngap_rel18.6_specs` | 8.02 MB | 8.08 MB | 103.7% | 117.9% |
| `lteNRRCC` | 8.45 MB | 68.58 MB | 202.0% | 204.4% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0405s | 0.0377s | +0.0028s | worse |
| `f1ap_rel18.6_specs` | 0.1169s | 0.1083s | +0.0086s | worse |
| `ngap_rel18.6_specs` | 0.0816s | 0.0780s | +0.0036s | worse |
| `lteNRRCC` | 0.1313s | 0.1284s | +0.0029s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 13.91 MB | 10.44 MB | 0.0% | 217.3% |
| `f1ap_rel18.6_specs` | 9.73 MB | 164.17 MB | 155.1% | 107.8% |
| `ngap_rel18.6_specs` | 9.25 MB | 10.17 MB | 156.1% | 210.2% |
| `lteNRRCC` | 8.85 MB | 88.43 MB | 149.2% | 221.1% |
<!-- BENCH_RESULTS_END -->
