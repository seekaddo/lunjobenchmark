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
Generated: 2026-03-23T11:00:28.171878+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0363s | 0.0371s | -0.0008s | improved |
| `f1ap_rel18.6_specs` | 0.1136s | 0.1155s | -0.0019s | improved |
| `ngap_rel18.6_specs` | 0.0769s | 0.0779s | -0.0010s | improved |
| `lteNRRCC` | 0.1211s | 0.1240s | -0.0029s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.68 MB | 53.55 MB | 95.0% | 106.9% |
| `f1ap_rel18.6_specs` | 32.68 MB | 161.93 MB | 106.9% | 102.9% |
| `ngap_rel18.6_specs` | 22.43 MB | 115.55 MB | 108.3% | 103.9% |
| `lteNRRCC` | 72.36 MB | 100.11 MB | 103.4% | 104.2% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0372s | 0.0356s | +0.0016s | worse |
| `f1ap_rel18.6_specs` | 0.0974s | 0.0954s | +0.0020s | worse |
| `ngap_rel18.6_specs` | 0.0688s | 0.0696s | -0.0008s | improved |
| `lteNRRCC` | 0.1331s | 0.1295s | +0.0036s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.45 MB | 35.95 MB | 92.6% | 110.0% |
| `f1ap_rel18.6_specs` | 21.66 MB | 103.41 MB | 111.8% | 104.9% |
| `ngap_rel18.6_specs` | 16.85 MB | 73.76 MB | 114.3% | 106.4% |
| `lteNRRCC` | 48.35 MB | 65.85 MB | 104.5% | 103.9% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0374s | 0.0342s | +0.0032s | worse |
| `f1ap_rel18.6_specs` | 0.0961s | 0.0890s | +0.0071s | worse |
| `ngap_rel18.6_specs` | 0.0665s | 0.0623s | +0.0042s | worse |
| `lteNRRCC` | 0.1312s | 0.1154s | +0.0158s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.49 MB | 55.08 MB | 96.4% | 109.4% |
| `f1ap_rel18.6_specs` | 34.69 MB | 163.73 MB | 111.8% | 106.7% |
| `ngap_rel18.6_specs` | 24.04 MB | 117.61 MB | 110.3% | 106.4% |
| `lteNRRCC` | 73.57 MB | 102.29 MB | 106.1% | 105.1% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0204s | 0.0211s | -0.0007s | improved |
| `f1ap_rel18.6_specs` | 0.0643s | 0.0639s | +0.0004s | worse |
| `ngap_rel18.6_specs` | 0.0455s | 0.0456s | -0.0001s | improved |
| `lteNRRCC` | 0.0673s | 0.0733s | -0.0060s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 3.92 MB | 4.44 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.73 MB | 4.62 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.44 MB | 3.75 MB | 0.0% | 0.0% |
| `lteNRRCC` | 6.92 MB | 4.06 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0392s | 0.0387s | +0.0005s | worse |
| `f1ap_rel18.6_specs` | 0.1076s | 0.1087s | -0.0011s | improved |
| `ngap_rel18.6_specs` | 0.0742s | 0.0732s | +0.0010s | worse |
| `lteNRRCC` | 0.1252s | 0.1365s | -0.0113s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 8.05 MB | 7.81 MB | 120.2% | 120.3% |
| `f1ap_rel18.6_specs` | 8.61 MB | 8.37 MB | 119.5% | 120.0% |
| `ngap_rel18.6_specs` | 8.23 MB | 8.18 MB | 119.9% | 118.6% |
| `lteNRRCC` | 8.08 MB | 68.60 MB | 119.1% | 118.7% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0395s | 0.0369s | +0.0026s | worse |
| `f1ap_rel18.6_specs` | 0.1140s | 0.1034s | +0.0106s | worse |
| `ngap_rel18.6_specs` | 0.0788s | 0.0726s | +0.0062s | worse |
| `lteNRRCC` | 0.1445s | 0.1251s | +0.0194s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 9.78 MB | 8.13 MB | 109.0% | 178.2% |
| `f1ap_rel18.6_specs` | 9.81 MB | 10.06 MB | 158.6% | 168.3% |
| `ngap_rel18.6_specs` | 10.57 MB | 10.57 MB | 115.5% | 116.9% |
| `lteNRRCC` | 9.55 MB | 98.96 MB | 97.4% | 113.7% |
<!-- BENCH_RESULTS_END -->
