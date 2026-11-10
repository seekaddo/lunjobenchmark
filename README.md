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
Generated: 2026-11-10T17:37:40.376908+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0424s | 0.0386s | +0.0038s | worse |
| `f1ap_rel18.6_specs` | 0.1293s | 0.1208s | +0.0085s | worse |
| `ngap_rel18.6_specs` | 0.0882s | 0.0847s | +0.0035s | worse |
| `lteNRRCC` | 0.1286s | 0.1262s | +0.0024s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.92 MB | 53.55 MB | 85.2% | 106.1% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.2% | 102.7% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.0% | 103.7% |
| `lteNRRCC` | 72.34 MB | 100.18 MB | 103.2% | 103.9% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0361s | 0.0314s | +0.0047s | worse |
| `f1ap_rel18.6_specs` | 0.1131s | 0.0991s | +0.0140s | worse |
| `ngap_rel18.6_specs` | 0.0773s | 0.0682s | +0.0091s | worse |
| `lteNRRCC` | 0.1199s | 0.0988s | +0.0211s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.85 MB | 34.65 MB | 73.9% | 103.6% |
| `f1ap_rel18.6_specs` | 21.27 MB | 101.27 MB | 107.1% | 103.1% |
| `ngap_rel18.6_specs` | 18.09 MB | 72.65 MB | 109.1% | 102.1% |
| `lteNRRCC` | 46.68 MB | 64.21 MB | 101.8% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0490s | 0.0375s | +0.0115s | worse |
| `f1ap_rel18.6_specs` | 0.1477s | 0.1148s | +0.0329s | worse |
| `ngap_rel18.6_specs` | 0.1007s | 0.0812s | +0.0195s | worse |
| `lteNRRCC` | 0.1426s | 0.1076s | +0.0350s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.93 MB | 53.73 MB | 81.8% | 106.2% |
| `f1ap_rel18.6_specs` | 32.86 MB | 162.11 MB | 106.7% | 101.2% |
| `ngap_rel18.6_specs` | 22.61 MB | 115.73 MB | 108.7% | 101.7% |
| `lteNRRCC` | 72.62 MB | 100.36 MB | 103.1% | 102.5% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0413s | 0.0415s | -0.0002s | improved |
| `f1ap_rel18.6_specs` | 0.1108s | 0.1128s | -0.0020s | improved |
| `ngap_rel18.6_specs` | 0.0770s | 0.0777s | -0.0007s | improved |
| `lteNRRCC` | 0.1401s | 0.1417s | -0.0016s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.35 MB | 7.70 MB | 0.0% | 151.2% |
| `f1ap_rel18.6_specs` | 8.45 MB | 8.12 MB | 103.9% | 99.5% |
| `ngap_rel18.6_specs` | 7.56 MB | 8.12 MB | 165.6% | 219.8% |
| `lteNRRCC` | 8.18 MB | 49.59 MB | 153.7% | 161.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0308s | 0.0417s | -0.0109s | improved |
| `f1ap_rel18.6_specs` | 0.0895s | 0.1179s | -0.0284s | improved |
| `ngap_rel18.6_specs` | 0.0635s | 0.0831s | -0.0196s | improved |
| `lteNRRCC` | 0.0986s | 0.1361s | -0.0375s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 10.92 MB | 0.0% | 145.3% |
| `f1ap_rel18.6_specs` | 11.27 MB | 12.09 MB | 208.5% | 141.3% |
| `ngap_rel18.6_specs` | 11.27 MB | 10.77 MB | 149.5% | 143.4% |
| `lteNRRCC` | 9.81 MB | 101.56 MB | 141.7% | 144.2% |
<!-- BENCH_RESULTS_END -->
