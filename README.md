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
Generated: 2026-03-23T22:40:43.129800+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0363s | +0.0011s | worse |
| `f1ap_rel18.6_specs` | 0.1151s | 0.1136s | +0.0015s | worse |
| `ngap_rel18.6_specs` | 0.0799s | 0.0769s | +0.0030s | worse |
| `lteNRRCC` | 0.1209s | 0.1211s | -0.0002s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 14.96 MB | 53.55 MB | 23.9% | 106.7% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 109.7% | 104.4% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 116.0% | 105.9% |
| `lteNRRCC` | 72.34 MB | 100.11 MB | 103.3% | 104.1% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0369s | 0.0372s | -0.0003s | improved |
| `f1ap_rel18.6_specs` | 0.0952s | 0.0974s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0677s | 0.0688s | -0.0011s | improved |
| `lteNRRCC` | 0.1306s | 0.1331s | -0.0025s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.29 MB | 36.72 MB | 18.0% | 110.0% |
| `f1ap_rel18.6_specs` | 21.93 MB | 103.09 MB | 111.8% | 105.0% |
| `ngap_rel18.6_specs` | 16.52 MB | 74.61 MB | 110.7% | 108.9% |
| `lteNRRCC` | 48.33 MB | 65.86 MB | 104.5% | 102.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0351s | 0.0374s | -0.0023s | improved |
| `f1ap_rel18.6_specs` | 0.0902s | 0.0961s | -0.0059s | improved |
| `ngap_rel18.6_specs` | 0.0617s | 0.0665s | -0.0048s | improved |
| `lteNRRCC` | 0.1223s | 0.1312s | -0.0089s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.50 MB | 55.85 MB | 88.5% | 113.8% |
| `f1ap_rel18.6_specs` | 34.42 MB | 164.38 MB | 109.4% | 105.1% |
| `ngap_rel18.6_specs` | 24.34 MB | 117.84 MB | 115.4% | 107.1% |
| `lteNRRCC` | 74.94 MB | 102.93 MB | 105.1% | 104.3% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0204s | 0.0204s | +0.0000s | flat |
| `f1ap_rel18.6_specs` | 0.0621s | 0.0643s | -0.0022s | improved |
| `ngap_rel18.6_specs` | 0.0403s | 0.0455s | -0.0052s | improved |
| `lteNRRCC` | 0.0683s | 0.0673s | +0.0010s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.45 MB | 3.94 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 4.16 MB | 4.16 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.14 MB | 4.39 MB | 0.0% | 0.0% |
| `lteNRRCC` | 3.91 MB | 4.72 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0385s | 0.0392s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.1047s | 0.1076s | -0.0029s | improved |
| `ngap_rel18.6_specs` | 0.0732s | 0.0742s | -0.0010s | improved |
| `lteNRRCC` | 0.1369s | 0.1252s | +0.0117s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.50 MB | 7.44 MB | 107.8% | 101.4% |
| `f1ap_rel18.6_specs` | 8.27 MB | 8.39 MB | 99.9% | 92.2% |
| `ngap_rel18.6_specs` | 7.91 MB | 8.00 MB | 107.8% | 103.0% |
| `lteNRRCC` | 51.84 MB | 49.32 MB | 233.6% | 117.5% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0384s | 0.0395s | -0.0011s | improved |
| `f1ap_rel18.6_specs` | 0.1062s | 0.1140s | -0.0078s | improved |
| `ngap_rel18.6_specs` | 0.0750s | 0.0788s | -0.0038s | improved |
| `lteNRRCC` | 0.1241s | 0.1445s | -0.0204s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.94 MB | 10.72 MB | 156.0% | 230.3% |
| `f1ap_rel18.6_specs` | 9.53 MB | 10.52 MB | 91.3% | 102.5% |
| `ngap_rel18.6_specs` | 8.96 MB | 10.45 MB | 164.7% | 110.2% |
| `lteNRRCC` | 9.62 MB | 98.70 MB | 218.7% | 155.6% |
<!-- BENCH_RESULTS_END -->
