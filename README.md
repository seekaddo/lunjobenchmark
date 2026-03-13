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
Generated: 2026-03-13T22:35:33.085929+00:00

### linux-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0394s | 0.0373s | +0.0021s | worse |
| `f1ap_rel18.6_specs` | 0.1223s | 0.1209s | +0.0014s | worse |
| `ngap_rel18.6_specs` | 0.0837s | 0.0821s | +0.0016s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 12.26 MB | 55.64 MB | 75.0% | 106.5% |
| `f1ap_rel18.6_specs` | 32.14 MB | 176.76 MB | 106.5% | 104.2% |
| `ngap_rel18.6_specs` | 22.14 MB | 125.64 MB | 112.0% | 103.7% |

### linux-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0370s | 0.0387s | -0.0017s | improved |
| `f1ap_rel18.6_specs` | 0.0990s | 0.1020s | -0.0030s | improved |
| `ngap_rel18.6_specs` | 0.0711s | 0.0726s | -0.0015s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.79 MB | 37.68 MB | 89.3% | 113.3% |
| `f1ap_rel18.6_specs` | 22.30 MB | 111.66 MB | 111.4% | 106.6% |
| `ngap_rel18.6_specs` | 16.66 MB | 80.08 MB | 110.3% | 106.4% |

### linux-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0352s | 0.0358s | -0.0006s | improved |
| `f1ap_rel18.6_specs` | 0.0942s | 0.0948s | -0.0006s | improved |
| `ngap_rel18.6_specs` | 0.0679s | 0.0680s | -0.0001s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 15.37 MB | 57.94 MB | 89.3% | 110.3% |
| `f1ap_rel18.6_specs` | 33.92 MB | 178.91 MB | 112.9% | 105.1% |
| `ngap_rel18.6_specs` | 23.81 MB | 127.86 MB | 111.5% | 106.5% |

### macos-aarch64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0241s | 0.0201s | +0.0040s | worse |
| `f1ap_rel18.6_specs` | 0.0648s | 0.0616s | +0.0032s | worse |
| `ngap_rel18.6_specs` | 0.0418s | 0.0418s | +0.0000s | flat |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 4.14 MB | 3.88 MB | 0.0% | 0.0% |
| `f1ap_rel18.6_specs` | 3.97 MB | 4.47 MB | 0.0% | 0.0% |
| `ngap_rel18.6_specs` | 4.08 MB | 4.69 MB | 0.0% | 0.0% |

### windows-i386

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0404s | 0.0416s | -0.0012s | improved |
| `f1ap_rel18.6_specs` | 0.1147s | 0.1131s | +0.0016s | worse |
| `ngap_rel18.6_specs` | 0.0817s | 0.0803s | +0.0014s | worse |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 7.47 MB | 7.29 MB | 92.1% | 160.6% |
| `f1ap_rel18.6_specs` | 7.99 MB | 8.06 MB | 78.7% | 82.0% |
| `ngap_rel18.6_specs` | 8.12 MB | 7.45 MB | 191.8% | 98.0% |

### windows-x86_64

#### Timing

| Fixture | Syntaxcheck mean | Previous | Delta | Trend |
| --- | ---: | ---: | ---: | --- |
| `e1ap_rel18.4_specs` | 0.0380s | 0.0442s | -0.0062s | improved |
| `f1ap_rel18.6_specs` | 0.1191s | 0.1267s | -0.0076s | improved |
| `ngap_rel18.6_specs` | 0.0778s | 0.0889s | -0.0111s | improved |

#### Resources

| Fixture | Parse RSS | Syntax RSS | Parse CPU | Syntax CPU |
| --- | ---: | ---: | ---: | ---: |
| `e1ap_rel18.4_specs` | 10.38 MB | 8.32 MB | 113.6% | 160.0% |
| `f1ap_rel18.6_specs` | 9.41 MB | 179.13 MB | 162.2% | 161.3% |
| `ngap_rel18.6_specs` | 10.58 MB | 10.36 MB | 233.4% | 106.6% |
<!-- BENCH_RESULTS_END -->
