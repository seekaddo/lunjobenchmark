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
Generated: 2026-08-02T23:00:26.564311+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0345s | 0.0377s | -0.0032s | improved |
| `f1ap_rel18.6_specs` | 0.1117s | 0.1145s | -0.0028s | improved |
| `ngap_rel18.6_specs` | 0.0754s | 0.0801s | -0.0047s | improved |
| `lteNRRCC` | 0.1196s | 0.1219s | -0.0023s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 18.80 MB | 53.55 MB | 79.2% | 107.4% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 101.5% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.7% | 102.1% |
| `lteNRRCC` | 72.35 MB | 100.11 MB | 103.5% | 101.4% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0349s | 0.0347s | +0.0002s | worse |
| `f1ap_rel18.6_specs` | 0.0931s | 0.0947s | -0.0016s | improved |
| `ngap_rel18.6_specs` | 0.0658s | 0.0661s | -0.0003s | improved |
| `lteNRRCC` | 0.1245s | 0.1308s | -0.0063s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.48 MB | 35.93 MB | 78.6% | 107.4% |
| `f1ap_rel18.6_specs` | 22.42 MB | 103.42 MB | 103.2% | 101.6% |
| `ngap_rel18.6_specs` | 17.56 MB | 73.78 MB | 108.0% | 102.3% |
| `lteNRRCC` | 48.74 MB | 66.41 MB | 101.6% | 101.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0366s | 0.0350s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0933s | 0.0919s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0658s | 0.0640s | +0.0018s | worse |
| `lteNRRCC` | 0.1180s | 0.1179s | +0.0001s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 17.45 MB | 55.10 MB | 84.0% | 103.7% |
| `f1ap_rel18.6_specs` | 34.52 MB | 164.57 MB | 107.1% | 101.7% |
| `ngap_rel18.6_specs` | 24.54 MB | 117.73 MB | 104.3% | 104.9% |
| `lteNRRCC` | 74.84 MB | 102.63 MB | 103.5% | 101.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0217s | 0.0217s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0657s | 0.0662s | -0.0005s | improved |
| `ngap_rel18.6_specs` | 0.0453s | 0.0479s | -0.0026s | improved |
| `lteNRRCC` | 0.0758s | 0.0753s | +0.0005s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.94 MB | 3.77 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.50 MB | 7.12 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.77 MB | 4.44 MB | 0.0% | 0.0% |
| `lteNRRCC` | 4.94 MB | 4.42 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0411s | 0.0406s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1118s | 0.1099s | +0.0019s | worse |
| `ngap_rel18.6_specs` | 0.0780s | 0.0773s | +0.0007s | worse |
| `lteNRRCC` | 0.1396s | 0.1417s | -0.0021s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 11.34 MB | 7.73 MB | 0.0% | 100.6% |
| `f1ap_rel18.6_specs` | 8.23 MB | 106.64 MB | 92.8% | 108.2% |
| `ngap_rel18.6_specs` | 7.98 MB | 8.36 MB | 179.8% | 112.2% |
| `lteNRRCC` | 50.79 MB | 70.17 MB | 104.0% | 104.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0378s | 0.0397s | -0.0019s | improved |
| `f1ap_rel18.6_specs` | 0.1072s | 0.1110s | -0.0038s | improved |
| `ngap_rel18.6_specs` | 0.0739s | 0.0773s | -0.0034s | improved |
| `lteNRRCC` | 0.1252s | 0.1281s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 0 KB | 8.58 MB | 0.0% | 162.7% |
| `f1ap_rel18.6_specs` | 9.71 MB | 164.20 MB | 178.9% | 107.1% |
| `ngap_rel18.6_specs` | 10.63 MB | 8.89 MB | 118.4% | 160.2% |
| `lteNRRCC` | 8.55 MB | 90.88 MB | 174.0% | 158.5% |
<!-- BENCH_RESULTS_END -->
